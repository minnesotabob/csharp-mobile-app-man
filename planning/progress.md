# Chapter 18 draft milestone — November 15, 2026 (Central)

First drafts now cover Chapters 1–18. The 8 × 10 proof is 125 pages; Chapter 18
starts on page 117 and adds approximately 3,100 words on the companion API, public
wire documents, revision-aware paging, validation/problems, OpenAPI, local host
configuration, HTTPS probing, device addressing and layered integration checks.

The contents remains one linked page and the PDF has 25 bookmarks. The nine new
chapter pages, tables, code and references were visually reviewed; all 125 pages
pass mirrored text-margin checks. Body/code sizes remain 11/9.5 points.

Verified companion source: 5c24e63dffd494463716730fdf553af74453a2ae.
- Portable Release build: zero warnings/errors; 245 tests pass (10 new document cases).
- API/test/probe Release compilation: zero warnings/errors; 26 integration cases pass.
- Actual temporary-loopback Kestrel HTTP startup/contract smoke passes and stops host.
- Android Debug compilation succeeds; final compile zero warnings/errors.
- Portable: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43709057778
- API/probe/smoke: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43709057781
- Android: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43709057777

TestServer exercises the actual API pipeline but does not use real sockets. The
Kestrel check uses loopback HTTP, not TLS. The HTTPS probe compiles but actual
certificate/device integration is unverified. Native device work and iOS builds
remain pending, as does the existing Android setup warning. No backend deployment,
tunnel, account, customer write, database or payment is activated. Main catalog
and native lab keep their previous bundled/in-process modes.

A transient publication review rejection was resolved by read-only verification
of repository ownership, public status, permissions and the existing draft PR.
Work remains on the same review branch and draft PRs; default branches unchanged.

Next: Chapter 19, Local Storage and Database Migrations, with temporary-database
tests, explicit persistence boundaries, schema upgrades and failed-write recovery.

## Earlier milestone record

# Chapter 17 draft milestone — November 15, 2026 (Central)

First drafts cover Chapters 1–17. The 8 × 10 proof is 116 pages, with Part IV
starting on page 107 and Chapter 17 on page 109. The new Part introduction previews
Chapters 17–21 and includes an original authored vector planning diagram with a
matching JPEG for typesetting. Chapter 17 adds approximately 3,000 words on the
public-catalog HTTP boundary, client lifetime, a total deadline, bounded bodies,
validation, selective retry, safe failure categories, connectivity hints and tests.

The one-page contents now omits redundant spacer rows while keeping the same
10.5-point type. Body/code remain 11/9.5 points. Contents, new Part diagram and
new chapter pages were visually reviewed; all 116 pages pass mirrored text-margin
checks. The PDF has 24 bookmarks. Part III's preview now describes its implemented
Chapters 14–16 accurately rather than retaining its older Chapter 13 status.

Companion source: 352b0bc901b6de7b54494922e181e6311edf34b1.
- Windows portable Release compilation: zero warnings/errors.
- Executable suite: 235 tests pass, including 37 new Chapter 17 cases.
- Android Debug compilation: success; final compile zero warnings/errors.
- Portable evidence: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43706546704
- Android evidence: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43706546699

The native lab uses an in-process HTTP handler with no live service contact.
Main catalog browsing remains bundled. Native Android/iOS checks, iOS compilation,
actual TLS/redirect/socket networking and local-PC reachability remain pending.
Android setup retains the documented cmdline-tools warning.

Manuscript and code remain in their existing draft PR #1; default branches are
unchanged. No new milestone tag or production deployment is made.

Next: Chapter 18, Building the Companion ASP.NET Core API, including its explicit
response schema, validation, OpenAPI and local phone/emulator-to-PC integration.

## Earlier milestone record

# Chapter 16 draft milestone — November 15, 2026 (Central)

First drafts now cover Chapters 1–16. The 8 × 10 proof is 106 pages; Chapter 16
starts on page 99. It adds approximately 2,800 words on archived price versions,
marginal discounts, decimal arithmetic, canonical quote snapshots, expiry,
idempotency, duplicate taps and uncertain-response recovery. The contents and
eight new chapter pages were visually reviewed; all 106 pages pass mirrored
text-margin checks and the PDF has 22 bookmarks. Fonts remain 11 pt body/9.5 pt code.

The companion source recovers Chapters 14–15 and adds quantity, 15-minute quotes,
a process-local simulated service and 30 new portable cases. A lost-response
fixture accepts first and then throws, verifying reuse of the original operation.
No live order, payment, email or customer transmission exists. The demo's pending
operations and accepted receipts disappear on restart. Device checks, iOS builds,
form localization and focus refinement remain pending.

