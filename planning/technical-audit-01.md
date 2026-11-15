# Technical and editorial audit — pass 1
**Date:** November 15, 2026  
**Scope:** Manuscript Chapters 1–18, existing source reference names, companion-learning-guide state and editorial structure.  
**Branch:** `work/chapter16-pricing` in manuscript and companion repositories.

## Checks completed

1. Retrieved all 18 current manuscript chapters and the companion repository's recursive tree at the review branch.
2. Confirmed every chapter has a distinct `What You'll Learn` section and `Chapter Summary` heading. Chapters 15–18 originally combined the summary and exercises; these have been separated without changing their exercises.
3. Counted Markdown code-fence delimiters in each chapter; all chapter totals are even. This is a structural check, **not** a syntax or compilation check.
4. Checked explicit filename references ending in `.cs`, `.xaml`, `.csproj`, `.json`, `.resx`, and `.ps1` against the checked-out companion repository's filename inventory. No unmatched source filename references were found. The URL fragment `openapi/v1.json` in Chapter 18 is a generated service endpoint, not a checked-in file.
5. Reviewed companion `docs/milestones.md`, `docs/verification.md`, `docs/learning-guide.md`, the Shell routes, catalog XAML and catalog code-behind. The guide still incorrectly said Chapters 6–18 needed their initial instructional pass; it has been updated to distinguish completed first-pass instruction from the outstanding technical certification.
6. Added targeted troubleshooting to Chapters 12–17 for validation, stale state, browser handoff, draft preservation, quote identity, and network contracts.

## Source-backed observations

- The Part I exercise should use the historical Part I source commit `0b8973660cc21269ff79eb54733edaf428fb5dac`, not the current Shell-based implementation.
- The companion milestone guide records a Part II revision `9497b0d7e8acb74c07c50be8cb56f26453664fbb` and Chapter 18 verified revision `5c24e63dffd494463716730fdf553af74453a2ae`.
- Current `AppShell.cs` registers `details`, `song-request` and `networking-lab` routes. CatalogPage XAML uses compiled `CatalogBrowserViewModel` bindings, a bound CollectionView, and a separate inline DetailsView; its code-behind owns the debounced search input and adjusts the layout through `AdaptiveLayout.IsWide(Width)`.
- The current companion verification log records **245 portable tests**, **26 API integration tests**, a Kestrel HTTP **loopback** smoke test, and Android Debug compilation for the Chapter 18 verified code revision. They are **historical CI evidence**, not tests executed by this audit. Actual Android/iOS device use, iOS compilation, and device-to-service HTTPS remain unverified.

## Outstanding before declaring the chapters technically reviewed

- Check each substantive code excerpt against the **matching historical source revision**, not only filename existence on the current review branch. Confirm type names, signatures, input values, and exact expected test results.
- Run fresh companion portable and API tests, then confirm Android builds and selected native device journeys. Do not treat compilation as device execution.
- Verify sample-file links and chapter-to-chapter cross references and review all code fences for actual C#/PowerShell/XAML syntax. Even fence counts are insufficient.
- Regenerate the complete **8 × 10 inch** paperback proof from the revised Markdown. Check pages, code wrapping, link targets, widow/orphan behavior, illustrations, table headings, and the print/EPUB-specific navigation and index.
- Conduct a substantive editorial pass on accuracy, continuity, duplicated explanations, and potential gaps. Chapter 19 has not been started by this audit.

**Result:** First-pass structural and source-inventory audit complete. Editorial fixes committed. Technical certification and typeset proof review **not complete**.

## Pass 2: targeted code-excerpt and contract cross-check — November 15, 2026

Reviewed the manuscript's fenced code excerpts for Chapters 12–18 and compared selected signatures, snippets, contracts and stated behavior against the companion source at `work/chapter16-pricing`. Source files checked include `CatalogSnapshot.cs`, `CatalogItem.cs`, `CatalogSearch.cs`, `Favorites.cs`, `DebouncedQuery.cs`, `DetailViewModel.cs`, `ContentLinks.cs`, `SongPricing.cs`, `SongSubmission.cs`, `BoundedJsonClient.cs`, `CatalogDocument.cs`, `GnazzosWorld.Api/Program.cs`, launch settings, the local-API run guide, and submission tests.

