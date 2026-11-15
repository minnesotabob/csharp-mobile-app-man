# Chapter 3
# Preparing a Windows Development Environment

## What You'll Learn

By the end of this chapter, you will be able to:

- Retrieve the source revision that matches the Part I starter.
- Identify the SDK, packages, workloads and native tools selected by the project.
- Build and run portable tests before introducing mobile dependencies.
- Compile Android and distinguish deployment failures from compilation failures.
- Record verification honestly and plan the separate Mac/iOS build boundary.

**Prerequisites:** Windows, Git, an appropriate .NET SDK, and permission to install development tools on your workstation. Android work additionally requires the supported workload and SDK/JDK. **What you will produce:** a recorded portable baseline and, where the native toolchain is available, an Android compilation result. Successful device launch remains a separate check.

A machine can have several .NET SDKs, Java installations, and Android toolchains. Selecting “latest” everywhere does not establish compatibility. We need to know which components a project selects and how to verify the result.

This chapter separates portable C# checks, Android compilation, device launch, and later iOS work. Begin with the fewest dependencies, then add platform tools.

## 3.1 Understand the layers

Visual Studio supplies the integrated Windows editing/debugging experience. The SDK supplies command-line build tools and the compiler. Workloads add platform tooling, while NuGet packages provide project dependencies. Android SDK/JDK components have additional native responsibilities.

These version numbers are related without being interchangeable. A stable SDK can discover an incompatible preinstalled preview workload. A package reference does not install every native tool. A successful library build does not verify Android packaging.

| Component | Purpose | Record |
|---|---|---|
| Visual Studio | Windows IDE/debugging | Exact version and workloads |
| .NET SDK | Compiler, build, CLI | --version and --info |
| MAUI workload set | Coordinated native tooling | workload list |
| MAUI Controls package | Framework dependency | Project version |
| Android SDK/JDK | Android build tools | SDK packages, java -version |
| Device/emulator | Runtime checks | Model, OS/API, architecture |

The foundation pins SDK 11.0.100, selects C# 15, and references MAUI Controls 11.0.10. Consult the current verification record rather than assuming arbitrary newer combinations are equivalent.

## 3.2 Prepare Windows

Use supported Windows and compatible stable Visual Studio with its MAUI development workload. Microsoft's SDK download page identifies the compatible Visual Studio version for .NET 11. Update an outdated installer before selecting a preview as a shortcut.

Allow disk space for SDKs, emulator images, and outputs. Emulator acceleration depends on host configuration. A physical Android device is useful when emulation is impractical, but neither choice can fix a compilation failure.

Open a new PowerShell session after installation, then inspect:

```powershell
dotnet --version
dotnet --info
dotnet workload list
java -version
```

Save the relevant output as an environment record without credentials or customer information. Include version, command, and first meaningful error when reporting a problem.

## 3.3 Retrieve and identify the source

Clone the companion repository or download a source archive for an initial read. Git makes revisions easier to identify.

```powershell
git clone https://github.com/minnesotabob/csharp-mobile-app-code.git `
    csharp-mobile-app-code-part1
Set-Location csharp-mobile-app-code-part1
git switch -c reader/part-01 `
    0b8973660cc21269ff79eb54733edaf428fb5dac
git rev-parse HEAD
git status --short
```

The commands above create an isolated reader branch at the Part I source checkpoint. In a fresh clone, git status --short should produce no entries. If reader/part-01 already exists, inspect that branch rather than forcing a replacement.

The manuscript is a separate repository. A code path in the book refers to the companion code unless stated otherwise. Chapter tags will be created only after verification; a planned tag is not a completed milestone.

The root global.json selects SDK 11.0.100 with patch roll-forward within its feature band. Directory.Build.props enables nullable references, implicit usings, deterministic builds, and language version 15.0. Inspect these before altering a machine-wide setup.

“SDK not found” and “workload missing” refer to different layers. Diagnose the first actual error instead of reinstalling all tools.

## 3.4 Verify the portable core first

The net11.0 library/tests do not require an emulator or mobile workload:

```powershell
$tests = "tests/GnazzosWorld.Core.Tests/GnazzosWorld.Core.Tests.csproj"
dotnet build $tests -c Release
dotnet run --project $tests -c Release --no-build
```

This project uses the generated xUnit executable runner. Its command is intentional; options for another test platform are not interchangeable.

The successful build establishes compilation and dependency resolution for those projects. The test run establishes the suite's cases, not device behavior. Record result and commit ID together.

For restore failures, distinguish connectivity, package availability, and framework compatibility. Suppressing a restore error does not produce a trustworthy later build.

## 3.5 Align stable mobile workloads

Use a workload set compatible with the pinned SDK. In an installer-managed workstation, follow the supported setup and verify the actual workload output. Our CI uses an isolated SDK directory to avoid preview components installed for other software.

The command-line baseline is:

```powershell
dotnet workload install maui-android --version 11.0.100
dotnet workload list
```