Work is published on work/chapter16-pricing for review. The code draft PR is
https://github.com/minnesotabob/csharp-mobile-app-code/pull/1 . Default branches
remain unchanged. Earlier default-branch automatic review rejection is not retried.
The corrected source revision 2d15aa9452ef2f70b66176c99aebb3acf8027362 passed
Windows portable compilation with zero warnings/errors and all 198 tests.
Evidence: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43704723565
Android Debug compilation also succeeded on the same source revision.
Evidence: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43704723559
The setup cmdline-tools warning remains; final compile is clean. Device/iOS checks remain pending.

Next: Part IV introduction and Chapter 17, HTTP APIs and Resilient Networking.
The full 40-chapter/eight-Part plan and final production work remain in place.

## Earlier milestone record

# Chapter 15 draft milestone — November 15, 2026 (Central)

First drafts now cover Chapters 1–15. The 8 × 10 proof is 98 pages, with the new
chapter starting on page 93. The one-page contents, six new chapter pages, tables,
code and references were visually reviewed. All pages passed a text-margin check;
the PDF has 21 bookmarks. Body and code sizes remain unchanged.

Chapter 15 adds the three-step custom-song form, conditional vocal notes, a clean
content default, contact/story validation, review invalidation, and explicit local
save/discard. A process-shared view model preserves navigation edits; a versioned
local JSON draft provides explicit saving across restarts. This is anonymous local
storage, without app-level encryption or account isolation. New form strings are
English; localization and field-level focus routing remain follow-up work.

29 new portable cases are authored. They have NOT been executed: this continuation
environment has no dotnet executable. Android/iOS compilation and all native checks
also remain pending. XML/JSON/resource syntax and whitespace checks passed. Chapter
14 source was recovered from its review bundle and is included with this milestone.
No new CI result or GitHub publication is claimed. Earlier automatic review blocked
default-branch publication; that rejected action was not retried here.

Next: execute the Chapter 14–15 suite and native builds when a suitable environment
is available; Chapter 16 introduces versioned example pricing and simulated reliable
submission. No actual order, email, payment or customer data transmission is added.

## Earlier milestone record

# Chapter 14 draft milestone — November 15, 2026 (Central)

First drafts now cover Chapters 1–14. The 8 × 10 proof is 92 pages. Chapter 14 adds
approximately 2,700 words on detail metadata, plain-text reading samples, provenance,
reviewed website destinations, browser handoff, stale-result ownership, exercises and tests.

Companion source adds a credited original teaching sample (not a published-book excerpt),
shared detail presentation, English/Spanish labels, a native Browser adapter and 27 new
portable test cases. XML/resource/JSON syntax and whitespace checks passed. The new
portable compilation, test execution and Android compilation remain PENDING: automatic
review blocked pushes to the default branch, including after prior authorization was retrieved.
No new CI pass is claimed. Chapter 13's 112-test/Android evidence remains historical only.

Local companion commit: 8aaf2d1. GitHub publication is pending approval. A separate artist
biography route, full ebook reader, playback, device observations and iOS builds remain pending.
Next: resolve publication/build verification, then Chapter 15's custom-song request form.

## Earlier milestone

# Chapter 13 draft milestone — November 14, 2026 (Central)

## Written and typeset

First drafts now cover Chapters 1–13, the preface, reader guide, introduction and Parts I–III introductions.
The selected 8 × 10 PDF is 84 pages with linked contents and bookmarks. Chapter 13 adds approximately
2,400 words covering combined search criteria, Unicode matching, deterministic ordering, input ownership,
favorites storage/failure behavior, native presentation, tests, exercises and review questions.

Parts I and II retain their original grayscale illustrations. Part III artwork, actual app screenshots,
remaining chapters, final front/back matter, index and accessible EPUB are pending. This remains an editorial
proof, not a finished book or final chapter-length forecast.

The new chapter, contents, code, table, exercise and final-reference pages were visually reviewed.
All 84 pages were checked for text outside the mirrored body margins. The PDF has 19 outline entries
and 38 internal links. References now use the small reference style, avoiding a nearly empty final page.

## Verified companion source

Revision: 51870ac298eff6198e098a063bdc391fecc665f8 in csharp-mobile-app-code.

- Windows portable Release compilation: 0 warnings/errors.
- Executable xUnit suite: 112 tests; 0 errors/failures/skipped/not run.
- Portable evidence: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43678204364
- Android Debug compilation: success; final compilation 0 warnings/errors.
- Android evidence: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43678204305

