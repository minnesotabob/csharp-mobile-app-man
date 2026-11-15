# Editorial visual revision — November 15, 2026 (Central)

Applied the supplied Chapters 1-20 editorial review without changing the 40-chapter
scope or lowering technical depth. See `planning/editorial-visual-pass.md` for the
concern-to-change map and outstanding native screenshot capture plan.

Added **nine authored figures**: initial search architecture, MVVM ownership, HTTP
acceptance gates, offline refresh, release roadmap, planned security boundary and
three visual recaps after Chapters 5, 11 and 16. All new diagrams distinguish their
milestone or planned state from actual device observations. Chapter 1 now directly
compares MAUI, Flutter, React Native, platform-native and browser approaches, with
when-not-to-use guidance and a concrete decision spike. Chapter 18 previews protected
customer-data architecture; Chapter 17 gains a systematic diagnostic contract. More
Northern Lights, Kai the Ninja and fictitious anniversary-song journeys connect the
engineering to Gnazzo's World. Chapters 35/37 in the outline now explicitly require
substantial diagnostics and full performance measurement labs.

**Verified proof revision:** `ba8d67d6dfcdd476293bba3eec4d18d2af86cf2d`.
https://github.com/minnesotabob/csharp-mobile-app-man/actions/runs/43734196520

The revised PDF contains **191 pages, 27 bookmarks and 12 distinct images** (three
existing Part illustrations plus nine new figures). Figure pages: 11, 17, 59, 71,
98, 141, 147, 157 and 184. All expected figure captions, chapter markers, 8x10 trim
and outer text boundaries passed the workflow checks. Independent PyMuPDF checks
confirmed no broad boundary violations and no orphan visual-recap headings. Every
new figure was reviewed as artwork and on its rendered manuscript page; comparison,
diagnostics and security-preview text was also rendered for review. The image renderer
now keeps a preceding subheading, figure and caption together after visual review
found one orphaned recap heading in the initial proof.

**Outstanding:** actual app screenshots, native browser wiring for Chapter 20, device/
provider/iOS verification, full later performance/diagnostics labs, and remaining book
production. Screenshot intervals are a capture/pagination goal, not satisfied by
these diagrams. No screenshot or benchmark is fabricated. This revision changes
manuscript, figures, outline and proof workflow only; it does not claim new app tests.
Earlier 266-test/Android evidence remains associated with its recorded code revisions.

## Earlier milestone record

# Chapter 20 and reviewed 182-page proof — November 15, 2026 (Central)

Chapter 20, Offline Operation and Background Work, is drafted (about 3,600 words),
with learning outcomes, ten instructional sections, complete companion components,
numbered lab, failure/recovery reasoning, troubleshooting, summary, worked exercises
and a native verification worksheet. The original 40-chapter scope remains.

Companion runtime implementation: `74d2df5ade5b1d69b306bdb1a406722d08057ed1`.
Final portable test/lab revision: `6553709cd7b2c770cfc6da8a8fcb2abcfa98ef7a`.
Documentation evidence commit: `02fb4b385dd0ed14193d97e7df67c9a46a4d7f9c`.

- Portable Release build: **0 warnings/errors; 266 tests passed**, none failed/skipped/not run.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43731444673
- Android Debug compilation passed with identical runtime/core source:
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43731012298
- Final manuscript proof at `45aae4596b3bfdf7f83b01cd7897e8752be92a4e`:
  https://github.com/minnesotabob/csharp-mobile-app-man/actions/runs/43731673320

The full proof has **182 pages, 27 bookmarks**, and Chapter 20 begins on **page 172**.
Automated trim and text-boundary checks passed. Independent local PyMuPDF checks
found no broad outer-boundary violations. Contents, Chapter 20 opening, code/table
pages, summary/exercises and the final worksheet/references were rendered and visually
inspected. The renderer now handles third-level headings and keeps short reference
lists together; a worksheet supplies useful native acceptance instructions on the
final page instead of an isolated reference tail.

