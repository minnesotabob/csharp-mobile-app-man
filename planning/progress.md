# Finishing pass: complete source/artifact reconciliation — November 17, 2026 (Central)

Confirmed the current saved proof has all forty chapters, four appendices, glossary,
index, 466 pages and 61 bookmarks. The saved version-29 PDF and matching EPUB included
five Part illustrations and their opener placement updates that were missing from
published main. Restored those existing illustrations as documented grayscale print
JPEGs and copied the exact image/paragraph order into Parts III–VII. Recovered the
matching title/overview/materials-notice wording. No chapter prose or application
C# changed; no scene or native screenshot was generated.

The repository README now lists all forty chapters in order, including previously
omitted links to Chapters 19–20 and 24–31 and the Part VI introduction. Added
planning/finishing-checklist.md to distinguish completed instruction/artwork from
remaining source/excerpt, prose, screenshot, native/provider, EPUB-reader and final
publication work. Updated the editorial-review response and production instructions;
older dated progress entries remain historical.

## Actual checks

- Local PDF rebuild: 466 pages, 61 bookmarks, 51 distinct images. All 466 pages
  preserve the saved proof's extracted text; all bookmark titles/destinations match.
- Navigation audit: forty chapter bookmarks exactly once in order, eight Parts,
  four appendices, eight distinct original Part illustrations, 442 numbered chapter
  reference expressions, 111 exact index headings and 222 matching destinations.
- PDF trim/text boundaries pass throughout. Visual inspection covers contents,
  draft overview, the restored Part openers and the linked index. The new materials
  paragraph was reconciled to the latest saved copy, rather than reverting its status.
- EPUB audit: 64 XHTML documents preserve the saved EPUB's body text; 155 exact
  code blocks, 51 described images, 111 subject links, 290 resolving package
  references and complete manifest/spine. W3C EPUBCheck 5.4.0 reports zero fatals,
  errors, warnings or infos. Pandoc remains 3.1.11.1; no new reader/device pass.
- The existing saved PDF/EPUB remain the authoritative downloadable copies. The
  compact print-asset rebuild does not replace their higher-size packaged artwork.

No new C#, API, Android, iOS, provider, store or accessibility execution is claimed.
This is a source/production reconciliation, not completion of the full line edit
or native screenshot collection. Next: source-listing/milestone review and real
native captures, followed by final reader, metadata and physical-proof acceptance.

# GitHub publication completed — November 17, 2026 (Central)

Both public minnesotabob repositories are now published on main. The reviewed
source snapshots match the local Git trees exactly:

- Manuscript: ac98cef2cc73d57d76193955966d1c09b7d5ce92.
- Companion: 00e4598e642dd57141f5f64a5233bd4f88bb2cae.
- Manuscript proof workflow passed: https://github.com/minnesotabob/csharp-mobile-app-man/actions/runs/44088936209
- Companion portable build/tests and selected console labs passed: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/44088647782

Publication used the connected GitHub account after confirming public ownership
and write authority. The published snapshots preserve the exact prepared file trees.
Original local checkpoints cited in the book remain recoverable from each
source-history/pre-publication.bundle. Fresh public clones successfully verified
and fetched both bundles; companion 22489d1 and manuscript dcd2f9b were recovered
as exact original commits. See source-history/README.md for the reader procedure.

This later record changes documentation only. The workflow observations above
retain their original snapshot identities and are not relabeled as runs of this
record commit. No fresh API, Android, device, iOS, provider or store result is
claimed. Those acceptance gaps remain as documented. Earlier publication-blocked
entries below are historical and no longer describe the current GitHub status.

# Scope corrections and first reflowable EPUB — November 17, 2026 (Central)

Completed a targeted milestone/integration wording pass in twelve documents. Early
API/navigation/storage/media limitations now name their chapter checkpoints and
separate later bounded implementations from still-pending native/production work.
No application source or companion C# changed. This does not close the remaining
full technical, line-edit, device or provider acceptance.

## EPUB production and actual validation

Added production/build_epub.py, audit_epub.py and epub.css. The EPUB derives from
the same 61-document source inventory as the PDF, combines chapter/Part/Appendix
headings, assigns unique internal anchors, packages the existing figures and uses
relative body/code/table styling. Its 111-entry subject index links directly to
sections rather than importing paper page numbers. No unrelated cover is used.
Raw HTML parsing is disabled so generic-type prose is escaped as text; code blocks
are independently checked for exact preservation.

Actual local checks: Pandoc 3.1.11.1 and official W3C EPUBCheck 5.4.0 with Java 21.
EPUBCheck reports zero fatals/errors/warnings/infos. Package audit passes 64 XHTML
documents, all 155 exact code blocks, 46 described image placements, 111 subject
links, 285 resolving local package references and complete manifest/spine. MuPDF
opened the actual EPUB at 390x780 and 820x1000; title/navigation, code and tables
received visual reflow review. A reader may still paginate a code block across
screens despite CSS cohesion requests; no code text is omitted. Apple Books,
Kindle conversion, actual hardware, screen-reader acceptance and final publishing
metadata/cover remain pending. Structural conformance is not accessibility or
store certification. See planning/epub-proof-review.md for exact hashes/tool scope.

## Updated PDF and saved deliverables

The corrected PDF remains 464 pages and 61 bookmarks. Production checks pass all
trim/text/image/chapter markers. Navigation audit verifies 442 numbered chapter
reference expressions, 111 exact paginated headings and 222 matching index links.
The twelve changed-statement pages received contact-sheet inspection.
The existing opening-draft-8x10.pdf was saved successfully as version 28.
The first Building-Mobile-Apps-CSharp15-proof.epub was saved successfully as
libfile_d89a607b942c81918a2d79b08bc8a0a5. Both local identities were applied by the
ordered prepared upload helper. No additional public artifact or deployment exists.

No GitHub push or remote workflow execution was attempted. The earlier explicit
main-publication requirement remains unresolved; changes are committed locally.

Next: remaining Part artwork and actual native captures, broader editorial/source
review, EPUB reader/accessibility acceptance, outstanding device/provider/iOS gates
and final production facts/credits. Do not characterize this EPUB or app as ready
for public distribution solely from these checks.

# Publication matter and linked subject index — November 17, 2026 (Central)

Added a draft publication notice, acknowledgments, conservative author biography,
companion-code/errata guide and materials/third-party notice map. Biography uses the
known author/creative/location/family facts without adding degrees, awards, years
of experience or unconfirmed credentials. ISBN/date/edition assignment, final
credits and any redistribution-license audit remain pending. No dedication was
invented. Existing title/imprint, 40-chapter scope and 8x10 typography are preserved.

The reader guide now reflects the existing appendices and draft instructional passes.
It distinguishes the proof index from final paperback indexing and notes matching
source checkpoints. Later local work awaiting repository publication remains identified
honestly in the companion access guidance; no unavailable milestone is promised.

## Curated index and cross-reference validation

planning/subject-index.json selects 111 unique substantive section openings across
chapters and appendices. production/subject_index.py validates exact source headings
and collects actual page locators through ReportLab multiBuild. Entries are sorted,
with linked terms and page locators. The index does not populate itself from every
word occurrence, guessed page ranges or old proof pagination. Its final editorial
coverage remains a production review task.

production/audit_navigation.py checks 61 included source documents, 428 numbered
chapter-reference expressions and relative Markdown targets. Each of the 111 source
headings is verified in the actual locator page. All 222 index links resolve, in the
correct term/locator order, to their corresponding section page objects. The checker
handles this PyMuPDF version's /Fit link representation by inspecting actual PDF
Dest references, rather than treating every LINK_NAMED classification as broken.
The existing production workflow now includes this audit and index-plan/source triggers.

## Saved proof and review

464 pages, 61 bookmarks, the unchanged 46 distinct images and a three-page subject
index beginning on page 462. Publication notice page 2, acknowledgments 8, companion
resources 457, materials/notices 459 and author bio 461. Added front matter shifts
chapter page numbers; all index and contents locators were regenerated together.
All required section/figure/image markers, 8x10 trim and outer text boundaries pass
locally. Contact-sheet and larger review covered the new matter, contents/overview,
reader guidance and compact index. Body/code remain 11/9.5 pt.
Final PDF SHA-256: 0806be93cdaded5e4e728a94b2e7267fec8cbce934f8bb6980b52627272fa1fa.
Existing opening-draft-8x10.pdf replaced successfully as version 27.

No application/companion code changed, and no new C#/API/Android/iOS/provider/device
execution is claimed. No push or other GitHub publication was attempted; earlier
explicit-main-authorization requirement still applies. Remote CI was not run.

Next: final editorial/continuity and source-listing review, remaining Part artwork
and real app captures, incomplete device/provider/privacy/iOS acceptance, final
publication facts/credits and accessible EPUB production. Re-review the subject index
when text stabilizes. The proof is still not a finished publication or released app.

# Appendices and glossary continuation — November 17, 2026 (Central)

Added the four planned substantive appendices and an alphabetical 73-entry glossary:

- Appendix A: targeted C# contracts, await/cancellation/result ownership, nullability,
  records/collections, events/disposal and DI, with excerpts from actual companion files.
- Appendix B: source versus historical/proposed tools, local/network/TLS identity,
  Android/iOS boundary diagnosis, customer-journey faults and bounded reporting.
- Appendix C: project/API/fixture/configuration navigation, protected synthetic routes,
  identity and storage distinctions, and complete-lab references.
- Appendix D: bounded optional watch-companion design, actual platform/tooling limits,
  stale/disconnected command policy and maintenance criteria. No watch code is promised.
- Glossary: 73 definitions with chapter pointers, including identity, storage,
  network/media, release and verification terms. These are not final index page numbers.

## Source and editorial checks

Companion snapshot inspected: 3f07b25743c00ef0a1ad64347f310673f5ecad7c.
No application or companion source changed. DebouncedQuery excerpts and named source
paths were checked directly; the five-record bundled catalog was verified. Relevant
endpoint/configuration/identity/platform declarations and existing labs were inspected.
Primary platform sources were checked for the watch discussion. No new C# execution,
mobile build, device observation or live-provider result is claimed. Existing pending
native/privacy/provider/signing gates are unchanged.

