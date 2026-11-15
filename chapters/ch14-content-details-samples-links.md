# Chapter 14
# Content Details, Reading Samples, and External Links

Selecting a title is the start of a decision. A reader wants to know which edition a book represents. A listener wants to distinguish a song listing from playable audio. Someone opening a link wants a useful next step if the operating system cannot complete the handoff.

Our existing detail page establishes identity: a stable catalog ID resolves to a record. This chapter develops the experience around that identity. We display the optional metadata introduced in Chapter 12, add a short bundled reading sample, and open reviewed website destinations through a native adapter. The same reusable detail view serves the dedicated page and the wide browser layout.

The result remains a catalog application. It does not implement an EPUB reader, stream songs, establish purchase rights, or confirm that a website is reachable. Keeping those responsibilities explicit lets us build a useful detail journey without hiding unfinished systems behind an impressive button.

## 14.1 Begin with the reader's questions

A detail view answers three questions: What is this record? What information is known about it? What can I do here?

The first question uses the title, creator display name, description, and content kind. The second uses edition, release date, duration, advisory, and availability. The third uses capabilities derived from the current record, rather than a button that always appears for every item.

| Record state | Detail behavior |
|---|---|
| Known book with a listed sample | Show metadata and the credited reading sample |
| Listed item with a reviewed website URL | Show the destination host and Open website |
| Known unavailable item | Keep its descriptive metadata; hide the sample and website action |
| Known item with unknown availability | Explain that availability is unconfirmed; offer no content action |
| Missing or invalid ID | Clear old content and explain that the record was not found |

Availability is catalog metadata, not a real-time health probe. Listed means that our current catalog includes the record. It does not guarantee that a retailer has stock, a streaming account has access, or a link will return a successful page.

The unavailable demonstration podcast illustrates the distinction. Its title and description remain useful even though no audio is included. A Play button would promise a capability this milestone does not provide.

## 14.2 Resolve identity before projecting presentation

DetailViewModel still accepts the current catalog and resolves the supplied ID through RoutePayload validation. Navigation passes the identifier, not serialized content or an arbitrary website URL.

The dedicated DetailsPage receives its ID through IQueryAttributable. The inline view receives its selected record through CatalogBrowserViewModel. Both paths call the same Load operation and use the same projection.

This keeps policy consistent. A book cannot have a reading sample in the tablet pane while appearing to have an unrelated playback action in the phone page. Fixing the shared detail model corrects both presentations.

Load also starts a new revision of detail state. Even loading the same ID again represents a new ownership boundary for an operation already in progress. Clear uses the same invalidation mechanism.

```csharp
private void ResetActions()
{
    revision++;
    LinkMessage = "";
    Notify(null);
    OpenExternal.Refresh();
}
```

Notify(null) tells bindings that every derived value may have changed. Refresh raises the command's availability notification. The two calls address different consumers: labels observe properties, while buttons also observe command state.

The catalog is still an in-memory snapshot. If a later repository replaces records asynchronously, it must arrange for the detail model to refresh or report removal. This chapter does not add a live subscription merely by storing an ID.

## 14.3 Display metadata without inventing it

The model exposes localized content-kind, availability, and advisory strings. Book-only edition information remains blank when absent. A known release date uses the current display culture; an unknown date stays blank rather than becoming today's date.

Audio duration uses a consistent hours:minutes:seconds form. A 185-second test fixture displays 00:03:05. The property is a duration, not a time of day or a progress position. A future player will supply its own current position and actual media duration.

The sample projection intentionally stays small. Missing optional fields currently bind to empty strings, which can leave modest gaps between labels. A more polished metadata grid could add visibility properties and explicit localized field captions. That refinement should follow native large-text and screen-reader observation; it must not introduce fabricated values just to fill space.

The creator line displays the catalog's primary creator string. CreatorId continues to distinguish identity in discovery filters. This milestone does not add a separate artist biography route, infer a person's biography from a stage name, or replace the related creator records established in Chapter 12. A future artist page should resolve those records by ID and reuse their relationship rules.

Unknown advisories remain visibly unknown for audio. An absent explicit-content flag is not evidence that a recording is clean. Books omit that audio-oriented label entirely in this small presentation.

## 14.4 Give a reading sample a clear content contract

A reading sample has its own heading, text, and credit:

```csharp
public sealed record ReadingSample(
    string Heading,
    string Text,
    string Credit);
```

CatalogItem receives an optional Sample parameter after its existing optional values. Existing construction remains valid. CatalogLoader validates a supplied sample: it must belong to a book, its three values must contain text, and its text cannot exceed 20,000 characters.

That ceiling is an application limit for this bundled example. It is not an ebook standard or a recommendation to put an entire manuscript inside catalog JSON. The loader rejects invalid samples rather than displaying an incomplete contract.

The fixture attached to Mastering Modern C# is newly written teaching text about application states. Its heading says Demonstration reading sample, and its credit explicitly says that it is not an excerpt from the published book. This avoids presenting invented prose as a quotation from an existing edition.

