# Building Mobile Apps with C# 15
## Detailed outline — draft 2

**Subtitle:** .NET 11 and .NET MAUI 11: A Windows Developer’s Guide to Android, iPhone, and Tablets  
**Author:** John F. Gnazzo  
**Proposed imprint:** DGreatGnazzini Press LLC  
**Planning date:** November 14, 2026  
**Status:** Parts I and II, Chapters 1–11, have first drafts and two section illustrations. Portable tests and Android compilation have passing Windows CI evidence; device/iOS checks remain pending. See planning/progress.md.

## Editorial brief

An independent, comprehensive guide for readers with basic C# knowledge and intermediate desktop and web development experience, but no mobile background. Readers build a public-release application provisionally called **Gnazzo’s World**, based on johngnazzo.com: books, five music artists, podcasts, and the Song for You custom-song service.

Windows is the primary development environment. Android and iOS phones and tablets are the core targets. Explain necessary Mac/Xcode access for iOS builds and signing early. Windows execution is useful for development and selected comparisons, but a public Windows desktop edition is not a core deliverable. Do not imply Windows testing substitutes for Android and iOS testing.

Cover basic mobile concepts, intermediate implementation, and advanced production concerns. Explain decisions and tradeoffs through realistic examples. Include limited backend development sufficient for content, user state, orders, and verified payment events. Exclude AI features and AI-development instruction.

### Publication requirements

- Paperback: 8 × 10 inches, black ink on white paper, color cover.
- Working typography: 11-point Source Serif 4 body text with about 14-point leading; 9.5–10-point Source Code Pro listings; Source Sans 3 headings. Verify embedding rights and readability in production.
- Target: approximately 800 total interior pages; editorial planning range 750–800. KDP’s currently verified maximum for this specification is 828 pages.
- Each Part and each chapter starts on a new page, either recto or verso. Internal chapter headings flow naturally.
- Each Part opens with a unique grayscale illustration, a substantive introduction, and descriptions of its chapters. Maintain a consistent illustration style and ebook alternative descriptions.
- Ebook: reflowable EPUB with semantic headings, navigation, cross-links, accessible images, and linked index entries. Do not reproduce print pagination as fixed-layout pages.
- Preserve readable code and useful explanations; if necessary, adjust scope or reconsider volumes instead of shrinking type.
- Initial word estimate is provisional: approximately 150,000–180,000 words, including explanations and supporting material. Re-estimate after laying out representative prose, code, table, and screenshot pages.

### Technology baseline and verification

As of the planning date, Microsoft’s official announcement and support policy identify .NET 11, C# 15, and .NET MAUI 11 as released. Use this family as the provisional current stable baseline. Confirm compatible Visual Studio, .NET SDK, MAUI workload, Android SDK/JDK, Xcode, deployment targets, and third-party libraries before code is authored. Record exact tested versions. Portable tests and Android compilation now have passing Windows CI evidence; device execution and iOS builds remain pending.

Use MAUI with XAML as the main implementation. Prefer maintained community libraries only where they serve a clear purpose. Select a Windows-compatible unit-test framework and a managed identity provider during the architecture spike. Choose the provider based on native-app OIDC support, MFA enrollment and recovery, account lifecycle, documented configuration, and practical reader access. Do not commit the book to an unverified provider flow.

Official sources:
- https://devblogs.microsoft.com/dotnet/announcing-dotnet-11/
- https://dotnet.microsoft.com/en-us/platform/support/policy/maui
- https://learn.microsoft.com/en-us/dotnet/maui/ios/pair-to-mac
- https://kdp.amazon.com/en_US/help/topic/G201857950

## Application scope and source assessment

The uploaded website archive contains 36 files. Its HTML, CSS, JavaScript, images, and external-service links form the source reference, not a ready-made native application.

