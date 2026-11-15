# Chapter 13
# Search, Filters, Sorting, and Favorites

A search box is a promise that the application will help someone find the right record. That promise includes more than matching a title. A creator filter should distinguish identities, an empty result should be understandable, and a favorite should still refer to the same item after the title changes.

This chapter extends the existing local browser. We combine text, content kind, creator identity, ordering, and an optional favorites set in one deterministic search policy. We add a small device-local favorites adapter and delay typing updates just long enough to avoid rebuilding on every keystroke.

There is still no remote search service. The cancellation examples control pending input, not an HTTP request. Network timeouts, server paging, and asynchronous remote-result publication belong to the later networking chapters.

## What You'll Learn

At the end of this chapter, you will be able to combine text, content kind, creator ID, sort order and favorites as one search policy; explain why stable ordering and identity matter; distinguish delayed typing from canceled network work; and verify persistence failures without silently losing a person's favorites.

**Prerequisites:** The validated Chapter 12 catalog and companion portable test runner. **Deliverable:** A predictable local discovery experience with a bounded, device-local favorites store.

### Guided lab: prove that filters compose

1. Open the companion catalog search implementation and its discovery tests. Start with the unfiltered five-item sample rather than data from a live provider.
2. Apply a content-kind filter, then add a creator ID. Before running the test, predict whether the second constraint should *replace* or *intersect* the first.
3. Enable favorites-only using an empty set. Verify that the result is empty, not the complete catalog. Then supply one known item's ID and confirm that only eligible favorites remain.
4. Sort two fixture records with the same visible title. Check that their stable IDs break the tie in a repeatable order.
5. In the debounce tests, arrange for an older text update to complete after a newer one. Confirm that the earlier completion cannot overwrite the latest results.
6. Simulate a failed preferences save. Check both the error state and the visible favorites list: the failed operation must not be shown as successfully saved.

**Expected result:** Criteria intersect, ties are deterministic, stale input cannot win, and failed saves preserve visible state. These portable tests do not establish native persistence across an actual app restart.

### Worked reasoning: three different notions of equality

Human text search may ignore case and accents, but creator IDs use ordinal equality. Sort-order ties also depend on IDs, while the favorites store persists IDs rather than labels. If these rules are collapsed into one comparer, a convenient search behavior can accidentally become an identity bug. Write down which comparison a particular operation requires before choosing the API.

## 13.1 Separate search policy from controls

CatalogSearch remains a portable function. It receives the data and criteria and returns a new ordered result array. It does not read a SearchBar, navigate, save preferences, or change selection.

Its expanded signature is:

```csharp
public static IReadOnlyList<CatalogItem> Find(
    IEnumerable<CatalogItem> source,
    string? query,
    ContentKind? kind = null,
    string? creatorId = null,
    CatalogSort sort = CatalogSort.Title,
    IReadOnlySet<string>? favoriteIds = null)
```

This is a method signature excerpt; the implementation is in CatalogSearch.cs. Existing calls that supply only a source, query, and content kind continue to work.

The criteria intersect. A Song filter, a particular CreatorId, a text query, and a favorites set all constrain the same record. We do not concatenate independent result lists and then remove duplicates.

Null has a specific meaning for optional filters. A null CreatorId means all creators. A null favoriteIds means favorites are not restricting the search. An empty favorites set means that the favorites-only view has no matching items.

That last distinction matters. Treating an empty set as “no filter” would show the whole catalog to someone who has not saved any favorites.

## 13.2 Match human text without weakening identity

The original policy trims the query and uses the invariant culture's comparison information with IgnoreCase and IgnoreNonSpace. We retain it so that searching BERET can find Béret violet.

DiscoveryTests also uses a decomposed accented title: the letter e followed by a combining accent. The test checks both an accented query and an unaccented one against that title. This catches a useful Unicode case without rewriting the stored title.

Search still covers Title and Creator. It is a substring search, not tokenization, fuzzy spelling correction, stemming, or a full-text index. Searching “violet beret” does not promise to match the words in a different order.

