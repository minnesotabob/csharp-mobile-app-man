# Chapter 4
# Building and Debugging the First Application

This chapter follows the Part I source milestone, commit 0b8973660cc21269ff79eb54733edaf428fb5dac in the companion code repository. Current main evolves the app into Shell and MVVM in Part II. See docs/milestones.md to select the source that matches this chapter.

The first screen is a tracing exercise. Follow its heading back to XAML, its records to the bundled catalog, search to portable C#, and startup to the application builder. Understanding that path is more useful than beginning with a large template full of unexplained features.

The starter displays books, songs, and demonstration podcast metadata. It has no live identity provider, backend, checkout, or player. This chapter explains its implementation and the checks required before calling it a verified mobile application.

## 4.1 Read the project from outside inward

src/GnazzosWorld.App contains the shared application and platform entry points. Its project file targets Android, adds iOS on macOS, enables MAUI/single-project resources, and references the portable core. RootNamespace connects XAML classes with C# partial classes.

ApplicationTitle is a displayed name; ApplicationId identifies the package. Review the provisional identifier before release. Package identity is not merely branding.

Resources contain icon and splash artwork. Android and iOS folders hold platform declarations. Shared UI does not eliminate native entry points or manifests. We will keep these visible rather than pretend every platform detail lives in one XAML file.

## 4.2 Follow startup through the container

MauiProgram.CreateMauiApp configures the app and dependencies:

```csharp
var builder = MauiApp.CreateBuilder().UseMauiApp<App>();
builder.Services.AddSingleton<IReadOnlyList<CatalogItem>>(
    _ => CatalogLoader.LoadBundled());
builder.Services.AddTransient<MainPage>();
return builder.Build();
```

The container invokes the catalog factory when resolving the dependency, not simply when registering it. The initial page construction triggers that chain. A malformed embedded catalog can therefore fail during startup.

The singleton snapshot is appropriate for this small immutable catalog. A transient page registration creates a page when resolved. These lifetimes need review when mutable data or multiple windows arrive.

Constructor injection makes the dependency visible: MainPage receives records rather than discovering a global application object. Later, a service or view model can replace the direct catalog dependency without teaching the page how HTTP and caching work.

## 4.3 Create the first window

App.xaml supplies shared resources. Its partial class initializes them and receives the initial page. CreateWindow establishes a navigation host:

```csharp
protected override Window CreateWindow(
    IActivationState? activationState)
    => new(new NavigationPage(page));
```

This does not implement the final tab/routing system. It also does not claim a complete multiwindow design: reusing a page in multiple windows would require a different page factory/lifetime. Chapter 8 develops navigation intentionally.

When generated fields or InitializeComponent are missing, check x:Class, namespace, file build action, and the first XAML compiler error. Copying a file from another template may introduce more mismatches.

## 4.4 Understand the layout

MainPage uses a Grid with automatic rows for heading/search and remaining space for CollectionView. Padding and spacing avoid fixed screen coordinates.

```xml
<Grid Padding="20" RowDefinitions="Auto,Auto,*"
      RowSpacing="12">
    <!-- Heading, search, and collection occupy the rows. -->
</Grid>
```

This explanatory extract is not a complete page; the repository contains namespaces and controls. The heading has a semantic level. SearchBar has a clear placeholder. CollectionView provides an empty message and a typed CatalogItem template showing title, creator, and description.

Typed binding metadata helps XAML compilation understand the template context. CatalogItem comes from the core assembly, not a second copy in the app.

The initial list is intentionally modest. Adaptive tablet details, themes, reusable cards, and comprehensive accessibility work follow. Resizing a list is not the same as finishing a tablet design.

## 4.5 Follow records onto the screen

MainPage initializes its controls, stores the injected catalog, and sets ItemsSource to the blank-query search result. The portable method treats a null query as empty and returns a sorted list.

The handler stays small:

```csharp
private void OnSearchChanged(
    object? sender, TextChangedEventArgs e)
    => CatalogView.ItemsSource =
        CatalogSearch.Find(catalog, e.NewTextValue);
```

Five in-memory records do not need a background task. Task.Run on every keystroke would add coordination without solving an observed problem. Remote search later introduces cancellation, debouncing, and stale-result handling.

Code-behind makes the first flow visible. Chapter 7 moves coordination into a view model and explains why. A design should acquire abstractions when they improve a real feature or test.

The core already supports a kind filter; the screen does not expose that filter yet. A tested method and a completed user-facing capability are different milestones.