- Home and biography: featured content and author information.
- Music: Minnesota Bob, Travis Rollins Jr., DGreatGnazzini, Conan Jahan III, and Reverend Paul.
- Catalog implementation: Apple lookups for several artists, embedded Minnesota Bob entries, and Spotify mappings. Normalize these into typed models with stable IDs; do not use titles as permanent record identities.
- Books: catalog descriptions, formats, images, and external purchase links.
- Podcasts: currently a placeholder; provide clearly labeled demonstration episodes until authorized real media is supplied.
- Newsletter: existing MailerLite integration; document the service boundary and consent behavior.
- Song for You: conditional form fields, song length/style/genre/occasion, pricing, multi-song discounts, customer story, external Stripe links, and delivery expectations.
- The supplied client code processes a checkout-return session and labels an order paid. The mobile reference design must establish payment status through verified server-side events; a return URL is not proof of payment.

Public browsing remains available without an account. Signed-in features include synchronized favorites, bookmarks, listening progress, request drafts, and customer order access. Include MFA and account recovery. Use distributable demonstration data and owned/authorized media; external platform links do not imply permission or technical access to stream or download their catalogs.

## Front matter

1. Half-title.
2. Title page with author and imprint.
3. Copyright, edition and publication information, ISBN placeholders, trademarks and third-party notices.
4. Optional dedication; acknowledgments.
5. Detailed table of contents.
6. Preface: why this book, intended outcomes, and the application’s origin.
7. How to use this book: prerequisites, paths through the material, conventions, repository milestones, exercises, troubleshooting, and errata.
8. Tested environment and equipment: Windows setup, Android devices/emulators, iOS build-host requirement, optional paid services, and sample-data mode.

## Chapter format

Each chapter states prerequisites, learning goals, and the application capability delivered; develops the concepts before implementation; explains relevant code with complete files in the repository; covers failure and recovery paths; supplies meaningful tests or device checks; and ends with a summary and exercises. Add basic/intermediate/advanced labels where they guide the reader, without forcing every topic into all three levels. Track index terms and source references while writing.

## Part I — From Desktop and Web to Mobile
**Chapters 1–5 · approximately 76 chapter pages**

**Part introduction:** Establish how mobile differs from familiar platforms, define the finished application, prepare a Windows workstation, and make the first application run. Introduce tests immediately so later features grow on a verified foundation.

**Illustration concept:** A Windows development workstation connected to a phone and tablet, with a small content hub suggesting books and music. Simple grayscale composition, no tiny code or interface text.

### 1. Understanding the Mobile Development Landscape
Explain native, cross-platform, hybrid, and browser-based approaches, and the book’s MAUI choice. Introduce lifecycle, process termination, touch, connectivity, permissions, battery, distribution, and the difference between sharing code and sharing every platform behavior. Compare desktop/web assumptions with mobile consequences.
**Outcome and verification:** A platform-capability matrix and device test plan that distinguish assumptions from verified support.

### 2. Defining Gnazzo’s World
Translate the website into user journeys and a native information architecture. Define anonymous browsing, signed-in features, catalog identities, music and book details, podcasts, and custom-song requests. Identify sample-data boundaries, acceptance criteria, account ownership, and public-release requirements.
**Outcome and verification:** Screen map, content model, feature priorities, and testable acceptance scenarios.

### 3. Preparing a Windows Development Environment
Install and verify compatible stable tools, workloads, SDKs, emulators, device drivers, and Git. Explain configuration, secrets, dependency versions, and repository layout. Introduce Mac/Xcode access for iOS, realistic hardware needs, and service costs without making them prerequisites for the first Android exercise.
**Outcome and verification:** Reproducible environment checklist and a successful empty Android build.

### 4. Building and Debugging the First Application
Inspect the MAUI project, resources, platform folders, startup, and generated code. Run a first branded screen on emulator and hardware; use debugging, logs, and supported reload features. Introduce lifecycle transitions, UI-thread work, and asynchronous initialization.
**Outcome and verification:** A runnable shell with repeatable launch, suspend/resume, and error-diagnosis checks.