Creator identity follows a separate rule. CreatorId comparisons use StringComparer.Ordinal. Two people with the same display name remain separate when their IDs differ, and an ID with different capitalization does not silently identify the same creator.

The picker labels come from creator display strings associated with the current catalog. Their selected indices map to a parallel array of IDs; an index is a temporary control position, never the stored identity. A production attribution browser should derive its display projection from the full creator relationships discussed in Chapter 12.

## 13.3 Make ordering repeatable

CatalogSort currently has Title and NewestFirst values. Title ordering retains the previous OrdinalIgnoreCase comparison and an ordinal ID tie-breaker.

NewestFirst applies these keys in order:

| Key | Rule |
|---|---|
| Date known? | Known release dates appear before missing dates |
| Release date | Later dates appear first |
| Title | Equal dates use the title comparison |
| Stable ID | Equal titles use the ordinal ID comparison |

Stable tie-breakers prevent records from jumping when source order changes. Tests reverse equal-title, equal-date records to verify the result.

Missing dates remain missing. The bundled sample still has no verified release dates, so selecting Newest release first does not manufacture a chronology. The policy is exercised with explicit dates in test fixtures.

Title sorting is deterministic rather than fully locale-tailored. Invariant matching and ordinal ordering also need not produce the same grouping. For a larger multilingual catalog, choose and test a documented display-sorting policy separately from identity equality.

Undefined content-kind and sort values throw ArgumentOutOfRangeException. A picker cannot legitimately select them, but portable callers can pass an invalid cast. Reporting an invalid option is clearer than accidentally treating it as the default.

## 13.4 Keep selection consistent with the result set

CatalogBrowserViewModel still owns Items, SelectedItem, and the inline Detail model. Rebuild now passes all active criteria to CatalogSearch, raises result notifications, and reconciles the selection.

If a selected item remains in the result set, the model preserves it. If filtering hides it, selection clears, inline detail clears, and Open selection becomes unavailable.

Favorites make this behavior especially visible. Select a saved item, enable Favorites only, and remove that item from favorites. The result disappears, so its details must disappear too. Leaving a stale detail pane would contradict the current browser state.

The regression test Removing_selected_favorite_from_filtered_results_clears_details verifies that sequence through the actual view model and commands. It checks the result list, selected item, detail state, and navigation command.

Changing the sort order does not create a new identity. The selected record can move within the list while remaining the same selection. Actual native selection restoration and scrolling still need device observation.

## 13.5 Delay typing without delaying every action

The native page now forwards SearchBar text changes through DebouncedQuery. Nonempty input waits 250 milliseconds before assigning the applied Query. A later text change cancels the earlier wait.

The view model itself remains synchronous. Direct assignments to Query rebuild immediately, which keeps portable state tests straightforward. Content-kind, creator, sort, and favorites changes also rebuild immediately using the latest applied query.

For five records, debounce teaches interaction and ownership rather than solving a measured performance problem. This synchronous search needs no worker thread.

The page uses a one-way binding from Query to the SearchBar and an explicit TextChanged handler for incoming input. A two-way binding that immediately changes Query would bypass the intended delay.

Clearing the text is immediate. The clear action also invalidates any earlier pending input, so an old delayed query cannot reappear after the user clears the box.

## 13.6 Cancellation needs an ownership check

DebouncedQuery creates one CancellationTokenSource for each update. Starting another update increments a revision number and requests cancellation of the previous wait.

Before publishing the new text, the operation checks both cancellation and revision:

```csharp
if (!own.IsCancellationRequested && current == revision)
    apply(text ?? "");
```

The checks express ownership: only the newest still-active input can change the applied query. Cancellation is cooperative, so the test delay deliberately ignores its token and completes the older operation last. The old text must still be ignored.

The class accepts an injectable delay function. Tests use manually completed tasks to control ordering without sleeping or relying on a fast CI machine.