Schema 3 adds retrieval metadata and a coalescing, durable public-refresh ticket.
One coordinator reads local/bundled data, performs bounded refresh attempts and
commits snapshot plus matching acknowledgment atomically. Existing favorites and
progress remain. Thirteen new executed cases cover freshness, reopen/recovery,
failure, cancellation, newer intent during fetch, rollback and worker exclusion.

Limits: native MAUI browser wiring, OS scheduler registration, physical crash/reboot,
phone SQLite execution, TLS/device and iOS remain unverified. No automatic retry
cooldown, customer transaction queue or multiworker lease is implemented. The
native worksheet is an acceptance plan, not a report of performed device tests.

Next: Chapter 21 — Synchronization and Conflict Resolution. Keep public catalog
replacement separate from user changes, versions, tombstones and account boundaries.

## Earlier milestone record

# Chapter 19 verification and 171-page proof — November 15, 2026 (Central)

**Status:** Chapter 19 has been drafted and committed, with working companion SQLite source, eight new real-file tests, and MAUI dependency registration. The companion code revision `3f7b162dc2f9c7553b3e170ef7b44dcc59c9f26b` passed **253 portable tests** with zero errors/failures/skips, and the Android Debug compilation passed. See `docs/verification.md` in the companion repository. No native SQLite runtime on Android/iOS or account-authentication/secret-storage claim is made.

**Proof:** The Chapter 19 addition initially revealed a right-margin code-line overflow in the 8 × 10 specimen. Shortening the PowerShell command fixed that defect; the renderer was also updated to print italic Markdown correctly. The latest full 19-chapter PDF proof was generated successfully by GitHub Actions at manuscript revision `79c02e7d7db52aa66ba188a0d8a2e670a49b011e`. It contains **171 pages, 26 bookmarks, and Chapter 19 starting on page 159**. A further independent local PyMuPDF inspection found zero text lines outside the broad page body margins and no unexpected nearly-empty pages, and the Chapter 19 opening was rendered for visual inspection.

- Manuscript proof workflow: https://github.com/minnesotabob/csharp-mobile-app-man/actions/runs/43721108408
- Downloadable artifact: https://github.com/minnesotabob/csharp-mobile-app-man/actions/runs/43721108408/artifacts/14164876195
- Portable code CI: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43720268893
- Android CI: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43720264777

**Editorial status:** This is a tested *first draft*, not an approved final chapter or finished KDP interior. Finish detailed editorial review, authoritative source cross-references, native verification and the remaining planned chapters. Chapter 20 is next: offline freshness, cache fallback and restart-safe pending work.

## Earlier milestone record

# Chapter 19 draft and SQLite companion implementation — November 15, 2026 (Central)

**Manuscript:** Chapter 19, `chapters/ch19-local-storage-migrations.md`, has been added. It teaches SQLite 11.0.0 storage for validated public catalog snapshots, local favorites and reading progress, version 0/1 to 2 migrations, transactions, scope boundaries, error handling and worked exercises. Existing chapters remain unchanged except for production metadata. The renderer now includes Chapter 19 and its preflight requires that marker.

**Code:** The companion `work/chapter16-pricing` branch adds `src/GnazzosWorld.Core/Storage/LocalCatalogDatabase.cs`, SQLite dependency 11.0.0, eight real-file integration cases, and MAUI DI registration (the browsing UI and sensitive JSON draft flow are unchanged). Fresh CI on code revision `3f7b162dc2f9c7553b3e170ef7b44dcc59c9f26b`: **253 portable tests passed** and **Android Debug compilation passed**. See companion `docs/verification.md` for exact evidence. No iOS/device runtime or database encryption claim.

**Proof:** The first new renderer run for 19 chapters found a right-edge overflow from a long PowerShell command. The command was shortened and the PDF workflow rerun; check the latest workflow artifact before quoting any new page count. This is a typesetting proof, not a KDP-ready interior.

## Earlier milestone record

# Visual paperback proof revision — November 15, 2026 (Central)

The **159-page** specimen was downloaded and inspected locally using rendered page images, PDF text positions and page-density scans. All 18 chapters started at the top of their own pages with consistent 54-point heading positions, PDF bookmarks numbered 25, and no discovered text outside the intended mirrored body frame. The inspection found one genuine orphan: **page 122 contained only the last Chapter 14 reference**.

