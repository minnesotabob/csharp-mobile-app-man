# Chapter 8
# Navigation and Application State

Navigation is a contract between an action, a destination, and the state needed to show that destination. The contract becomes important when a detail view can open from a list, a shared link, a notification, or a restored session.

Our current scope is public in-app navigation. We introduce named Shell routes and validated catalog IDs. Authenticated links, notifications, persistent restoration, and account-dependent continuation remain later features.

## 8.1 Preserve earlier examples through milestones

The Part I application used NavigationPage around MainPage. Part II moves startup to AppShell and different pages. Both designs remain understandable only if a reader knows which source revision belongs to which explanation.

docs/milestones.md identifies the Part I commit. Main represents the evolving implementation. Use history to reproduce an earlier example rather than retaining several divergent applications without version labels.

The old MainPage files remain as an educational starter in the source tree, but Part II startup does not resolve them. The current composition root registers HomePage, CatalogPage, DetailsPage, and AppShell.

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

## 8.6 Handle missing content as a normal state

A validly shaped ID may be absent from the current catalog. DetailViewModel.Load then clears the prior Item and displays an unavailable message. It must not leave the previous record's creator or description visible.

Tests first load a valid record, then an unknown ID, and assert that old content disappears. This scenario catches a common reuse defect that a single fresh-page test would miss.

An invalid parameter follows the same clear unavailable experience at this public detail boundary. Do not manufacture a record from user input just to avoid an empty destination.

## 8.7 Keep navigation behind a narrow interface

ICatalogNavigation exposes OpenItemAsync. The view model does not know about Shell, platform pages, or URI formatting. Tests record selected IDs through a small fake.

The MAUI adapter obtains the current Shell when called. In this milestone, navigation is designed around the application's active single browsing window. Full simultaneous multiwindow navigation would need a window-scoped service rather than relying on a global current Shell.

This is an important limit to document. Making AppShell transient at window creation avoids reusing the same root page instance, but does not by itself complete multiwindow coordination.

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

## Checkpoint and exercises

The app has named top-level destinations, a public detail route, a stable-ID payload, and tested parsing/unavailable states. It does not yet implement external deep links, account-dependent routes, or restart restoration.

1. Open a record, return, and record whether query/selection remain on each device.
2. Send an unknown ID after a valid ID and inspect stale-content clearing.
3. Explain why a translated tab title should not rename its route.
4. Design a saved-route record that handles a removed catalog item.
5. Describe what must change for two simultaneously active windows.

## References and index terms

Shell navigation: https://learn.microsoft.com/en-us/dotnet/maui/fundamentals/shell/navigation  
Dependency injection: https://learn.microsoft.com/en-us/dotnet/maui/fundamentals/dependency-injection

Index: Shell; routes; TabBar; absolute navigation; relative navigation; IQueryAttributable; query payload; stable ID; back stack; restoration; multiwindow scope.
