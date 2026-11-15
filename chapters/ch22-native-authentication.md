# Chapter 22
# Native-App Authentication and Managed Identity

A reader opens Gnazzo's World to find Northern Lights. Browsing should remain straightforward. Later, that reader may choose to sign in so a future private draft or saved position can be associated with a real account. The second action introduces a trust boundary; it should not make the first action depend on a successful login.

Chapter 21 selected a simulated account to test synchronization. That was useful for protocol behavior, but anyone running the fixture could choose its account string. Now we introduce a managed identity provider and a maintained native-client SDK. The application delegates interactive authentication instead of collecting the reader's password or interpreting a callback as proof by itself.

The provider example is **Auth0**, using **Auth0.OidcClient.MAUI 1.4.0**. The source includes an optional Account page, public client configuration, platform callbacks, cancellation handling and portable checks. It intentionally ships without a configured tenant. No completed provider sign-in, MFA enrollment or native screenshot is claimed until the documented setup and device checks have actually been performed.

## What You'll Learn

By the end of this chapter, you will be able to:

1. Explain the roles of a native public client, a hosted identity provider, a browser callback and a protected API.
2. Configure the example's public settings and exact platform callback without placing a client secret in the mobile app.
3. Delegate authorization-code, PKCE and OpenID Connect validation to the provider SDK while retaining clear application-state ownership.
4. Handle cancellation, duplicate taps, incomplete results and late callbacks without publishing an unintended local identity.
5. Distinguish presentation tests, protocol-engine rejection checks, Android compilation and a real provider/device round trip.

**Prerequisites:** Chapters 17–21 and a verified Android MAUI workstation for native exercises. Portable checks require the SDK in `global.json`, without a mobile workload. The previous companion checkpoint is `d4010432b77bd677e911bf658f233987e665ea59`. The corrected implementation is `13b32a90075de1d1bd8701237c61f404253f707d`; consult `docs/verification.md` for any correction and its executed evidence. Completing the hosted sign-in exercise also requires an Auth0 development tenant and disposable test user that you control.

**What you will build:** A native SDK adapter and Account page that can initiate hosted sign-in after configuration, plus portable state and invalid-callback checks. The distributed app remains unconfigured. The resulting identity is kept only for the process; persistent tokens, authenticated API calls and account-linked synchronization belong to Chapter 23. No existing favorite or draft is silently reassigned to the signed-in reader.

## 22.1 Identify the decision before choosing a token

Authentication answers a question about identity. Authorization answers whether that identity may perform a particular operation on a particular resource. Showing a reader's name after sign-in establishes neither ownership of an anniversary-song request nor permission to download a customer delivery.

The app is a public client: people can obtain and inspect its package. Public settings such as provider hostname, client ID and callback address identify its registration; they are not a client secret. Obfuscating a shared secret inside a mobile binary would not turn it into a confidential server application.

A managed provider supplies the hosted authentication experience and account policies. Our code still owns when sign-in starts, what the UI displays, what happens after cancellation, and which local data is associated with an account. The backend must later validate credentials and enforce ownership independently of those presentation decisions.

| Item | Job in the architecture | What it does not establish |
|---|---|---|
| Public client ID | Select the provider's native application registration | A private credential embedded in the app |
| Browser callback | Return a protocol response to the native client | A validated identity by itself |
| ID token | Supply validated identity information to its intended client | Permission to call a customer API |
| Access token | Carry an authorization credential for its intended resource | Permission to access every customer's record |
| Local display name | Help the reader recognize the current UI context | A stable account key or an MFA guarantee |

This chapter requests basic identity scopes and does not expose tokens to its view model. A future API requires its own audience, policies and ownership checks. Keep that next decision visible rather than treating the first successful login as a universal key.

## 22.2 Follow the browser journey

![Figure 22.1. The app asks its SDK to begin sign-in; the system browser presents the provider; the platform returns the response to the SDK; only an accepted result may update process-local identity. Cancellation or rejection leaves anonymous browsing available.](../assets/figures/fig-22-native-signin.png)

The reader taps Sign in with provider from the Account page. The SDK prepares an authorization-code request with transaction-specific correlation and PKCE information. The platform browser displays the provider's hosted experience. A return URI routes the response back to the application, where the SDK completes its protocol checks before our adapter projects the result into a reader identity.

PKCE binds the eventual code exchange to the attempt that created its verifier. State correlates the authorization response with the attempt; OpenID Connect adds identity-token validation and nonce-related protections. They have different purposes. A matching custom URI scheme does not replace any of them.

