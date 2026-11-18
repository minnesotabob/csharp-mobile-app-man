# Chapter 9
# Collections, Images, and Reusable Views

A catalog row appears simple until the same information must work in several places. A title, creator, thumbnail, selection state, and accessible reading order need a consistent relationship. Repeating a visual tree in every page makes that relationship harder to maintain.

This chapter extracts CatalogCard and DetailsView, explains their binding boundaries, and develops a realistic plan for images and larger collections. The implementation still uses five bundled records and a local decorative placeholder. Remote artwork and incremental retrieval are explicitly future extensions.

## What You'll Learn

By the end of this chapter, you will be able to explain why CollectionView owns visual recycling but not search policy; give each DataTemplate the correct binding type; preserve stable item identity across filter changes; choose sensible placeholder and image sizing strategies; and distinguish bundled assets from remote-artwork features not yet implemented.

**Prerequisites:** Chapters 1–8 and the Part II interface checkpoint linked in the companion repository’s `docs/milestones.md`. All application paths below are relative to `src/GnazzosWorld.App`; core paths are relative to `src/GnazzosWorld.Core`.

**Deliverable:** A reusable catalog card and detail view with clear binding scope, selected appearance and a bundled image fallback.

## 9.1 Choose the collection's responsibility

CollectionView displays a sequence and manages selection. The browser view model supplies its current result list and selected record. The row template supplies presentation.

Do not make a row responsible for searching the entire catalog or deciding which server endpoint to call. Likewise, the view model should not create native row controls. These responsibilities change at different rates and are tested at different boundaries.

The current list uses single selection. Selecting an item updates inline details on a wide layout; the explicit Open selection command can open the full detail destination. Narrow layouts retain that explicit action instead of hiding a navigation rule inside every card.

The command makes repeated activation behavior easy to test. Whether the selection/action sequence is sufficiently discoverable requires a device usability check.

## 9.2 Give each template the right type

The collection's DataTemplate declares CatalogItem as its data type:

```xml
<DataTemplate x:DataType="catalog:CatalogItem">
    <views:CatalogCard />
</DataTemplate>
```

Each instantiated card inherits that item's BindingContext. CatalogCard's own XAML also declares the expected type, so its title and creator bindings have a clear contract.

Do not set the card's BindingContext to itself merely to reach its properties. That would hide the inherited catalog record. A different reusable control can intentionally expose bindable properties, but then its implementation must distinguish the consumer's context from its own internal source.

Our card is deliberately specific: it presents a CatalogItem. Reuse does not require turning it into a universal card with dozens of modes before a second requirement exists.

### Connect the collection and row

Inside the existing catalog page, the complete collection region is:

```xml
      <CollectionView Grid.Row="5" ItemsSource="{Binding Items}"
                      SelectedItem="{Binding SelectedItem, Mode=TwoWay}"
                      SelectionMode="Single"
                      EmptyView="{x:Static text:UiText.Empty}">
        <CollectionView.ItemTemplate>
          <DataTemplate x:DataType="catalog:CatalogItem">
            <views:CatalogCard />
          </DataTemplate>
        </CollectionView.ItemTemplate>
      </CollectionView>
```

`ItemsSource` comes from the browser. `SelectedItem` sends the selected object back through a two-way binding. The template changes the data type to one `CatalogItem`; a row’s `Title` therefore refers to that item rather than the browser model.

Open `Views/CatalogCard.xaml`. Keep its `ContentView` declaration, `x:Class` and `x:DataType="catalog:CatalogItem"`; its visual content is:

```xml
  <Grid Padding="12" ColumnDefinitions="48,*" ColumnSpacing="12">
    <Image Source="catalog_placeholder.png" WidthRequest="48"
           HeightRequest="56" Aspect="AspectFit"
           AutomationProperties.IsInAccessibleTree="False" />
    <VerticalStackLayout Grid.Column="1" Spacing="4">
      <Label Text="{Binding Title}" FontAttributes="Bold" />
      <Label Text="{Binding Creator}" />
    </VerticalStackLayout>
  </Grid>
```

The fixed-width image column leaves the remaining width for text. Title and creator stack vertically without a fixed row height. You can change text spacing here once and see the result for every catalog row. The view inherits each item as its binding context; its constructor should call `InitializeComponent` without assigning `BindingContext = this`.