## 4.6 Understand embedded data and ownership

The core project embeds catalog.json. LoadBundled opens it by qualified resource name, deserializes it, and disposes the stream. Load(Stream) accepts a caller's stream without assuming ownership.

This distinction matters when tests or future adapters supply streams. An HTTP adapter should control its response lifetime. A reusable loader should not unexpectedly dispose an arbitrary caller's resource.

Validation rejects duplicates, invalid metadata, and unsupported link schemes. Required JSON fields are also declared explicitly in the updated model. This protects the loader's contract; it does not establish every policy needed when launching an external URL.

For bundled application data, failing early exposes a packaging defect. A future network update needs more recovery: retain a valid cached copy and report why a refresh failed rather than replace usable data with a broken response.

## 4.7 Debug the data path

Set breakpoints in LoadBundled, the page constructor, and OnSearchChanged. Launch on a configured target and inspect records. Type BERET and follow the comparison path into CatalogSearch.

Inspect values: the trimmed query, matched title, and returned IDs. Clearing a query is a separate case. A breakpoint being reached is evidence of execution, not evidence that the result is correct.

If no content appears, locate the first divergence: missing resource, validation failure, wrong ItemsSource, binding mismatch, or layout allocation. An exception during page construction can originate in JSON. Replacing the visual tree cannot fix it.

If portable tests pass but the screen does not update, inspect event wiring and presentation. If the project does not compile, emulator settings are not yet relevant.

## 4.8 Observe lifecycle without assuming guarantees

Window exposes activation, deactivation, stop, and resume events. On a device, compare switching apps with restarting the process. Exact sequences and guarantees depend on the platform and situation.

For an experiment, temporarily subscribe to window events in CreateWindow and write only short event names to Debug output. Do not log tokens or customer stories. Remove temporary diagnostics or control them appropriately before release.

Press Home, return, rotate, and restart as distinct checks. An existing process returning to the foreground is different from a new process reconstructing state.

The search field may not need permanent recovery. A valuable customer draft does. That requirement determines save points; do not assume one final lifecycle callback will always preserve data.

## 4.9 Keep UI work appropriate

The interface thread must remain responsive. A tiny synchronous search is cheap; blocking HTTP or a large data operation is not. Use asynchronous I/O when the feature needs it, then update controls through the appropriate UI context.

Avoid Result or Wait on asynchronous work in constructors. Introduce an explicit loading lifecycle with loading/empty/error/success states. Event handlers may require async void signatures, but delegated work should generally return observable Tasks.

Cancellation is normal when work becomes irrelevant. An unowned fire-and-forget operation can lose failures after navigation. The connected chapters will supply a complete pattern rather than inserting asynchronous methods into the starter without explaining their owner.

## 4.10 Perform a focused launch check

After compilation, launch on a configured Android target. Confirm the five sample entries, BERET matching, an unknown-term empty state, and clearing the query.

Then test orientation, large text, keyboard visibility, and TalkBack reading order. The semantic heading is a start, not accessibility certification.

Do the corresponding iPhone/iPad checks after an iOS build exists. Platform folders are not evidence of launch compatibility. Record device, OS, build revision, and result for each check.

Describe defects concretely. “BERET returns the right record, but the keyboard hides it at large text size” identifies a different problem from a failing comparison.

## 4.11 Preserve useful diagnostics

Keep build logs, portable results, and device observations separate. Native dependency resolution belongs to build evidence. Runtime exceptions and system behavior belong to device output. A recording can reveal keyboard/focus problems, but must use sample data.

Logs have privacy and performance consequences. Retain useful error categories without including personal requests. Review binary build logs before publishing them because they can contain local environment details.

## Summary and exercises

You can trace the composition root, window creation, typed collection, embedded resource, and portable search. You can also separate compilation, binding, data, and device failures.

1. Correct a demonstration title without changing its ID; verify search.
2. Temporarily remove the resource declaration, observe the failing boundary, and restore it.
3. Compare lifecycle events when switching apps and restarting the process.
4. Find a keyboard or large-text layout defect and explain why a search unit test cannot detect it.

## References and index terms

Dependency injection: https://learn.microsoft.com/en-us/dotnet/maui/fundamentals/dependency-injection  
Lifecycle: https://learn.microsoft.com/en-us/dotnet/maui/fundamentals/app-lifecycle

Index: composition root; constructor injection; lifetime; CreateWindow; XAML partial class; CollectionView; ItemsSource; embedded resource; code-behind; UI thread; debugging.
