# Chapter 17
# HTTP APIs and Resilient Networking

Your application has just displayed five catalog entries. The customer pulls into a parking garage, changes from Wi-Fi to cellular service, and taps Refresh. A moment later the server returns a successful HTTP status with a hotel login page as its body. The screen should not erase its useful catalog and announce that no books exist.

A network request has several separate questions to answer: did the connection work, did the service accept the request, did the response match the contract, and is this result still relevant to the screen? This chapter establishes the first three boundaries for public catalog reads. The UI continues to use its bundled catalog while a separate networking lab exercises the new client through an in-process HTTP handler. Chapter 18 will supply a real companion API.

**Prerequisites:** the validated catalog model from Chapter 12, asynchronous state ownership from Chapters 13–14, and the distinction between retries and new operations from Chapter 16. **Learning goals:** define a small HTTP boundary; reuse a client; apply one cancellation/deadline policy to headers, bodies and waits; validate bounded JSON; and retry only selected failures. **Delivered capability:** a GET-only catalog adapter, deterministic transport tests, and a labeled native demo screen without a deployed dependency.

## What You'll Learn

You will learn to isolate HTTP access behind a narrow catalog interface; enforce response size and schema constraints; apply one total request deadline; choose bounded retry behavior for safe reads; classify failures without exposing private data; and verify behavior with an injected HTTP handler.

**Prerequisites:** Chapter 12's catalog contract and the companion HTTP lab. **Deliverable:** A portable networking boundary whose failure handling can be tested without running a public service.

### Guided lab: challenge a successful status code

1. Execute the companion HTTP client tests against an in-process handler that returns a valid catalog document. Record the expected number of items.
2. Return HTTP 200 with an HTML captive-portal page instead of JSON. Confirm that the client rejects its content type rather than treating the catalog as empty.
3. Return an oversized response. Verify that the configured body limit stops ingestion before unbounded allocation.
4. Arrange a transient read failure followed by a valid response. Observe which failures the bounded retry policy permits; do not generalize this policy to unsafe writes.
5. Cancel the operation or exhaust its overall deadline. Check that later retries do not extend the logical request indefinitely.
6. On failure, check that the existing bundled catalog remains available and logs do not contain response bodies or secrets.

**Expected result:** HTTP status, media type, byte limits, schema, and operation ownership are evaluated separately. Handler tests do not establish TLS, routing or mobile-device connectivity.

### Worked reasoning: 200 OK does not mean useful data

HTTP success means the transport protocol received a response classified as successful. It does not prove that the response is the application's expected document. A hotel portal, proxy error or unexpectedly shaped JSON can all violate the contract. Verify the bytes and the domain model before replacing useful on-screen content.

## Begin with the contract

ICatalogSource exposes one operation: load a complete read-only list of catalog items. The asynchronous boundary takes a CancellationToken. It does not expose HttpResponseMessage, native connectivity enums, a customer account, or payment state to the rest of the application.

```csharp
public interface ICatalogSource
{
    Task<IReadOnlyList<CatalogItem>> LoadAsync(
        CancellationToken cancellationToken = default);
}
```

The Chapter 17 transport expects a single HTTP 200 response with application/json content and a JSON array accepted by CatalogLoader. An empty array is a legitimate empty catalog. A blank body, null, an object, or malformed metadata is a failure, not an empty result. A 204 response is outside this deliberately narrow contract and is rejected.

This is an interim public-items contract. CatalogLoader checks item metadata and duplicate IDs, while CatalogSnapshot checks creator relationships when it receives both item and creator inputs. The HTTP adapter currently loads only items: it cannot verify a creator relationship against a creator list that was not transferred. Chapter 18 will make the service contract explicit before the main browser switches to remote data. Pagination, envelope versions, creator refresh and conditional requests are later extensions, not implied capabilities of this list endpoint.

Keep provider-specific payloads behind another adapter. Apple, Spotify and a companion API do not necessarily use the same identities, fields, response limits or authorization. A successful metadata request also gives the app no new media rights. A provider's web page or music-service link is not an audio stream or a substitute for its documented API.

## Reuse the client and own its configuration

HttpCatalogSource receives an HttpClient rather than creating one for every refresh. The application owns and eventually disposes that client. In the native demo, DemoCatalogSource is registered as a singleton, owns its reusable client, and delegates catalog reads to the HTTP adapter. Its fixture handler opens the bundled JSON resource for each response. Response disposal closes that resource stream.

For a future real endpoint, choose an application-level HttpClient/handler configuration or an appropriately configured IHttpClientFactory registration. Connection-pool and DNS behavior depend on the chosen handler and platform; validate the configuration against the Android and iOS handler actually in use. Do not present a Windows-only configuration experiment as proof of native networking behavior.