## 9.3 Keep item state out of recycled visuals

A collection may reuse or recreate item visuals as its viewport changes. Store durable selection and feature state in the presentation model, identified by record ID, rather than in whichever row instance happens to be visible.

A favorite should not be an untracked Boolean field in a row's code-behind. Otherwise, scrolling or rebinding can confuse state between records. When favorites arrive, their data will live in the appropriate local/account model.

Our row has no private catalog state. It displays the current context and responds to visual selection states. The selected record lives in CatalogBrowserViewModel.

Stress testing with repeated titles and distinct IDs helps reveal accidental identity assumptions. A large synthetic dataset can exercise scrolling, but should not be confused with actual backend pagination.

## 9.4 Represent selected appearance through visual states

CatalogCard declares Normal and Selected visual states. Selected uses theme-aware colors; Normal returns to a transparent background.

The state communicates appearance, not authorization or data identity. The selection model remains correct even if a visual-state setter is wrong. Conversely, a highlighted row alone does not prove that its corresponding item is the one passed to navigation.

Check selected contrast in both themes and with native accessibility selection announcements. Color alone should not be the only way a person can understand which item is active.

A future row can use an additional indicator or accessible description if platform testing shows the default selection experience is inadequate. Avoid inventing a spoken message without listening to the resulting native announcement.

### Express the two row appearances

The following block belongs directly inside `CatalogCard`’s `ContentView`, before its Grid:

```xml
  <VisualStateManager.VisualStateGroups>
    <VisualStateGroup Name="CommonStates">
      <VisualState Name="Normal">
        <VisualState.Setters>
          <Setter Property="BackgroundColor" Value="Transparent" />
        </VisualState.Setters>
      </VisualState>
      <VisualState Name="Selected">
        <VisualState.Setters>
          <Setter Property="BackgroundColor"

        Value="{AppThemeBinding
          Light={StaticResource SelectionLight},
          Dark={StaticResource SelectionDark}}" />
        </VisualState.Setters>
      </VisualState>
    </VisualStateGroup>
  </VisualStateManager.VisualStateGroups>
```

Keep both states. A row returning to Normal must lose its selected background. The theme resource names come from `App.xaml`, so a missing key belongs in the resource dictionary investigation rather than the search code.

**Try it:** select a row, select a different row, then filter away the selection. Check the previous row’s appearance each time. This sequence is more revealing than inspecting one selected screenshot.

## 9.5 Package the first image predictably

The sample includes catalog_placeholder.svg as a MauiImage resource. MAUI's build process prepares platform assets, and the view references catalog_placeholder.png. This filename relationship is part of the framework's image-resource convention.

```xml
<Image Source="catalog_placeholder.png"
       WidthRequest="48" HeightRequest="56"
       Aspect="AspectFit"
       AutomationProperties.IsInAccessibleTree="False" />
```

The image adds a visual cue without claiming to be actual album or book artwork. Its information is already supplied by adjacent text, so the sample excludes it from the accessibility tree. This use of the exclusion property does not replace semantic descriptions for meaningful images elsewhere.

Local assets keep the first UI independent of network conditions. They also make a missing-resource defect reproducible through packaging rather than a changing remote URL.

## 9.6 Plan remote artwork as an adapter concern

A future artwork source can return image locations or downloaded files, but should preserve a stable fallback when images are unavailable. A record should remain readable and actionable without its cover.

MAUI supports local, URI, and stream image sources. Their lifetime and failure behaviors differ. A stream source must supply data with a suitable lifetime. A URI source introduces retrieval and caching behavior. Cache policy should reflect expected updates and privacy rather than an assumption that a filename never changes.

The small sample does not implement a remote-image pipeline. Its next version should define a state model for pending, ready, failed, and canceled work; prevent a stale result from appearing on a rebound row; and bound image sizes before repeated decoding consumes memory.

A temporary spinner is not a substitute for that contract. Decide whether every thumbnail needs visible activity or whether a quiet placeholder is sufficient.

## 9.7 Size for the destination

A small thumbnail does not need the same source dimensions as a full-width detail image. Excessive source resolution can consume memory and decoding time without improving the visible result.

Layout constraints and decoding strategy are related but distinct. Setting WidthRequest limits presentation; it does not automatically establish that the application has downloaded or decoded an appropriately sized original.