The renderer combines each Appendix label/title into one contents/bookmark entry,
watches appendices/back-matter in proof CI, and distinguishes glossary term labels
with the existing heading font without altering body/code sizes. The production
validation requires all four appendices and the glossary.

## Saved print proof

454 pages, 56 bookmarks and the same 46 distinct images. Appendix starts: A 428,
B 434, C 440, D 446; glossary 449. All expected markers, 8x10 trim and outer text
boundaries pass the production workflow's validation locally. All 27 new reference
pages received contact-sheet review; code, tool/configuration tables, glossary,
contents and draft overview received larger inspection. Final PDF hash:
8d9103e2bec5aecf99ed944985aa2f4dd13245a49564593a7dbffa218fc7900c.
The existing opening-draft-8x10.pdf was updated successfully to version 26.

No GitHub push was attempted in this continuation. Prior automatic-review publication
blocks remain unresolved; local commits preserve the work. No new remote CI is claimed.

Next: complete the remaining front/back matter and companion/errata reference, review
cross-references and prepare the substantive index after text stabilizes. Final author
bio/legal/ISBN details must use confirmed information. Remaining Part artwork,
verified native screenshots, device/provider/iOS acceptance and accessible EPUB are
still outstanding. The manuscript remains an editorial proof.

# Chapter 40 release rehearsal and maintenance — November 17, 2026 (Central)

All forty planned chapters now have instructional drafts. Chapter 40 adds five
outcomes/prerequisites, candidate/source/evidence mapping, existing workflow inventory,
explained packet validation, actual synthetic failure/restoration, distribution authority,
old/new client compatibility, rollback limits, dependency/diagnostic maintenance,
reader checkpoints/errata, owner-role worksheet, guided reasoning, troubleshooting,
summary and independent extensions. Two authored diagrams show evidence and recovery.

## Executed new sample

Companion implementation: 22489d1906110ebf4925aa6b2a2b04c0b2833130.
Later companion documentation: 3f07b25. Actual local Python is 3.12.14 on Linux.
All 17 boundary tests pass without skips. The synthetic packet validates, changed
candidate bytes are rejected, and restoring the owned fixture validates again.
Retained JSON keeps its original selected manuscript metadata
 dcd2f9b1bfe64a9a80c99beb51b8d2aa76224e56 (the preceding Chapter 39 checkpoint).
It is not relabeled as the later Chapter 40 manuscript. Generated receipt passes are
invented fixtures, not new app/platform passes. Fixed output retains manual not_run,
distribution blocked and release readiness unassessed. No application C# changed.

The new workflow is manual-dispatch only, contents-read, secret-free and unexecuted.
No fresh C# suites, Android/API, iOS/device, live provider or store run is claimed.
Existing real Android update and published HTTPS restore observations retain their
original source/harness/run identities and limits. The chapter explains how a real
subject graph differs from the deliberately strict single-artifact synthetic fixture.

## Manuscript and saved proof

The proof is 427 pages, 51 bookmarks and 46 distinct images: four Part illustrations
plus forty-two authored technical diagrams/recaps. Chapter 39 starts on page 403;
Chapter 40 starts on page 416. All 427 pages pass the production workflow's actual
chapter/caption/image, 8x10 trim and outer text-boundary validation locally. A contact
sheet covers all twelve new pages; opening, contents, About This Draft, code, workflow
and summary/exercise/reference pages received larger visual inspection. Body/code
remain 11/9.5 pt. The existing PDF was replaced successfully as version 25.

## GitHub publication remains blocked

The continuation request did not satisfy automatic review's explicit-main-publication
requirement. Both attempted Chapter 39 pushes were rejected again. No indirect route,
alternative publication or additional push was attempted. All Chapter 39–40 changes
are committed locally; remote manuscript main remains e688ee8 and companion main
remains 0d81cdc. No new GitHub production CI result is claimed. User must explicitly
authorize pushing both repositories to main before publication is retried.

## Next work

Begin the targeted appendices and consolidate the environment/source reference, then
glossary, index planning and remaining front/back matter. Preserve all advanced scope.
In parallel when prerequisites exist, execute Chapter 39's iOS/native/signing gates,
complete physical-device/provider/privacy acceptance, remaining Part artwork and
verified app captures. Final index pagination and accessible EPUB follow stable text.
Forty chapter drafts do not certify release readiness or a finished publication.

# Chapter 39 iOS release instructional draft — November 16, 2026 (Central)

Added Chapter 39, iOS Signing and App Store Release from Windows, with five
learning outcomes, prerequisites, explicit project evaluation, compatible-toolchain
research, controlled signing/archive procedures, source-to-artifact configuration,
TestFlight/update recovery, reviewer access, troubleshooting, guided reasoning,
summary and independent extensions. Two authored grayscale diagrams distinguish
build locations and candidate gates. Companion documentation commit: 2a2bf75.

Actual source review found the macOS-conditional iOS framework entry, existing
URL/background/photo declarations, and no checked-in iOS entitlements/privacy
manifest files. Generated output and dependency behavior remain to inspect.
The primary-source candidate is SDK 11.0.100, workload set 11.0.100.1, iOS pack
27.2.11039 and Xcode 27.2. The Microsoft release's macOS 16.6+ wording conflicts
with Apple's Tahoe 26.6+ Xcode table; host planning explicitly follows Apple's table.
No toolchain upgrade was applied to the companion.

The new proof has 415 pages, 50 bookmarks and 44 distinct images (four Part
illustrations and forty technical figures/recaps). Chapter 39 begins on page 403.
All pages pass 8x10 trim and outer text-boundary checks. A contact sheet covered
all thirteen new pages; opening, declaration table, publish/inspection source and
summary/exercises received larger visual inspection. Body/code remain 11/9.5 pt.
The production workflow now requires Chapter 39 and both new figure captions.

No production application C# changed. No fresh portable, API or Android execution
is claimed for documentation-only edits. iOS simulator compilation/launch, device
archive signing, Windows remote publication, TestFlight processing, physical-device
acceptance and store submission remain not_run. Chapter 39's planned signed-candidate
outcome is still incomplete. The release worksheet retains each pending gate.

PDF writeback succeeded: existing opening-draft-8x10.pdf, version 24, 415 pages.
Manuscript implementation commit e5d12b2 and companion documentation commit 2a2bf75
are local only. Automatic approval review rejected both pushes to default main as
insufficiently authorized by the continuation request. No push retry or alternative
publication was attempted. Remote manuscript remains e688ee8; remote companion
remains 0d81cdc. Independent production CI has not run for the new chapter.

Next: execute iOS verification on a compatible Mac with controlled signing assets
when available; Chapter 40 release automation and maintenance remains the next
unwritten chapter. Complete front/back matter, index, remaining artwork, native
captures and accessible EPUB also remain in the agreed scope.

# Chapter 38 Android signing and observed upgrade — November 16, 2026 (Central)

The signed candidate was built at `b15607e6afe2427d4d21b38a913dafcbbc85a082`.
The final smoke harness is `698aa3d431d0f7e39239c3a31a174263acf0295c`.
Application/Core/API production C# is unchanged by the later harness corrections.

| Check | Actual result | Evidence |
| --- | --- | --- |
| Portable Release at final harness source | 644 cases pass; no errors/failures/skips/not-run | https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43950480838 |
| Python package-audit guards | 12 tests pass locally and in package job | https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43947661043 |
| Signed Release publication and package audit | v1/v2 x86-64 APKs and v2 arm64 AAB pass identity, signature, manifest/SDK, native alignment and bundle checks | Same package run; package job succeeded although its earlier implicit-launch harness failed |
| Corrected immutable-candidate emulator recheck | Actual installation, Home launch, synthetic draft save, replacement update, same UID, Home relaunch and persisted draft read all pass | https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43950480975 |

## Exact observations and retained evidence

The emulator reported `sdk_gphone64_x86_64`, API 35, x86_64 and a 4096-byte page size.
It used the Pixel-6 runner profile. APK version codes 1 and 2 installed in order, without
an intervening uninstall. Both source APK hashes matched their package report.
The actual FileRequestDraftStore saved and recovered invented `release@example.test`
data through the guarded test-only probe. Normal app builds do not contain that probe.
Cleanup removed only the disposable package after the observation.

The built artifacts report minimum API 26 and target API 37. Both APK signature and
16 KiB ZIP-alignment checks passed; all ten native libraries in each of the three
artifacts passed the static ELF load-alignment checks. The AAB passed jarsigner,
certificate and pinned bundletool validation. Actual 16 KiB execution remains not_run.
Individual Release publish summaries reported zero compiler warnings/errors; historical
Android dependency-install/runner deprecation notices remain separate from compilation.

Safe original reports are retained without rewriting their provenance:

- `docs/reviews/ch38-package-evidence.json`: candidate b15607e / package run 43947661043.
- `docs/reviews/ch38-upgrade-evidence.json`: same candidate, harness 698aa3d / run 43950480975.
- `docs/reviews/ch38-package-evidence-b0e4729.json`: earlier successful package audit.

Artifacts 14265787394 (packages) and 14266347694 (bounded upgrade JSON) expire after
seven days; no private keystore/password, customer database or raw diagnostic file is
uploaded as safe evidence. GHA console diagnostics remain a separate channel.
Original JSON hashes/source fields are comparison metadata, not independent attestation.

## Failures investigated and corrected

Current apksigner labels the certificate by signature scheme (`V3.0 Signer:`), and
current aapt2 labels the minimum `minSdkVersion`. The parser preserves one-signer,
expected-certificate, package/version and SDK assertions while supporting those formats.
Distinct explicit versioned manifest inputs fixed stale package-version reuse. The
emulator's empty successful package-list query replaced pm path, whose nonzero absence
status had stopped the freshness guard. Finally, the installed manifest was inspected:
its MAIN/LAUNCHER filter was present. Resolving and explicitly starting that component
fixed the implicit shell-intent failure, without altering the candidate application.

The immutable recheck downloads a named audited artifact with contents/actions read
permissions, verifies candidate identity and APK hashes, and records both candidate and
harness revisions/runs. It does not relabel old package bytes as a new compilation.
The optional frozen fixture expires; rebuild/audit a new one before updating its pointer.
The full signing workflow still builds fresh candidates for app/publisher/audit changes.

## Scope limits