The adapter requires an absolute HTTPS endpoint without embedded credentials or a fragment. It rejects a relative path because the teaching contract does not depend on an implicit BaseAddress. Treat the endpoint as application configuration, never as arbitrary customer input. The adapter itself does not own redirect policy. The future real handler must control redirects and preserve certificate verification; a test handler's refusal of a 302 does not prove a default native handler will refrain from following it.

The demo endpoint is https://catalog.example.invalid/catalog/items. That address labels the fixture; no DNS lookup occurs because FixtureHandler supplies the response directly. Do not replace it with a real service and assume the rest of the deployment, API or authentication setup has been completed.

## Give the whole operation one deadline

There are two reasons to stop waiting. The caller can cancel because the screen went away or the customer selected Cancel. Separately, the adapter can exhaust its own total time budget. Preserve that distinction so navigation cancellation does not produce an alarming service-failure message.

The example gives one logical catalog load a twenty-second deadline. That budget covers every request attempt, response-body read and retry wait. A sequence of three twenty-second attempt timeouts would have a very different user experience. The code uses TimeProvider so tests can trigger deadline cancellation without waiting for wall-clock time.

```csharp
using var deadline = new CancellationTokenSource(
    Deadline, clock);
using var linked =
    CancellationTokenSource.CreateLinkedTokenSource(
        cancellationToken, deadline.Token);
var ct = linked.Token;
```

The received HttpClient must have Timeout.InfiniteTimeSpan configured. The adapter rejects another client timeout so this example has one clearly owned budget. That choice is part of this client's contract; it is not an instruction to disable timeouts in every application. Pass ct to SendAsync, ReadAsStreamAsync, each ReadAsync, and the delay between attempts.

The adapter uses ResponseHeadersRead to inspect status and headers before buffering a response body. In that mode, a completed SendAsync does not mean the body has arrived. The adapter therefore continues using its linked token while reading the body. A server that sends headers promptly and then stalls cannot escape the overall deadline.

Synchronous validation is also bracketed by cancellation checks. The bounded JSON parser does not become interruptible halfway through merely because a token exists; the final check prevents publication after cancellation was observed at that boundary. Larger datasets need a separately designed streaming or paginated contract, rather than a much larger buffer and optimistic assumptions about responsiveness.

## Bound the body before trusting it

A response can be syntactically valid HTTP and still consume unreasonable memory. The adapter sets a one-mebibyte body limit: 1,048,576 bytes. A declared Content-Length above that limit is rejected before the body is read. A missing or inaccurate length does not disable the limit; bytes are counted during the read loop.

```csharp
var read = await stream.ReadAsync(
    block.AsMemory(), ct).ConfigureAwait(false);
if (read == 0) break;
if (buffer.Length + read > MaximumBytes)
    throw new CatalogFetchException(
        CatalogFetchProblem.TooLarge);
buffer.Write(block, 0, read);
```

This excerpt is inside ReadOnceAsync in src/GnazzosWorld.Core/Networking/HttpCatalogSource.cs. The complete method reads blocks of 8,192 bytes and checks each before writing it to the bounded buffer. It can receive one final block that crosses the limit, but it does not append that block or grow the buffer beyond the allowed payload. The limit applies to the stream the configured handler presents; server, proxy, decompression and header limits require their own configuration.

Require the agreed media type before parsing. A gateway may return text/html with status 200; parsing that response as a catalog is neither helpful nor reliable. In this example application/json is the supported media type, with case-insensitive comparison. Other JSON media types are intentionally outside the contract until supported explicitly.

After a complete bounded read, CatalogLoader validates the list. The adapter translates malformed JSON and invalid catalog metadata into InvalidPayload. It never publishes a partially parsed list. It does not replace the main catalog at all in this chapter, so a failed lab request leaves bundled browsing available.

All request, response, stream and buffer lifetimes are explicit. In particular, an unsuccessful response is disposed before the retry delay. Holding a response open while sleeping can retain network resources that the next attempt needs. Tests verify the disposal boundary rather than merely counting retry calls.

## Retry a narrow set of read failures

The adapter sends GET only. That restriction is useful: retrying a public catalog read does not ask the service to create a new customer order. Do not reuse this loop around the submission operation from Chapter 16. Writes need their own operation identity, server reconciliation and authorization rules.

A retry budget should answer three questions: which failures qualify, how many attempts are allowed, and how long the whole operation may take. This example allows three total attempts, including the first, with the shared twenty-second deadline. It retries only the status and transport categories shown below.