Our app does not generate its own authorization URL, implement a token endpoint exchange, decode a JWT to establish identity, or write a password form. The provider SDK and its underlying OpenID Connect engine own those protocol operations. The browser adapter adds application-specific destination and cancellation boundaries; it is not a replacement security protocol.

**Worked reasoning:** A string arriving at the callback with `code=example` is still untrusted input. If its state belongs to another attempt, it must not advance the interface to "signed in." The portable engine check exercises that rejection with static metadata and a no-network handler. It does not establish a successful login or a valid production token.

The native-app browser recommendations in RFC 8252 and the PKCE mechanism in RFC 7636 explain the separation. They also make the custom-scheme limitation relevant: another application may register a competing scheme. A reverse-domain name reduces accidental collisions but does not prove exclusive ownership. Production evaluation should include platform-supported claimed HTTPS return links and provider support, with their own device evidence.

## 22.3 Use a provider deliberately

Auth0 is the concrete teaching provider because it supplies a documented MAUI SDK and a hosted login path. That choice makes the walkthrough reproducible without introducing a homegrown identity server. It is not a claim that its pricing, enrollment options or MFA policies fit every reader or organization.

The project pins the MAUI package to 1.4.0. Its official quickstart describes earlier .NET targets; the repository's .NET 11 build is a separate compatibility check. A package restore or computed NuGet compatibility entry is not a guarantee about every OS, device or provider feature. Record the exact package, runtime and native observations used for this book.

Before provisioning a development environment, review current service terms, relevant MFA availability, tenant limitations and optional costs. Use a tenant you control and a disposable reader account. Do not supply a real customer's story to prove that a login screen opens. The public catalog exercises remain available while provider setup is pending.

### Register the native application

In the Auth0 Dashboard, open Applications > Applications and create an application of type **Native**. Configure its Allowed Callback URLs with exactly:

```text
com.johngnazzo.gnazzosworld://callback/
```

Save the settings and note the application's Domain and Client ID. Confirm that an appropriate development login connection is enabled. Never copy the application's client secret into the mobile project. This chapter does not invoke provider logout, so it does not require a logout return address; Chapter 23 must configure and verify that separate journey when it is implemented.

The callback's trailing slash is part of the example. Keep the provider registration, SDK setting and platform handler consistent. If the provider rejects the return address, diagnose the exact mismatch instead of adding broad wildcards to make the error disappear.

## 22.4 Keep public configuration bounded

`src/GnazzosWorld.App/Identity/AuthenticationConfiguration.cs` ships with `Current` set to null. That means the sample can compile and browse without a tenant. Pressing Sign in explains what configuration is missing rather than sending a request to an invented provider.

After creating your own registration, replace null with your public settings:

```csharp
public static NativeIdentitySettings? Current { get; } =
    new("your-tenant.us.auth0.com", "YOUR_PUBLIC_CLIENT_ID");
```

This is the complete property declaration to place inside the existing configuration class; the illustrative strings must be replaced. Use the actual lowercase hostname without a scheme, port or path. The value is not a password. A deployment pipeline can later supply environment-specific public configuration, but it should preserve the same reviewed boundary.

The portable `NativeIdentitySettings` validates those inputs and exposes the expected issuer. This teaching configuration accepts standard `.auth0.com` tenant domains. It deliberately does not accept an arbitrary URL or automatically support custom domains. Adding a custom domain requires a controlled configuration change and matching validation, not trusting a destination supplied by a deep link.

`ValidateBrowserRequest` checks that the SDK's start address uses HTTPS on the configured host, on the expected authorize path, and that its requested return address equals our callback. This limits what the browser adapter launches. It does not validate the returned authorization code or state; the SDK still owns those checks.

**Example diagnostic:** `https://demo.auth0.com.evil.example/authorize` is not a request to `demo.auth0.com`. Comparing a substring would accept a different host. Parse the URI and compare its host, scheme and path under the declared policy. The tests include wrong destinations and a changed callback so those boundaries remain executable.

## 22.5 Register the platform return path

Android needs an exported callback activity so the operating system can deliver the browser return. The complete file is `src/GnazzosWorld.App/Platforms/Android/AuthenticationCallbackActivity.cs`. Its intent filter specifies the example's scheme, host `callback` and root path. The Android manifest also declares the Custom Tabs service query required by the browser integration.

The activity delegates to MAUI's `WebAuthenticatorCallbackActivity`. It does not look up an account, accept a user ID from a query string or set a signed-in Boolean. Routing and authentication remain separate decisions. An exported entry point is expected for this OS interaction, which makes the SDK's correlation checks essential.

