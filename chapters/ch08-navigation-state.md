# Chapter 8
# Navigation and Application State

Navigation is a contract between an action, a destination, and the state needed to show that destination. The contract becomes important when a detail view can open from a list, a shared link, a notification, or a restored session.

Our current scope is public in-app navigation. We introduce named Shell routes and validated catalog IDs. Authenticated links, notifications, persistent restoration, and account-dependent continuation remain later features.

## What You'll Learn

By the end of this chapter, you will be able to identify the Shell composition root and named routes; pass stable IDs rather than serialized catalog objects; validate missing or malformed route parameters; distinguish top-level navigation from pushed detail destinations; and design interrupted navigation without claiming full restoration is implemented.

**Prerequisites:** Chapters 1–7 and the Part II interface checkpoint linked in the companion repository’s `docs/milestones.md`. All application paths below are relative to `src/GnazzosWorld.App`; core paths are relative to `src/GnazzosWorld.Core`.

**Deliverable:** A complete Home-to-Discover-to-details route with validated IDs and predictable unavailable-content handling.

## 8.1 Preserve earlier examples through milestones

Use the Part II interface checkpoint linked from `docs/milestones.md`. Its startup creates `AppShell`, with Home and Discover tabs. The Part I `MainPage` and `NavigationPage` remain available in the earlier checkpoint for the first-application exercises.

In this chapter, work in `AppShell.cs`, `Navigation/ShellCatalogNavigation.cs` and `Pages/DetailsPage.xaml.cs`. The portable contract and parser live in the core project’s `Presentation` folder. Keep the checkpoint fixed while following the walkthrough so later application features do not obscure this smaller navigation path.

## 8.2 Define routes intentionally

AppShell creates a TabBar named main with home and discover tabs. Their content routes are welcome and catalog. A separately registered details route creates a destination pushed above the current browsing context.

```csharp
Routing.RegisterRoute("details", typeof(DetailsPage));
```

Home's browse action uses the defined absolute hierarchy:

```csharp
await Shell.Current.GoToAsync("//main/discover/catalog");
```

Named routes are more dependable teaching material than unspecified generated names. Changing a route is a navigation-contract change, even if the visible tab title remains identical.

The route title can be localized without changing its identity. Translating Discover to Explorar should not invalidate internal navigation or saved references.

### Read the whole Shell hierarchy

`AppShell.cs` builds its hierarchy in C# so constructor injection can supply the pages:

```csharp
using GnazzosWorld.App.Pages;
using GnazzosWorld.Core.Localization;
namespace GnazzosWorld.App;
public sealed class AppShell : Shell
{
    public AppShell(HomePage home, CatalogPage catalog)
    {
        FlyoutBehavior = FlyoutBehavior.Disabled;
        Routing.RegisterRoute("details", typeof(DetailsPage));
        var tabs = new TabBar { Route = "main" };
        var homeTab = new Tab { Route = "home", Title = UiText.Home };
        homeTab.Items.Add(new ShellContent
            { Route = "welcome", Title = UiText.Home, Content = home });
        var discoverTab = new Tab
            { Route = "discover", Title = UiText.Discover };
        discoverTab.Items.Add(new ShellContent
            { Route = "catalog", Title = UiText.Discover, Content = catalog });
        tabs.Items.Add(homeTab);
        tabs.Items.Add(discoverTab);
        Items.Add(tabs);
    }
}
```

Follow `Items.Add(tabs)` outward: Shell owns a TabBar; it owns two tabs; each tab owns ShellContent. This yields the absolute path `//main/discover/catalog`. The registered `details` route is separate: it is a destination pushed above the active browsing context.

| Name | Location | Purpose |
|---|---|---|
| `main` | TabBar | Root tab hierarchy |
| `home` / `welcome` | Tab / ShellContent | Home destination |
| `discover` / `catalog` | Tab / ShellContent | Catalog destination |
| `details` | Registered route | Detail page above the active tab |

Change a visible title through `UiText`; preserve these route identifiers unless you deliberately change the callers too.

## 8.3 Distinguish top-level and pushed destinations

A top-level destination belongs to the Shell hierarchy. A detail view can be registered outside that hierarchy and pushed from a selected item. Back should return to the prior browsing context instead of reconstructing a new list unnecessarily.

Absolute navigation is useful for choosing a known top-level location. Relative detail navigation preserves the current context. A page should not use arbitrary absolute paths merely to avoid understanding the stack.

The exact hardware/software Back experience is platform behavior. Verify it on Android and iOS rather than conclude it works from a valid route string.

## 8.4 Pass an identity, not an entire customer object

ShellCatalogNavigation validates a catalog ID and sends it with a short-lived query-parameter object:

```csharp
return shell.GoToAsync("details",
    new ShellNavigationQueryParameters { ["id"] = id });
```

Passing an ID keeps the destination independent of the source view's object instance. The receiving view resolves the record from its own catalog. The parameter object is for a navigation operation; it is not a persistent state store.

Public metadata is appropriate here. Tokens, personal request stories, and private files should not be casually placed into route strings or retained navigation dictionaries. Later secure links must also validate authorization on the server.