The renderer's reference typography was adjusted to 8.6-point Source Sans / 10.5-point leading / 3-point spacing. The proof was rebuilt successfully in workflow https://github.com/minnesotabob/csharp-mobile-app-man/actions/runs/43719476039 (commit `e5d54891ff9c4de3bc7a9fb7b2c9439e80cfdb11`; artifact https://github.com/minnesotabob/csharp-mobile-app-man/actions/runs/43719476039/artifacts/14164305199). The **revised proof has 158 pages**. A fresh local PDF check found **no body text outside the mirrored frame**, no pages with fewer than five main-text lines, and all **18 chapters** beginning independently at the same vertical position. The formerly orphaned Chapter 14 citation now fits on page 121; Chapter 15 begins on page 122. The key fixed page was also rendered and visually inspected.

These are real PDF-layout observations, not a guarantee of publication readiness. Additional complete visual proofing, code-line inspection at printed size, illustrations, index, final KDP front/back matter and physical print checks are still required. The older 159-page artifact remains historical; use the **158-page replacement**.

## Earlier milestone record

# Revised 18-chapter proof and fresh CI — November 15, 2026 (Central)

**Proof:** The manuscript proof was regenerated by GitHub Actions using source commit `7662939586552e83f063ee92d20209cbf59580b1`. It contains **159 pages** at 8 × 10 inches and includes Chapters 1–18. The automated check passed expected chapter markers, PDF trim size and broad outer text bounds. The proof is downloadable as the `manuscript-8x10-proof` artifact (ZIP containing the PDF) at https://github.com/minnesotabob/csharp-mobile-app-man/actions/runs/43719077194/artifacts/14163557926 . Artifact retention is 14 days, until approximately November 29, 2026.

The renderer's stale chapter-status description was corrected, and its overlong `KeepTogether` behavior for chapter summaries was replaced by keeping only each heading and its opening paragraph together. This proof is an editorial/typesetting specimen, not a KDP-ready interior. No comprehensive visual page-by-page inspection, body-gutter-specific overflow audit, physical proof or finished index/front-back matter verification was performed by the new CI workflow.

**Code CI:** Fresh Windows GitHub Actions on companion code revision `e0368e4d810215b78b303abc2eab7bfdd17e049a` passed portable tests, ASP.NET Core API integration/smoke checks, and Android compilation. The code change was an XML documentation comment only; the check does not assert Android device execution or iOS compilation.

- Portable https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43718726273
- API https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43718726243
- Android https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43718726297
- Manuscript proof https://github.com/minnesotabob/csharp-mobile-app-man/actions/runs/43719077194

**Next:** Visually inspect representative/full PDF pages for code/table overflow and chapter starts, then expand the manuscript's pedagogical depth and finish outstanding production matter. Source CI success is not sufficient to certify device UI or a bookstore-ready release.

## Earlier milestone record

# Fresh CI verification requested — November 15, 2026 (Central)

A nonfunctional XML comment was committed to the companion repository's `Directory.Build.props` at revision `e0368e4d810215b78b303abc2eab7bfdd17e049a` to initiate the existing GitHub Windows validation workflows for the revised documentation baseline.

- Portable tests: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43718726273
- ASP.NET Core API checks: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43718726243
- Android compilation: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43718726297

All three runs were still **in progress** at the last status check. This record does not claim they passed. No local .NET execution or device tests occurred. The current environment cannot clone the public repository directly because GitHub host resolution fails; consequently a full refreshed 8 × 10 PDF proof was **not** generated in this pass. A complete source checkout, the existing `production/render_opening.py` renderer, and visual inspection remain necessary.

## Earlier milestone record

# Technical/editorial audit — first pass, November 15, 2026 (Central)

The first structural/source-inventory audit of Chapters 1–18 is recorded in [technical-audit-01.md](technical-audit-01.md). All chapters have learning objectives and standalone summaries; Chapters 15–18 now separate exercises from summaries. Chapters 12–17 gained targeted troubleshooting. Markdown fence parity and explicit companion source-filename checks passed. The companion learning guide was corrected to describe this initial instructional work accurately.