### 5. Establishing Testable Application Foundations
Separate portable application logic from device services using a small number of purposeful projects. Introduce interfaces, dependency injection, deterministic clocks/IDs, test doubles, assertions, and a Windows unit-test project. Begin automated build/test feedback; avoid elaborate architecture before it earns its cost.
**Outcome and verification:** First meaningful catalog-validation and state tests running locally and in CI.

## Part II — Building a Native Interface
**Chapters 6–11 · approximately 98 chapter pages**

**Part introduction:** Turn the starter project into an accessible, navigable application. Explain XAML and binding from first principles, then develop maintainable view models, reusable views, and layouts that work beyond one screen size.

**Illustration concept:** One catalog composition adapting into phone and tablet arrangements, joined by a subtle shared grid.

### 6. XAML, Controls, Layouts, and Resources
Teach layout measurement, grids, stacks, scrolling, constraints, images, fonts, resources, and styles. Build the home and biography pages. Explain why desktop-sized controls and deeply nested layouts fail on small screens.
**Outcome and verification:** Home screen checked at narrow widths, large text settings, and with missing images.

### 7. Data Binding, Commands, and MVVM
Introduce binding contexts, observable state, commands, validation feedback, and computed properties. Use maintained MVVM tooling where appropriate and explain generated behavior. Model loading, empty, success, and error states explicitly.
**Outcome and verification:** Featured-content view model with behavior tests independent of MAUI views.

### 8. Navigation and Application State
Build routes, tabs, detail navigation, back behavior, and safe parameter passing. Explain modal flows, restored state, invalid destinations, and lifecycle-aware navigation. Reserve authenticated link handling for the security chapters.
**Outcome and verification:** Home-to-artist-to-song and home-to-book journeys with back-stack checks.

### 9. Collections, Images, and Reusable Views
Build artist, song, and book lists using templates, selection, image placeholders, and appropriate collection controls. Explain incremental loading, identity, recycling, image sizing, and responsive loading indicators.
**Outcome and verification:** Reusable catalog cards tested against large lists, unavailable artwork, and empty catalogs.

### 10. Design Systems, Accessibility, and Localization
Define typography, contrast, spacing, semantic labels, focus order, screen-reader behavior, theme changes, and localization resources. Include long translations, right-to-left considerations, dynamic text, and accessible error messages.
**Outcome and verification:** A shared visual system checked with screen readers, light/dark themes, and a second sample locale.

### 11. Phone, Tablet, and Foldable Layouts
Adapt to available width, orientation, safe areas, keyboards, and multiwindow resizing. Build list/detail tablet views and explain when platform-specific presentation is justified. Treat foldable support as measured layout behavior, not a promise based on device labels.
**Outcome and verification:** One feature verified across a documented phone/tablet/window-size matrix.

## Part III — Useful Catalogs and Real Forms
**Chapters 12–16 · approximately 82 chapter pages**

**Part introduction:** Make browsing useful and introduce a demanding real form. Consolidate the website’s mixed content sources into models that support search, saved items, and a maintainable custom-song workflow.

**Illustration concept:** Books, album tiles, a podcast waveform, and a custom-song request converging into a coherent catalog.

### 12. Modeling Books, Artists, Songs, and Episodes
Define stable IDs, DTO boundaries, optional metadata, editions, content availability, explicit-content labels, and typed sample fixtures. Explain how original HTML and JavaScript data informs the catalog without scraping the production website on every app launch.
**Outcome and verification:** Validated bundled catalog with duplicate/missing-data tests.

### 13. Search, Filters, Sorting, and Favorites
Implement searchable catalogs, artist/type filters, release-date sorting, debounced input, cancellation, and saved favorites. Explain Unicode-aware search, stale results, identity, and persistence boundaries.
**Outcome and verification:** Search tests for accented titles, overlapping requests, empty results, and stable sort order.

### 14. Content Details, Reading Samples, and External Links
Build book, artist, song, and episode detail experiences. Add owned reading samples, accessible long text, external service links, and graceful unavailable-content handling. Explain the boundary between a catalog, an ebook reader, and third-party playback.
**Outcome and verification:** Detail journeys with missing metadata and canceled/failed external launches.

