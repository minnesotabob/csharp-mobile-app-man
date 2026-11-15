# Chapter 9
# Collections, Images, and Reusable Views

A catalog row appears simple until the same information must work in several places. A title, creator, thumbnail, selection state, and accessible reading order need a consistent relationship. Repeating a visual tree in every page makes that relationship harder to maintain.

This chapter extracts CatalogCard and DetailsView, explains their binding boundaries, and develops a realistic plan for images and larger collections. The implementation still uses five bundled records and a local decorative placeholder. Remote artwork and incremental retrieval are explicitly future extensions.

## What You'll Learn

By the end of this chapter, you will be able to explain why CollectionView owns visual recycling but not search policy; give each DataTemplate the correct binding type; preserve stable item identity across filter changes; choose sensible placeholder and image sizing strategies; and distinguish bundled assets from remote-artwork features not yet implemented.

**Prerequisites:** Complete the preceding chapters and use the matching Part II source revision from `docs/milestones.md`. **Deliverable:** A testable improvement or diagnostic exercise in the Gnazzo's World application, without assuming native-device verification.

### Guided lab: inspect a reusable catalog row

1. Open `CatalogCard`, `DetailsView`, the browser page and their view models at the Part II milestone.
2. Follow one `CatalogItem` from the result collection into the row template. Record which view supplies `BindingContext` and which binding paths are compiled against a declared type.
3. Add two synthetic test records with the same title and different IDs. Verify that selection and navigation rely on ID rather than the row index or visible text.
4. Inspect the bundled placeholder asset and its build action. Identify what appears when actual artwork is absent. Do not assume remote images have already been downloaded.
5. Sketch an asynchronous artwork adapter that receives an item ID and cancellation token. If a reused row now represents another ID when bytes arrive, the older image result must not be displayed there.
6. Increase the catalog size in a disposable fixture. Compare a bounded `CollectionView` with an unbounded nested scrolling layout and note why measurement and virtualization matter.

**Expected result:** The reader can state which reusable views own presentation, where state belongs, and how to prevent recycled visuals from implying the wrong catalog item.

### Troubleshooting the walkthrough

A correct list with incorrect row text often indicates template binding scope. A selected highlight attached to the wrong row suggests visual state has become detached from item identity. Missing artwork may be a missing packaged resource, not a network issue. Blank or sluggish large lists warrant checking their viewport and nested scroll containers before micro-optimizing the data model.

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

## 9.9 Grow the list without hiding tradeoffs

Collection virtualization helps avoid constructing every native row at once, but does not eliminate costs in data preparation, image handling, or layout complexity. Keep templates modest and test real scrolling.

For later incremental loading, define a cursor or page contract, an in-flight guard, cancellation, end-of-data, and retry behavior. Deduplicate by stable identity and avoid appending stale results after a filter change.

Replacing the whole result set is reasonable for our small local search. An API-backed catalog may need a different update strategy. Make that transition through observable requirements rather than replacing every list with a complex collection abstraction now.

Keep list and detail scrolling independently bounded in the wide layout. Avoid wrapping both in one large scrolling parent that prevents the list from receiving a useful viewport.

## Checkpoint and exercises

CatalogCard and DetailsView now provide two purposeful reusable components. Their binding context, selected appearance, and image fallback are explicit. Remote artwork and pagination remain planned implementation work.

1. Add two synthetic records with equal titles and distinct IDs, then inspect selection.
2. Remove the placeholder resource locally and identify the build/runtime boundary.
3. Design an artwork response arriving after a row has been rebound to another record.
4. Specify pagination behavior when a query changes during an in-flight request.
5. Compare large-text and screen-reader behavior in narrow and wide layouts.

## Chapter Summary

Reusable views help a catalog maintain consistent display and semantics, but they must not quietly become a second data layer. A `CollectionView` owns row presentation and selection interaction; search, identity and navigation are handled elsewhere. Explicit template binding types and stable IDs protect the relationship between data and visuals. Placeholder images and deterministic sizing give the current bundled sample predictable behavior. Future remote artwork needs lifetime, cancellation and stale-result policies because recycled views can represent different records over time. The guided lab examines template scope and identity, then separates actual bundled assets from planned network retrieval and pagination. Native scrolling performance and screen-reader behavior remain device-verification tasks.

## References and index terms

Images: https://learn.microsoft.com/en-us/dotnet/maui/user-interface/controls/image  
CollectionView: https://learn.microsoft.com/en-us/dotnet/maui/user-interface/controls/collectionview/  
Visual states: https://learn.microsoft.com/en-us/dotnet/maui/user-interface/visual-states

Index: DataTemplate; reusable view; binding inheritance; selection; virtualization; image placeholder; MauiImage; stream lifetime; pagination; stable identity.
