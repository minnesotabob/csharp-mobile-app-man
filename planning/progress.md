# Foundation milestone — November 14, 2026

## Completed

- Updated the approved title to **Building Mobile Apps with C# 15** and subtitle to **.NET 11 and .NET MAUI 11: A Windows Developer’s Guide to Android, iPhone, and Tablets**.
- Preserved the 40-chapter outline, 8 Parts, 8 × 10 paperback specification, approximately 800-page budget, ebook requirements, and front/back matter plan.
- Drafted preface, reader orientation, substantive introduction, Part I introduction/chapter previews, and Chapter 1.
- Committed a .NET 11 portable core, five-record demonstration catalog, search, validation, snapshot pricing, xUnit v3 tests, MAUI first-screen scaffold, and Windows CI to the code repository.
- Installed and inspected .NET SDK 11.0.100 locally. Static validation passed for nine project/XAML/XML/plist/SVG files and five unique sample records.
- Verified GitHub-hosted Windows CI success at commit 0f05bf9c16a1e97118a2f85a56fc477cbe01ddd8: restore, Release build, and xUnit executable test steps all succeeded.

Evidence: https://github.com/minnesotabob/csharp-mobile-app-code/actions/runs/43669410320

## Constraints and remaining work

Automatic approval review rejected local workload installation and test/restore processes after cloud metadata endpoint access was attempted. They were not retried. The Windows CI route runs in a separate GitHub-hosted environment with read-only repository permissions and no secrets; it successfully verifies portable code, not MAUI platforms.

Android/iOS compilation, emulator/hardware behavior, signed packages, and remote iOS setup remain unverified. No tenant, MFA, backend, live media player, payment system, or deployment is implemented. Chapter 1 is an editorial draft, not a completed Part I; Chapters 2–5 remain to write.

The initial layout PDF is an 8 × 10 typography specimen of the opening material, not a production-ready book. Final Part illustrations and real screenshots remain pending. Ch01/edition tags are not created yet because the chapter milestone is not fully validated on devices.

## Next implementation targets

1. Verify Android/iOS scaffold builds in an appropriate toolchain; record precise SDK/JDK/Xcode/OS combinations.
2. Draft Chapter 2 application specification and Chapter 3 Windows environment instructions against those results.
3. Develop Chapter 4/5 examples and device checks; introduce portable tests already present.
4. Create the Part I illustration once its composition is settled and complete acknowledgments/bio/legal pages from author-approved details.
