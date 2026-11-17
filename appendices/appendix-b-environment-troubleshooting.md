# Appendix B
# Environment and Troubleshooting Reference

Use this reference to identify the failing boundary before changing the application. Version numbers below describe a source setting, a recorded historical execution or a proposed toolchain. They are deliberately labeled. See companion docs/verification.md for exact source/run identities and Chapters 3, 18, 38-40 for complete procedures.

## B.1 Start with an environment inventory

At the selected companion checkout, record these commands in a private working note. Review output before sharing it; machine paths and user details are not public-safe evidence by default.

```powershell
git rev-parse HEAD
git status --short
dotnet --version
dotnet --info
dotnet workload --info
```

A build's first meaningful error is usually more useful than the final count of failed targets. Retain the exact command, target, configuration and source revision. Change one suspected cause at a time and record what the next attempt established.

| Item | Source or recorded value | Status and interpretation |
| --- | --- | --- |
| SDK | global.json: 11.0.100, latestPatch | Current source request; inspect actual installed resolution |
| Language | Directory.Build.props: 15.0 | Current shared compiler setting |
| Nullability | Nullable enable | Compiler analysis, not external-input validation |
| MAUI Controls | 11.0.10 | Current app package reference |
| Android framework | net11.0-android | Default app target |
| iOS framework | net11.0-ios | Added conditionally on macOS in source |
| Android minimum | API 26 | App source setting; inspect actual candidate manifest |
| iOS minimum | 16.0 | App source setting; native output remains unverified |
| Historical Android pack | 37.2.29 | Recorded earlier build environment; not a fresh inventory |
| Historical JDK | Microsoft OpenJDK 21.0.11+10 | Recorded Android environment |
| iOS candidate tools | Workload set 11.0.100.1; Xcode 27.2 | Primary-source preparation; not executed for this app |
| Synthetic release lab | Python 3.12.14 on Linux | Actual Chapter 40 local execution |

The Xcode host requirement deserves care. Chapter 39 records a conflict between Microsoft's macOS wording and Apple's table. Host planning follows Apple's Xcode table, which lists Tahoe 26.6+ for Xcode 27.2. Recheck the exact workload/Xcode pair rather than using a platform's minimum OS as the build host requirement.

## B.2 Run the smallest appropriate check

For portable logic, build and execute the actual test project from the repository root:

```powershell
dotnet build tests/GnazzosWorld.Core.Tests -c Release
dotnet run --project tests/GnazzosWorld.Core.Tests `
  -c Release --no-build