This does NOT certify code excerpts, native behavior, fresh CI or a revised typeset proof. The latest historical Chapter 18 result is 245 portable and 26 API tests, with Android compilation and loopback service smoke evidence; no new execution is asserted here. Continue with per-excerpt historical-revision checking, then fresh CI and PDF proof regeneration.

## Earlier milestone record

# Instructional revision checkpoint — November 15, 2026 (Central)

Chapters 1–18 now have an initial instructional treatment in the review branch. Chapters 6–11 received learning objectives, source-oriented guided labs, troubleshooting, and independent Chapter Summary sections. Chapters 12–18 received explicit objectives and worked guided labs; Chapters 12–14 received separate chapter summaries while Chapters 15–18 retain existing summary/exercise sections. The technical scope and planned 40 chapters remain unchanged.

This is a manuscript-text review-branch checkpoint, **not** a newly generated typeset proof. The previously recorded 142-page PDF is historical and does not incorporate these newer chapter edits. There is no new word-count/page-count estimate for the revised edition yet. The narrative examples reference existing companion code, but no fresh compilation, automated test run, device check, iOS build, screenshot inspection, or source-to-text line-by-line audit was performed as part of this checkpoint. Earlier CI results must be treated as historical source-revision evidence.

Next: compare each Chapter 1–18 claim and code excerpt with the matching companion-code revision, fix discrepancies, run code CI, and regenerate and inspect the complete 8 × 10 proof. Then begin Chapter 19. The full manuscript remains an editorial draft, not publication-ready.

## Earlier milestone record

# Part I instructional revision — November 15, 2026 (Central)

The manuscript remains at Chapters 1–18 and is now 142 pages. Chapters 1–5
received their first substantive instructional pass, adding approximately 5,600
words overall while preserving scope, 11-point body and 9.5-point code.

Each revised chapter now has What You'll Learn, prerequisites/deliverable, guided
work, worked reasoning, troubleshooting, a distinct 100–150-word Chapter Summary
and independent exercises. Chapter 3 identifies the matching historical starter
checkout; Chapters 4–5 trace its actual source and 37-case portable baseline.
The new companion Part I lab consolidates those instructions.

All 18 chapters received a structural inventory, recorded in instructional-audit.md.
Only Chapters 1–5 received substantive instructional review in this pass. Chapters
6–18 still need it, starting with the native-interface material in Chapters 6–11.
The first five still require actual native observations, verified screenshots and
reader feedback before being treated as final.

The revised Part I pages and contents were visually reviewed. Table headings are
kept with their tables, and each revised chapter's closing summary/exercises/
references form a coherent ending. All 142 pages pass text-margin and internal
link checks; the PDF has 25 bookmarks and 50 links.

No application or test implementation changed. Command paths, starter resources,
expected fixture IDs, named tests and matching revision were checked against the
repository. Historical build/test results remain historical; no fresh Windows
red/green or device run is claimed for these documentation changes.

Next: the substantive instructional revision of Chapters 6–11. Chapter 19 remains
the next new technical chapter after the existing foundations receive the planned
learning-focused pass.

## Earlier milestone record

# Editorial direction update — November 15, 2026 (Central)

Retain the current sophistication and full planned scope. John's instruction is to
provide enough documentation and working samples for a valuable resource and
learning tool. No advanced topics are removed and no second volume is approved.

The 800-page estimate is no longer a fixed quota. No replacement page target is
approved. The 125-page Chapters 1–18 proof remains a first draft, pending a fuller
instructional pass. New teaching-standard.md defines reader setup, complete source,
numbered walkthroughs, explained decisions, expected results, troubleshooting,
worked exercises and separate verification requirements.

The companion learning guide and Chapter 18 guided lab are the first documentation
improvements. Existing source and recorded 245 portable / 26 API results are
unchanged. No new code/device verification is claimed for this documentation edit.
Continue implementation with Chapter 19 while expanding and auditing earlier drafts;
chapter count alone is not a teaching-completeness measure.

## Earlier milestone record

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

