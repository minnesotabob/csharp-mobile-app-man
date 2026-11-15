# Chapter 4
# Building and Debugging the First Application

## What You'll Learn

By the end of this chapter, you will be able to:

- Trace the starter's dependency registration, window creation and page construction.
- Connect XAML controls, generated fields, event handlers and catalog records.
- Predict and inspect the results of the first in-memory search.
- Diagnose whether a defect belongs to data, a rule, event wiring or presentation.
- Record device observations without treating compilation as a runtime result.

**Prerequisites:** the Part I checkout and portable baseline from Chapter 3. A compatible Android target is needed for the native debugging steps. **What you will build and inspect:** the existing starter catalog page and a controlled local debugging experiment. Complete source is supplied; the walkthrough explains the assembly and reasoning rather than requiring you to reconstruct the app from isolated excerpts.

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

## Guided Walkthrough: connect the five source boundaries

Use the Part I checkpoint from Chapter 3. You do not need to create a second MAUI project or replace the app with fragments copied from this chapter. The complete starter already contains the files below. Follow the connections in this order, comparing the actual source with each explanation.

1. Open src/GnazzosWorld.App/MauiProgram.cs. Locate the catalog factory and MainPage registration. The factory supplies an IReadOnlyList of CatalogItem; the page constructor must request that same dependency shape.
2. Open App.xaml.cs. Follow its MainPage constructor parameter into the private page field, then into CreateWindow. That is the first page instance displayed by this milestone. Changing an unused page file cannot alter the visible startup path.
3. Open MainPage.xaml and compare x:Class with the namespace/class in MainPage.xaml.cs. Locate x:Name="CatalogView" and TextChanged="OnSearchChanged". These declarations connect the generated control field and event to the code-behind partial class.
4. Follow the constructor's initial ItemsSource assignment. CatalogLoader.LoadBundled supplies the fixed metadata; CatalogSearch.Find returns the blank-query sorted result. The JSON file order and displayed order need not be identical.
5. Open src/GnazzosWorld.Core/Catalog/CatalogSearch.cs. Read the trim/null handling, optional kind filter, title/creator comparison and final ordering. The interface page exposes text search at this stage; the presence of a kind parameter does not add a visible filter control.
6. Inspect Data/catalog.json and the EmbeddedResource entry in the core project file. A plain file copied beside the app is not automatically the same resource the assembly opens. Resource naming and ownership belong to the data path you are tracing.
7. Launch only after the Chapter 3 build checks succeed. Record what you observe using the expected-results table below. If native launch is unavailable, complete the source trace and mark runtime observations pending.

The dependency direction is page to portable rule, with the composition root providing its data. The portable rule neither creates a page nor retrieves global application services. This is the small beginning of the separation expanded into MVVM later. Understanding it now prevents a larger view model from becoming another place to hide unexplained dependencies.

## Worked Trace: find an accented title

For the query “ beret VIOLET ”, the first useful intermediate value is the trimmed term. The comparison searches titles and creators while ignoring case and nonspacing marks. That lets the unaccented input match Béret violet. The final sort uses a separate deterministic ordering policy; search matching and sort order are different decisions.

At a breakpoint, inspect the result ID rather than relying on a similar-looking title. The expected ID is song-minnesota-bob-beret-violet and the result count is one. The page then assigns the returned collection to ItemsSource. If the rule returns the right record but the old list remains visible, continue into the assignment and control binding rather than changing the comparison algorithm.

| Interaction | Expected portable result | Native observation to record |
|---|---|---|
| First launch / blank query | Five sorted records | Cards are visible and readable |
| Type BERET | One matching song ID | The matching card appears during text entry |
| Type KAI | One book with ID book-kai-01 | Book metadata appears without a sign-in prompt |
| Type an unknown term | Empty result | The page presents its empty message |
| Clear the query | Five records again | Clear action and results remain usable with keyboard/large text |

These are expected behaviors of the starter, not a report that a device was exercised during this editorial pass. Pair each actual observation with its target, source and result. A photograph of a development machine does not replace those details.

## Guided Debugging Exercise: break the handoff, not the rule

Start with a clean exercise branch and a successful baseline. Save the original OnSearchChanged implementation before making one local change. Temporarily replace its result assignment with an empty method body, keeping the event name and signature valid. The application can compile while its search interaction no longer updates the result list.

1. Launch the changed starter and type BERET. Predict that the initial five records remain visible because nothing assigns the new result to the control.
2. Place a breakpoint inside the empty handler. If it is reached, event wiring is functioning. A reached event does not establish a completed presentation update.
3. Run the portable suite. Its search cases should still pass because the portable rule was not changed. That result correctly leaves the native handoff defect outside its coverage.
4. Restore the original assignment, build again and repeat the interaction. Review git diff so that only your intended experiment is removed; preserve unrelated work.
5. Write a defect explanation that names the failed promise and boundary: text input reached the page, but the handler did not publish the computed result.

The worked answer is to restore the assignment, not to weaken a search test or add a background task. This exercise is specified for readers to perform; no local red/green native execution is claimed here. Its purpose is to show why correct pure logic can coexist with a broken screen.

## Troubleshooting the visible result

| Symptom | Boundary to inspect | Useful next check |
|---|---|---|
| InitializeComponent or CatalogView is missing | XAML/C# generated linkage | Compare x:Class, namespace, build action and first compiler error |
| App fails before the first list appears | Construction and embedded data | Break in the loader and inspect the original exception |
| Search handler never runs | Event wiring / active page | Confirm TextChanged and that this is the displayed milestone page |
| Correct records returned, stale cards remain | Publication / control state | Inspect the ItemsSource assignment and actual target control |
| IDs are correct, text is clipped | Native layout and text settings | Observe width, font scale and keyboard on the chosen target |
| Switching away preserves text, restart loses it | Process lifetime and storage | Determine whether the requirement includes persisted recovery |

Do not solve an unexplained UI defect by adding several abstractions at once. Establish the first incorrect value or transition, repair it, and repeat the relevant check. The later MVVM chapter will explain a different coordination structure using the same boundary discipline.

## Chapter Summary

The starter's behavior can be traced through dependency registration, App window creation, XAML/C# linkage, an embedded catalog, a portable search and the ItemsSource assignment. Each boundary gives you a concrete place to inspect when the visible result is wrong. Constructor injection makes the data dependency visible, and the small code-behind handler makes the first handoff easy to follow.

The debugging exercise separates a correct search rule from a missing presentation update. Compilation and passing portable cases leave native interaction, layout and accessibility checks unresolved until observed on a target. Chapter 5 builds on this distinction by treating tests as executable requirements and explaining how a controlled defect produces useful evidence.

## Exercises

1. Correct a demonstration title without changing its ID; verify search.
2. Temporarily remove the resource declaration, observe the failing boundary, and restore it.
3. Compare lifecycle events when switching apps and restarting the process.
4. Find a keyboard or large-text layout defect and explain why a search unit test cannot detect it.

## References and index terms

Dependency injection: https://learn.microsoft.com/en-us/dotnet/maui/fundamentals/dependency-injection  
Lifecycle: https://learn.microsoft.com/en-us/dotnet/maui/fundamentals/app-lifecycle

Index: composition root; constructor injection; lifetime; CreateWindow; XAML partial class; CollectionView; ItemsSource; embedded resource; code-behind; UI thread; debugging.