```

The companion uses an executable xUnit runner. Follow its README before substituting test-platform flags. A passing portable suite exercises the selected rules and adapters; it does not establish a visible native interaction.

For the actual API pipeline, use tests/GnazzosWorld.Api.Tests with the same build/run pattern. For a real local listener, follow eng/Smoke-Api.ps1. For workstation TLS, follow docs/local-api.md and the CatalogProbe. These checks answer different questions. Run the one that can distinguish your suspected causes before performing a costly full platform rebuild.

## B.3 Understand where localhost points

| Client location | Meaning of localhost | Consequence |
| --- | --- | --- |
| Windows probe | Windows workstation | Can reach its loopback API with matching trust |
| Standard Android emulator | Emulator | Host alias 10.0.2.2 still needs valid TLS name/trust |
| iOS simulator on Mac | Mac | A Windows API needs a deliberately reachable endpoint |
| Physical phone or tablet | That device | Workstation loopback is not a device endpoint |

Changing a hostname to an IP address does not change the certificate's identity. Trusting a development certificate on Windows does not install trust on a phone. Keep certificate validation enabled. Use a deliberate development endpoint with a matching certificate and a known trust path.

The default API launch profile serves HTTPS on localhost:7443 and HTTP on localhost:5080. Those are teaching workstation defaults, not public deployment configuration. AllowedHosts checks incoming hostnames; it does not create a listener, authenticate a customer or open a firewall. A tunnel exposes a service and must be treated as a separate deliberate integration step. See Chapter 18 before using one.

## B.4 Diagnose Android build and runtime separately

If restore fails, compare SDK resolution, workload inventory, configured feeds and actual connectivity. If compilation fails, inspect the first compiler/target error. If a package cannot install, inspect package identity, signature, version and device compatibility. If it installs but fails to launch, inspect the actual launch component and bounded diagnostics for that build.

Do not infer a runtime result from a successful compile. The historical Android environment reported a cmdline-tools resolution warning during dependency setup while the final compiler summaries were clean. Keep those observations separate. A warning's age or location does not make it irrelevant, but its presence is not the same as a C# compilation failure.

Chapter 38's observed emulator used API 35, x86_64 and 4096-byte pages. Its static package alignment checks do not establish a 16 KiB runtime. The package's target API is a third number. Record each rather than labeling all three Android version.

## B.5 Diagnose the iOS boundary

A Windows editor cannot replace the Mac's Xcode tools. First establish the Mac's selected Xcode, workload and simulator architecture. Then inspect the source's conditional TargetFrameworks. The chapter's explicit iOS override avoids relying on macOS-only evaluation when preparing a Windows remote command.

Simulator compilation, simulator launch, physical-device provisioning, distribution archive, Windows remote publication and TestFlight processing require separate results. A certificate without its private key does not provide signing authority. A successful archive does not establish a working provider callback or an update that preserves a draft.

Use docs/ios-release-lab.md and its pending review worksheet. Do not work around a signing error by removing capabilities the feature needs. Resolve the application/team/profile/entitlement relationship and rebuild the intended candidate.

## B.6 Troubleshoot the customer journey

| Symptom | First useful check | Boundary to investigate |
| --- | --- | --- |
| Search shows an older query | Trace debounce revision and departure cancellation | Result ownership and page lifetime |
| Favorite changes disappear | Inspect save result and actual restart | Storage success versus in-memory state |
| Draft restores older text | Identify the last confirmed save | Explicit-save contract |
| Request appears accepted twice | Compare original operation key and server records | Idempotency and reconciliation |
| Sign-in returns to the wrong page | Compare scheme, provider registration and dispatch | Native callback path |
| Account B sees account A data | Inspect issuer/subject partition and stale leases | Ownership and session fencing |
| Media pauses unexpectedly | Observe focus, interruption and route events | Platform playback policy |
| Download restarts or is corrupt | Compare range validator, revision and final hash | Resume identity and file publication |
| Restored server refuses work | Inspect schema/readiness/generation hold | Controlled recovery release |
| New build fails only in Release | Inspect trimming/runtime/package differences | Actual published target |

Preserve affected synthetic state before changing it. Clearing storage or reinstalling may erase the evidence that distinguishes a save failure from an update migration failure. Neither operation belongs in a normal data-preserving upgrade rehearsal.

## B.7 Collect a useful bounded report

A useful report names the selected source, actual package/build, environment, shortest repeatable steps, expected result and observed result. Record whether a draft was explicitly saved, whether the process restarted and whether an update involved an uninstall. For network problems, distinguish a request that never reached the server from a lost response after a possible commit.

Keep tokens, contact stories, private media URLs, payment secrets and raw databases out of public issues. Use invented fixtures to reproduce a fault. Safe hashes and operation categories help compare observations without exposing the underlying private input. Chapter 35 explains the supported diagnostic boundary.

For device acceptance, record physical or virtual device, OS/API, architecture, text size, screen reader, orientation, keyboard state and the actual candidate. A screenshot helps locate a visible defect, but a still image cannot demonstrate a complete accessible journey, restart recovery or successful background playback.

## B.8 Know when to stop changing the code

If the portable rule is correct and the device cannot reach the endpoint, changing the pricing method is unlikely to help. If the artifact hash differs from the audited package, fix candidate selection before debugging a fictional regression. If the signer/profile is unavailable, record that blocked prerequisite rather than describe the tutorial as executed.

The goal is a diagnosis that predicts the next observation. Keep a known working checkpoint, make one purposeful change, run the boundary-specific check and retain its scope. Chapter 40 extends this method to incidents and maintenance.

## References

- Complete source/run evidence: companion docs/verification.md.
- Workstation/API networking: companion docs/local-api.md.
- Android package lab: companion docs/android-release-lab.md.
- iOS preparation: companion docs/ios-release-lab.md.
- Device scenarios: companion docs/device-checks.md.
