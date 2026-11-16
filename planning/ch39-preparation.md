# Chapter 39 preparation — November 16, 2026 (Central)

This is a source/review plan, not executed iOS evidence. Chapter 38 remains the
current instructional milestone. The agreed scope remains Windows-centered iPhone
and iPad development with the Mac/Xcode boundary explained explicitly.

## Current primary references

- https://developer.apple.com/news/upcoming-requirements/
- https://developer.apple.com/help/app-store-connect/manage-builds/upload-builds/
- https://learn.microsoft.com/dotnet/maui/ios/pair-to-mac
- https://learn.microsoft.com/dotnet/maui/ios/deployment/publish-cli
- https://learn.microsoft.com/dotnet/maui/ios/deployment/publish-app-store

Apple's checked requirement states that since April 28, 2026, uploads must use
Xcode 26 or later with the applicable iOS/iPadOS 26-or-later SDK. This is a submission
minimum, not the exact Xcode version supported by the pinned .NET 11 workload.
Resolve and record that compatibility before preparing an executable native build.
Keep the minimum deployment OS distinct from the SDK used for submission.

Microsoft documents remote Mac compilation/signing from Windows and saved SSH-key
access after pairing. Avoid copying the documentation's inline password example
into a public workflow. Establish a supported controlled authentication route; do
not infer that a Linux runner or Windows-only publish can replace Apple tools.

## Implementation and evidence tasks

1. Read the current project/platform configuration, including the conditional iOS
   TargetFrameworks entry. Check how a Windows remote invocation selects the iOS
   target instead of assuming macOS-only project evaluation works on Windows.
2. Identify the exact supported .NET 11 SDK/workload/Xcode/macOS pair and available
   runner image. Compile a simulator target first with no distribution identity.
   Record the source/configuration and any link/AOT/package failures honestly.
3. Add an explicit source-to-artifact map for bundle ID/version, Info.plist,
   entitlements, provider callback, media/background capabilities, privacy manifests,
   usage strings and signing/provisioning. Do not copy Android probe authority into
   the production iOS application.
4. Keep simulator launch and unsigned inspection separate from device provisioning,
   signed archive/export, TestFlight processing and actual install/upgrade evidence.
   A public CI simulator result cannot establish access to a publisher's private key.
5. Provide a complete Windows/Mac procedure for controlled developer/distribution
   identities, profiles, device registration where applicable and recovery/cleanup.
   No paid membership, certificate purchase or store submission is implied by writing
   the tutorial. Use a concrete candidate for any later authorized publication.
6. Recheck current Apple privacy/account-deletion/payment/reviewer-access rules and
   implement review access compatible with the managed identity/MFA design. The
   existing account/provider labs do not constitute live deletion or store compliance.
7. Explain internal/external TestFlight testing, build expiration, reviewer metadata,
   genuine phone/tablet screenshots, final submission and forward recovery. Record
   actual completed rows separately from expected steps.

The manuscript's 40-chapter plan and comprehensive intermediate/advanced scope
remain unchanged. Pending Mac/device/store evidence must remain visible even if a
simulator compilation succeeds. This note does not certify a signed iOS candidate.