### 15. Building the Custom-Song Request Form
Implement length, vocal/instrumental choice, genre, occasion, clean/explicit preference, customer story, and contact fields. Develop conditional inputs, keyboard behavior, multistep navigation, validation, draft saving, and accessible summaries.
**Outcome and verification:** A request builder that survives navigation and reports errors without losing user input.

### 16. Pricing Rules and Reliable Submission
Model the archived pricing and multi-song discounts as versioned example data. Use decimal arithmetic, separate presentation from business rules, and explain quote expiration, validation, duplicate taps, idempotency, and server authority over final prices.
**Outcome and verification:** Parameterized pricing/discount tests and a simulated submission contract; no live charging.

## Part IV — Data, Connectivity, and a Small Backend
**Chapters 17–21 · approximately 86 chapter pages**

**Part introduction:** Move from bundled examples to connected data while retaining predictable offline behavior. Build only the backend the mobile application needs and introduce synchronization against a local test service before adding real identity.

**Illustration concept:** A phone’s local database exchanging selected records with a modest cloud service through an intermittent connection.

### 17. HTTP APIs and Resilient Networking
Introduce HttpClient, JSON contracts, cancellation, timeouts, connectivity signals, retry limits, backoff, and safe diagnostics. Wrap external catalog providers behind interfaces. Separate public metadata access from media permissions and service authentication.
**Outcome and verification:** API-client tests for malformed payloads, rate limits, timeouts, and cancellation.

### 18. Building the Companion ASP.NET Core API
Create a small API for catalog data and later customer workflows. Explain DTOs, validation, pagination, error responses, OpenAPI, configuration, dependency injection, and local mobile-to-PC networking. Use local development fixtures before protected endpoints are introduced.
**Outcome and verification:** Executable API contract and integration tests; no public unauthenticated customer endpoints.

### 19. Local Storage and Database Migrations
Choose preferences, files, secure storage, or SQLite based on data purpose. Store catalog records, favorites, progress, and request drafts. Cover transactions, schema migration, corruption recovery, account-scoped data, and backup considerations.
**Outcome and verification:** Database tests against real temporary databases, including upgrade and failed-write scenarios.

### 20. Offline Operation and Background Work
Design cached browsing, freshness indicators, refresh behavior, queued work, and retry policies. Explain mobile operating-system restrictions and why permanent background execution cannot be assumed. Account for metered connections, low storage, and interrupted work.
**Outcome and verification:** A usable offline catalog and restart-safe pending-work queue.

### 21. Synchronization and Conflict Resolution
Define changes, versions, deletions, cursors, and conflict policies for favorites, bookmarks, progress, and drafts. Separate public catalog refresh from per-account synchronization. Exercise the protocol with a local fake user context; connect real identity in Part V.
**Outcome and verification:** Tests for duplicate delivery, concurrent edits, tombstones, reconnects, and account boundaries.

## Part V — Identity, MFA, and Account Security
**Chapters 22–26 · approximately 88 chapter pages**

**Part introduction:** Add identity through a managed provider rather than writing a password system. Explain the complete account journey, from first sign-in through MFA and recovery to data deletion, while protecting server resources independently of the user interface.

**Illustration concept:** An account key, two independent verification steps, and a protected collection of personal records.

### 22. Native-App Authentication and Managed Identity
Explain OAuth 2.0/OIDC, public clients, browser-based authorization, authorization code with PKCE, redirect registration, and identity/access-token differences. Configure a selected, verified provider with a reproducible reader setup. Mobile binaries cannot protect client secrets.
**Outcome and verification:** Anonymous browsing plus a real sign-in flow with canceled and invalid callbacks tested.

