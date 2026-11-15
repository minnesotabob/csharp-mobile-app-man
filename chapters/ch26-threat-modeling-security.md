# Chapter 26
# Threat Modeling and Security Verification

A customer opens an anniversary-song request in Gnazzo's World. Another signed-in customer changes the request ID in a captured URL. A third person shares a convincing link that looks like the sign-in provider. Meanwhile, a diagnostic message records more information than the operator intended. These are different threats against different boundaries; one successful sign-in cannot answer all of them.

Part V has introduced identity, API sessions, MFA/recovery design and account lifecycle. This chapter reviews the system we actually have, turns abuse cases into explicit enforcement decisions and adds focused hardening to the protected preview route. The result is a threat register with executable checks, not a declaration that the application is secure in every environment.

## What You'll Learn

1. Identify valuable assets, untrusted inputs and the component responsible for each decision.
2. Turn a plausible abuse case into a rejection test without bypassing the relevant security layer.
3. Share a bounded request-ID policy while preserving independent server enforcement.
4. Add private-response cache instructions, an aggregate read budget and minimal decision events.
5. Review dependency, secret, local-data and future customer-file risks with explicit evidence limits.

**Prerequisites:** Chapters 17–25, the pinned .NET 11 SDK and familiarity with the API tests. Start from companion checkpoint `4cb8f9b9c85f38226ff562f9b01e7e6e676f9b64`. Chapter 26 implementation begins at `a3d2a880195714dc61a2971bc2ab3f7aab1d78a9`; follow any corrective revision in `docs/verification.md`. Portable and test-host work uses fictitious data and requires no live identity tenant. Native follow-through requires the earlier platform/provider setup.

**What you will build:** a shared `RequestIdPolicy`, a server protected-read policy and decision projection, new portable/API regression cases, `docs/security/threat-model.md` and `docs/labs/ch26-security-verification.md`. Existing token, session, SQLite and callback tests remain part of the evidence. No customer-file endpoint, privileged lifecycle route or production deployment is added.

## 26.1 Begin with a promise worth protecting

“Make the app secure” does not identify a test. “A valid token for customer B must never reveal customer A's anniversary story” identifies an asset, an actor, a target and an unwanted outcome. It also tells us where to enforce the promise: the service that returns the story must validate the credential and filter the record by its owner.

List the assets before listing defenses. In this application, credentials and private request stories matter differently from public song titles. Local preferences can reveal account activity even when they contain no payment information. Export documents aggregate data that may otherwise be dispersed. Logs can become another sensitive data store. Build credentials can affect every package the business distributes.

An attacker need not be anonymous. A legitimate customer can supply a different request ID, call the API without the mobile interface or repeat a request far more often than normal. A lost/shared tablet introduces another actor. A compromised package source or build credential introduces a supply-chain path. Write down the capability being assumed instead of giving every actor unlimited powers by default.

OWASP MASVS provides useful mobile review families such as storage, authentication, networking, platform interaction and privacy. Use them to prompt questions. A chapter test list is not a MASVS assessment or certification, and the server needs its own verification beyond mobile controls.

## 26.2 Draw the boundary that makes an input trustworthy

![Figure 26.1. Untrusted links and callbacks enter the native boundary; the managed provider and SDK own authentication, while the API independently validates permission and owner. Local SQLite and platform storage have separate protection requirements. Passing one boundary does not authorize another.](../assets/figures/fig-26-trust-boundaries.png)

The running API currently exposes public catalog reads and one protected request-preview read. Its default customer store is empty. Tests inject fictitious records and ephemeral signing metadata. The native account/session examples and portable lifecycle workspace are separate labs; they do not yet form a completed authenticated customer product.

That inventory changes the threat model. We can test a cross-owner preview against real bearer middleware. We cannot claim to have tested a customer-file download route that does not exist. We can verify local SQLite rollback. We cannot infer native encryption or backup erasure from it. Keep implemented, simulated and planned boundaries visible on the same review record.

The companion threat model assigns T-IDs to abuse cases. Each row names the asset, control, executable evidence and residual work. Treat the register as living source alongside the code. When a later media feature introduces a new URL or file, revisit the affected boundary rather than appending a generic security paragraph.

## 26.3 Translate threats into controls and evidence