Measure memory and scrolling with realistic sources when artwork arrives. Inspect portrait and landscape covers, transparent images, and unavailable content. Do not claim a smooth large-media catalog based on a five-row list with one tiny SVG.

AspectFit preserves the image's proportions within its region. Other aspect modes have different cropping behavior. Choose based on whether cropping would remove meaningful artwork.

## 9.8 Reuse detail content without owning navigation

DetailsView receives a DetailViewModel and presents message, title, creator, and description. It is used inside a full detail page and inside the wide catalog pane.

The view does not decide how it was reached. DetailsPage applies its route payload, while the browser updates its inline detail from selection. This division avoids forcing a reusable view to inspect Shell or navigation state.

Do not share one visual instance between two parents. Reuse the view type and presentation contract; each placement creates its own native visual tree.

The model also clears stale content when a lookup fails. Reusing a view without clearing its old creator and description could present the previous record beneath an unavailable message.

### Reuse the detail presentation

`Views/DetailsView.xaml` supplies the same content hierarchy for a full screen and an inline pane:

```xml
<?xml version="1.0" encoding="utf-8" ?>
<ContentView xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:vm=
  "clr-namespace:GnazzosWorld.Core.Presentation;assembly=GnazzosWorld.Core"
             x:Class="GnazzosWorld.App.Views.DetailsView"
             x:DataType="vm:DetailViewModel">
  <ScrollView>
    <VerticalStackLayout Padding="16" Spacing="12">
      <Label Text="{Binding Message}" />
      <Label Text="{Binding Title}" FontSize="26"
             SemanticProperties.HeadingLevel="Level1" />
      <Label Text="{Binding Creator}" />
      <Label Text="{Binding Description}" />
    </VerticalStackLayout>
  </ScrollView>
</ContentView>
```

The full detail page supplies its injected model as the inherited context. The catalog’s inline placement sets `BindingContext="{Binding Detail}"` explicitly. That expression reads the browser model’s `Detail` property and makes it the child view’s context.

`Message` tells the reader to choose an item or explains that content is unavailable. `Title`, `Creator` and `Description` then reflect the resolved record. With no matching record, the model returns empty creator/description values. The reusable visual tree can therefore render a cleared state without page-specific cleanup.

## 9.9 Grow the list without hiding tradeoffs

Collection virtualization helps avoid constructing every native row at once, but does not eliminate costs in data preparation, image handling, or layout complexity. Keep templates modest and test real scrolling.

For later incremental loading, define a cursor or page contract, an in-flight guard, cancellation, end-of-data, and retry behavior. Deduplicate by stable identity and avoid appending stale results after a filter change.

Replacing the whole result set is reasonable for our small local search. An API-backed catalog may need a different update strategy. Make that transition through observable requirements rather than replacing every list with a complex collection abstraction now.

Keep list and detail scrolling independently bounded in the wide layout. Avoid wrapping both in one large scrolling parent that prevents the list from receiving a useful viewport.

## 9.10 Establish a performance baseline before optimizing

Imagine a listener scrolling past Minnesota Bob to find a particular song. A correct result is useful only if the list remains practical to navigate. Begin with a reproducible observation rather than a claim that shared C# or a particular control guarantees speed. This optional measurement lab prepares for Chapter 37.

1. Use a disposable fixture containing 500 valid records with distinct IDs. Keep its generation deterministic, preserve required relationships, and record the fixture revision. Retain the existing placeholder so the first comparison isolates list and layout work.
2. Record the source commit, device, OS, build configuration, text size and profiler. Use a physical device for conclusions about shipping behavior. Label emulator observations separately. Keep the debugger attachment and profiler settings consistent between comparisons.
3. Define the journey: open Discover, scroll to the end and back, select one known ID, return, and repeat five times. Record visible stalls and the instrumented interval you actually measured. An app-side timer cannot prove the time at which a native frame became visible.
4. Capture a memory trace for the repeated journey. Inspect whether retained objects keep increasing and use a suitable profiler to identify owners before calling the change a leak. Allocation, retained managed memory and process memory measure different things.
5. Change one suspected cause, such as unnecessary layout nesting. Repeat the same journey with the same fixture and conditions. Preserve individual observations; do not report the fastest pass as the normal result. Confirm that selection, large text and navigation still work.

