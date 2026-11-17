# Glossary and Acronyms

Definitions follow this book's application and verification vocabulary. Chapter pointers identify the primary discussion; they are not final print-index page numbers. A broader platform term can have additional meanings outside this project.

## A-C

**Acceptance evidence.** An observation tied to a requirement, identified source/artifact and named conditions. Different evidence layers establish different claims. See Chapters 1 and 36.

**Access lease.** The companion's token-plus-generation value used to reject work belonging to an earlier local session. It does not replace server credential validation. See Chapter 23.

**Accessibility.** The ability to complete the intended interaction using supported input and assistive technologies, text settings and layouts. A source-color calculation or screenshot alone does not establish it. See Chapters 10 and 37.

**AOT (ahead-of-time compilation).** Compilation performed before runtime. NativeAOT is a particular deployment model with its own compatibility requirements; do not use the terms as proof that a package was published or tested. See Chapters 37 and 40.

**API (application programming interface).** A contract through which components interact. In this book, an HTTP API is the server boundary; a C# interface can describe a different, process-local boundary. See Chapters 17-18.

**Artifact.** A produced file or package, such as a signed client, archive, symbol set or bounded report. Retain its identity and intended audience. See Chapters 38-40.

**Authentication.** Establishing the identity represented by a credential through a supported validation process. It does not by itself permit access to every resource. See Chapter 22.

**Authorization.** Deciding whether a validated identity may perform the requested operation on the requested resource. Enforce the decision at the trusted server boundary. See Chapters 23 and 26.

**Background execution.** Work governed by platform lifecycle and resource policies while an application is not foreground-visible. An ordinary task is not permission for unlimited background work. See Chapters 20 and 28.

**Bearer token.** A credential whose possession can permit access under its validated scope and lifetime. Keep it out of logs and public reports. See Chapter 23.

**Binding.** The connection between a view property and its data source. It coordinates presentation; it does not create persistence or authorization. See Chapter 7.

**Bundle or package identifier.** The platform application identity used in installation, signing and update relationships. A display title is a separate property. See Chapters 38-39.

**Callback.** A later invocation that reports or completes an operation. Native identity callbacks also involve registered URL/redirect configuration. See Chapters 22 and 30.

**Cancellation.** A request to stop cooperative work. It does not undo a remote commit or independently prevent every stale result. See Chapters 13, 17 and 32.

**Candidate.** The identified source, configuration and artifacts proposed for evaluation or release. A corrected build is a new candidate observation, even if the display version is unchanged. See Chapter 40.

**Checkpoint.** A deliberately retained recovery or source position. A playback checkpoint contains media identity/revision and position; a source checkpoint identifies code for a chapter. See Chapters 27 and 40.

**CI (continuous integration).** Automated checks triggered by repository events or an explicit workflow invocation. Read their actual triggers, inputs and scope before inferring a result. See Chapter 40.

**Claim.** In identity code, a statement carried by a validated credential, such as issuer, subject or scope. In editorial verification, a statement requiring suitable supporting evidence. See Chapters 23 and 36.

**Conflict.** A condition in which an operation cannot safely apply under the expected state or version. The correct response can require reconciliation rather than an automatic retry. See Chapters 21 and 34.

**Contract.** The agreed shape, constraints and behavior at a boundary, including failure and compatibility rules. A type declaration alone may not express all of it. See Chapters 12 and 18.

**Correlation identifier.** A bounded value used to associate related diagnostic observations. It is not a credential, an authorization decision or a substitute for preserving the original operation identity. See Chapter 35.

## D-I

**Debounce.** Delaying a reaction while input is changing, then applying the eligible latest input. Cancellation and result ownership still need explicit handling. See Chapter 13.

**Deep link.** A route into a particular application destination. Validate its shape and apply normal authentication/ownership checks before showing protected detail. See Chapter 30.

**Dependency injection (DI).** Supplying dependencies through construction/composition rather than creating them invisibly inside a component. Lifetime and ownership still need deliberate design. See Chapters 5 and 7.