| Threat | Enforcement already present or added here | Evidence still required |
|---|---|---|
| B requests A's private story | Token validation, required scope and issuer/subject owner lookup | Real service data and deployment configuration |
| A route ID becomes a URL or path | Fixed API origin and bounded identifier alphabet | Actual native redirects/TLS behavior |
| A link resembles the publisher/provider | Exact reviewed host and callback checks; SDK validation | OS callback ownership and interception checks |
| An old account result arrives late | Session generation and workspace handle fencing | Native dispatcher, visible cache and focus behavior |
| Repeated authorized reads consume resources | Shared protected-read budget with no queue | Production load, fairness and shared-edge protection |
| Diagnostics expose private material | Allowlisted read-decision projection | Framework/proxy/provider log review and restricted retention |
| Removed data reappears | Local intent/freeze/receipt transaction in the workspace lab | Server, other-device, provider and backup cleanup |

Prioritize the paths that can expose another customer's data or credentials. A high-impact threat with an unverified boundary deserves a concrete owner and next observation. A severity word alone is not a mitigation. Conversely, do not add a large abstraction for a feature that has no current entry point; specify the invariant before implementing the later feature.

For the anniversary story, the first forbidden read matters even when it happens only once. Rate limiting cannot compensate for a missing owner filter. Encryption in transit cannot compensate for returning the wrong customer's record. A current session cannot compensate for publishing a result that belongs to a previous account.

## 26.4 Treat identifiers as data

The existing protected client accepted a small identifier alphabet before building its fixed API route. The server also needs that decision because an attacker can skip the client entirely. `RequestIdPolicy` now provides a shared, explicit contract in the portable networking namespace:

```csharp
public const int MaximumLength = 64;
public static bool IsValid(string? id) =>
    !string.IsNullOrEmpty(id) && id.Length <= MaximumLength &&
    id.All(c => char.IsAsciiLetterOrDigit(c)
        || c is '-' or '_');
```

The client and server both call this method, but sharing the source is not what enforces security. The server call remains necessary. A URL, query selector, encoded separator or filesystem path does not become a valid private request ID. The alphabet is intentionally narrower than some catalog navigation IDs; do not broaden it merely to reuse another helper.

In `Program.cs`, a scoped caller with an available budget permit gets a generic 400 for invalid ID shape before owner lookup. A validly shaped unknown ID and another owner's ID both get the existing generic 404. An actual owner gets the preview. Token validation and scope authorization happen earlier, so malformed input does not become a way to retrieve private data without authentication.

The new tests include malformed and oversized server IDs, path/URL-shaped private identifiers and provider/publisher lookalikes. Existing tests already cover other reviewed-link and SDK-state rejection cases; the threat register references those rather than pretending they were all newly implemented here.

## 26.5 Preserve the browser and transport boundaries

`NativeIdentitySettings.ValidateBrowserRequest` constrains the configured tenant destination, HTTPS port, authorization path and exact callback. `ProviderBrowser` hands the flow to the supported native authenticator, and the SDK owns protocol state and credential validation. Recognizing a callback scheme does not establish that the response belongs to the login attempt.

The new portable cases add changed callback paths, provider-host suffixes, user-information tricks and authorization fragments. Publisher links also reject a visually similar internationalized hostname and an unreviewed trailing-dot spelling. Those checks concern what the application is willing to launch. They do not prove which installed app receives an OS callback or how a real browser returns after cancellation.

For private reads, `ProtectedRequestClient` builds a URI from one configured HTTPS API origin and a validated identifier. It attaches the bearer credential to the individual request, not reusable default headers. The native HTTP handler disables automatic redirects. Existing tests reject redirect responses and obsolete leases. Keep those responsibilities together when replacing transport adapters.

Real TLS evidence must show that the intended device accepts the intended service and rejects an invalid certificate or unexpected destination. A loopback smoke and a test-host response do not establish that. Do not fix a development certificate problem by disabling certificate validation. If production later adopts certificate pinning, it also needs key-change, recovery and operational verification; this chapter does not add a pinning implementation.

## 26.6 Keep private responses out of ordinary caches

The API now sets `Cache-Control: no-store` for the protected request prefix before authentication and authorization. That covers private success as well as challenge, denial, invalid-input and rate-limit responses produced later in the pipeline.