Skipping manifest updates does not guarantee reproducibility. The first Android CI attempt retained a preinstalled preview manifest and compiled stable MAUI references against an incompatible Java.Interop assembly. The correction is toolchain alignment, not randomly changing application packages until an error disappears.

Check workload output for unexpected preview suffixes. SDK and workload-set versions belong separately in the environment record.

## 3.6 Install Android dependencies for this project

The InstallAndroidDependencies target examines the project to identify required components. Microsoft documents its directory properties and behavior. Use actual absolute paths; the following directories are examples:

```powershell
$app = "src/GnazzosWorld.App/GnazzosWorld.App.csproj"
$androidSdk = "C:\Android\Sdk"
$javaSdk = "C:\Java\jdk-21"
$dependencyArgs = @(
  "build", $app, "-t:InstallAndroidDependencies",
  "-f", "net11.0-android",
  "-p:AndroidSdkDirectory=$androidSdk",
  "-p:JavaSdkDirectory=$javaSdk",
  "-p:AcceptAndroidSdkLicenses=True"
)
dotnet @dependencyArgs
```

The last property accepts the relevant SDK licenses. Review their terms before running it. Do not relocate installer-managed SDKs simply to match example paths.

Microsoft's dependency documentation recommends its OpenJDK 21 build. Record the JDK path selected by MSBuild, which may differ from a Java executable found first on PATH.

Compile using those directories:

```powershell
$buildArgs = @(
  "build", $app, "-f", "net11.0-android", "-c", "Debug",
  "-p:AndroidSdkDirectory=$androidSdk",
  "-p:JavaSdkDirectory=$javaSdk"
)
dotnet @buildArgs
```

Compilation precedes launch debugging. A missing emulator cannot cause a compiler error; successful compilation cannot establish device authorization.

## 3.7 Prepare an emulator or device

Create a compatible virtual device using supported Android/Visual Studio tooling and wait for boot to complete. Record API level and architecture. For physical hardware, enable developer debugging, connect it, and approve the computer when prompted.

Inspect connectivity with the intended SDK's platform tools:

```powershell
adb devices
```

Invoke adb by full path if necessary. An unauthorized entry requires device-side approval; an offline device and no device at all are different conditions.

Choose Android and the desired device in Visual Studio, then launch. A CLI launch with one known target can use:

```powershell
dotnet build $app -f net11.0-android -t:Run
```

The first runtime check is the bundled list, a BERET search, and clearing the query. Record it separately from CI compilation.

The minimum supported Android API and the build target are not the same setting. The minimum controls eligible devices; build dependencies reflect the selected target/toolchain. Record both.

## 3.8 Plan the iOS boundary

Apple build tools run on a Mac. Windows-to-Mac development needs a compatible IDE, SDK/workloads, Xcode, reachable build host, and signing configuration. An iOS package on Windows does not replace those requirements.

The scaffold has iOS source and conditionally adds its target on macOS. It does not yet implement a complete remote Windows-to-Mac setup. An iOS simulator compilation, a signed device build, and App Store distribution are distinct milestones.

You can complete portable/Android exercises before arranging iOS equipment, but should know the requirement now. An iOS folder is source, not compatibility evidence.

## 3.9 Preserve configuration boundaries

The first examples require no customer credentials. Later settings will include public client identifiers and private server secrets, which have different security properties. Keep secrets, signing material, and real requests out of the public repository.

Do not turn machine-specific paths into everyone else's committed defaults. Capture known versions before upgrades; change a defined layer and repeat relevant checks. Simultaneous SDK, workload, package, and emulator changes make failures harder to explain.

## 3.10 Diagnose in order

Confirm working directory and selected SDK first, then the initial restore/compiler error, then workload/native versions. After compilation, investigate deployment, device authorization, and runtime behavior.

A binary log can help explain dependency resolution but may contain local paths and environment details. Inspect it before sharing; never publish secrets to make troubleshooting convenient.

The environment record separates SDK inspection, portable tests, Android compilation, iOS compilation, and device checks. Mark pending steps explicitly.

## Guided Lab: establish the Part I baseline

Run this lab from the dedicated Part I clone created in section 3.3. If you already have a working copy with valuable changes, leave it in place and use a second directory. The starter's recorded source checkpoint is 0b8973660cc21269ff79eb54733edaf428fb5dac. It uses MainPage and NavigationPage; the later review branch has Shell, forms and an API. Mixing those instructions can produce a perfectly valid application with the wrong screen for this lesson.