This establishes one actual isolated signed Release emulator scenario. It does not
complete full native acceptance, production migration/recovery, physical Android/iOS,
16 KiB runtime, TalkBack/VoiceOver, real identity/MFA, real checkout, Play signing/test
tracks/submission, public hosting or iOS compilation/signing. Existing manual acceptance
rows and release_readiness remain unassessed unless separately observed. No store
upload, production signer or real customer/provider account was used. Earlier API and
other workflow evidence retains its own source and scope; it was not silently rerun.

## Manuscript and next work

Chapter 38 supplies five outcomes/prerequisites, Windows signing steps, explained
APK/AAB audit source, actual package and emulator observations, a frozen-candidate
recheck, Play submission/test-track preparation, MFA reviewer access, guided work,
troubleshooting, a 132-word summary and independent extensions. Two authored figures
explain signer boundaries and the data-preserving update. Original grayscale test-bench
artwork now opens Part VIII, with the exact authored roadmap retained separately.
The outline's 40-chapter scope, sophistication and 8x10 typography remain unchanged.

Next: Chapter 39, iOS Signing and App Store Release from Windows. Preparation notes
record Apple's current submission minimum and the need to verify the exact supported
.NET 11/Xcode pair; no iOS or store execution is implied. Chapter 40 and complete
front/back matter, index, remaining artwork, native captures and EPUB remain future work.

# Chapter 37 performance, reliability and accessibility — November 16, 2026 (Central)

Final executable source: `c82eff270ec50c3ef4916c4401576ba1b893b1a9`.
All six workflows pass at that exact revision:

| Check | Executed result | Evidence |
| --- | --- | --- |
| Portable Release | 644 cases; no errors/failures/skips/not-run; build 0 warnings/errors | https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43876553252 |
| API/probe Release | 109 cases; builds 0 warnings/errors; actual Kestrel public contract smoke passes | https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43876553224 |
| Android Debug | Final compile 0 warnings/errors; merged capability checks pass | https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43876553443 |
| Traceable acceptance | 18 projector checks, 644/109 C# cases, six mapped automated rows pass; six manual rows not_run and release readiness unassessed | https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43876553254 |
| Published HTTPS recovery | Actual pinned-loopback Staging/restore/hold/release/redacted-trace drill passes | https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43876553320 |
| Release performance investigation | API publish and runner build succeed without compiler diagnostics; actual search/API/retention report generated | https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43876553256 |

The Android dependency-install phase retains the earlier cmdline-tools;21.0 resolution
warning, separate from the final clean compile. Node runner deprecation messages are
not C# warnings. No local dotnet runtime exists in this workspace; C# execution occurred
on GitHub-hosted Windows. Eight new portable cases preserve deterministic stress data,
reference/snapshot equivalence across both orders/queries/filters/favorites, ownership,
invalid/empty input and view-model selection behavior. Existing suites remain intact.

## Measurements actually observed

Host: Microsoft Windows 10.0.26100, .NET 11.0.0, X64, four logical processors on a shared
GitHub VM. Same build/data, 10,000 records, five queries, three paired warmups and 21
alternating-order pairs. Complete ordered ID sequences are checked outside timing.
No fixed elapsed-time pass threshold or forced GC is used in the search samples.

| Metric per five-query batch | Reference filter + sort | Reused snapshot |
| --- | ---: | ---: |
| Median | 107.7073 ms | 93.4096 ms |
| Nearest-rank p95 | 128.6835 ms | 121.0163 ms |
| Median current-thread allocated bytes | 633,032 | 140,896 |

Observed median time reduction is 13.27%; allocation reduction is 77.74%. These are
scoped desktop observations, not a repeated-device speed guarantee. The first snapshot
construction separately costs 28.8451 ms and allocates 1,196,968 bytes, including
first-use/JIT work. Its cost is excluded from warmed queries, not free. Matching remains
linear; remaining CPU work needs a trace before another optimization.

Actual published public API child process-to-first-health is 614.9966 ms with 100 ms
polling. After three warmups, 21 sequential five-record catalog HTTP/body reads have
median 0.3119 ms, p95 0.3419 ms and 2,731 response-body bytes. This is loopback HTTP,
not native first-frame startup, TLS/WAN load, capacity, wire/egress or energy evidence.

The controlled omitted-Dispose experiment uses 32 existing BackgroundPlaybackOwner
instances retained through a long-lived fake player's event, each with a synthetic
64 KiB closure. Subscriber count changes from 32 to 0 after explicit disposal; observed
weak owners change from 32 to 0. Only subscription invariants are required; weak counts
are diagnostic observations. Forced GC occurs only in this reachability experiment,
not in the application/search timing. This is not a discovered native page leak or
physical erasure result.

The safe observed JSON with all sample values is retained at
`docs/reviews/ch37-desktop-evidence.json`, source/run identity unchanged. Artifact
14229802314 expires November 23, 2026; digest
`sha256:5d1e054946769e6a4db638ffb15ef2406458024e294c34cf2eac075fda379165`.
Only safe JSON is uploaded; no raw process logs, dumps, private requests or environment
secrets are exported by this workflow. Hash/source fields are not independent provenance.

## Native, image and accessibility boundaries

The new transient PerformanceLabPage is wired from Home. It prepares/searches bounded
public metadata off the UI thread and fences obsolete results by visibility/generation.
Its CollectionView has a finite Grid viewport outside the controls ScrollView, flexible
text rows and cumulative template-construction inspection. Android compilation passes;
no actual frame/scrolling/lifecycle observation is inferred from compilation or counts.
The main browser still uses the original five bundled records with the stable snapshot.

Original raw PNG variants are 1200x1400/13,263 encoded bytes and 96x112/7,112 bytes.
One RGBA-plane estimate is 6,720,000 versus 43,008 bytes (156.25 ratio), not measured
native memory; caches/downsampling/stride/GPU/intermediate buffers remain to observe.
Generators, dimensions and byte hashes are retained. No existing private delivery cache
policy is relaxed to enable the public stress fixture.

The device/accessibility review under docs/reviews explicitly remains incomplete.
Declared source-color ratios are calculated from App.xaml (minimum inspected pair
8.0415:1, above 4.5:1); disabled/focus/high-contrast/rendered states remain unobserved.
No native WCAG/accessibility acceptance or named-device result is invented.

Physical Android/iOS startup/frames/decoded memory/energy/wire counters, TalkBack/
VoiceOver, large text/localization/focus, actual OS recovery and signed-package/install/
upgrade remain pending. Full trim/NativeAOT compatibility is not claimed: current
string-path bindings, reflection JSON and auth/media dependencies need target-specific
review. Current official .NET 11 CoreCLR/diagnostic/trim/AOT guidance is referenced in
the chapter/worksheet; no Mono default or completed AOT publish is asserted.
Public production hosting, live identity/MFA/provider checkout, real customer recovery,
remote diagnostics/newsletter integration and iOS also retain their earlier constraints.

## Manuscript and editorial proof

Final chapter source `6eef168d92873bec05ad75f7f7d6857ced0863b5` independently passes
PDF production CI:
https://github.com/minnesotabob/csharp-mobile-app-man/actions/runs/43879295673

Chapter 37 adds five outcomes/prerequisites, anniversary/catalog-scale narrative,
explained snapshot/allocation/retention/UI-publication source, actual before/after and
image-size tables, full Release/device profiling protocol, runtime/trim/AOT review,
source palette/accessibility disposition, eight-step guided lab, troubleshooting,
116-word summary, worked reasoning and three independent extensions. Two authored
figures show matched measurement paths and event-root retention. The full planned
40-chapter intermediate/advanced scope is preserved. The measured investigation does
not complete the physical-device/accessibility observations in the outline.

The proof has **387 pages**, 8 x 10 inches, 11-point body/9.5-point code,
48 bookmarks and 39 distinct images (three original Part illustrations plus 36 authored
figures). Chapter 37 starts on page 374. All trim sizes, expected markers and outer
text boundaries pass. Contact-sheet inspection covered the new chapter; opening,
diagrams, actual comparison/allocation tables, code, retention, summary/exercises and
revised overview received larger inspection. Learning outcomes/prerequisites/build
scope fit the chapter's first page. The existing downloadable PDF was updated successfully.

Next: Chapter 38, Android Signing and Google Play Release. Recheck current official
requirements, prepare a reproducible candidate/key-boundary workflow and keep actual
account/store upload, secrets and install/upgrade observations explicit. No public
publishing is implied by the tutorial. Chapter 39 retains iOS signing/publication work.

# Chapter 36 complete-application testing — November 16, 2026 (Central)

Final executable acceptance source: `dd137ed10809a40ae38217b485b331fe33552760`.
The C# composed journey was introduced at `2326551d55d2209d861509781dbf2dec7c58d791`;
subsequent executable changes affect the Python projection/workflow only. No application,
Core or API production source changed in Chapter 36.

| Check | Executed result | Evidence |
| --- | --- | --- |
| Portable Release at final source | 636 cases pass; no errors/failures/skips/not-run; build 0 warnings/errors | https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43872069017 |
| Complete acceptance workflow at final source | 18 Python projector checks; 636 portable and 109 API cases; both builds 0 warnings/errors; automated evidence gate passes | https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43872068773 |
| API/probe workflow at unchanged C# test source | 109 cases pass; API/probe builds 0 warnings/errors; actual Kestrel public HTTP smoke passes | https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43869939065 |

The 636 portable cases are unchanged; two new API theory rows exercise actual clients,
real on-disk journals, signed bearer middleware and the real API pipeline through
TestServer. DropCommittedReply fires after the endpoint returns success. The rows cover
acceptance or revision uncertainty, journal reopen/reconciliation, one operation/order,
revision replay after later review, duplicate synthetic TEST payment events, server
store/host reopen, coherent history, private WAV grant/read/hash and foreign-owner denial.
The fault-fired and absent-confirmation assertions prevent an unnoticed happy-path pass.
Provider checkout, identity discovery and production/review transitions remain controlled
fixtures. TestServer is in-process, not a native UI, real socket/TLS or live provider run.

## Acceptance evidence actually generated

The final workflow generates fresh xUnit XML and projects it through the versioned plan
within one source-bound job. All six exact method selectors resolve with their reviewed
case counts: 2 order-recovery, 5 authorization and one each sync replay, media resume,
restore review and diagnostic privacy. The six manual rows remain **not_run**, and
release_readiness remains **unassessed**. The selected spine is not full requirement
coverage or a percentage of the application's behavior. Complete suites must also pass;
an unmapped failure still fails the gate.