```csharp
if (context.Request.Path.StartsWithSegments(
    "/api/v1/requests"))
    context.Response.Headers.CacheControl = "no-store";
```

The complete middleware continues to the next component after setting the header. Integration tests inspect successful and unauthorized responses, plus new 400/429 cases. This is a response-policy assertion. It does not establish that every reverse proxy or native cache behaves correctly, and it cannot recall data the application deliberately wrote elsewhere.

The visible preview also has account ownership. Clear or replace account-dependent presentation according to the session contract. Consider app-switcher snapshots, screenshots, notification previews and exported documents during native review. A header attached to an API response does not protect those other copies.

The public catalog has a different data classification and future caching policy. Do not use the private-prefix rule as evidence that all content should lose caching. Make the classification deliberate and test the relevant response contract.

## 26.7 Add a bounded read budget

`ProtectedReadSecurity` registers a named fixed-window limiter. The teaching policy permits eight authorized protected reads per minute within one API process and has no waiting queue. The limit is deliberately small enough for an integration test to exhaust without a load generator.

```csharp
options.AddFixedWindowLimiter(Policy, limiter =>
{
    limiter.PermitLimit = PermitLimit;
    limiter.Window = Window;
    limiter.QueueLimit = 0;
    limiter.AutoReplenishment = true;
});
```

`Program.cs` makes the order explicit: routing, private-prefix cache instructions, authentication, authorization, rate limiting and endpoint execution. The protected route requires both the existing authorization policy and the new named rate policy. Public health/catalog routes remain outside this budget.

This placement is a tradeoff. Missing or underscoped credentials return 401/403 without consuming the protected budget, so an anonymous caller cannot exhaust those permits directly. However, those calls still consume authentication resources. This is not an authentication-cost limiter, public-route protection or a DDoS solution. Deployment needs separately designed controls at the relevant earlier boundary.

The budget is shared across authenticated subjects. Changing subjects does not create a fresh partition or unbounded limiter entries, but one customer can reduce another customer's availability. The tests deliberately demonstrate that shared behavior; they do not certify fairness. Fixed windows can permit bursts around a reset, process restart resets counters and multiple service instances have separate counters. Production sizing and shared-edge enforcement need load evidence and an operational design.

## 26.8 Handle rejection without inventing success

When the protected budget is exhausted, the API returns 429, a generic problem response and a positive `Retry-After` value derived from limiter metadata. The endpoint does not look up or return the private story. Queue length zero means the request is not waiting inside this limiter for a later permit.

`ProtectedRequestClient` already treats a non-success private read as unavailable; it does not blindly refresh credentials on 429 or replay a customer mutation. An interface can explain that the customer should try later. It must not translate throttling into “request deleted,” “session expired” or an empty successful record.

The integration test spends eight permits, observes 429 on the next call and checks that public browsing still works. Another test switches to a second valid subject and still observes exhaustion. The tests do not sleep until the window resets, infer production throughput or simulate a volumetric attack. Their claim is narrowly about the configured middleware and route contract.

## 26.9 Record decisions without recording the story

A useful diagnostic event should answer a question without becoming a copy of the customer request. `ReadSecurityAudit` accepts an enum, maps it to four fixed strings and logs event 2601. Its outcomes are `invalid_identifier`, `granted`, `unavailable` and `rate_limited`.

```csharp
logger.LogInformation(
    new EventId(2601, "OwnedReadDecision"),
    "Owned request read: {Decision}", value);
```

The complete method rejects unknown enum values. It accepts no principal, request path, token, summary, account name or arbitrary caller message. Its minimalism is intentional: there is no sensitive write endpoint requiring a richer mutation audit in this sample.

The capture-provider test sends a fixture token, a private-looking query story, an account label and a malformed secret-looking identifier. It checks the exact custom event outputs and confirms those supplied values are absent. A 404 stays `unavailable`; it does not distinguish another customer's existing record in the event projection.

This is not a complete audit system. It does not record every 401/403, identify an operator, correlate deletion progress or provide immutable retention. Framework, hosting, proxy and identity-provider logs have separate schemas and may retain request information. Review those actual sinks independently. If later operations require account-linked audit data, define its purpose, access, tamper protection, retention and safe correlation rather than adding raw request objects to this logger.

## 26.10 Apply least privilege to the whole route