For iOS, `Platforms/iOS/Info.plist` registers the custom URL scheme. The source is present, but compilation, signing and browser return behavior require the Mac and device workflow described earlier. The presence of a plist entry in Git cannot establish that an iPhone successfully returned from hosted login.

When changing application identity or callback addresses for another product, update the configuration constant, Android filter, iOS registration and provider registration together. Test a valid return and an unsolicited or mismatched return on each platform. Do not assume Android observations fill an iOS verification row.

## 22.6 Adapt the SDK without leaking its result

`src/GnazzosWorld.App/Identity/Auth0InteractiveSignIn.cs` implements the portable `IInteractiveSignIn` contract. It creates the provider client only when configured sign-in is actually attempted. The SDK receives these application decisions:

```csharp
Domain = settings.Domain,
ClientId = settings.ClientId,
RedirectUri = NativeIdentitySettings.Callback,
Scope = "openid profile",
LoadProfile = false,
Browser = browser,
EnableTelemetry = false
```

This is an initializer excerpt from the complete adapter, not a standalone program. The surrounding code owns `settings`, `browser`, the SDK instance and error handling. `openid profile` limits the initial request to identity information; this chapter does not request offline access or a customer-API audience. The explicit telemetry option is a sample configuration choice, not a claim that the provider or operating system performs no logging.

After successful SDK processing, the adapter projects the result into `SignedInReader`: issuer, subject and a bounded display name. It does not return the raw token response to the Account page. Issuer and subject identify the account boundary; email and display name can change and are not suitable permanent record keys.

The adapter reads the validated principal returned by the SDK, rather than parsing a token itself. If the required subject is absent, it rejects the result. If an optional name is unsuitable for display, it uses a neutral label. The presentation layer also checks its expected issuer and bounded identity shape before updating its process state. Those application checks supplement the provider validation; they do not prove a token signature independently.

The token-bearing SDK result exists transiently during processing and is neither logged nor persisted by our adapter. This is narrower than a claim of secure durable session management. Chapter 23 must define storage, expiration, renewal and API authorization before those features are enabled.

## 22.7 Make cancellation reach the browser

The pinned SDK's default MAUI browser implementation accepts a cancellation token but does not forward it to the platform authentication call. That detail matters to an application which promises to cancel a pending attempt. We therefore provide `ProviderBrowser`, a small implementation of the SDK's browser interface.

The adapter validates the start and end destinations, then calls MAUI WebAuthenticator with the supplied cancellation token. It returns the platform properties in the response format expected by the SDK. An operation-canceled result is classified as browser cancellation, not a successful identity. No authorization URL or token validation is reimplemented in this layer.

`SignInSession` keeps only one active attempt. Duplicate taps cannot open another browser. An explicit Cancel button requests cancellation; leaving the Account page also requests cancellation. Those requests must still be observed on the real platform: a portable canceled task does not establish how an Android browser tab closes or how an iOS authentication sheet behaves.

A generation counter protects a different boundary. Forgetting local identity increments that counter and cancels the pending attempt. If a provider or test double later returns success anyway, the older generation cannot repopulate the local identity. Cancellation asks work to stop; result ownership decides whether its eventual completion is still relevant.

The source's presentation operations are intended to be called on the UI thread. Awaiting the native command preserves that context for visible changes. A future background caller must marshal presentation updates deliberately. The single-attempt guard is not a promise that all observable properties form a general-purpose multithreaded session cache.

## 22.8 Provide an honest Account page

Home now links to Account and sign-in. The existing Home and Discover routes remain public. `MauiProgram.cs` registers one provider adapter and one `SignInSession`, while the Account page receives that shared session through dependency injection.

The page displays anonymous or process-local identity, a status message, Sign in with provider, Cancel pending sign-in and Forget local sign-in. These labels are deliberate. The last action clears the app's current identity projection; it does not claim to end the provider's browser session, revoke tokens, delete an account or erase every local draft.

A reader who signs in again may therefore encounter a remembered provider session. That is not proof that local clearing failed. It shows that browser-session state and application state have different owners. Chapter 23 will explain the complete sign-out contract and how to verify each affected layer.

The page is a minimal native integration surface, not the finished account experience. It has meaningful headings and bounded messages, but native focus, status announcements, large text and cancellation still need device testing. Screenshots must come from that actual interface using fictitious profile data. Figure 22.1 cannot stand in for a photographed or captured native result.

## 22.9 Guided lab: build, configure and observe