The projector's 18 checks separately exercise missing selectors/count changes, failed/
skipped/not-run cases, environment errors, invalid schema, duplicate per-run IDs,
optional metadata, equal display names, UTF-8/UTF-16 declaration handling, private-output
exclusion and non-overwrite. These Python checks are not counted as C# cases.
Only the bounded acceptance-report.json is uploaded, with seven-day retention. Raw XML,
private failure messages, paths and captured output remain outside uploaded artifacts.
Runner console output is a separate channel and these public fixtures stay synthetic.
Input hashes enable comparison; they do not authenticate an arbitrary report or prove
its revision. Same-job workflow execution supplies the association in this lab.

The initial report workflow failed input validation even while all 636/109 C# cases
passed. Safe diagnostic codes identified the case-identity guard. The parser initially
required unique human display names and type/method metadata for every row. It now uses
documented per-run IDs, accepts absent optional metadata for unmapped cases and still
refuses to satisfy an absent required selector. Success was first demonstrated at
`6d6e8f02f71d216caafe2784ae528741313f3bc9` in run 43871552234, then verified at the final
encoding-guard revision above. The initial failed report is not counted as acceptance.

## Evidence retained separately

Application/API/Core source remains identical to the Chapter 35 verified implementation
`89eeecf23fffa599fbc3f262f79f711f8624afe4`:

- Android Debug final compilation and merged capability checks pass in
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43860401923.
  The dependency-install phase's cmdline-tools;21.0 resolution warning remains recorded
  separately from the final compile's zero warnings/errors. No new native run is claimed.
- Actual published-process pinned-loopback HTTPS, restored readiness hold/release,
  preserved TEST payment replay, invalidated old grants and redacted failure trace pass in
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43860402147.
  This is isolated synthetic staging, not public provisioning or customer recovery.

Chapter 36 adds the device/provider record format and proposed risk-based phone/tablet/
iPhone/iPad matrix in complete-application-testing.md. No device model/OS observation,
Appium driver/session, accessibility acceptance, OS process-kill recovery, live MFA,
hosted TEST payment or iOS release result is fabricated. Those manual rows stay not_run.
No production business authority, remote crash/exporter, real newsletter integration,
signed package/install/upgrade or final release approval is supplied by this chapter.
This workspace has no dotnet runtime; C# execution occurred on GitHub-hosted Windows.

## Manuscript and editorial proof

Final chapter source `9aaa2b04edc0f6fa56d0e14ac3d1e3aada25989c` independently passes
PDF production CI:
https://github.com/minnesotabob/csharp-mobile-app-man/actions/runs/43872121912

Part VIII's introduction and roadmap connect regression, native/provider observation,
release preparation and maintenance. Chapter 36 adds five outcomes/prerequisites,
anniversary uncertainty/recovery narrative, explained actual test/handler/reporter
listings, evidence-layer and troubleshooting tables, safe artifact/provenance reasoning,
risk-based device/accessibility/provider matrix, eight-step guided lab, a 122-word summary,
one worked exercise and three independent extensions. Two new authored figures show the
Part roadmap and evidence projection. The 40-chapter intermediate/advanced scope remains.

The final proof has **373 pages**, 8 x 10 inches, 11-point body/9.5-point code,
47 bookmarks and 37 distinct images: three original Part illustrations plus 34 authored
figures. Part VIII starts on page 359 and Chapter 36 on page 361. All page sizes, expected
markers and outer text boundaries pass. The new material received contact-sheet review;
opening/roadmap, evidence figure, code/parser, troubleshooting and summary/exercises were
inspected at larger scale. The About This Draft overview stays on one page without an
orphaned copyright line. Existing downloadable PDF was updated successfully.

Next: Chapter 37, Performance, Reliability, and Accessibility Review. Add reproducible
large-data/image fixtures and measured investigations while keeping named-device
benchmarks, physical-device behavior and accessibility results pending until observed.
Preserve the planned 40 chapters and explicit release/provider constraints.

# Chapter 35 hosting, diagnostics and recovery — November 16, 2026 (Central)

Final executable source: `89eeecf23fffa599fbc3f262f79f711f8624afe4`.
All four independent Windows workflows pass at that exact revision:

| Check | Executed result | Evidence |
| --- | --- | --- |
| Portable Release | 636 cases; zero errors/failures/skips/not-run; build 0 warnings/errors | https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43860402055 |
| API/probe Release | 107 cases; zero errors/failures/skips/not-run; builds 0 warnings/errors; actual Kestrel public contract smoke passes | https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43860401915 |
| Android Debug compilation | Final compile 0 warnings/errors; merged capability checks pass | https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43860401923 |
| Published HTTPS staging/recovery | API publish and runner build pass; actual pinned-loopback TLS drill passes | https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43860402147 |

The Android dependency-install phase still emits the earlier cmdline-tools;21.0
resolution warning. It is separate from the final clean compile. Runner Node deprecation
messages are not C# compiler warnings. This workspace has no dotnet runtime; execution
evidence comes from these GitHub-hosted Windows jobs, not a local test claim.

The 19 new portable cases exercise real SQLite initialization, legacy migration,
future-version refusal without mutation, online WAL snapshot, manifest/byte tampering,
new-directory restore and exact-generation hold release. They also cover typed/default-off
local diagnostics and separately consented newsletter boundaries. Eight new API cases
cover opt-in routes, readiness, restore release, safe failure fields, body bound, bounded
metric labels and invalid deployment flags. Initial source passed portable/Android/real
staging, but five API cases exposed services registered before test-host configuration
was final. Lazy settings and final options validation corrected that host-layering defect;
the final 107 cases all pass. No failed result is counted as acceptance.

## What the published-process drill actually established

OperationsLab launches the published API DLL under explicit Staging with synthetic
business writes disabled and an allowlisted environment. It creates an ephemeral
localhost certificate; its fixed-origin client pins the exact certificate, checks the
hostname and rejects other TLS errors/redirects. No machine trust root is installed.
It verifies a real restored SQLite snapshot and original WAV artifact through HTTPS:

- Liveness 200 while restore hold makes readiness 503; exact-generation review changes
  readiness to 200 without restarting the process.
- Original order/history and verified TEST event replay remain intact; the pre-backup
  delivery grant has been invalidated. No live source file is replaced.
- A controlled failure returns generic 503 plus a generated operation ID. The matching
  3502 trace is read from actual process output; API tests independently check 3501
  completion fields and bounded Meter tags.
- URL/header/body/exception canaries, old grant and certificate password are absent
  from the bounded raw capture. Liveness remains 200 afterward.
- Only an allowlisted evidence JSON is uploaded, with seven-day retention. Raw logs,
  database, private audio and PFX/private-key material are not CI artifacts.

The seeded payment is a locally verified synthetic TEST fixture. This is actual
published-process HTTPS/recovery/diagnostic evidence, not public cloud provisioning,
real payment, customer recovery or a fatal crash. See operations-lab.md for reproducible
commands, configuration, recovery worksheet and acceptance matrix.

## Native, provider and production limits

Android compilation does not establish local consent UX, persistence/lifecycle,
accessibility, managed/native fatal-crash capture or iOS. DiagnosticsLabPage initializes
no remote SDK and exports no records. Sentry.Maui is a documented maintained candidate,
not a configured or compatibility-tested integration. Server ILogger/Meter/ActivitySource
projections are exercised locally; no remote OpenTelemetry collector is configured.
The newsletter port sends nothing and never equates pending confirmation with subscribed.

Schema 1 and restore release are lab-specific. Plaintext synthetic backups plus a hash
are not authenticated/encrypted offsite recovery. Public hosting/TLS/proxy/secrets/storage,
real artifact inventories, provider/client reconciliation after the snapshot, production
traffic cutover, retention/erasure and realistic RPO/RTO/load/cost measurements remain
explicit work. Production operations and real business authorization are not enabled.

## Manuscript and editorial proof

Final chapter source `bf6cff99e1a31e46bef39a09d86401d026645d9c` independently passes
PDF production CI:
https://github.com/minnesotabob/csharp-mobile-app-man/actions/runs/43862245092

Chapter 35 adds six learning outcomes, prerequisites, the anniversary restore/diagnostic
narrative, explained migration/backup/log/metric code, a guided published HTTPS lab,
troubleshooting, a 114-word summary, one worked exercise and three independent exercises.
Two authored figures separate deployment resources and restore review. This completes
Part VII while preserving the intermediate/advanced scope and planned 40 chapters.

The proof has **358 pages**, 8 x 10 inches, 11-point body/9.5-point code, 45 bookmarks
and 35 distinct images (three Part illustrations plus 32 authored figures). Chapter 35
starts on page 346. All page dimensions, expected markers and outer text boundaries pass.
The new chapter was inspected as a contact sheet; opening, diagrams, code, diagnostic
explanation and summary/exercises received enlarged inspection. No native screenshot or
fatal-crash observation is invented. The existing downloadable PDF was updated successfully;
the saved file preserves all manuscript text and bookmarks.

Next: Part VIII introduction and Chapter 36, Testing the Complete Application. Preserve
actual-source versus native/provider evidence and the remaining release constraints.

# Chapter 34 tracking, revisions and private delivery — November 16, 2026 (Central)

Final executable/fixture source: `4a4ba828dc7d32dee68c8334da9f8687c2c000ff`.
SDK 11.0.100; C# 15; MAUI 11.0.10; Android minimum API 26.

- Portable Release build: **0 warnings/errors; 617 cases pass** (27 new fulfillment
  cases), no errors/failures/skipped/not-run cases. Chapter 21/25 console labs and the
  new Chapter 34 synthetic fulfillment console smoke execute successfully.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43825891878
- API/probe Release builds at unchanged API/core implementation
  `025d86e13ac447b5cdcf2f4ddadf17e0d2dfa7e6`: **0 warnings/errors; 99 cases pass**
  (12 new fulfillment cases), no errors/failures/skipped/not-run cases. Public Kestrel
  catalog/media range/hash loopback smoke passes.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43823960239
- Android Debug compilation: **success; 0 final compiler warnings/errors**. Existing
  merged media/notification/link/capability/share configuration assertions pass.
  Dependency setup retains its historical unresolved cmdline-tools;21.0 warning,
  separate from final compilation.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43825891872