A current failure reports a localized search error. An older failure is ignored after newer input supersedes it. Retrying by entering text starts a new operation.

The controller is used from one serialized context, the page's UI thread. Its await preserves that context for the normal delay path. It is not a general concurrent service; callers must not start manipulating its state from unrelated worker threads.

When the page disappears, it cancels pending input and applies the last typed text synchronously to preserve browsing state before navigation. The pending operation cannot later apply its old text. This preserves state within the living page/view model; it does not save the query across process termination.

A future remote search flow will need the same ownership principle around returned results, plus separate loading, timeout, cancellation, and error states. This chapter does not implement that remote contract.

## 13.7 Store IDs rather than catalog copies

IFavoriteStore has two operations:

```csharp
public interface IFavoriteStore
{
    IReadOnlyList<string> Load();
    void Save(IReadOnlyList<string> ids);
}
```

The stored values are item IDs. We do not serialize CatalogItem copies into favorites because those copies would retain outdated titles, descriptions, dates, and creator display strings.

FavoriteCatalog owns the working set and exposes a defensive snapshot for filtering. Editing the returned snapshot cannot alter the service.

Unknown IDs are retained in the saved set. An item may temporarily disappear from the available catalog and return later. Searching the current catalog naturally shows only IDs that resolve there, while preserving the person's saved choice.

This behavior is different from displaying unavailable catalog content. A saved identifier does not create a replacement catalog record, prove access rights, or authorize a download.

The service compares IDs ordinally. The codec removes duplicates and sorts IDs before serialization, making stored examples and comparisons predictable.

## 13.8 Save before changing visible state

Toggling a favorite builds a candidate set, validates it, and asks the store to save it. Only after Save succeeds does FavoriteCatalog replace its working set.

```csharp
var ordered = FavoriteIdCodec.Validate(next);
store.Save(ordered);
ids = new HashSet<string>(
    ordered, StringComparer.Ordinal);
```

If Save throws, the old working set remains available. The view model reports the error and does not rebuild as though the change succeeded.

This ordering prevents a false success in the interface. It does not turn every storage adapter into a transactional database. If an adapter writes data and then throws, the caller may need to reload and reconcile. The small preferences example has no distributed transaction or crash-recovery journal.

Reload also validates a candidate before replacing the old set. A failed reload keeps the last known good in-memory data. An initially failed load leaves editing disabled so that the first tap cannot overwrite unread favorites with an empty set.

The browser remains usable when favorites cannot load. An error explains the problem, and Reload favorites provides an explicit retry. Corrupt saved JSON is not silently treated as an empty collection.

The current app offers no automatic repair or destructive reset for corrupted preferences. During development, inspect the fixture or clear test-app data deliberately. Later storage chapters will add a fuller recovery design.

## 13.9 Use preferences for a bounded local example

PreferencesFavoriteStore is the native adapter. It stores a JSON string under catalog-favorites-v1 using Preferences.Default. The portable tests use MemoryFavoriteStore or a controllable failing store instead of loading native APIs.

FavoriteIdCodec bounds this teaching format to 32 unique IDs, 128 characters per ID, and 4,096 UTF-8 bytes in the serialized payload. A smaller byte limit can reject a set before it reaches the count limit, particularly when JSON escapes characters.

These are application limits for a small example, not universal platform capacity claims. The intent is to keep preferences small and predictable. A substantial catalog history belongs in a storage design that can grow and migrate.

The key includes a format version so that a future reader can distinguish this layout. That naming choice does not implement migration by itself.

Device preferences are not account synchronization. The favorite set belongs to the app's local installation and may be affected by platform backup, restore, or app-data removal. It is not encrypted customer data or a replacement for authenticated ownership.

The registered FavoriteCatalog is shared within the current single-window app. The implementation does not broadcast changes across multiple independent browser view models. Multiwindow and cross-account behavior remain later work.

## 13.10 Expose filters without filling the screen