**Matches observed:** The Chapter 13 search signature, favorites-store contract and debounce revision guard match their implementations. Chapter 14's approved-HTTPS-host policy and browser adapter match the source. Chapter 16's versioned pricing multipliers (1, 1.9, 2.7) and quote/attempt record shapes match. The Chapter 17 20-second linked deadline and 1,048,576-byte payload limit match `BoundedJsonClient`. The Chapter 18 API's read-only routes and localhost:7443 launch profile match `Program.cs` and `launchSettings.json`. The reported Chapter 16 two-minute instrumental example totals (79.00, 150.10, 213.30 USD) follow the checked source.

**Corrections committed:**
- Chapter 12's optional `CatalogItem` constructor tail is identified explicitly as a Chapter 12 milestone excerpt; current source also includes the later optional `ReadingSample` field.
- Chapter 14's abbreviated `OpenAsync` code snippet now says `result` is produced by omitted browser/exception handling, and points readers to the complete method rather than suggesting the fragment compiles independently.
- Chapter 15 no longer implies the existing API accepts song requests. It accurately states that the API currently provides public catalog reads only and a future request endpoint must independently validate character limits.

**Limits:** This targeted inspection is not an exhaustive diff of all 18 chapter claims or every line of source. No `dotnet` compilation/test command or native-device run was executed during this audit. Do not convert reviewed excerpts into a claim of fully reproducible code until the paired revision is checked and executed.

## Pass 3: historical source milestone review — November 15, 2026

Checked the Chapter 1–11 manuscript code snippets and selected assertions against two **specific historical** code revisions rather than the default branch:

- Part I (Chapters 1–5): `0b8973660cc21269ff79eb54733edaf428fb5dac`
- Part II (Chapters 6–11): `9497b0d7e8acb74c07c50be8cb56f26453664fbb`

Source files inspected include Part I `MauiProgram.cs`, `App.xaml.cs`, `MainPage.xaml`, `MainPage.xaml.cs`, the starter `CatalogSearch.cs`, `CatalogTests.cs`, `PricingTests.cs`, `SongPricing.cs`, `catalog.json`, `global.json` and project files; and Part II `CatalogBrowserViewModel.cs`, `CatalogPage.xaml`, `CatalogPage.xaml.cs`, `CatalogCard.xaml`, `App.xaml`, `AppShell` navigation adapter, `DetailsPage.xaml.cs`, `UiText.cs` and `AdaptiveLayout.cs`.

### Verified by source comparison

- Chapter 4's DI setup, NavigationPage startup, XAML row structure and code-behind search handler correspond to the original Part I files.
- Chapter 5's xUnit v3 package version 4.0.0, historical catalog ID expectations, and the three-minute vocal three-song expected total USD 483.30 correspond to the checked-in tests and pricing rule.
- Chapter 6's themed label style and six-row catalog layout correspond to Part II XAML.
- Chapters 7–8's view-model commands, notifications, Shell route and validated ID navigation correspond to Part II source.
- Chapter 9's image reference `catalog_placeholder.png` is declared in XAML while the source asset is `catalog_placeholder.svg` registered via the MAUI image pipeline. It is a generated-resource name rather than a missing checked-in PNG.
- Chapter 10's RESX/ResourceManager lookup and singular/plural result text correspond to Part II.
- Chapter 11's `WideBreakpoint = 900` and `IsWide` policy correspond to the portable implementation and native page code.

### Manuscript corrections committed

1. Chapter 7 now explicitly distinguishes the Part II two-way SearchBar binding from Chapter 13's later one-way view-model binding plus page-owned 250-ms debounce. Readers must select the appropriate source revision to reproduce either example.
2. Chapter 8 no longer describes the default `main` branch as the evolving implementation; it names the two historical revision IDs and the current `work/chapter16-pricing` review branch.

**Audit status:** These are read-only source comparisons and documentary fixes. They do not prove that the book's excerpts build alone, that fresh tests passed, or that Android/iOS behavior was exercised. Fresh CI, physical/emulator checks, and revised typesetting remain outstanding.