The native session requests the scoped capability used for the read, and the API requires that scope before owner lookup. The API does not accept a mobile display name as authority. There is no mobile client secret or embedded administrative credential that turns the public client into a trusted backend.

The tests generate private signing material per factory and inject static metadata only into that test host. The running API has no corresponding private signing key or seeded customer accounts. Keep that separation when extracting test utilities; a convenient fixture issuer must not become production token issuance.

Backend secrets belong to the backend deployment mechanism with bounded access and rotation. Development Secret Manager keeps values outside the source tree but does not encrypt them into a production secret store. Environment configuration is not automatically hidden from operators, crash output or process access. Avoid printing entire configuration or environment collections during diagnosis.

The repository workflows request read-only content permission. Future deployment credentials, artifact signing and hosted-service access need their own minimum scope and lifecycle. A successful compilation says nothing about whether a release credential was appropriately scoped or exposed in build logs.

## 26.11 Review packages and customer files before widening the system

A direct package reference can introduce many transitive packages. Review the resolved graph, not just the short project file. With the pinned SDK and a restored portable test project, the documented command is:

```powershell
dotnet package list `
    --project tests/GnazzosWorld.Core.Tests `
    --include-transitive --vulnerable `
    --format json --output-version 1 --no-restore
```

Repeat for API tests and the resolved native framework on its supported workstation. The portable solution does not cover every native SDK dependency. Record the source revision, SDK, date, feed availability, resolved versions, findings and decision. An unavailable advisory feed is unknown, and “no reported advisories” is not a proof that every package is safe. These chapter tests do not run an advisory or secret scan; the worksheet identifies that pending work.

Customer-file access is another future boundary. A request ID must not become a filesystem path, arbitrary URL or storage-container key supplied by the client. A delivery service should map an opaque authorized record to a controlled object, enforce the owner and define expiry/revocation for delivery. Unpredictable filenames alone do not grant permission. Check range requests, cached copies and alternate URLs when that feature exists. This API has no customer-file route to claim as verified today.

Local data remains part of the review. The Chapter 25 workspace is unencrypted and retains an account-linked deletion receipt without expiry. The earlier drafts and replica labs have separate limits. A protected session vault does not encrypt every database or remove backup copies. Record these as concrete production gaps, not as problems solved by a large automated-test total.

## Guided Lab: trace the first forbidden read

Use `docs/labs/ch26-security-verification.md`. Keep the actual bearer middleware enabled in API tests; the ephemeral metadata provides repeatability without replacing authorization with a fake success handler.

```powershell
dotnet build tests/GnazzosWorld.Core.Tests -c Release
dotnet run --project tests/GnazzosWorld.Core.Tests `
    -c Release --no-build
dotnet build tests/GnazzosWorld.Api.Tests -c Release
dotnet run --project tests/GnazzosWorld.Api.Tests `
    -c Release --no-build