Initial source passed all 617/99 cases and Android compilation. Two xUnit analyzer
warnings (Single predicate and test cancellation) and a nullable Home event-handler
warning were corrected. A runnable synthetic local fixture and CI smoke were added;
application policy/core/API code is unchanged from its verified initial implementation.
The final Android run checks the corrected native handler. No compiler pass is treated
as native identity, file-read, accessibility or listening evidence.

Real temporary SQLite tests cover owned live paging, coherent tracking/history/notices,
revision replay before later version/state checks, changed-key facts, stale/foreign/
invalid/capacity outcomes, two independent writer connections and forced notice-insert
rollback. They cover atomic/replayed delivery publication, hashed owner/version-bound
grants, exact expiry/renewal, capacity, reopen, revocation and publication replay that
cannot restore revoked access. New controlled publication requires verified TEST paid
state; legacy graph-only fixtures cannot substitute for it.

The production revision journal/coordinator is tested for reopen/account/resource
partitioning, unresolved replacement blocking, local persistence failure before HTTP,
committed-but-lost reply with both databases reopened after a later review, and sign-out
before a delayed committed reply. Simulated HTTP loss is explicit; database operations
are real. Private-client tests verify the exact original WAV, corrupt/oversized/wrong
media rejection and owned-buffer clearing on disposal.

Signed JWT in-process API integration exercises actual quote/accept HTTP, controlled
signed synthetic payment/production/review, customer revision, later review/delivery,
production TrackingApiClient/coordinator and exact authorized WAV bytes. It verifies
no-store, nosniff, strict revision fields, owned list/detail scopes, foreign/anonymous/
missing/expired/revoked/wrong-delivery access, query-grant rejection, unsupported Range
and absent static fixture path. This is an actual service/client contract test with
controlled publication/payment, not a real commission, provider charge or native read.

Native page supports explicit owned pages/history/notices, save/send/retry revision and
memory-only verified sample retrieval. It creates no private cache, player or share file.
Notices are durable in-app observations, not APNs/FCM/email receipts. Grants last two
minutes and remain bound to JWT owner/current artifact/version/state; expiry/revocation
cannot erase a response already authorized. VerifiedDelivery clears its owned array,
not all managed/OS/transport copies. The WAV is original generated public-source test
content; route tests establish access policy, not secrecy of those known sample bytes.

FulfillmentLab smoke uses a temporary database. Its explicit local seed/review/deliver/
revoke commands require GNAZZO_SYNTHETIC_FIXTURES=1 and direct disposable-development
database authority. They manufacture signed TEST payment evidence and are never real
administration or production authorization. See fulfillment-lab.md for runnable commands,
configuration, protocol, artifact provenance and pending acceptance matrix.

**Pending:** native identity/TLS/list/selection/editor/lifecycle/screen-reader/large-text
and memory verification observations; iOS compilation; actual private listening/offline/
export composition; real customer/admin/artifact ingestion, provider push/email, complete
production authorization, replacement/retention/migration/audit/backups/recovery and
privacy export/deletion composition. Sign-out retains original-owner pending revisions;
logical revocation and buffer clearing are not physical erasure.


Manuscript source `0756d1799c296630ff50252e4eb5e0812b816591` independently passes PDF
trim, expected chapter/figure markers and text boundaries:
https://github.com/minnesotabob/csharp-mobile-app-man/actions/runs/43825986897

The 3,233-word chapter adds six outcomes, a lost-revision/shared-tablet narrative,
explained replay/journal/hash source, owned-route and controlled-transition tables,
authored private-read diagram, guided runnable-fixture/customer journey, troubleshooting,
118-word summary and worked/independent exercises. It distinguishes immutable revision
receipts from later tracking snapshots, in-app notice from provider delivery, and future
read revocation from physical erasure. The cumulative draft-status page is condensed to
avoid an isolated copyright line; typography/trim are unchanged and footer date updated.

Proof: **345 pages**, 8 x 10 inches, 11-point body/9.5-point code, 44 bookmarks,
33 distinct images (three Part illustrations plus 30 authored figures). Chapter 34
starts on page 336. All pages pass local trim/text-bound checks; contact and enlarged
opening/about/diagram/code/closing-page views confirm readable layout. Updated working
PDF saved successfully with Chapter 34.

Next: Chapter 35, Hosting, Diagnostics, and Operating the Small Backend. Preserve the
planned 40 chapters and intermediate/advanced scope. Historical verification follows.

---

# Chapter 33 payment boundaries and verified events — November 16, 2026 (Central)

Final executable source: `bbeb33e201ffa0cc233bfd1e7991aad4fe9ca416`.
SDK 11.0.100; C# 15; MAUI 11.0.10; Android minimum API 26.

- Portable Release build: **0 warnings/errors; 590 cases pass** (38 new payment
  cases), no errors/failures/skipped/not-run cases. Earlier Chapter 21 and 25 console
  labs also execute successfully.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43819553353
- API/probe Release builds: **0 warnings/errors; 87 cases pass** (10 new payment
  cases), no errors/failures/skipped/not-run cases. Public Kestrel catalog/media
  range/hash loopback smoke passes.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43819553341
- Android Debug compilation: **success; 0 final compiler warnings/errors**. Existing
  merged media/notification/link/capability/share configuration assertions pass.
  Dependency setup retains the historical unresolved cmdline-tools;21.0 warning,
  separate from final compilation.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43819553425

The initial 583-case run compiled cleanly but failed one independently generated signed
fixture: Windows Git checkout converted its JSON line endings. The verifier correctly
rejected altered raw bytes. A -text attribute preserves that protocol fixture; the
corrected 588-case suite passed. Final review then added canceled-order checkout/URL suppression and canonical HTTPS
return-origin regression cases, yielding 590. All final application/core/API source is at
the revision above. The signature implementation was not weakened to accept normalized
messages.

The restricted direct-account Stripe TEST adapter verifies account, fixed API origin,
explicit API version, stable server idempotency key, immutable USD amount and hosted
checkout destination. Live keys are rejected. Whole-operation deadline and response
bounds apply. Payment routes require Development + separate commerce/payment opt-ins;
no provider credentials are shipped. The native order page only refreshes owned TEST
status and never launches checkout. Browser return/cancel pages never write state.

Real temporary SQLite tests cover durable reservations/reopen, provider reply loss and
stable key reuse, 23h automatic retry cutoff, verified paid/unpaid/failure/expiry policy,
two-connection duplicates, forced payment-update rollback, event-ID fact conflicts,
amount/session/account binding, payment-reference conflicts, canceled-order review,
controlled paid production gate and suppression of canceled checkout creation/URLs.
Crypto tests cover tampering, stale/future delivery, wrong secret, duplicate timestamp,
multiple v1 signatures, live/Connect/duplicate-JSON rejection and the independent Python
vector. Provider HTTP contract tests use a simulated handler, not api.stripe.com.

Signed in-process JWT/API integration reserves/attaches a simulated hosted session,
applies signed synthetic webhook bytes, reads one owned Paid receipt and proves that
forged return/cancel queries cannot mark Paid. It checks scopes, empty checkout bodies,
no-store, foreign-owner URL privacy, missing/oversized signatures, ordering and retryable
unbound events. The service never changes production order state on payment receipt.
StartProductionForPaymentLab is a controlled fixture only; Chapter 32 AdvanceForLab
remains a legacy graph fixture and is not a real production/payment authorization path.

**Pending:** actual hosted Stripe sandbox/CLI/test-card/API-version execution; native
identity/TLS/status/switching/storage/accessibility observations and iOS compilation;
storefront/product/region/program eligibility and approval. Refunds/disputes, ledger,
payment replacement, automatic provider reconciliation sweep, fulfillment outbox,
financial audit, migration/retention/backup/recovery and real administrative production
authorization are not implemented. Unsupported signed events are acknowledged without
effect, not financially reconciled. Existing provider URLs are not revoked by local
order cancellation; later success requires ReviewRequired. No real payment or public
checkout is supplied. See payment-lab.md for setup, protocol and acceptance matrix.


Manuscript source `4e22bf8203b03f1fe6664c227bec34e235641406` independently passes PDF
trim, expected chapter/figure markers and text boundaries:
https://github.com/minnesotabob/csharp-mobile-app-man/actions/runs/43819067606

The 3,193-word chapter adds six outcomes, a forged-return/closed-browser narrative,
explained durable reservation/raw-signature/transaction code, payment-state table,
authored boundary figure, guided developer/provider lab, troubleshooting, 115-word
summary and worked/independent exercises. Current official Stripe, Apple and Google
references were checked; product/storefront eligibility remains an explicit release gate.

Proof: **335 pages**, 8 x 10 inches, 11-point body/9.5-point code, 43 bookmarks,
32 distinct images (three Part illustrations plus 29 authored figures). Chapter 33
starts on page 327. All pages pass local trim/text-bound checks; contact and enlarged
opening/diagram/code/closing-page views confirm readable layout. Updated working PDF
saved successfully with Chapter 33.

Next: Chapter 34, Order Tracking, Revisions, and Delivery. Preserve the planned 40
chapters and intermediate/advanced scope. Historical verification records follow.

---

# Chapter 32 / Part VII — owned quotes/orders — November 15, 2026 (Central)

Final executable source: `6e5921d05cc25fa965a2c93a326e571228d1f0d9`.
SDK 11.0.100; C# 15; MAUI 11.0.10; Android minimum API 26.

- Portable Release build: **0 warnings/errors; 552 cases pass** (29 new commerce
  cases), no errors/failures/skipped/not-run cases. Both earlier synchronization and
  account lifecycle console labs execute successfully.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43814370719
- API/probe Release builds at unchanged API/core source
  `95ca22e178978f6bf9ce7558c018d5e5339a8319`: **0 warnings/errors; 77 cases pass**
  (15 new commerce cases), no errors/failures/skipped/not-run cases. Kestrel public
  catalog/media range/hash loopback smoke passes.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43813143415
- Android Debug compilation: **success; 0 final compiler warnings/errors**. Earlier
  merged capability/share/media/notification/link configuration assertions pass.
  Dependency setup retains its historical unresolved cmdline-tools;21.0 warning,
  separate from final compilation.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43814370792

