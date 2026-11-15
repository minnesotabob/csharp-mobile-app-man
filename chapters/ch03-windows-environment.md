# Chapter 3
# Preparing a Windows Development Environment

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
git clone https://github.com/minnesotabob/csharp-mobile-app-code.git
Set-Location csharp-mobile-app-code
git rev-parse HEAD
```

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

## Summary and exercises

The repeatable sequence is SDK selection, portable tests, workload alignment, native dependencies, compilation, and finally launch on a known device. iOS retains its own Mac-dependent build/signing boundary.

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