### Send the selected ID through the adapter

The complete `Navigation/ShellCatalogNavigation.cs` file is small enough to inspect as one unit:

```csharp
using GnazzosWorld.Core.Presentation;
namespace GnazzosWorld.App.Navigation;
public sealed class ShellCatalogNavigation : ICatalogNavigation
{
    public Task OpenItemAsync(string id)
    {
        if (!RoutePayload.IsValidId(id))
            throw new ArgumentException("Invalid catalog ID.", nameof(id));
        var shell = Shell.Current
            ?? throw new InvalidOperationException("The shell is not ready.");
        return shell.GoToAsync("details",
            new ShellNavigationQueryParameters { ["id"] = id });
    }
}
```

`OpenItemAsync` receives the snapshot ID chosen by the browser command. It validates the ID, obtains the active Shell, and passes a single-use parameter dictionary. It leaves catalog lookup to the destination. Setting a breakpoint on each side of `GoToAsync` lets you follow one record without serializing the whole object.

## 8.5 Validate the incoming payload

DetailsPage implements IQueryAttributable and delegates parsing to a portable helper:

```csharp
public void ApplyQueryAttributes(
    IDictionary<string, object> query)
    => viewModel.Load(RoutePayload.ReadItemId(query));
```

The helper requires a string value under id, limits length, and allows the application's ID alphabet. It rejects path-like or query-like input instead of treating it as another route.

This is shape validation for public catalog identifiers. It does not prove ownership or turn the catalog into a security authority. A future protected order route needs authentication and resource-level authorization.

Because these parameters are passed directly as objects, we do not repeatedly URL-decode them. Other entry mechanisms have their own parsing rules. Double decoding can turn an apparently harmless value into a different string.

### Receive and validate the parameter

In `Pages/DetailsPage.xaml.cs`, retain the constructor as well as the query callback:

```csharp
using GnazzosWorld.Core.Presentation;
namespace GnazzosWorld.App.Pages;
public partial class DetailsPage : ContentPage, IQueryAttributable
{
    private readonly DetailViewModel viewModel;
    public DetailsPage(DetailViewModel viewModel)
    {
        InitializeComponent();
        this.viewModel = viewModel;
        BindingContext = viewModel;
    }
    public void ApplyQueryAttributes(IDictionary<string, object> query)
        => viewModel.Load(RoutePayload.ReadItemId(query));
}
```

The constructor stores the injected view model and uses it as the page’s binding context. Shell then supplies query attributes. `Presentation/RoutePayload.cs` performs the portable parsing:

```csharp
namespace GnazzosWorld.Core.Presentation;
public static class RoutePayload
{
    public static string? ReadItemId(IDictionary<string, object> query)
    {
        ArgumentNullException.ThrowIfNull(query);
        if (!query.TryGetValue("id", out var value) || value is not string id)
            return null;
        return IsValidId(id) ? id : null;
    }
    public static bool IsValidId(string? id)
        => !string.IsNullOrEmpty(id) && id.Length <= 128
        && id.All(c => char.IsAsciiLetterOrDigit(c) || c is '-' or '_' or '.');
}
```

A missing key, a number instead of a string, or a path-like value produces `null`. A well-formed ID may still refer to no catalog item; `DetailViewModel.Load` handles that next. Format validation and record lookup are two separate steps with useful separate tests.

## 8.6 Handle missing content as a normal state

A validly shaped ID may be absent from the current catalog. DetailViewModel.Load then clears the prior Item and displays an unavailable message. It must not leave the previous record's creator or description visible.

Tests first load a valid record, then an unknown ID, and assert that old content disappears. This scenario catches a common reuse defect that a single fresh-page test would miss.

An invalid parameter follows the same clear unavailable experience at this public detail boundary. Do not manufacture a record from user input just to avoid an empty destination.

## 8.7 Keep navigation behind a narrow interface

ICatalogNavigation exposes OpenItemAsync. The view model does not know about Shell, platform pages, or URI formatting. Tests record selected IDs through a small fake.

The MAUI adapter obtains the current Shell when called. In this milestone, navigation is designed around the application's active single browsing window. Full simultaneous multiwindow navigation would need a window-scoped service rather than relying on a global current Shell.

This is an important limit to document. Making AppShell transient at window creation avoids reusing the same root page instance, but does not by itself complete multiwindow coordination.

### Register the dependencies at startup

In `MauiProgram.cs`, the catalog and navigation service have application-wide lifetimes; page and view-model registrations are transient:

```csharp
        builder.Services.AddSingleton<IReadOnlyList<CatalogItem>>(
            _ => CatalogLoader.LoadBundled());
        builder.Services.AddSingleton<
            ICatalogNavigation, ShellCatalogNavigation>();
        builder.Services.AddTransient<CatalogBrowserViewModel>();
        builder.Services.AddTransient<DetailViewModel>();
        builder.Services.AddTransient<HomePage>();
        builder.Services.AddTransient<CatalogPage>();
        builder.Services.AddTransient<DetailsPage>();
        builder.Services.AddTransient<AppShell>();
```

