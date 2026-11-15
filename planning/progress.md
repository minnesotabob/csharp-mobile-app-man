# Part I draft milestone — November 14, 2026

## Written and illustrated

- Approved title and 40-chapter/eight-Part plan remain in place.
- Preface, reader guide, introduction, Part I overview, and Chapter 1 were drafted in the foundation milestone.
- First drafts of Chapters 2–5 now cover requirements/acceptance scenarios, Windows tooling, the first screen/startup/debugging, and portable tests.
- Part I now has its own original grayscale illustration with a meaningful alternative description. A 300-DPI placement is used in the PDF.
- The opening PDF now contains 39 pages with Chapters 1–5, the Part I illustration, and opening material. It is an editorial draft, not final book pagination or a production-ready paperback.
- Final author/legal pages, detailed TOC, index, other Part illustrations, and verified app screenshots remain future production work.
- Chapter lengths are first-draft coverage; hands-on material and verified screenshots will expand during technical/editorial passes. The approximately 800-page full-book budget is still provisional.

## Verified code

Portable Windows CI: 37 tests, zero errors/failures/skips.  
Run: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43672656910  
Code revision: bf6f2f55b57223d28ea1cf0181b289a362ba8d40

Android Debug build on Windows CI: successful; final compile zero warnings/errors.  
Run: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43672619935  
Code revision: 45e17eb16bfc7b5cfd17e2ea3cebc48d3e8398d4

The later portable revision only adjusts one test case; application/core code matches the Android build revision. The successful Android environment used SDK/workload set 11.0.100, MAUI manifest 11.0.0, MAUI Controls 11.0.10, Android pack 37.2.29, and Microsoft OpenJDK 21.0.11+10.

Required JSON fields now prevent an omitted kind from defaulting to Book. Boundary tests cover missing properties, malformed JSON, empty arrays, caller stream ownership, and null streams.

The dependency-install target reported an unresolved cmdline-tools;21.0 warning; final Android compilation itself was clean. This is recorded in the code verification log.

## Limits

Android compilation is not emulator or hardware launch evidence. Device/accessibility checks, iOS builds/signing, and remote iOS configuration remain pending. No live MFA, backend, player, checkout, or public deployment is implemented yet.

Prior local workload/testing attempts were blocked by automatic review after attempted cloud metadata access. They were not retried. Separate GitHub-hosted Windows workflows now provide the relevant build/test evidence.

## Next

1. Run the first Android application on an emulator/device; capture genuine screenshots and lifecycle/large-text/keyboard observations.
2. Verify iOS compilation in a compatible Mac/Xcode environment.
3. Develop Part II XAML, binding/MVVM, routing, reusable views, accessibility, and adaptive layouts.
4. Revise Part I procedures against observed IDE/device results and expand its hands-on exercises.