The initial implementation passed 552 portable/77 API cases and Android compilation
at `95ca22e178978f6bf9ce7558c018d5e5339a8319`. Subsequent native-page review exposed
all vocal/explicit fields for review and clears the displayed order receipt on actual
route departure; final portable/Android runs above verify the revised composition.
The API, portable policy and tests are unchanged by those UI/documentation refinements.

Real temporary SQLite tests exercise server-calculated/canonical/immutable price
snapshots, two independent writer connections, same-key replay, different-key quote
reuse, cross-owner/issuer lookup, expiry, changed payload, forced history-insert rollback,
optimistic state versions and terminal transitions. Journal tests prove partitioning,
reopen, unresolved replacement blocking, rejection policy, receipt version checks and
redacted record text. Production coordinator tests prove persistence failure sends no
HTTP and committed-but-lost reply survives both databases reopening after quote expiry.
Controlled delayed HTTP verifies A's sign-out prevents late publication under B.

Signed JWT API integration covers default-disabled routes, dedicated scopes, owner
predicates, no-store, strict bounded JSON and absence of customer state/payment updates.
The production OrderApiClient/coordinator also create/accept/persist and GET-refresh a
controlled fixture version through the actual middleware. These are in-process tests,
not live provider or device/TLS evidence. Server AdvanceForLab is trusted in-process
simulation only; it has no customer HTTP route and supplies no payment authorization.

The opt-in API stores synthetic plaintext quotes/orders/history in a separate v1 SQLite
file. Quoted historical amounts are teaching snapshots, not live offers. Accepted means
recorded request, not paid or real production. App journal stores one last operation per
issuer/subject/origin/audience (16 partitions), no tokens, and persists before POST and
before UI success. Unresolved ambiguity retains the original key. Only ExpiredQuote,
ChangedRequest and Unavailable are definitive post-replay rejection codes. Sign-out
retains original-owner journal for reconciliation; it is not a physical purge.

**Pending:** live tenant grants/sign-in/refresh/sign-out; native TLS, callback/browser,
route/window, restart/storage/accessibility observations; iOS compilation; payment and
real production authorization (Chapter 33), full owned history/private delivery (34),
privacy export/deletion composition, schema migration/retention/backups/distributed
budgets and operational audit (35). Historical quote rows count against lab capacity;
there is no automatic cleanup. Customer attachment upload remains separate.
See commerce-lab.md for configuration, protocol, state graph and acceptance worksheet.


Manuscript source: `69b91f0274590772ee0263f83810366bce76c325`. Independent PDF CI passes
trim, chapter/figure markers and text boundaries:
https://github.com/minnesotabob/csharp-mobile-app-man/actions/runs/43814071923

The new chapter has 3,164 words, six learning outcomes, an anniversary-request/lost-reply
narrative, explained transaction and persistence code, contract tables, guided lab,
troubleshooting, 122-word summary and worked/independent exercises. Added Part VII
introduction/roadmap and an authored transaction/reconciliation figure. Condensed the
cumulative About This Draft into one page without changing type size or trim.

Proof: **326 pages**, 8 x 10 inches, 11-point body/9.5-point code, 42 bookmarks,
31 distinct images (three Part illustrations plus 28 authored figures). Part VII starts
on page 317 and Chapter 32 on page 318. All pages pass local trim/text-bound checks;
contact and enlarged opening/Part/figure/code/end-page views confirm readable layout.
The updated working PDF was saved successfully with Chapter 32.

Next: Chapter 33, payments and verified external events. The planned 40 chapters and
intermediate/advanced scope remain. Historical verification records follow.

---

# Chapter 31 — native capabilities and attachments — November 15, 2026 (Central)

Added optional provider-stream reference selection, strict bounded UTF-8/photo policy,
native image normalization behind a portable port, PNG framing/CRC/ancillary removal,
late-result scope fencing, verified staged replacement and separately retained share
copies. Narrow Android FileProvider configuration, connectivity hints and optional
haptics accompany the local lab. No customer upload/account attachment composition or
location acquisition is supplied; the optional location extension remains an exercise.

Corrected workflow/executable source: `82a68ba52c2a83b84d5c1f68be7d4e733312e338`.

- Portable Release build: **0 warnings/errors; 523 cases pass** (35 new real-file/
  synthetic-image/fallback cases), no errors/failures/skipped/not-run cases. Both earlier
  synchronization/account console labs also execute successfully.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43809402430
- API/probe Release builds at unchanged API/core parent
  `64eac79b6fa795ecef58b15fa746caa29e641f58`: **0 warnings/errors; 62 cases pass**;
  public Kestrel catalog/media range/hash loopback smoke passes. No attachment API added.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43808574847
- Android Debug compilation: **success; 0 final compiler warnings/errors**. Merged
  capability permissions, absent camera/location permissions, one narrow source share
  root and merged provider-resource reference pass with prior media/link assertions.
  Dependency setup retains the historical cmdline-tools;21.0 warning, separate from
  final compilation.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43809402360
- Manuscript source `7b3a8d1dc3c1977f8f1d76db8927b0314926eaf5`: independent PDF CI
  passes page size, expected chapter/figure markers and text boundaries.
  https://github.com/minnesotabob/csharp-mobile-app-man/actions/runs/43809723662

The initial compile/tests were successful; an XML assertion confused the element name
with its name attribute through PowerShell's XML adapter. XPath now validates the same
strict root policy and emits exact source/merged XML. That correction changes workflow,
not application behavior, and remains configuration rather than runtime URI evidence.

The chapter closes Part VI with an anniversary-reference journey, provider/normalize/
stage/export ownership diagram, explained source, resource-lifetime table, guided native
acceptance, troubleshooting, optional location design, 122-word summary and worked/
independent exercises. It distinguishes declared-resource checks from a full decoder
proof and metadata stripping from removal of private information in pixels.

Proof: **317 pages**, 8 x 10 inches, 11-point body/9.5-point code, 40 bookmarks,
29 distinct images (three Part illustrations plus 26 authored figures). Chapter 31
starts at page 309. Every page passed local trim/text-bound inspection; contact sheet
and enlarged revised opening/figure/code/end-page checks confirmed readable layout.
Updated working PDF saved successfully with Chapter 31.

**Pending:** iOS compilation and native provider/codec/permission/orientation/metadata/
share URI/grant/tablet/receiver results; cache/process/write behavior and capability
settings. Portable normalizer tests are simulated. Customer uploads, durable account
attachment composition, orphan inventory and optional location implementation remain
separate. No cross-process lock, decoder isolation, delivery/revocation or physical-erasure
claim is inferred from the sample. Native acceptance worksheet records every pending row.

Next: Part VII introduction and Chapter 32, Quotes, Orders, and Customer Ownership.
The planned 40 chapters and intermediate/advanced scope remain. Historical records follow.

---

# Chapter 30 — notifications, deep links and sharing — November 15, 2026 (Central)

Added native local notification permission/post/tap adapters, canonical typed links,
a bounded SQLite routing inbox, ready-window routing, explicit private-request sign-in
continuation and public share-sheet invocation. Optional push registration includes a
persist-before-send generation coordinator, current-session HTTP sink and scoped,
owner-bound API registry with body/budget/cap/expiry limits. No live FCM/APNs project,
SDK token acquisition, delivery sender/receiver or verified HTTPS association is enabled.

Corrected executable source: `23e90f12d28060120d331d02a9e77d07a1091843`.

- Portable Release build: **0 warnings/errors; 488 cases pass** (40 new parser/inbox/
  registration-policy cases), no errors/failures/skipped/not-run cases. Earlier Chapter
  21 and 25 console labs also execute successfully.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43772049238
- API/probe Release builds at unchanged API/core parent
  `09ed64e9d2cb16851b080d0a9816b767b1984f24`: **0 warnings/errors; 62 cases pass**
  (9 new cases), no errors/failures/skipped/not-run cases. Actual session sink registers
  and removes through signed-token middleware. Kestrel public media range/hash and
  catalog smoke remains successful; no native/provider delivery is inferred.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43771527612
- Android Debug compilation: **success; 0 final compiler warnings/errors**. Merged
  notification permission, canonical VIEW/DEFAULT/BROWSABLE scheme/host filter and
  earlier media service assertions pass. Dependency setup retains the historical
  cmdline-tools;21.0 warning, separate from final compilation.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43772049172
- Manuscript source `d0d13380b78503cfddf1ee26a0871247e7b8f8db`: independent PDF CI
  passes page size, expected chapter/figure markers and text boundaries.
  https://github.com/minnesotabob/csharp-mobile-app-man/actions/runs/43806478870

The first native pass exposed nullable notification manager results and an assertion
that expected host/scheme on one data node. Generated Android filters use separate
nodes with collective semantics. The corrected adapter handles manager absence; the
assertion validates and emits the complete matching filter. It remains configuration
evidence, not an OS activation test.

The chapter contains public Minnesota Bob/private anniversary-request journeys,
validation/inbox/readiness/authorization figure, explained excerpts, guided acceptance,
troubleshooting, 114-word summary and worked/independent exercises. It names remaining
account cleanup/outbox and real SDK/provider gates instead of implying registration
success is delivery. No private content appears in notification or share samples.

Proof: **308 pages**, 8 x 10 inches, 11-point body/9.5-point code, 39 bookmarks,
28 distinct images (three Part illustrations plus 25 authored figures). Chapter 30
starts at page 300. About This Draft expansion shifts earlier positions by one page;
historical records retain their original proof pagination. Every page passed local
trim/text-bound checks; contact sheet and enlarged revised opening/figure/end-page
inspection confirmed readable layout. Updated working PDF saved successfully.

**Pending:** iOS compilation; native permission/channel behavior, warm/cold/default
tap ordering, ready-window activation, private-read cancellation and share-sheet return.
Live FCM/APNs acquisition/delivery, installation/provider proof, durable registry and
account cleanup/outbox, verified HTTPS association and routing metadata backup/privacy
review remain unimplemented or unverified. No global exactly-once navigation claim.

Next planned chapter: 31, Native Capabilities, Attachments, and Platform Extensions.
The planned 40 chapters and intermediate/advanced scope remain. Historical records follow.

---

# Chapter 29 — downloads and media storage — November 15, 2026 (Central)