The page places a Filters button beside the search box. It reveals a bounded scrolling panel with content type, creator, sort order, Favorites only, and Reload favorites.

Keeping the additional controls collapsible leaves room for the collection in the normal browsing state. The panel's maximum height is a starting layout choice, not a guarantee that every keyboard and text-size combination works well.

Save favorite and Remove favorite describe the action on the selected record. Their command is disabled when nothing is selected or an initial favorites load has failed.

All new labels and error messages have neutral English and Spanish resources. Their presence in resources does not prove that translated controls fit or that a screen reader announces every state change clearly.

Device checks must cover expanded and collapsed filters, keyboard visibility, landscape height, large text, focus order, and the meaning of the selected favorite action. Particular attention is needed where two actions share a row.

## 13.11 Test observable behavior

DiscoveryTests covers Unicode matching, intersected filters, stable ordering, favorites persistence contracts, invalid data, storage failures, and retained identities.

Controlled-delay tests verify latest-input ownership, immediate clearing, page cancellation, and error reporting. They complete operations in deliberate order without relying on elapsed time.

The portable store-recreation test demonstrates the contract for loading saved IDs. It does not demonstrate that Android or iOS persists Preferences through an actual process restart. That behavior needs a native device check.

Run the complete portable suite using the README commands. The Android build checks XAML and native adapter compilation separately. Neither check supplies an iPhone build or a successful app-launch observation.

## 13.12 Hands-on exercise: keep a favorite through change

Use fictitious data in a development checkout.

1. Run the portable tests and locate the restart-and-rename favorites case.
2. Add a test record whose title changes while its ID remains the same. Confirm that favorites filtering still finds the renamed record.
3. Add another record with the same title and a different ID. Confirm that saving the original does not save both.
4. Create test records with two equal release dates and one missing date. Reverse the source order and confirm the sorted ID sequence stays the same.
5. In the manual-delay test, complete the second input before the first. Confirm that only the second text is applied.
6. Use the failing test store to reject Save. Confirm that visible favorites remain unchanged and the error appears.

For the native exercise, launch a development build, save one item, close and restart the app, and open Favorites only. Record the source revision, platform, device, and result. Until that exercise is actually performed, leave its verification status pending.

Also remove the selected favorite while Favorites only is active. Confirm that details and navigation no longer refer to the removed result. Repeat with expanded filters, the keyboard open, and increased text size.

## 13.13 Review questions

- Why is an empty favorites set different from a null favorites filter?
- Which search comparisons are intended for people, and which are intended for identity?
- What breaks a tie when two items share a title and release date?
- Why check a revision even after requesting cancellation?
- When is it safe to replace the in-memory favorites set?
- What does the portable restart test fail to prove about native persistence?

Chapter 14 develops content details, reading samples, and external links. It will use these stable selections and identities while making the next boundary explicit: a catalog record is not the content itself.

## Chapter Summary

Search is a coordinated policy, not a stack of unrelated UI filters. This chapter combines text, kind, creator identity, ordering, and optional favorites restrictions while preserving deterministic results. It treats human-readable text differently from stable IDs and gives empty favorites a precise meaning. Input debouncing improves the typing experience, but a revision check is still necessary to reject stale completion. Device-local preferences are a small teaching store, not synchronized account state, and failed writes must not alter the visible favorites set. The guided lab makes each distinction observable with portable tests and deliberate failures. Full native restart, accessibility, and keyboard behavior still require device verification.

## Official references

- Microsoft Learn, Preferences: https://learn.microsoft.com/en-us/dotnet/maui/platform-integration/storage/preferences
- Microsoft Learn, Cancellation in managed threads: https://learn.microsoft.com/en-us/dotnet/standard/threading/cancellation-in-managed-threads
- Microsoft Learn, Task.Delay: https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.delay

Editorial index terms: search; filters; Unicode; combining character; sorting; release date; stable ordering; creator identity; favorites; preferences; JSON; debouncing; cancellation; revision; stale completion; stream-independent tests; persistence boundary; storage failure.