The companion's `docs/labs/ch22-identity.md` contains the setup checklist and native result matrix. Begin at the recorded source checkpoint and run the portable checks from the repository root:

```powershell
$tests = "tests/GnazzosWorld.Core.Tests"
dotnet build $tests -c Release
dotnet run --project $tests -c Release --no-build
```

Then use the existing Windows Android build workflow or your verified workstation to compile the MAUI app. Portable success and Android compilation are separate results. A configured provider round trip adds another result rather than replacing either one.

1. Leave the distributed configuration null. Follow the Account route and verify its configuration message while Home and Discover remain available. Record the device result; do not mark it passed from the source alone.
2. Inspect `NativeIdentitySettings.cs`, `SignInSession.cs` and the provider adapter. Identify which component owns configuration, the browser boundary, protocol validation and visible identity.
3. Register your development Native application and enter its public hostname and client ID. Rebuild after changing the source configuration. Confirm that the compiled callback and dashboard return address agree exactly.
4. Run on the chosen device and initiate hosted sign-in with a disposable user. Record browser launch, provider completion, application return and the displayed identity separately. Keep passwords, codes and token responses out of the record.
5. Repeat with browser cancellation and with Cancel pending sign-in. Confirm that no identity appears, a later attempt remains possible and the catalog continues to work. Repeat after leaving the Account page during the operation.
6. Clear local identity, then sign in again. Explain any remembered browser session without claiming that the earlier button performed remote logout. Restart the app and confirm that the chapter's process-only identity is absent.
7. Complete the Android and iOS rows independently. Leave unavailable rows pending. A build artifact and a fixture reply do not fill a real-provider or physical-device row.

Do not weaken SDK validation to make an incomplete setup appear successful. If the browser never returns, inspect the registered callback and platform filter first. If the SDK rejects the result, keep the reader anonymous while collecting an appropriately sanitized diagnostic category.

## 22.10 Test what the current boundary can prove

`SignInTests.cs` supplies simulated provider replies to exercise presentation ownership. Its cases cover duplicate taps, cancellation, retry, invalid identity shape, sanitized errors and a late success after local clearing. A fake success is useful to test the UI state machine; it does not authenticate anyone.

`OidcEngineTests.cs` uses the same underlying OpenID Connect engine version as the pinned MAUI package. Static provider metadata replaces discovery, and a no-network handler records any attempted token request. The cases supply an unrelated state, a response without an authorization code and a canceled browser result. They must report failure without producing identity or exchanging a code.

The test fixture does not supply a valid token or disable production validation. Its discovery-only metadata setting exists to isolate these early rejection paths. Passing those checks does not establish live discovery, key retrieval, token validation against the real tenant or native callback routing.

| Evidence | What it establishes | Additional check still needed |
|---|---|---|
| Presentation tests | Ownership and messages under simulated outcomes | Native layout, focus and real provider behavior |
| Protocol-engine rejection tests | Invalid transaction responses do not reach the token handler | Valid signed tokens from the configured provider |
| Android compilation | Source and selected dependencies compile for that target | Installed app, browser return and lifecycle behavior |
| iOS configuration source | The scheme registration is recorded | Mac build, signing and iPhone observations |
| Hosted sign-in observation | The recorded tenant/device journey completed | Protected API authorization, renewal and account isolation |

At corrected companion revision `13b32a90075de1d1bd8701237c61f404253f707d`, Windows CI passed all 307 portable cases, including 23 new Chapter 22 cases, and Android compilation completed with zero final compiler warnings or errors. The existing API regression workflow also passed at the initial implementation; see `docs/verification.md` for exact runs and scope. The last row is pending until a configured tenant and native run are available. The chapter's implementation and verification log must retain that limitation even if every portable check is green.

## 22.11 Troubleshoot without exposing credentials

| Symptom | Inspect | Corrective action |
|---|---|---|
| Configuration message appears | Public settings in the built revision | Supply public development settings and rebuild |
| Provider rejects return URI | Exact callback string, including trailing slash | Correct dashboard and platform registration together |
| Browser opens but never returns | Android intent filter or iOS scheme and OS behavior | Test the platform return path; preserve pending status |
| A previous user is remembered | Provider browser-session state | Distinguish local clearing from provider logout |
| Cancel appears to do nothing | Token reaches `ProviderBrowser`; platform run recorded | Diagnose native cancellation rather than publishing success |
| Old attempt signs in after local clearing | Generation ownership at completion | Ignore the obsolete result and preserve anonymous state |
| Name appears but private API fails | API audience, validation and ownership policy | Implement Chapter 23; do not use the ID token as an API credential |