Added a separate foreground public download lab, trusted descriptor and safe storage
identity, explicit cancellation/restart, validated Range/If-Range resume, bounded body
reads, complete length/hash verification, same-directory promotion, quota/free-space
reserve and serialized verification/deletion. The companion API embeds the original
10-second WAV at a fixed GET/HEAD range-capable route. Private delivery descriptors
are rejected; no customer media or account-authorized delivery is implemented.

Executed companion source: `373dad1f2ebe14843989c3f4bb578e5a97b02b19`.

- Portable Release build: **0 warnings/errors; 448 cases pass**, including 35 new
  real-file cases with simulated HTTP/free-space conditions; no errors/failures/
  skipped/not-run cases. Both earlier console labs execute successfully.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43769261598
- API/probe Release builds: **0 warnings/errors; 53 cases pass**, including 7 new
  media cases and actual downloader cancel/resume through real ASP.NET range handling.
  Real Kestrel loopback HTTP smoke checks the full fixture hash and exact ranged slice
  in addition to health/catalog/paging. This is not HTTPS/native evidence.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43769261609
- Android Debug compilation: **success; 0 final compiler warnings/errors**; existing
  merged service permission/type checks pass. Dependency installation retains the
  historical unresolved cmdline-tools;21.0 warning, separate from final compilation.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43769261603
- Manuscript source `7384dff5c02c119201c623a04ab014243c44b830`: independent PDF CI
  passes page size, chapter/figure markers and text boundaries.
  https://github.com/minnesotabob/csharp-mobile-app-man/actions/runs/43769864461

The chapter includes the Minnesota Bob trip-north narrative, private anniversary-song
boundary, receive/verify/promote diagram, response decision table, explained source,
guided restart/TLS lab, troubleshooting, 124-word summary and worked/independent
exercises. Updated Part VI roadmap wording describes scope without conflating pending
native work with implementation. The planned 40 chapters and advanced scope remain.

Proof: **298 pages**, 8 x 10 inches, 11-point body/9.5-point code, 38 bookmarks,
27 distinct images (three Part illustrations plus 24 authored figures). Chapter 29
starts at page 290. Every page passed local trim/text-bound checks; new contact sheet
and enlarged figure inspection confirm readable layout. The updated working PDF was
saved successfully with Chapter 29.

**Pending:** iOS compilation and native HTTPS trust/reachability, cancellation timing,
process restart, cache eviction, competing disk usage and actual write/rename behavior.
A free-space check is not a reservation and rename is not power-loss durability.
Public cache storage is replaceable/anonymous; private delivery service/access,
account-scoped publication, encryption/backup, background transfer registration and
downloaded-path player composition remain unimplemented. The native acceptance matrix
records these limits rather than converting compiler/test success into device claims.

Next planned chapter: 30, Notifications, Deep Links, and Sharing. Historical records follow.

---

# Chapter 28 — background playback and system controls — November 15, 2026 (Central)

Added a separate opt-in native audio lab, portable BackgroundPlaybackOwner, original
60-second PCM timing fixture, public metadata/system-command observations, Media3
focus/noisy configuration, iOS audio background mode and pause-only observers. One
mounted host survives the internal browse panel; Shell departure destroys its owner.
The chapter includes a Minnesota Bob listening journey, lifecycle diagram, explained
source, guided device worksheet, troubleshooting, 124-word summary and exercises.

Corrected executable source: `a9e893d75689a48ecfbbe9f4e107fc5761780481`.
The first checks exposed a remote-pause checkpoint defect and an inaccessible pinned
toolkit Player API. The correction saves the event's position and configures the public
native PlayerView/IExoPlayer, with visible failure if absent. The final follow-up handles
nullable builder bindings explicitly rather than suppressing compiler warnings.

- Portable Release build: 0 warnings/errors; **413 cases pass**, including 18 new
  simulated playback-owner cases plus one new fixture header/hash case. No errors,
  failures/skips/not-run cases; Chapter 21 and 25 console labs execute successfully.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43767142547
- API/probe Release builds at unchanged API parent bedeec9000f65a3492989fe80778bd7f1a3e76b6:
  0 warnings/errors; **46 API cases pass**; public loopback smoke passes.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43766620130
- Android Debug compilation: **success; 0 final compiler warnings/errors**.
  Merged manifest assertions pass for both foreground-service permissions and the
  toolkit mediaPlayback service type. Dependency installation retains its historical
  unresolved cmdline-tools;21.0 setup warning; this is separate from final compilation.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43767142544
- Revised manuscript proof source: `1d50a58b08c2536f9aca06bc1cab1a17c5fe8c04`.
  Independent PDF CI passed page size, chapter/figure markers and text boundaries.
  https://github.com/minnesotabob/csharp-mobile-app-man/actions/runs/43767216352

Proof: **289 pages**, 8 x 10 inches, 11-point body/9.5-point code, 37 bookmarks,
26 distinct embedded images (three Part illustrations plus 23 authored figures).
Chapter 28 starts at page 281. Local checks covered every page's trim/text bounds;
contact-sheet and enlarged new-page inspection found readable text, code and figure.
Existing working PDF updated successfully with the corrected native source excerpt.

Native listening, decoding, system controls, focus gain/loss, calls, wired/Bluetooth
routes, task removal, process death, power constraints and iOS compilation remain
pending. Timers are best effort; no app-wide/process-resilient playback architecture,
private delivery access or real Minnesota Bob media is claimed. The public native view
hierarchy is a pinned toolkit compatibility dependency, rechecked on upgrades.

Next planned chapter: 29, Downloads and Media Storage. The 40-chapter plan and
intermediate/advanced teaching scope remain unchanged. Historical entries follow.

---

# Part VI / Chapter 27 - foreground audio and podcast progress - November 15, 2026 (Central)

Added Part VI's media roadmap, Chapter 27's source-ownership diagram, foreground
native player/lab, original generated WAV fixtures with provenance/hash manifest,
absolute-time SQLite progress, guided work, failure recovery, troubleshooting and
worked exercises. Streaming-service links are not treated as playable audio files.

Corrected companion source: `c73f3cd25e175d7e89de84f3cbdaa9bacdd86af6`.
Initial compilation exposed a documentation namespace/parameter mismatch; the sample
uses CommunityToolkit.Maui and isAndroidForegroundServiceEnabled: false. It pins
MediaElement 12.0.0 with SDK 11.0.100 and MAUI 11.0.10. Android minimum becomes API 26.

- Portable Release compilation: 0 warnings/errors; **394 cases pass**, including 34
  new playback/storage/fixture cases; no errors/failures/skips/not-run cases. Both
  earlier console labs execute successfully.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43764322521
- API/probe Release builds: 0 warnings/errors; **46 API cases pass**; public loopback
  smoke passes with no errors/failures/skips/not run.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43764322453
- Android Debug compilation: success; **0 final compiler warnings/errors**. Dependency
  setup retains the documented unresolved cmdline-tools;21.0 warning.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43764322496

The proof contains **280 pages, 36 bookmarks and 25 distinct images**: three Part
illustrations and twenty-two authored technical figures. Part VI begins on page 268;
Chapter 27 begins on page 270. All 13 new pages were rendered for inspection; the
source diagram, bootstrap, evidence, summary/exercises and references received larger
page review. All-page 8x10 trim/text-boundary and figure-reference checks pass.

Limits: tests supply native observations and inspect real SQLite/source WAV bytes;
they do not listen or prove a phone decoded the packaged assets. Foreground page owns
one player, source tickets reject late events, and checkpoints are anonymous/local,
unencrypted and not account-synchronized. Periodic/boundary save is not a guarantee at
arbitrary process death. Native listening, seeks, lifecycle/cleanup, audio focus/calls,
headphones, iOS and screenshots remain pending. No background controls, remote stream,
private media transport or download feature is enabled here.

Next: Chapter 28 - Background Playback and System Controls, with explicit platform
setup, long-lived player ownership and real interruption/lock-screen acceptance work.
Preserve the editorial review's concrete app narrative, visual architecture and separate
build/test/device evidence.

## Earlier milestone record

# Chapter 26 - threat modeling and security verification - November 15, 2026 (Central)

Added the final initial Part V chapter, an authored trust-boundary diagram, focused
T-ID threat register, guided verification lab, least-privilege/dependency/secret/file
review, worked abuse cases and explicit native/deployment evidence limits.

Verified companion executable source: `a3d2a880195714dc61a2971bc2ab3f7aab1d78a9`.

- Portable Release build: 0 warnings/errors; **360 cases pass**, including 15 new
  destination/private-ID cases; no errors/failures/skipped/not-run cases. Both
  earlier console labs also execute successfully.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43761369874
- API/probe builds: 0 warnings/errors; **46 API cases pass**, including nine new
  protected-read security cases; public loopback smoke passes.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43761369921
- Android Debug compile: success; 0 final compiler warnings/errors. SDK dependency
  setup retains the documented unresolved cmdline-tools;21.0 warning.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43761369900

The API enforces the shared bounded ID policy, sends no-store for private-prefix
responses, applies an eight/minute shared process-local read budget after authorization,
and emits only fixed event-2601 outcomes. Tests retain real JWT middleware/static
fixture metadata. No new package, customer write, lifecycle or file endpoint is added.

The proof has **267 pages, 34 bookmarks and 23 distinct images**: three Part illustrations
and twenty authored technical figures. Chapter 26 starts on page 256. All 12 new pages
were rendered for inspection; the trust-boundary and final summary/exercise pages were
also reviewed at larger scale. All-page trim/text checks and image references pass.

Limits: shared budget is not production fairness/distributed/auth-cost/DDoS protection.
The custom audit test covers one projection, not proxy/provider/framework logs or a
complete mutation audit trail. Native/provider/TLS/storage/backup/full lifecycle checks,
current advisory/secret scans, deployment sizing and customer-file access remain pending.
The register names owners and needed evidence instead of claiming complete security.

Next: Part VI and Chapter 27 - Audio Playback and Podcast Progress. Use authorized media,
explicit playback ownership and the same interruption/evidence standards. Preserve the
supplied editorial review's visual architecture and concrete application narrative.

## Earlier milestone record

# Chapter 25 - profiles, privacy and lifecycle - November 15, 2026 (Central)

Added the account-workspace chapter, two authored figures, real SQLite profile and
intent/receipt lab, scoped local export, preference revision/choice reasoning, guided
walkthrough, troubleshooting, worked exercises and explicit native/service follow-through.
The anniversary-request narrative continues through account switching and removal.

