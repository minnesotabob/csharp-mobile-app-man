# Parts I and II draft milestone — November 14, 2026 (Central)

## Written and illustrated

First drafts now cover Chapters 1–11, preface, reader guide, introduction, and two Part introductions with chapter previews. Part II adds XAML/resources, binding and MVVM, Shell navigation/state, collections/images/reuse, accessibility/localization, and adaptive layouts. Both Parts have distinct original grayscale illustrations with alternative descriptions.

The 68-page opening PDF includes linked contents/bookmarks and the selected 8 × 10 typography. It remains an editorial proof; chapter coverage, hands-on walkthroughs and real screenshots will expand after technical/device review. The 40-chapter/eight-Part plan and approximately 800-page budget remain provisional. These short first drafts are not final chapter lengths.

Final front/back matter, acknowledgments, author biography, ISBN/legal details, remaining Part art, complete index, accessible EPUB, and release production remain pending. Editorial index terms are retained in Markdown for later indexing.

## Verified code

Source revision: 9497b0d7e8acb74c07c50be8cb56f26453664fbb in csharp-mobile-app-code.

- Portable Release build and executable xUnit suite on Windows CI: 61 tests, 0 errors, failures, skipped or not run.
- Evidence: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43674393990
- Android Debug compilation on Windows CI: success, final compile 0 warnings/errors.
- Evidence: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43674393959

The companion app now has Home/Discover Shell navigation, typed bindings, a portable catalog browser model, search/kind filtering, stable-ID details, reusable cards/detail view, English/Spanish resources, light/dark resources, and a width-based inline-detail policy. Tests exercise state and command boundaries; they do not prove native accessibility or rendering.

Toolchain: SDK/workload set 11.0.100, MAUI manifest 11.0.0, Controls 11.0.10, Android pack 37.2.29, Microsoft OpenJDK 21.0.11+10. Dependency installation reports an unresolved cmdline-tools;21.0 warning; final Android compilation is clean. See companion docs/verification.md.

## Limits and next work

Device/emulator launch, native navigation/keyboard/rotation, screen-reader/large-text/theme/language checks, and iOS compilation/signing remain pending. Multiwindow navigation, remote artwork, backend, identity/MFA, playback, checkout and deployment are not implemented. Follow docs/device-checks.md rather than marking these passed from unit tests.

Earlier local workload/test attempts were blocked by automatic review after attempted cloud metadata access; they were not retried. Separate GitHub-hosted Windows CI provides the evidence above.

Next: develop Part III catalogs, search and the request/pricing workflow; expand earlier chapters against actual device observations when available. Preserve the Part I source milestone for Chapters 4–5 using companion docs/milestones.md.