### 23. Sessions, Secure Storage, and API Authorization
Handle token acquisition, expiration, refresh, revocation, sign-out, and safe logs using maintained libraries. Add API token validation, scopes/policies, user ownership checks, and per-account state. Explain authentication versus authorization.
**Outcome and verification:** Rejection tests for missing/invalid tokens and attempts to access another customer’s records.

### 24. Multifactor Authentication and Recovery
Implement the provider’s supported MFA enrollment, challenge, factor replacement, recovery codes, and lost-device process. Explain authenticator factors, phishing resistance, and provider-specific limitations. Distinguish local biometric unlock from account MFA.
**Outcome and verification:** Documented real-provider MFA and recovery scenarios, supplemented by app-state tests rather than fake MFA claims.

### 25. Profiles, Privacy, and Account Lifecycle
Add profile preferences, synchronization consent, notification choices, data export/deletion requests, reauthentication, and account removal. Define what sign-out clears, what deletion removes, and how failures or delayed processing appear to the user.
**Outcome and verification:** Account switching and deletion/retry checks that demonstrate isolation of personal data.

### 26. Threat Modeling and Security Verification
Review deep-link handling, local data, network boundaries, dependency risks, backend secrets, request validation, and customer-file access. Introduce least privilege, rate limiting, sensitive-action audit events, and practical abuse cases.
**Outcome and verification:** Focused threat model and executable security regression cases for the features already built.

## Part VI — Media and Native Device Experiences
**Chapters 27–31 · approximately 88 chapter pages**

**Part introduction:** Make the application feel useful on actual devices. Add authorized media playback and controlled downloads, then integrate notifications, sharing, attachments, and links with lifecycle and permission handling.

**Illustration concept:** A player waveform surrounded by download, notification, sharing, and device-control symbols, all in grayscale.

### 27. Audio Playback and Podcast Progress
Introduce an audio-service abstraction, supported formats, streaming versus local playback, play/pause/seek, queues, progress persistence, and unavailable media. Use owned/authorized demo files; do not treat Spotify links as audio URLs.
**Outcome and verification:** Playback-state unit tests plus physical-device checks for seeking, interruption, and resume.

### 28. Background Playback and System Controls
Implement platform-specific background audio requirements, media metadata, lock-screen controls, audio focus, headphone disconnects, interruptions, and lifecycle transitions. Describe battery and system constraints explicitly.
**Outcome and verification:** Android/iOS device scenarios for screen lock, calls or other audio, and process interruption.

### 29. Downloads and Media Storage
Build download progress, cancellation, restart behavior, integrity checks, storage quotas, deletion, and safe file names. Distinguish public sample media from authenticated customer deliveries; test range/resume behavior against an endpoint that supports it.
**Outcome and verification:** Interrupted-transfer and low-storage tests plus account-safe download access.

### 30. Notifications, Deep Links, and Sharing
Introduce local notifications, then a bounded push integration with permission choices and device-token lifecycle. Route shared links to content and authenticated order views. Handle cold launches, malformed links, revoked permission, duplicate messages, and sign-in continuation.
**Outcome and verification:** Link-routing tests and real-device notification checks with minimal server support.

### 31. Native Capabilities, Attachments, and Platform Extensions
Use file/photo selection for optional request attachments, native sharing, connectivity information, and restrained haptics. Explain permissions, cancellation, image sizing, handlers, conditional compilation, and disposal. Include an optional location-based song-discovery exercise to teach location without making it a core permission.
**Outcome and verification:** Safe attachment handling and capability fallbacks on both target platforms.

## Part VII — Customer Workflows and Order Delivery
**Chapters 32–35 · approximately 76 chapter pages**

**Part introduction:** Bring the custom-song form, identity, and backend together into an understandable transaction workflow. Keep the implementation small while demonstrating authoritative state, reliable events, and private delivery.

**Illustration concept:** A request moving through quotation, production, revision, and delivery, with customer and service checkpoints.

### 32. Quotes, Orders, and Customer Ownership
Turn saved drafts into server-validated quotes and requests. Model immutable price snapshots, idempotency keys, order states, and authenticated ownership. Keep the production/admin side to a documented minimal service interface or controlled fixture.
**Outcome and verification:** Integration tests for duplicate submissions, stale quotes, invalid transitions, and cross-account access.