**Deterministic fixture.** Invented controlled input that makes a scenario repeatable. A fixture result does not establish live provider or native behavior outside the boundary it controls. See Chapters 5 and 36.

**DTO (data transfer object).** A type used to carry data across a boundary. Its validation and compatibility rules must match the receiving contract. See Chapters 17-18.

**Entitlement.** A signed Apple-platform declaration participating in capability authorization. Source declarations, profile permissions and final signed output must agree appropriately. See Chapter 39.

**ETag.** An HTTP entity validator used to identify a representation. The downloader uses validator/revision relationships to avoid combining bytes from different content. See Chapter 29.

**Explicit save.** A persistence promise confirmed after a requested write succeeds. Later unsaved edits are not automatically included in that promise. See Chapters 1 and 15.

**Fixture authority.** The deliberately narrow ability of a teaching tool to prepare invented state. A synthetic fulfillment tool's capability is not production administration or a customer privilege. See Chapters 33-34.

**Forward recovery.** Repairing compatibility or state through a controlled later change, rather than assuming an older binary or backup reverses every side effect. See Chapter 40.

**Generation.** A monotonically changing identity used to distinguish current work or recovered server state. Local session generations and restored-server generations serve different boundaries. See Chapters 23 and 35.

**Hash.** A digest used here to compare candidate bytes or canonical input identity. Hashing does not encrypt private content or independently attest its producer. See Chapters 29, 32 and 40.

**HTTP.** The request/response protocol used by the companion API. HTTPS adds TLS protection; correct endpoint identity and trust still matter. See Chapters 17-18.

**Idempotency key.** The stable operation identity used by the application's replay protocol to reconcile repeated submissions. A new key after uncertainty can represent new work. See Chapters 16 and 32.

**Immutable snapshot.** A selected view of data intended to remain stable for its operation or revision. Verify collection ownership rather than infer deep immutability from a record keyword. See Chapters 12 and 37.

**In-process test.** A check executed without the intended external process/transport boundary. TestServer exercises the API pipeline but does not establish a real network socket or certificate path. See Chapters 18 and 36.

**Issuer.** The authority that issued a credential, represented by the validated identity configuration/claim. Combine it with subject when defining the owner's identity. See Chapter 23.

## J-R

**Journal.** Durable local information used to recover or reconcile an unfinished operation. The pending order journal preserves the original acceptance identity across interruption. See Chapter 32.

**JSON.** The serialized data format used by selected contracts. Valid JSON syntax alone does not satisfy field, size, ownership or business rules. See Chapters 17-18.

**JWT (JSON Web Token).** A token format used by the selected API identity integration. Decoding its payload is not signature, audience or lifetime validation. See Chapter 23.

**Lease fencing.** Rejecting a result whose captured lease/generation no longer belongs to the current session. The server must still enforce its own authorization. See Chapters 23 and 32.

**Lifecycle.** The platform-controlled transitions affecting visibility, activity and possible termination. Preserve valuable state without relying on one final callback. See Chapters 1, 8 and 20.

**MAUI.** .NET Multi-platform App UI, the shared application framework used for the phone/tablet implementation. Shared source does not erase native tooling or runtime requirements. See Chapters 1 and 3.

**MFA (multifactor authentication).** A provider-enforced identity journey using the configured factors and recovery policy. A local biometric unlock is not automatically the same protection. See Chapter 24.

**Migration.** A controlled change to a persistent schema/data representation. It must preserve the promised customer state or fail deliberately without destructive ambiguity. See Chapters 19 and 40.

**MVVM.** Model-View-ViewModel, a presentation organization separating bound view state/actions from the visual controls. It does not guarantee correct cancellation or thread access. See Chapter 7.

**Native observation.** Behavior actually observed through the intended platform/device path. Compilation or a portable double cannot stand in for it. See Chapters 36-39.