```

1. Open T01 in `docs/security/threat-model.md`. Name the asset and the attacker capability: B has a valid account token and guesses A's request ID.
2. Follow `RequestAuthorizationTests` through signature/issuer/audience validation, required scope and owner-filtered lookup. Observe that changing the account query label does not change the owner.
3. Follow the new server identifier tests. An authorized caller with an available permit receives 400 for malformed shape; the response does not echo the submitted value.
4. Follow the budget test and observe the ninth protected request's 429 response. Verify that the authorization test establishes confidentiality before throttling enters the story.
5. Inspect the event-capture test. Verify only the intended category's projection, and explain why it does not establish that proxy logs are safe.
6. Map the earlier session/workspace failure tests to T04/T08. Write the native and remote observations they leave unresolved.
7. Add one new threat to the register with an owner and a concrete acceptance check. Do not label a proposed check as a performed test.

## Troubleshooting

| Symptom | Diagnostic check and corrective action |
|---|---|
| All reads succeed after the budget | Check endpoint policy attachment and middleware order; do not remove authorization to isolate the issue |
| B can exhaust A's availability | That is the shared-budget contract; design production fairness separately |
| ID rejected by client but accepted by server | Verify the server call to the shared policy; clients are bypassable |
| Log test passes but a proxy contains query text | Review that separate sink and retention; the custom projection test covers one category |
| 429 is shown as an expired login | Preserve HTTP failure meaning; do not refresh credentials merely for throttling |
| Package review cannot reach its feed | Record unknown and resolve access; do not report an empty scan as clean |
| Native test and portable result differ | Identify the platform boundary and keep both observations with source/device details |

## Verification record and Part V recap

At source `a3d2a880195714dc61a2971bc2ab3f7aab1d78a9`, portable Release compilation has zero warnings/errors and 360 cases pass, including 15 new boundary cases. API/probe builds are clean and all 46 API cases pass, including nine new protected-read cases. The public loopback smoke and both console labs also pass. Android compilation succeeds; its exact final/compiler and setup evidence is recorded separately in `docs/verification.md`. The new API cases exercise real middleware for identifier rejection, cache instructions, budget exhaustion, public-route availability and decision projection. Portable additions cover relevant lookalike destinations and private-ID bounds. Existing signed-token, SDK-state, session-generation and real SQLite tests remain part of the suite.

Part V's evidence has several levels. Session/ownership rejection and portable persistence have executable evidence. Live provider login, MFA/recovery, native secure storage and full export/deletion still need their documented observations and service composition. No test total closes those gaps. The current package-advisory/secret review, production load controls and customer-file delivery remain pending too.

This chapter ends the initial Part V draft with a reviewable threat register and smaller, enforceable contracts. Before public release, assign owners to the remaining records and require the appropriate observations. When Part VI introduces playback, downloads, notifications and platform integration, reuse this method to identify the new data and boundaries instead of assuming earlier authentication solves them.

## Chapter Summary

Threat modeling connects a valuable promise to the actor who could break it, the boundary that must enforce it and the evidence that can support the claim. The protected preview now shares a bounded ID policy with its client, sends no-store instructions, limits authorized reads through a bounded process-local budget and records fixed decision events. Tests verify those behaviors without replacing real bearer middleware. The review also preserves unresolved work: native callback/TLS/storage observations, production fairness and traffic controls, dependency/secret scans and complete lifecycle/file delivery. Security claims remain scoped to their evidence. Part VI begins with authorized media playback, where URLs, file permissions, background behavior and account-owned progress add new boundaries to examine.

## Exercises

### Worked exercise: eight safe denials are still not authorization

B guesses A's ID and receives 404. After repeated reads, B receives 429. A developer proposes removing the owner filter because the limiter stops repeated guessing. What changes?

**Worked answer:** The first allowed read could disclose A's data before the budget is exhausted. Keep token, permission and owner enforcement on every request. The limiter reduces downstream repetition; it does not decide who owns the record. The cross-owner test must continue passing when a fresh budget is available.

### Worked exercise: the audit event is safe, the request log is not

Event 2601 contains only `granted`, but an access log includes the customer story from a query parameter. Did the projection test fail to test its own contract?

**Worked answer:** No. It tested one category's explicit projection. The access log is another sink requiring separate design and inspection. Avoid sending private stories in URLs, configure that sink's collection/redaction and access, and add an appropriate verification record. Do not expand the custom event to copy the query while investigating it.

### Independent extensions

1. Design an account-aware production read policy. Include partition-cardinality bounds, fairness, multiple instances, authentication cost and recovery after a limiter-store failure. Identify which outcomes require load or deployment evidence.
2. Add a hypothetical delivery route to the register. Specify owner checks, controlled storage lookup, URL expiry, range requests, removal and caching.
3. Perform the package review on a supported workstation. Record an unavailable feed as unknown and a reported advisory with its affected resolved dependency path. Propose a bounded correction and the relevant verification before updating packages.

## Official references

- OWASP, using MASVS and control families: https://mas.owasp.org/MASVS/03-Using_the_MASVS/
- Microsoft, rate-limiting middleware: https://learn.microsoft.com/aspnet/core/performance/rate-limit
- Microsoft, package inventory and vulnerability reporting: https://learn.microsoft.com/dotnet/core/tools/dotnet-package-list
- Microsoft, development secret handling: https://learn.microsoft.com/aspnet/core/security/app-secrets

The retrieved rate-limit and secret-handling guidance uses the .NET 10 documentation view. It supports general design and setup guidance; the pinned .NET 11 implementation is evaluated through its own compilation and test record.

Index: threat model; trust boundary; request identifier; cache control; rate limit; audit projection; least privilege; dependency review; secret management; customer-file authorization; MASVS.