### 33. Payment Boundaries and Verified Events
Explain hosted checkout, server-created sessions, verified webhook processing, event replay protection, and state reconciliation. Build in a payment sandbox. Before public release, verify current store rules for custom services versus digital content and permitted checkout methods for each storefront; external web links are not automatically a compliant mobile checkout design.
**Outcome and verification:** A test payment reconciled server-side; canceled/forged return URLs cannot mark an order paid.

### 34. Order Tracking, Revisions, and Delivery
Build status history, revision requests, delivery notifications, and authenticated file access using expiring authorization where appropriate. Handle retries, access expiration, and outstanding work when the user signs out.
**Outcome and verification:** Customer journey from request to delivered sample audio, including unauthorized file-access tests.

### 35. Hosting and Operating the Small Backend
Deploy the API, database, and file storage with configuration and secret separation. Cover HTTPS, migrations, backups/restores, health checks, minimal observability, cost awareness, and reliable webhook handling. Describe newsletter integration as a bounded service adapter.
**Outcome and verification:** Staging deployment, restore exercise, and a documented operational checklist; production provisioning is a separate explicit action.

## Part VIII — Verification, Publication, and Maintenance
**Chapters 36–40 · approximately 96 chapter pages**

**Part introduction:** Consolidate the tests already built, assess actual device behavior, and prepare the application for public distribution. Finish with a repeatable release and maintenance process, rather than stopping at a successful development build.

**Illustration concept:** Phone and tablet builds moving through a test bench and release pipeline toward readers and listeners.

### 36. Testing the Complete Application
Organize unit, integration, contract, and UI suites; use deterministic data, isolated accounts, and CI artifacts. Cover device matrices, accessibility regression, offline recovery, MFA/provider testing, and payment sandboxes. Explain what cannot be proved by mocks or code coverage.
**Outcome and verification:** Traceable acceptance coverage with separate automated and manual results.

### 37. Performance, Reliability, and Accessibility Review
Measure startup, allocations, list scrolling, images, API latency, battery, and download costs in release-like builds. Review screen readers, focus, contrast, large text, and localization on real devices. Introduce profiling, trimming/AOT considerations, crash diagnostics, and platform extension leaks where relevant.
**Outcome and verification:** Before/after measurements and a release-quality accessibility/device report.

### 38. Android Signing and Google Play Release
Prepare identifiers, signing and upload keys, release builds, target requirements, store assets, content ratings, data declarations, testing tracks, and rollout plans. Verify current requirements while writing and again at release.
**Outcome and verification:** Reproducible Android release candidate and store-submission checklist, with an install/upgrade smoke test.

### 39. iOS Signing and App Store Release from Windows
Explain the Mac/Xcode build boundary, developer-account setup, bundle IDs, capabilities, certificates/profiles, signing, device testing, TestFlight, store metadata, privacy disclosures, and review access including MFA considerations. Distinguish Windows-authored code from Mac-required build work.
**Outcome and verification:** Signed iOS release candidate, TestFlight validation plan, and review checklist.

### 40. Automated Releases and Long-Term Maintenance
Connect manuscript/code milestones, automated Windows tests, platform builds, secure signing material, and explicit release gates. Cover updates, schema and API compatibility, migration testing, crash feedback, rollback limits, dependency servicing, errata, and matching book/code edition tags.
**Outcome and verification:** Documented release rehearsal, upgrade test, and maintenance ownership plan.

## Appendices and other back matter