**OAuth/OIDC.** OAuth authorization and OpenID Connect identity protocols used through the selected supported SDK/provider. The sample does not implement its own password or one-time-code service. See Chapter 22.

**Operation identity.** The stable identifier of one intended business action across uncertainty and retries. A diagnostic correlation ID can serve a different purpose. See Chapters 32-35.

**Owner partition.** A storage or access boundary associated with the intended owner and relevant service scope. An anonymous partition string is not authenticated identity. See Chapters 19 and 25.

**PKCE.** Proof Key for Code Exchange, a protocol mechanism used by supported native sign-in flows. Use the selected SDK's implementation rather than constructing a substitute from a diagram. See Chapter 22.

**Provisioning profile.** Apple-platform configuration connecting application/team, signing context and permitted capabilities for a distribution channel. See Chapter 39.

**Range request.** An HTTP request for selected representation bytes. Safe resume additionally requires validator/revision and final integrity checks. See Chapter 29.

**Readiness.** The application's decision about whether the selected service state can handle its intended work. Basic process liveness does not establish schema or restored-generation readiness. See Chapter 35.

**Receipt.** A response or retained observation describing an operation's result under a specific contract. Synthetic Chapter 40 fixture receipts are declared examples, not authenticated test attestations. See Chapters 32 and 40.

**Reconciliation.** Resolving uncertain local and server knowledge while preserving intended operation identity and ownership. It differs from blindly repeating a new request. See Chapters 21 and 32.

**Replay.** Repeating a previously identified operation or event. Correct deduplication depends on matching identity and content under the contract. See Chapters 32-33.

**Revision.** An identity for content, an expected state version or a source commit, depending on context. Use the correct subject when comparing it. See Chapters 18, 27 and 40.

**Rollback.** Returning selected code or state to an earlier version. It does not automatically undo migrations, external transactions or downloaded data. See Chapter 40.

## S-Z

**Scope.** In identity, a granted permission category. In verification, the precise behavior and conditions an observation establishes. A requested identity scope is not automatically granted. See Chapters 23 and 36.

**Signing identity.** The controlled key/certificate relationship used to sign an application. A public fingerprint identifies a certificate without conveying its private signing authority. See Chapters 38-39.

**SQLite.** The embedded relational store used by several teaching persistence boundaries. A file-backed store still needs migration, concurrency, privacy and recovery decisions. See Chapters 19 and 32.

**Stale result.** A response belonging to an earlier query, page visit, media selection or account session. It may be technically successful while no longer permitted to update current state. See Chapters 13 and 23.

**Subject.** In identity, the validated identifier within an issuer's namespace. In artifact/evidence discussion, the particular source/package/environment to which an observation applies. See Chapters 23 and 40.

**Synchronization.** Exchanging state between replicas under a defined conflict/replay protocol. Connectivity alone does not establish consistent or authorized state. See Chapter 21.

**TestFlight.** Apple's beta-distribution path used in the iOS release procedure. Processing, tester installation and observed application behavior remain distinct gates. See Chapter 39.

**TLS (Transport Layer Security).** The transport protection underlying HTTPS. Certificate trust and hostname validation remain necessary; changing localhost to an IP does not repair them. See Chapter 18.

**Trimming.** Removing code according to a deployment model and analysis. Reflection and dynamic access can require specific review; a Debug build does not establish published compatibility. See Chapter 37.

**Uncertain outcome.** A state in which the client lacks a definitive response about a potentially completed operation. Preserve its original identity until the contract resolves it. See Chapters 16 and 32.

**Webhook.** A provider-to-server event delivery path. Validate the event's authenticity and scope and handle replay; a browser return is a different signal. See Chapter 33.

**XAML.** The markup used to declare MAUI views, resources and bindings. The runtime still needs the corresponding types, resources and platform behavior. See Chapter 6.

**Xcode.** Apple's toolchain used on the Mac side of iOS compilation/signing. Its supported version must match the selected .NET workload and host OS. See Chapter 39.