Messages shown to readers are intentionally general. Raw provider exceptions can include callback data or other sensitive context. Diagnostic records should use bounded categories and approved identifiers, while keeping tokens, passwords, OTPs, recovery codes and personal stories out of routine logs.

## Chapter Summary

Native authentication combines provider, browser, platform and application responsibilities. A public mobile client cannot keep a shared secret, so this chapter delegates hosted authorization-code sign-in and OpenID Connect validation to a maintained SDK. Public configuration and exact callback registration make the return path explicit. The application owns one pending attempt, requests cancellation and rejects obsolete completions before publishing process-local identity. Anonymous catalog browsing remains available. Presentation doubles and protocol-engine rejection tests exercise specific boundaries, while compilation establishes compatibility only for its recorded target. A live tenant round trip, iOS execution and native screenshots require separate observations. The resulting identity is not yet a persistent session, an MFA guarantee or authorization to access customer records. Chapter 23 connects those concerns through session management and independent API enforcement.

## Exercises

### Guided exercise: a late successful reply

Read `Forgetting_local_identity_fences_a_late_success_even_if_provider_ignores_cancel`. Predict the visible state when the test provider returns success after Forget local sign-in.

**Worked answer:** The generation has changed. The earlier attempt no longer owns the result, even if its provider ignored the cancellation request. The session leaves its reader empty, preserves the local-clearing message and permits a later attempt after the older operation unwinds. Checking only whether a task returned success would repopulate identity incorrectly.

### Guided exercise: separate the callback checks

A browser return reaches the expected scheme but contains state from a different attempt. Which component should reject it, and what does a passing destination guard prove?

**Worked answer:** The SDK's transaction validation must reject the unrelated state. The destination guard only constrains the addresses used to launch and return from the browser integration. Native routing gets the message to the process; it does not authenticate its contents. Run the engine rejection case and verify that no token request occurs.

### Independent extension

Design a provider test record that captures valid sign-in, browser cancellation, app interruption and retry on both target platforms without retaining tokens or credentials. Define which screenshots can be safely published and which account fields must be fictitious. Then propose a claimed-HTTPS callback configuration, including domain association and provider requirements, while retaining the tested custom-scheme example until the replacement is actually verified.

## Native verification record

Keep one record per platform and source revision. The reader should be able to tell which result came from an actual device and which came from a controlled test. Use a disposable profile when gathering publication screenshots.

| Record field | What to enter after the check |
|---|---|
| Source and environment | Commit, SDK, package versions, device and OS |
| Provider setup | Development tenant/application reference; no secret or password |
| Successful return | Observed browser launch, completion, app return and local identity |
| Cancellation | Browser Cancel and app-requested cancellation as separate observations |
| Interrupted attempt | Navigation away, late result and the final anonymous state |
| Local clearing | Identity removed locally; any remembered browser session documented |
| Screenshot | Actual app state, fictitious display name and accessible caption |

Leave a field pending when it has not been observed. Do not record a real callback URL containing a code, a token response, a password, an OTP or a recovery code. If a provider error requires investigation, retain only an approved category and suitably sanitized reference.

This record is an acceptance worksheet, not evidence that the journey has been completed. A real provider result must be added before this chapter's hosted-login walkthrough is considered verified. The application can remain useful for public browsing while those checks are outstanding.

## Official references

- Auth0 MAUI quickstart: https://auth0.com/docs/quickstart/native/maui
- Pinned SDK package: https://www.nuget.org/packages/Auth0.OidcClient.MAUI/1.4.0
- SDK source at the selected release: https://github.com/auth0/auth0-oidc-client-net/tree/maui-1.4.0
- MAUI WebAuthenticator: https://learn.microsoft.com/dotnet/maui/platform-integration/communication/authentication
- Native-app OAuth guidance: https://www.rfc-editor.org/rfc/rfc8252
- PKCE: https://www.rfc-editor.org/rfc/rfc7636
- ID-token purpose: https://auth0.com/docs/secure/tokens/id-tokens

Provider documentation and package metadata were inspected for the implementation. Their earlier-target examples do not substitute for this book's recorded .NET 11 compilation and native verification. Recheck current provider and platform instructions when completing the pending device matrix.

## Editorial index terms

Native public client; managed identity; Auth0; OpenID Connect; authorization code; PKCE; state; nonce; callback URI; issuer; subject; ID token; access token; browser cancellation; generation ownership; local identity clearing; provider session; anonymous browsing.