For a genuine production excerpt, replace the fixture with approved text and accurate attribution. Record the source edition and permission in the project's asset provenance. A nonempty Credit field cannot prove permission; it only ensures that this required presentation field was supplied.

Text and catalog metadata also have different update needs. A corrected description might ship with a catalog refresh, while a reading sample may need an edition identifier and a longer retention policy. Later data chapters can separate those resources when the small bundled format stops serving the application.

## 14.5 Render plain text as plain text

DetailsView displays the sample in ordinary Label controls inside its existing ScrollView. The sample heading is marked as a level-two semantic heading. Credit precedes the body so that someone encountering the fixture understands what it represents before reading it.

Paragraph breaks are retained in the string. We do not insert the sample into HTML or a WebView. A string containing angle brackets is text for this experience, not executable markup or an embedded website.

```xml
<VerticalStackLayout IsVisible="{Binding HasSample}"
                     Spacing="10">
  <Label Text="{Binding SampleHeading}" FontSize="20"
         SemanticProperties.HeadingLevel="Level2" />
  <Label Text="{Binding SampleCredit}" />
  <Label Text="{Binding SampleText}" />
</VerticalStackLayout>
```

HasSample requires a book, Listed availability, and an actual sample object. When selection changes or a record disappears, the derived heading, body, and credit become empty as well as hidden. Clearing the backing values avoids leaving stale content in another consumer of those properties.

This deliberately limited reader has no page numbering, bookmarks, text-size preference, annotation system, EPUB navigation, or rights management. Native text scaling and scrolling remain relevant, but their actual behavior must be checked on devices.

For lengthy samples, consider a dedicated reading route that preserves position and offers reader controls. Do not keep expanding the catalog detail page until its primary actions require several minutes of scrolling to reach.

## 14.6 Treat a website destination as a reviewed capability

The import already rejects non-HTTPS external URLs. The action adds a narrower destination policy. ContentLinks currently permits only johngnazzo.com and www.johngnazzo.com, over HTTPS on port 443, with no user information in the URL.

The policy compares the parsed host exactly. It does not accept a URL because the raw text contains the author's domain. For example, johngnazzo.com.evil.test is a different host. A path containing the text johngnazzo.com does not make another site's URL acceptable either.

```csharp
public static bool IsAllowed(Uri? uri) => uri is
    { IsAbsoluteUri: true, Scheme: "https", Port: 443 }
    && string.IsNullOrEmpty(uri.UserInfo)
    && (uri.IdnHost.Equals("johngnazzo.com",
            StringComparison.OrdinalIgnoreCase)
        || uri.IdnHost.Equals("www.johngnazzo.com",
            StringComparison.OrdinalIgnoreCase));
```

This is intentionally an explicit teaching allowlist. Adding Amazon, Spotify, or another service means reviewing and adding its actual destination hosts and tests. It does not mean accepting arbitrary schemes or any host that looks familiar.

HasExternalLink combines destination approval with Listed availability. The view shows the parsed host above a button labeled Open website. Current links lead to website catalog pages; the label does not claim to buy a book or play a specific track.

A host allowlist constrains the initial handoff. It does not control a site's redirects, certify all pages on the host, or prove a business transaction. Do not attach tokens, customer details, or private delivery credentials to these public catalog URLs.

## 14.7 Keep native browser APIs behind an interface

The portable project declares IExternalBrowser with one method:

```csharp
public interface IExternalBrowser
{
    Task<bool> OpenAsync(Uri uri);
}
```

Its Boolean describes the initial handoff. The native ExternalBrowser adapter checks ContentLinks again, then calls Browser.Default.OpenAsync with BrowserLaunchMode.External. This requests the external browser experience supported by the platform.

The second check protects the adapter from direct callers that bypass the view model. It also keeps the adapter's contract understandable when another page eventually uses it.

MauiProgram registers IExternalBrowser as a singleton and supplies it to the detail and browser view models. The browser model passes that dependency to its inline DetailViewModel. Tests supply a fake adapter with controlled results instead of opening real windows.

The optional null dependency preserves earlier portable callers. Their detail metadata still works, while the website command remains disabled. In the running application, registration is required for an enabled action; forgetting it should be caught during the native smoke test.

Browser.OpenAsync completes around launching, not around someone finishing a visit. A true result does not prove that the remote page loaded, a user signed in, a song played, or an order was paid. The message therefore says Handed off to the browser.

## 14.8 Distinguish failure, cancellation, and return

A false browser result produces a retryable opening error. An exception produces the same safe, localized message. Raw exception text and full URLs do not appear in the interface.

An OperationCanceledException produces a neutral cancellation message. The portable test exercises that contract explicitly. Actual platform behavior varies: the native browser API does not provide this application with a universal event meaning that the user canceled or closed an external browser.

Pressing Back after visiting a website is an ordinary return. It does not undo the handoff and should not manufacture a failure. Likewise, opening a page successfully and later losing network connectivity is beyond what this adapter can observe.