- **Appendix A — Targeted C# refresher:** async/await, cancellation, interfaces, generics, events, nullable references, and dependency injection in mobile examples; no general C# textbook.
- **Appendix B — Environment and troubleshooting reference:** tested version matrix, device setup, local networking, build-host/signing failures, and diagnostic collection.
- **Appendix C — API, data, and configuration reference:** contracts, sample datasets, schema versions, configuration keys, and safe example settings.
- **Appendix D — Watch companions and future extensions:** bounded discussion of watch workflows, platform/tooling boundaries, and an optional quick-action companion; not a promise of MAUI watchOS support or a second full application.
- Glossary and acronym reference.
- Official references and further reading, organized by topic.
- A substantive index generated after print pagination; linked targets in EPUB.
- About the author, prepared from approved current biographical details.
- Companion-code access, errata, and updates.
- Optional selected related titles and imprint information.
- Final third-party acknowledgments/notices where required.

## Page budget

| Component | Target pages |
|---|---:|
| Chapters 1–40 | 690 |
| Eight Part openers, illustrations, introductions, and chapter previews | 24 |
| Front matter, including TOC and reader orientation | 24 |
| Appendices | 30 |
| Glossary and references | 10 |
| Index | 16 |
| Author, support, notices, and remaining back matter | 6 |
| **Total** | **800** |

These are layout budgets, not chapter limits. KDP’s total includes unnumbered and blank interior pages. The 28-page allowance below 828 is a contingency, not planned chapter space. Reforecast after sample typesetting and each completed Part.

## Companion repositories and milestones

Manuscript: https://github.com/minnesotabob/csharp-mobile-app-man  
Code: https://github.com/minnesotabob/csharp-mobile-app-code

Proposed code layout:
- src/GnazzosWorld.App — MAUI views and platform adapters.
- src/GnazzosWorld.Core — portable models, rules, use cases, and contracts.
- src/GnazzosWorld.Infrastructure — data/network adapters where a separate project is useful.
- src/GnazzosWorld.Api — small companion backend.
- tests — portable unit tests, database/API integration tests, and supported UI automation.
- samples — distributable fixtures and authorized media.
- docs — setup, configuration, version matrix, and device/manual checks.

Keep manuscript examples traceable to actual source paths and chapter milestones; avoid forty diverging copies of the application. Propose chapter tags ch01 through ch40 and matching edition tags in both repositories. These tags do not yet exist.

| Milestone | Delivered capability |
|---|---|
| Part I | Runnable starter, development checklist, first tests |
| Part II | Navigable accessible phone/tablet interface |
| Part III | Useful catalogs, search, request builder, pricing rules |
| Part IV | Connected/offline data and synchronization protocol |
| Part V | Real identity, MFA, authorization, account lifecycle |
| Part VI | Authorized playback, downloads, notifications, device integration |
| Part VII | Secure customer orders and verified sandbox payment/delivery |
| Part VIII | Measured, tested, signed release candidates and maintenance workflow |

Public repository content must use demonstration accounts, fictitious customer requests, and authorized assets. Preserve the original uploaded website as reference; do not copy live service forms, customer identifiers, payment configuration, or the full archive into the companion code by default.

## Illustration and production plan

Create eight distinct illustrations after the outline is accepted and the relevant Part’s emphasis is stable. Favor a consistent editorial illustration style, good grayscale contrast, and simple compositions; place precise labels in typeset captions rather than relying on generated text. Technical architecture and data diagrams must be exact, authored separately from decorative illustrations.

Before full typesetting, produce representative 8 × 10 pages containing prose, code, a screenshot, a table, and a Part opener. Validate line length, grayscale rendering, gutter allowance, code wrapping, font embedding, EPUB reading order, and screen-reader descriptions.

## Decisions to settle during initial implementation

1. Application name and visual identity; title and subtitle have been approved.
2. Exact stable toolchain and compatible packages, documented after a build spike.
3. Managed identity provider and practical reader MFA/recovery setup.
4. Unit-test framework and verified platform UI-test tooling.
5. Authorized demonstration media and optional real podcast material.
6. Production checkout approach after current storefront policy review.
7. Hosting selection and explicit service-cost choices before provisioning.
8. Final page budget after sample layout.

No production deployment, payment activation, account creation, app-store submission, or live customer-data migration is authorized merely by this outline.