| Observation to record | What it can establish |
|---|---|
| Repeated scroll trace and visible stalls | Where to investigate frame or layout work on this device |
| Retained-object trace after repeated navigation | Which objects remain reachable and their ownership paths |
| Source image dimensions and decode activity, once artwork exists | Whether thumbnail work uses excessive source resources |
| Fixture, commit and device details | Whether a later comparison repeats the same experiment |

**Worked interpretation:** If search completes promptly but scrolling still stalls, the search timing does not explain native presentation. Inspect layout, binding and image work in the trace. If an apparent improvement disappears when large text is restored, it has not met the original conditions. Battery, startup and real image-loading measurements receive dedicated treatment in Chapter 37; this list exercise does not establish those results.

## Guided Lab

1. Open `Pages/CatalogPage.xaml` and `Views/CatalogCard.xaml` side by side. Point to the place where the binding type changes from browser model to catalog item.
2. Run Discover, select Kai, then select a song. Check title, creator and selected appearance. Search for a string that matches neither and inspect the empty-result message.
3. Temporarily increase the card’s `Spacing` from 4 to 12. All row text groups should change together. Restore 4.
4. Inspect `Resources/Images/catalog_placeholder.svg` and the project’s MauiImage inclusion. Trace the view’s `.png` reference back to that bundled asset.
5. Follow one item into the full DetailsPage and, at a wide viewport, into the inline DetailsView. Compare the two view instances and their binding contexts.
6. Run the selection tests. Then add two temporary fixture items with distinct IDs and identical titles; verify each opens its own detail record. Remove the temporary fixtures after the exercise.

**Expected result:** each row shows its own data, selection follows the model, and both detail placements render the same record contract.

## Worked Example

Suppose a book and a song are both titled “Northern Lights.” Selecting the second row must use that row’s ID, even though the visible titles match. The collection gives the view model the selected `CatalogItem`; the command snapshots its ID; the destination resolves that ID.

If both rows open the same record, search for a title-based lookup or an index saved before filtering. If the destination is correct but the highlighted row is wrong, inspect visual states and selection binding. If only the image is wrong, inspect its resource or asynchronous image ownership. These symptoms belong to different parts of the row contract.

## Troubleshooting

| Symptom | First correction |
|---|---|
| Every card displays the same data | Remove an unintended card BindingContext override and check template scope. |
| Selection background sticks to an old row | Restore both Normal and Selected visual states and inspect selection binding. |
| The placeholder is missing | Check the MauiImage resource and the generated .png reference. |
| Full details work but the inline pane is blank | Check that the inline view receives the browser’s Detail model. |

## Chapter Summary

Reusable views help a catalog maintain consistent display and semantics, but they must not quietly become a second data layer. A `CollectionView` owns row presentation and selection interaction; search, identity and navigation are handled elsewhere. Explicit template binding types and stable IDs protect the relationship between data and visuals. Placeholder images and deterministic sizing give the current bundled sample predictable behavior. Future remote artwork needs lifetime, cancellation and stale-result policies because recycled views can represent different records over time. The guided lab examines template scope and identity, then separates actual bundled assets from planned network retrieval and pagination. Native scrolling performance and screen-reader behavior remain device-verification tasks.

## Exercises

CatalogCard and DetailsView now provide two purposeful reusable components. Their binding context, selected appearance, and image fallback are explicit. Remote artwork and native catalog pagination remain follow-up implementation work. Chapter 18 later adds service-side paging; that does not by itself implement a paged native collection.

1. Add two synthetic records with equal titles and distinct IDs, then inspect selection.
2. Remove the placeholder resource locally and identify the build/runtime boundary.
3. Design an artwork response arriving after a row has been rebound to another record.
4. Specify pagination behavior when a query changes during an in-flight request.
5. Compare large-text and screen-reader behavior in narrow and wide layouts.

## References and index terms

Images: https://learn.microsoft.com/en-us/dotnet/maui/user-interface/controls/image  
CollectionView: https://learn.microsoft.com/en-us/dotnet/maui/user-interface/controls/collectionview/  
Visual states: https://learn.microsoft.com/en-us/dotnet/maui/user-interface/visual-states

Performance measurement: https://learn.microsoft.com/en-us/dotnet/maui/deployment/performance

Index: DataTemplate; reusable view; binding inheritance; selection; virtualization; image placeholder; MauiImage; stream lifetime; pagination; stable identity.