Chapter 13 adds 29 portable cases. The app combines text, kind, ordinal creator identity, title/release
sorting and favorites. A page-owned debounce applies the latest input and cancels pending work on departure.
Favorites use a bounded, versioned local Preferences adapter; failed saves preserve visible state and
unreadable initial storage disables edits without preventing ordinary browsing.

The device-local format supports at most 32 IDs, 128 characters per ID and 4096 serialized UTF-8 bytes.
Portable reconstruction tests exercise the store contract; they do not prove actual native restart persistence.
Device launch, native persistence, keyboard/large-text/layout/focus checks and iOS compilation remain pending.
Remote search, accounts, synchronization, migration/repair, checkout and deployment are not implemented.
Android dependency installation retains the previously documented cmdline-tools setup warning.

## Next work

Chapter 14: content-specific details, owned reading samples and controlled external-link journeys,
including missing content and canceled/failed launches. Continue expanding earlier chapters against actual
device observations. Chapters 15–16 will introduce request-form and simulated submission workflows.

## Earlier Chapter 12 record

# Chapter 12 draft milestone — November 14, 2026 (Central)

## Written and illustrated

First drafts now cover Chapters 1–12, preface, reader guide, introduction, and two Part introductions with chapter previews. Part II adds XAML/resources, binding and MVVM, Shell navigation/state, collections/images/reuse, accessibility/localization, and adaptive layouts. Both Parts have distinct original grayscale illustrations with alternative descriptions.

The 77-page opening PDF includes linked contents/bookmarks and the selected 8 × 10 typography. It remains an editorial proof; chapter coverage, hands-on walkthroughs and real screenshots will expand after technical/device review. The 40-chapter/eight-Part plan and approximately 800-page budget remain provisional. These short first drafts are not final chapter lengths.

Final front/back matter, acknowledgments, author biography, ISBN/legal details, remaining Part art, complete index, accessible EPUB, and release production remain pending. Editorial index terms are retained in Markdown for later indexing.

## Chapter 12 additions

Part III now has an introduction and Chapter 12 has approximately 2,200 words, examples,
validation tables, exercises, review questions and official references. Companion code adds
creator identities and relationships, optional release dates, editions, audio durations,
availability and content advisories. The bundled import validates related creator records.
Unknown dates and advisories are not invented. Twenty-two new regression cases extend the suite.

The new metadata is not displayed in the native detail UI yet. Artist pages, favorites,
debounced search, request forms, draft persistence and simulated submission remain planned.

The PDF renderer now includes Chapter 12, keeps tables together where possible, renders
bulleted questions separately, fits the contents on one page and explicitly selects mirrored
body margins by page parity. The 77-page PDF was checked for text outside body margins and
visually reviewed at contents, Part/chapter starts, tables, code and the new exercise pages.

## Verified code

Source revision: cda4092131cfbf9793587fc36a2c5bba67bfd52d in csharp-mobile-app-code.

- Portable Release build and executable xUnit suite on Windows CI: 83 tests, 0 errors, failures, skipped or not run; portable build 0 warnings/errors.
- Evidence: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43676066332
- Android Debug compilation on Windows CI: success at d496a51b86d1bb9b123745eecf58379695e62bbc. The later revision only changes a test assertion to remove an analyzer warning; application/core source is identical.
- Evidence: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43675861183

The companion app now has Home/Discover Shell navigation, typed bindings, a portable catalog browser model, search/kind filtering, stable-ID details, reusable cards/detail view, English/Spanish resources, light/dark resources, and a width-based inline-detail policy. Tests exercise state and command boundaries; they do not prove native accessibility or rendering.

Toolchain: SDK/workload set 11.0.100, MAUI manifest 11.0.0, Controls 11.0.10, Android pack 37.2.29, Microsoft OpenJDK 21.0.11+10. Dependency installation reports an unresolved cmdline-tools;21.0 warning; final Android compilation is clean. See companion docs/verification.md.

## Limits and next work

Device/emulator launch, native navigation/keyboard/rotation, screen-reader/large-text/theme/language checks, and iOS compilation/signing remain pending. Multiwindow navigation, remote artwork, backend, identity/MFA, playback, checkout and deployment are not implemented. Follow docs/device-checks.md rather than marking these passed from unit tests.

Earlier local workload/test attempts were blocked by automatic review after attempted cloud metadata access; they were not retried. Separate GitHub-hosted Windows CI provides the evidence above.

Next: Chapter 13 search, filters, sorting and favorites; later Chapters 14–16 detail journeys and the request/pricing workflow; expand earlier chapters against actual device observations when available. Preserve the Part I source milestone for Chapters 4–5 using companion docs/milestones.md.
