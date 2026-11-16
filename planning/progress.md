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
Part illustrations and eleven authored figures). Trim and outer text-boundary checks
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