1. Run git rev-parse HEAD and compare the full result with the checkpoint. Run git status --short; a fresh exercise copy should have no local changes. Record any deliberate exercise edits separately.
2. Read global.json and Directory.Build.props before building. The SDK choice, language version and project target are different settings. Read the test and core project files to confirm that this step targets portable net11.0 rather than a mobile framework.
3. Run dotnet --info from this repository root. If the selected SDK does not meet global.json, stop at that problem. A mobile-workload installation cannot fix selection of a missing portable SDK.
4. Run the portable Release build from section 3.4. Check that it exits successfully before using --no-build. If it fails, use the first meaningful restore or compilation message as the starting diagnosis.
5. Run the executable test suite. The recorded Part I milestone has 37 passing cases. A total of 245 identifies the later Chapter 18 portable suite, not a newly discovered defect in the starter. Compare the source revision before changing test code.
6. Save an environment/result note using the template below. Leave device and iOS rows pending unless you actually perform those checks.
7. If Android tooling is available, perform sections 3.5–3.6 and record compilation separately. Proceed to launch only after that build succeeds. Chapter 4 provides the runtime trace.

This sequence is intentionally useful even with no emulator installed. It isolates compiler selection, package resolution and portable behavior before adding native tools. It also gives you a concrete success criterion: the matching source compiles and its own recorded suite runs, with failures interpreted against the correct milestone.

| Record field | Example or expected entry |
|---|---|
| Source checkpoint | Full Part I commit ID, plus any local exercise changes |
| Selected SDK | Actual dotnet --info result; compare with global.json |
| Portable build | Release; success/failure and first meaningful diagnostic |
| Portable tests | Actual count and outcome; historical baseline is 37 |
| Android build | Actual framework/tool paths/result, or pending |
| Android launch | Device model, OS and observed behavior, or pending |
| iOS build/launch | Mac/Xcode/target and result, or pending |

Do not replace the word pending with passed merely because the next row succeeded. The note is a record of observations, not a checklist to make visually complete.

## Worked Diagnosis: the wrong test total

Suppose the tests pass but report 245 cases, and your launch opens a Home tab with a request button. You have likely selected the later implementation. Repeating the tests will not produce the Part I screen. Compare the commit and the source-milestone record, then open the dedicated starter checkout for Chapters 4–5.

A different case is a matching Part I revision with an SDK-selection error. Inspect the installed SDK list and the nearest global.json affecting the command. The SDK resolver uses directory context; running a command from another directory can change which configuration is found. Move to the intended repository root and repeat the inspection before editing global.json.

The worked principle is to repair the boundary that failed. Do not change a test expectation to 245 to hide a revision mismatch, remove an SDK pin to hide an unsupported toolchain, or adjust an emulator to fix a compiler error. Each change should have an explanation tied to the observed result.

## Troubleshooting the first build and launch

| Symptom | First diagnostic check | Corrective direction |
|---|---|---|
| Requested SDK is unavailable | Inspect global.json and installed SDKs | Install a supported matching SDK; keep the pin deliberate |
| NuGet restore fails | Read the package/source error before compilation messages | Resolve connectivity, package availability or compatibility |
| Java.Interop version conflict | Compare workload manifests with the pinned stable toolchain | Align SDK/workload/native package versions |
| Android build cannot find Java or SDK tools | Inspect resolved absolute paths | Use the actual supported installations, not example paths |
| adb lists unauthorized | Check the device's debugging approval prompt | Authorize the intended computer on that device |
| Build passes, deployment has no target | Inspect adb devices and emulator boot state | Select one available authorized target |
| A first-page screenshot does not match the chapter | Compare source commit and startup classes | Use the Part I checkpoint for this walkthrough |

For a support request, include the source ID, command, selected tool versions and first relevant diagnostic. Describe whether the failure happened during restore, compilation, deployment or interaction. Review logs for local details before sharing them. A short reproducible report is more useful than an unsorted screenshot of every subsequent message.

## Chapter Summary

A reproducible environment starts with a known source revision and the tools that revision selects. SDK choice, language version, NuGet references, workload manifests and Android SDK/JDK paths are related settings with different responsibilities. Build the portable projects and run their matching suite before introducing deployment or runtime questions.

The Part I checkpoint's recorded baseline is 37 cases and successful Android compilation. Your environment note must state what you actually ran, including any pending device or iOS work. A different test total can reveal a source mismatch rather than a broken rule. With that baseline established, Chapter 4 traces construction, data, controls and search through the starter application.

## Exercises

1. Record installed and selected SDK, workload, package, JDK, Android SDK, and device versions.
2. Explain why --skip-manifest-update can preserve an incompatible environment.
3. Classify a missing SDK, Java.Interop mismatch, and unauthorized device, and state the first check for each.
4. Run portable tests with the emulator closed. Explain what this establishes.

## References and index terms

SDK: https://dotnet.microsoft.com/en-us/download/dotnet/11.0  
Android dependencies: https://learn.microsoft.com/en-us/dotnet/android/getting-started/installation/dependencies  
Workload install: https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-workload-install  
Pair to Mac: https://learn.microsoft.com/en-us/dotnet/maui/ios/pair-to-mac

Index: SDK; global.json; feature band; workload set; JDK; PowerShell; emulator; adb; build host; preview manifest; environment record.