The existing AsyncCommand prevents repeated taps from launching overlapping operations through the same command. Its finally block reenables the action after completion, including failure. A retry starts with a cleared message and uses the currently selected URL.

There is no automatic browser retry. Opening another application is a visible user action, so repeated attempts belong to explicit taps.

## 14.9 Prevent old completions from changing new details

Suppose the wide layout shows one book and starts a browser handoff. Before that task completes, the user selects another record. A late failure must not appear under the second book as though its link had failed.

The detail model captures its revision and URL before awaiting. It handles the result or exception, then publishes only if that revision still owns the view:

```csharp
var own = revision;
var url = Item!.ExternalUrl!;
// Await the adapter and produce a localized result.
if (own != revision) return;
LinkMessage = result;
Notify(nameof(LinkMessage));
```

The complete method in DetailViewModel.cs catches exceptions before the ownership check. This matters: an old exception is as stale as an old successful result. Handling all failures in a generic command callback without ownership information would let an earlier request overwrite the current record's message.

Changing selection cannot retract a handoff already sent to the operating system. The revision prevents stale presentation; it does not cancel the external browser. This is the same ownership principle introduced for search in Chapter 13, applied to a different boundary.

The model assumes serialized UI use. Load, Clear, and command execution occur on the UI context in the app. This revision counter is not a synchronization primitive for callers manipulating the model from unrelated threads.

## 14.10 Test journeys rather than platform guesses

DetailJourneyTests uses a fake browser that records destinations and returns controlled tasks. It verifies allowed hosts, wrong schemes, user information, deceptive domains, relative URLs, and nonstandard ports.

Journey tests also verify missing-record cleanup, unavailable content, audio metadata without a sample, successful and failed handoffs, cancellation and retry, repeated taps, selection changes during a pending operation, and Clear invalidation. Both late success and late exception cases are included.

The controlled task tests do not depend on elapsed time. They start an opening, change detail state, and then complete the old operation deliberately. The assertions inspect the current title, message, and command availability.

Import tests reject samples attached to songs and samples with missing required text. A fixture-provenance test ensures that the bundled demonstration remains labeled as an invented teaching sample rather than a published excerpt.

Run the full portable suite using the repository's documented executable xUnit commands. Compile Android separately to check native API and XAML compatibility. Only an actual launch can establish how the operating system handles the browser transition and return.

## 14.11 Hands-on exercise: return without losing context

Start from a known working source revision and use demonstration data.

1. Run the portable tests. Locate the case that changes the selected record before an opening completes.
2. Change the fake adapter to fail the old opening. Confirm that the new record's message remains empty.
3. Give two records different reviewed website paths. Verify that each action sends its own captured URL to the fake browser.
4. Mark the book unavailable. Confirm that its title remains visible while sample and link capabilities disappear.
5. Remove the sample credit from a JSON fixture. Confirm that import rejects the fixture instead of presenting unattributed text.
6. Add another destination host only after writing both an accepted-host case and a deceptive-subdomain rejection case.

On Android, open a book detail page, launch the website, and return with the system navigation. Record whether the same detail remains visible. Repeat in the wide layout, with large text, in Spanish, and after backgrounding the app. Check the unavailable podcast and an unknown ID as well as the happy path.

For accessibility, follow focus from the title through metadata, sample heading, credit, body, destination, and button. Check whether the result message is discoverable after a failed opening; a bound Label alone does not prove a screen reader announces changes. Record any announcement or focus improvement needed before claiming accessibility completion.

## 14.12 Review questions

- Why can a listed song have a website link without having playable audio?
- What is the difference between validating an HTTPS URL and approving its destination?
- Why keep the sample's provenance visible before its body text?
- What does a successful browser result prove, and what remains unknown?
- Why must stale exceptions pass the same ownership check as stale successes?
- Which detail behaviors require device observation even when all portable tests pass?

Chapter 15 moves from discovering content to entering a custom-song request. The form will need a richer state model because a customer's unfinished input must survive validation and navigation rather than being replaced by another catalog selection.

## Official references

- Microsoft Learn, Browser API and launch modes: https://learn.microsoft.com/en-us/dotnet/maui/platform-integration/appmodel/open-browser
- Microsoft Learn, IBrowser.OpenAsync return contract: https://learn.microsoft.com/en-us/dotnet/api/microsoft.maui.applicationmodel.ibrowser.openasync
- Microsoft Learn, Uri class: https://learn.microsoft.com/en-us/dotnet/api/system.uri
- Microsoft Learn, Accessibility: https://learn.microsoft.com/en-us/dotnet/maui/fundamentals/accessibility

Editorial index terms: content details; reading samples; attribution; fixture provenance; availability; metadata; external browser; HTTPS; URI host; allowlist; dependency injection; command; cancellation; stale completion; revision; native handoff; plain text; semantic headings; accessibility; ebook boundary; playback boundary.