These lines belong inside the existing `CreateMauiApp` method. Keep its `using` directives for pages, navigation, catalog, presentation and dependency injection. Registration tells the container how to construct a detail page and its model when the route needs one. A constructor parameter alone does not register that service.

## 8.8 Prevent repeated activations

The browser command disables itself while navigation is pending and captures the chosen ID before awaiting. A repeated tap therefore does not stack several copies of the same request.

The selected record can still change as the app responds to other input. Snapshotting the ID means the operation follows the user's original activation rather than whichever record happens to be selected after the await.

Error handling belongs at a boundary that can produce useful feedback. A failed navigation command reports a localized message and re-enables. It does not leak a technical exception into the user-facing screen.

## 8.9 Separate navigation from restoration

The browser view model preserves query and selection while its Shell content instance remains alive. That is in-memory retention, not restart restoration.

Persistent restoration requires deciding which values to save, when to save them, and how to validate them against the next catalog version. A selected ID may no longer exist after an update. An expired account may not permit a previously protected destination.

A future saved navigation model should use small identities and explicit versioning, not serialize native page objects. Storage and authenticated continuation arrive later, where they can be tested with real lifecycle requirements.

## 8.10 Plan modal and interrupted flows

A modal interaction, such as an optional picker or consent step, needs a clear cancellation outcome. Returning to a prior page should not imply that the operation succeeded.

Our current application has no sign-in modal or checkout return. Describe those future flows in terms of pending action, required prerequisite, success/cancel/error, and safe continuation. Avoid implementing a placeholder success screen that would be mistaken for a real integration.

Back behavior, application interruption, and a canceled asynchronous task are related but distinct. A navigation test can cover coordination rules, while actual OS transitions still need device checks.

## Guided Lab

1. Trace the four route levels in `AppShell.cs`, then compare them with Home’s browse handler. Activate Browse from Home.
2. Select Kai and choose Open selection. Inspect the ID entering `ShellCatalogNavigation.OpenItemAsync` and the dictionary arriving at `ApplyQueryAttributes`.
3. Return to Discover using the platform’s Back action. Compare query and selection with their state before opening details.
4. Run the route-parser tests with a missing `id`, a numeric value and `../private`. Each should return no accepted ID.
5. In `Unknown_detail_clears_previous_content`, follow a valid ID with an unknown ID. Inspect the creator, description and unavailable message.
6. Change a tab’s visible resource label in a temporary copy while keeping its route. Browse should still reach the same destination. Restore the label.

**Expected result:** a selected public item reaches its detail screen by stable ID; malformed or missing items show an unavailable state instead of old content.

## Worked Example

A reader opens Kai, returns to Discover and then opens a link to an item removed from the bundled catalog. The second destination must clear Kai’s title, creator and description. The parser may accept the new ID’s shape, but lookup determines availability.

To diagnose this case, first inspect the received `id`, then the parser’s output, then `DetailViewModel.Item`. If the item is null but the old description remains on screen, investigate clearing and notifications rather than changing route names. This keeps navigation, lookup and rendering failures distinguishable.

## Troubleshooting

| Symptom | First correction |
|---|---|
| Browse reaches no destination | Compare the absolute path with the named Shell hierarchy. |
| The detail page cannot be constructed | Check page and view-model registrations and their constructor dependencies. |
| The incoming record ID is rejected | Inspect the dictionary key, value type and allowed ID characters. |
| Old details remain after an unavailable ID | Inspect model clearing and notifications before changing routes. |

## Chapter Summary

Navigation describes both where the user goes and what minimal identity the destination needs. This chapter moves from the earlier `NavigationPage` starter to named Shell routes, keeping the source milestones explicit. Stable IDs travel across route boundaries; full catalog objects and translated labels do not define destination identity. Parsing failures, removed records, repeated taps and stale details are normal cases rather than exceptions to hide. The guided lab traces an item through route registration and lookup, exercises invalid IDs, and designs a minimal restoration record. Portable routing tests support these rules, while hardware back behavior, process termination, multiwindow state and authenticated deep links require later implementation and device checks.

## Exercises

At the Chapter 8 checkpoint, the app has named top-level destinations, a public detail route, a stable-ID payload, and tested parsing/unavailable states. External deep links and account-dependent routes arrive in later chapters; a complete restart-restoration journey still needs its own implementation and native verification.

1. Open a record, return, and record whether query/selection remain on each device.
2. Send an unknown ID after a valid ID and inspect stale-content clearing.
3. Explain why a translated tab title should not rename its route.
4. Design a saved-route record that handles a removed catalog item.
5. Describe what must change for two simultaneously active windows.

## References and index terms

Shell navigation: https://learn.microsoft.com/en-us/dotnet/maui/fundamentals/shell/navigation  
Dependency injection: https://learn.microsoft.com/en-us/dotnet/maui/fundamentals/dependency-injection

Index: Shell; routes; TabBar; absolute navigation; relative navigation; IQueryAttributable; query payload; stable ID; back stack; restoration; multiwindow scope.