Verified companion executable source: `3309637a8abc06ecf1e65fafd1bec32afbbe315b`.

- Portable Release compilation: 0 warnings/errors; **345 cases pass**, including 24
  new workspace cases; no errors/failures/skipped/not-run cases. Both console labs run.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43760294885
- API/probe builds: 0 warnings/errors; **37 API cases pass**; public loopback smoke passes.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43760294883
- Android Debug compilation: success; 0 final warnings/errors. Setup retains the earlier
  unresolved cmdline-tools;21.0 dependency warning.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43760294896

The proof has **255 pages, 33 bookmarks and 22 distinct images**, comprising three
Part illustrations and nineteen authored technical figures. Chapter 25 opens on page
243. Its 13 pages were rendered for inspection; all-page trim/text-boundary checks pass.
Final figure, evidence, summary and exercise pages were also inspected at larger scale.

Limits: the new database is a separate local lab, not native account/session composition.
Service receipts and reauthentication statuses are simulated; provider identity and remote
data are untouched. The retained deletion marker has no expiry, SQLite is not encrypted,
and physical erasure/backups are unverified. No complete service export, lifecycle API,
notification registration or account migration is enabled. Native/device, iOS and screenshots
remain pending. These limits appear in both chapter and companion acceptance worksheet.

Next: Chapter 26 - Threat Modeling and Security Verification, using the existing ownership,
callback, transport, storage and lifecycle boundaries. Continue the supplied editorial review.

## Earlier milestone record

# Chapter 24 - MFA and recovery lab - November 15, 2026 (Central)

Added the provider-owned enrollment/challenge/recovery chapter, one authored boundary
figure, development configuration walkthrough, factor-replacement and revocation
reasoning, future step-up contract, troubleshooting, worked exercises and a companion
acceptance worksheet. The anniversary-request narrative carries stable account ownership
through lost-device recovery. Official provider sources reviewed on this date.

The proof contains **242 pages, 32 bookmarks and 20 distinct images** (three Part
illustrations and seventeen authored technical figures). Chapter 24 opens on page 234.
All-page trim and text-boundary checks passed; all nine new chapter pages were rendered
and visually inspected. No app/API executable or dependency changes in this milestone;
Chapter 23's 321 portable and 37 API results remain historical evidence, not MFA tests.

Live tenant enrollment/challenge/recovery, consumed-code rejection, factor replacement,
renewal policy interaction, native accessibility, iOS and screenshots remain pending.
No provider tenant has been provisioned and no sensitive-write step-up endpoint is added.
The reader must execute the documented development lab before claiming those outcomes.

Next: Chapter 25 - Profiles, Privacy, and Account Lifecycle. Preserve the existing
review's diagrams, concrete app narrative, security and honest verification boundaries.

## Earlier milestone record

# Chapter 23 — sessions, storage and API authorization — November 15, 2026 (Central)

Added the session/API chapter, two authored diagrams, bounded credential-envelope and
request-client walkthroughs, real bearer-middleware tests, diagnostics, worked exercises
and native/provider verification records. The anniversary-request narrative connects
credential lifetime and persistence to independently enforced record ownership.

Companion source: `50a5abf391e37fef04866c0528af4da195954354`.

- Portable Release build: 0 warnings/errors; **321 cases passed**, no errors/failures/
  skipped/not-run cases, including 14 new session/client cases.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43746174414
- API and probe builds: 0 warnings/errors; **37 API cases passed**, including 11 new
  signed-token/ownership cases. Public loopback smoke also passed.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43746174402
- Android Debug compilation: success; 0 final compiler warnings/errors. Dependency
  installation retains the documented unresolved cmdline-tools;21.0 setup warning.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43746174337

The reviewed proof has **232 pages, 31 bookmarks and 19 distinct images** (three Part
illustrations plus sixteen authored figures). Chapter 23 begins on page 220. Opening,
diagrams, code, guided lab, evidence/diagnostic tables, summary, worked exercises and
final native record/reference pages were rendered for inspection. Text-boundary and
8x10 trim checks cover every page. The supplied editorial review remains the guide.

Limits: the session vault/provider tests are doubles; API tests use ephemeral RSA keys
and static metadata through the real JWT middleware. The running API has no customer
fixtures or signing private key. Live provider acquisition/rotation/revocation, phone
SecureStorage/reinstall, device TLS, iOS/runtime and screenshots remain pending. The
Session lab is separate from Chapter 22's process-only example and does not migrate
existing favorites/drafts. Local clearing does not imply remote logout or deletion.

Next: Chapter 24 — provider-supported MFA and recovery. A real tenant and device matrix
is still required before claiming complete identity/session/MFA journeys.

## Earlier milestone record

# Part V / Chapter 22 identity draft — November 15, 2026 (Central)

Added Part V's introduction and identity roadmap, and Chapter 22's hosted-sign-in
ownership diagram, exact provider setup, code walkthrough, cancellation/late-result
reasoning, troubleshooting, exercises and native verification record. Auth0 is the
implementation candidate; actual hosted login remains pending a tenant/device matrix.
The supplied review's visual architecture and concrete Gnazzo's World narrative remain.

Corrected companion source: `13b32a90075de1d1bd8701237c61f404253f707d`.

- Portable Release build: 0 warnings/errors; **307 executable cases passed**, no
  failures/errors/skips/not-run cases, including 23 Chapter 22 cases.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43744434467
- Android Debug compilation: success; final compilation 0 warnings/errors. Dependency
  setup retains the documented unresolved cmdline-tools;21.0 warning.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43744434539
- Existing API regression workflow passed at the initial implementation; the follow-up
  correction only disambiguates the provider browser interface in native source.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43743986823

The proof contains **219 pages, 30 bookmarks and 17 distinct images** (three original
Part illustrations plus fourteen authored figures). Part V begins on page 206 and
Chapter 22 on page 208. Its opening, diagrams, setup, commands, evidence table,
troubleshooting, summary, exercises and native worksheet were rendered for inspection.
Trim/text-boundary checks cover every page; the three selected Source fonts are embedded.

Limits: the app ships without tenant configuration. Portable engine tests check invalid
state, missing code and canceled browser with static metadata/no network; simulated
presentation replies do not authenticate anyone. Live provider login, Android browser
return, native cancellation, iOS build/runtime, MFA/recovery and screenshots remain
pending. The chapter is an integration/setup draft, not a completed real-provider
verification milestone. No private API access, persistent session or account migration
is enabled. Chapter 23 is next for sessions and independent API authorization; real
provider setup must be exercised before claiming end-to-end identity.

## Earlier milestone record

# Chapter 21 — synchronization and conflict resolution — November 15, 2026 (Central)

The new Chapter 21 completes Part IV with a guided two-replica lab, a conflict diagram,
version/operation-ID reasoning, durable outboxes, explicit resolution, tombstones,
atomic feed/cursor application, failure diagnostics, worked exercises and a native
acceptance/screenshot worksheet. It preserves the supplied editorial review's emphasis
on visual architecture, concrete Gnazzo's World journeys and verified boundaries.

Companion implementation: `84a3278e5d00b64699ccf8cee963a657da9fdec8`.

- Portable Release build: 0 warnings/errors; **284 cases passed**, no failures/errors/
  skipped/not-run cases. This includes 18 new synchronization cases.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43737262027
- The console lab executed its expected draft-conflict and favorite-deletion transcript.
- Existing API regression suite: **26 passed**, no failures/errors/skips/not run.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43737262061
- Android Debug compilation: success; final compilation 0 warnings/errors. Dependency
  setup retains the recorded unresolved cmdline-tools;21.0 warning.
  https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43737262069

The proof now contains **205 pages, 28 bookmarks and 15 distinct images** (three Part
illustrations plus twelve authored figures). Chapter 21 starts on page 195. Its opening,
conflict diagram, commands/transcript, troubleshooting, summary, exercises and final
worksheet were rendered for visual inspection. All pages passed trim and text-boundary
checks. The manuscript proof workflow now also runs for updates on main.

Limits: two actual SQLite files on Windows CI, but a process-local in-memory server
and simulated account context. No sync endpoint, durable hosted server, real identity,
native sync wiring, phone-runtime tests or screenshots are claimed. The teaching
replicas do not migrate existing MAUI favorites/drafts. Chapter 22 begins Part V with
managed identity and native-app authentication; provider setup must be verified.

## Earlier milestone record

# Editorial follow-through — November 15, 2026 (Central)

Added a Chapter 19 migration/rollback figure, a Chapters 17-20 progress recap and a
Chapter 9 performance-observation lab. The lab defines reproducible fixture/device
conditions and explains which measurement can support which conclusion; no results
are invented. The migration figure explicitly targets the schema-2 teaching checkpoint.

The regenerated proof has **194 pages, 27 bookmarks and 14 distinct images** (three
Part illustrations and twelve authored figures). Trim and outer text-boundary checks
passed across all pages. The added lab, migration figure and recap were rendered for
visual inspection. This is an editorial revision; no application source changed and
no new app build, device observation or performance result is claimed.

Current source remains on `work/chapter16-pricing`; `main` is an earlier milestone.
Native screenshots and Chapter 20 browser integration remain outstanding. Chapter 21
synchronization is the next planned implementation chapter.

## Earlier milestone record

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



## Chapter 38 print-proof inspection

The final local proof has 402 pages, 49 bookmarks and 42 distinct images: four original
Part illustrations and 38 authored technical figures/recaps. Chapter 38 starts on
page 388. All 8x10 trim sizes, image references and outer text boundaries pass.
The expanded chapter received contact-sheet review plus full-size opening, code,
SDK example, actual emulator record, diagrams, troubleshooting and summary/exercise
inspection. The About This Draft overview was shortened to keep copyright on the
same page; the preface follows cleanly on the next page. Part/chapter starts remain
new-page starts. The proof remains editorial, not a finished paperback or EPUB.

Independent PDF production also passed at manuscript source
`649b66c6a2bd829ba4436ef963a203caa988d8df`:
https://github.com/minnesotabob/csharp-mobile-app-man/actions/runs/43951781223
The existing downloadable opening-draft-8x10.pdf was successfully updated to the
402-page proof after visual and boundary inspection. The final progress-only commit
does not change the chapter, rendering source or verified PDF bytes.