| Observation | Adapter policy |
|---|---|
| 408, 429, 500, 502, 503, 504 | Retry within the attempt/deadline budget |
| Connection, name-resolution or prematurely ended response transport errors | Retry within the same budget |
| I/O failure while reading the body | Retry the GET within the same budget |
| Certificate/security transport failure | Return Network failure; no automatic retry |
| 400, 401, 403, 404 or other unexpected status | Return HttpStatus failure; no retry |
| Invalid media type, JSON or metadata | Return InvalidPayload; no retry |
| Body exceeds the limit | Return TooLarge; no retry |
| Caller cancellation | Stop and propagate cancellation |
| Adapter deadline expires | Return Deadline failure |

The selected status set is an explicit example policy. It does not mean every 500 error is temporary or every connection failure will improve. Bounded attempts prevent those assumptions from becoming an endless loop. A future API can supply better problem codes, and production policy should use that documented behavior.

Without a Retry-After header, the first wait is 200 milliseconds plus up to 100 milliseconds of jitter; the second is 400 milliseconds plus the same bounded jitter. Increasing waits reduce immediate repeated pressure, while jitter spreads independent clients. Tests inject zero jitter and a recording delay to make expected timing deterministic. They do not sleep in order to inspect the policy.

The example accepts Retry-After as either a relative duration or an absolute date. An absolute date is compared with the injected clock, and a date in the past becomes a zero wait. This depends on the client's clock being reasonably correct; a production protocol can incorporate additional clock-skew handling.

If the requested wait is more than five seconds, the adapter returns the status failure instead of retrying earlier than the service requested. The UI can offer a later explicit retry. It does not shorten a sixty-second server instruction to five seconds and immediately send another request. A smaller wait still shares the total deadline, so repeated waits cannot extend the operation indefinitely.

## Make failure useful without revealing its contents

CatalogFetchException reports a small failure category and, when applicable, the HTTP status. It does not preserve response bodies, authorization headers, full endpoint URLs or the original transport exception as an inner exception. This keeps the teaching exception safe to display in the demo and avoids accidental disclosure through a casual exception log.

In a production diagnostic pipeline, record a bounded operation name, attempt count, elapsed time, outcome category and approved correlation identifier. Keep query strings, tokens, contact details and customer stories out of routine logs. Deliberately scrub any richer platform diagnostics before retaining or sharing them. The current adapter supplies typed failure information; it does not implement a full observability system.

The final cancellation handlers check caller cancellation first. If both cancellation sources are signaled, the caller's request wins. Deadline expiration produces Deadline, while an unexpected cancellation originating inside a handler becomes Network. That convention makes the outcome predictable for the caller and avoids confusing a handler's interruption with an intentional screen departure.

An HTTP 401 is also not a reason to repeatedly send the same public request or to open an unsolicited login screen. Authentication will be introduced through the later identity chapters. A provider that requires credentials belongs behind its explicitly configured adapter and authorization flow.

## Use connectivity as a hint

The native NetworkingLabPage shows Connectivity.Current.NetworkAccess when the page appears. It labels this value as a hint and says that it does not verify service reachability. A device can have a network interface and still encounter a captive portal, a blocked host, expired credentials or an unavailable API.

The lab's request is available even if the device reports no internet, because its handler is intentionally local. This makes the distinction visible: running the lab proves the HTTP contract path and validation, not actual internet access. Main browsing continues to use bundled data. The page does not claim to provide an offline cache, synchronize records or contact a deployment.

For a real refresh, use connectivity information to improve messaging or avoid obviously wasteful background work, while still handling the request result as authoritative. A preliminary connectivity check cannot guarantee that the connection remains available a millisecond later. Later offline work will define freshness, queued operations and restart behavior rather than using one connectivity enum as the whole policy.

The lab captures a cancellation source for the active request and cancels it on page departure. A generation value prevents a late completion from publishing success to an obsolete visit. The load button prevents overlapping calls in this single-page flow, and a finally block restores its state. Physical devices must still verify navigation, focus and screen-reader behavior; the code's ownership rule is not a screenshot or an accessibility test result.

## Test the boundary without a public service

HttpCatalogTests supplies HttpMessageHandler implementations that return a response, throw a classified transport exception, or expose a controlled body stream. The tests exercise the actual HttpCatalogSource. They do not replace the client method with a stub and then assert that the stub returned its configured result.

The suite verifies request method, endpoint and Accept header; an empty valid catalog; the native demo's bundled fixture; malformed JSON and metadata; unexpected statuses; retry counts and waits; Retry-After durations and dates; certificate failures; advertised and unknown body lengths; disposal; caller cancellation; and total deadline enforcement during a body read.

The deadline test is especially useful. Its Clock supplies the timer used by CancellationTokenSource. A custom body stream fires that timer when the adapter starts reading, then checks the received token. The expected result is Deadline, one request attempt and a disposed stream. This detects an implementation that protects only the header request and forgets to pass cancellation into body reads.

The rate-limit disposal test is another boundary check. A tracked content object records disposal. The injected delay asserts that the unsuccessful response has already been closed before it records the server's two-second wait. A client can pass a retry-count test while still holding responses open; this test distinguishes those implementations.

Run the executable portable tests using the pinned SDK and record their source revision. Follow with Android compilation and the Chapter 17 device checklist. Real integration tests in Chapter 18 must additionally establish TLS trust, redirects, local-PC reachability, actual response encoding, cancellation under a socket transport and service behavior. In-process handlers cannot establish those facts.

## Prepare for the companion API

The networking lab is a deliberate bridge between bundled data and a real service. Its fixture does not use HttpClient's socket transport, so it needs no listener, certificate bypass or internet permission experiment to run. Replacing the handler later is an integration change with new checks, not evidence that a backend already exists.

Chapter 18 will define the companion API's route, response schema, validation, errors and local development address. It will also explain why localhost inside an emulator or phone is not automatically the Windows workstation. Keep development endpoint and certificate configuration explicit. Never solve a test connection problem by disabling certificate checks globally or shipping a development exception in a public release.

The client already gives us the contract boundary on which to build: one operation, typed outcomes, bounded memory, one total time budget, and controlled retries for a public GET. The next chapter can focus on what the service promises because the application is no longer assuming that every response is immediate, trustworthy or complete.

## Chapter Summary

HTTP success, valid data and current UI ownership are separate conditions. The catalog adapter validates each response before returning a complete list, stops within explicit time and memory budgets, and retries a narrow set of read failures. The native demo makes that path inspectable while preserving bundled browsing and clearly identifying the simulated transport.

## Exercises and Review Questions

1. Configure a fake response with status 200 and text/html. Confirm that it produces InvalidPayload, does not retry, and leaves the main catalog available. Explain why converting this outcome to an empty array would mislead a customer.
2. Compare a Retry-After duration of two seconds with sixty seconds. Predict attempts and waits before running the corresponding tests. Explain why the client must not shorten the longer instruction into an early retry.
3. Trace the body-deadline test. Remove the linked token from ReadAsync in an isolated experiment, then identify which assertion no longer establishes correct cancellation. Restore the implementation before keeping changes.
4. Sketch a refresh state model that keeps the last valid catalog visible while reporting a failed refresh. Specify how it will represent a legitimate empty catalog and a stale snapshot in Chapter 20.
5. Before connecting Chapter 18's service, write a device checklist for local addressing, TLS trust, redirects, network changes and canceled navigation. Mark each as integration or native evidence rather than claiming it from the handler suite.

**Review questions:** Why is a client timeout alone insufficient with ResponseHeadersRead? Why is a GET retry policy inappropriate for accepting a custom-song order? Which validations can the items-only contract establish, and which creator relationships require another input? What does the networking lab prove when the phone is offline?

## References

- Microsoft, Guidelines for using HttpClient: client and handler lifetimes. https://learn.microsoft.com/en-us/dotnet/fundamentals/networking/http/httpclient-guidelines
- Microsoft, HttpCompletionOption: header completion, body reads and timeout scope. https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpcompletionoption
- Microsoft, Connectivity: platform network-access information and its limitations. https://learn.microsoft.com/en-us/dotnet/maui/platform-integration/communication/networking
- Microsoft, Build resilient HTTP apps: maintained resilience tooling and method-specific retry policy. https://learn.microsoft.com/en-us/dotnet/core/resilience/http-resilience
- Companion source: src/GnazzosWorld.Core/Networking/HttpCatalogSource.cs and DemoCatalogSource.cs; src/GnazzosWorld.App/Pages/NetworkingLabPage.cs; tests/GnazzosWorld.Core.Tests/HttpCatalogTests.cs. The bounded loop is a focused teaching implementation, not a replacement for evaluating maintained production resilience tooling.

## Editorial index terms

HttpClient; HttpMessageHandler; catalog source; GET; ResponseHeadersRead; cancellation; deadline; TimeProvider; content type; body limit; JSON validation; Retry-After; backoff; jitter; transport failure; connectivity hint; captive portal; native networking lab; safe diagnostics; handler tests; local API.
