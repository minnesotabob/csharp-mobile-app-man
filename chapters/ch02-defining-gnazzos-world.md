# Chapter 2
# Defining Gnazzo's World

An application becomes easier to build when requirements describe actions and outcomes rather than a collection of attractive screens. “Show the music” is an idea. “Let a visitor find a song by title or artist, inspect its details, and choose an available destination without signing in” is a journey we can design and verify.

The source website presents books, five music identities, a developing podcast area, and a custom-song service. Some content is public. Some state belongs to an individual. Some actions involve external providers. Orders and delivered files need ownership checks and trustworthy status. This chapter turns those differences into a content model, navigation map, feature progression, and acceptance scenarios.

## 2.1 Start with the source

The archive contains HTML, JavaScript, CSS, images, and service links. Its home page introduces the creator and featured works. The artist pages cover Minnesota Bob, Travis Rollins Jr., DGreatGnazzini, Conan Jahan III, and Reverend Paul. The book catalog provides descriptions and purchase formats. The podcast page is a placeholder. Song for You supplies a detailed customization and ordering form.

This inventory describes a snapshot, not a permanent production contract. A displayed song count may differ from dynamically loaded results. External pages and prices can change. We must distinguish imported content from the application's own stable records.

The first bundled catalog therefore contains a few representative entries. Real titles appear as metadata, while a fictitious podcast episode is clearly labeled. It includes neither complete book text nor music files. Readers can run the example without an account or live service, and cannot mistake an external streaming link for distributable audio.

## 2.2 Define people and goals

The app serves three contexts: a visitor discovers work, a returning reader/listener saves preferences and progress, and a custom-song customer submits and follows a request. These can be the same person at different times; they need not become separate account types.

A person browsing anonymously should be able to continue into an account-dependent action without losing context. Conversely, canceling authentication should not prevent continued public browsing.

| Context | Goal | Failure to handle |
|---|---|---|
| Public visitor | Find and inspect content | Missing metadata or unavailable destination |
| Returning reader/listener | Resume a personal experience | Offline state, session expiry, device change |
| Song customer | Submit and follow a request | Lost draft, duplicate submission, wrong-account access |

Staff-facing administration is not the primary mobile application. Controlled fixtures or a small administrative service can move teaching orders through their states. Avoid adding a full second product merely because a chapter needs a delivered order.

## 2.3 Define complete journeys

The catalog journey begins at Home or a category. Search matches titles and creators; filters narrow results; a detail view presents relevant actions. An empty result is valid behavior, distinct from a failed catalog load.

Saved content begins locally, then becomes account-linked. A favorite should survive a restart. Before synchronization, decide how anonymous favorites meet an existing account collection. A merge policy should be intentional rather than an accidental overwrite.

The media journey uses authorized sample files. Users play, pause, seek, and return to a position. Background playback and system controls follow the basic player. Downloads add storage and authorization responsibilities rather than simply another button.

The customer journey is longer: choose length and style, describe an occasion, save a draft, review a quote, submit once, track status, request an allowed revision, and retrieve delivery. Persistence, pricing, payment verification, and file access are different boundaries even if the interface presents a smooth sequence.

## 2.4 Map navigation without overbuilding the first screen

A plausible finished structure is Home, Discover, Library, and Song for You, with account/preferences consistently reachable. Discover contains search and categories. Library contains favorites, bookmarks, and downloads. This information architecture does not require implementing every tab immediately.

The first screen is a heading, search field, and collection. It establishes a traceable data flow. The navigation chapter later develops routes and the full structure.

For each destination, specify entry paths, data, visible states, and Back behavior. A shared content link may open without a prior in-app list. A protected order link may require sign-in before continuation.

| Destination | Access | Information |
|---|---|---|
| Home | Public | Featured content and category entry points |
| Catalog/detail | Public | Titles, creators, descriptions, links |
| Library | Personal/local, later synchronized | Favorites, bookmarks, downloads |
| Request builder | Local draft, then personal submission | Customer selections and story |
| Order/delivery | Account-protected | Status, revisions, files |
| Preferences | Personal | Session, MFA entry points, choices |

## 2.5 Establish stable identity

CatalogItem separates Id from Title because titles can be corrected, translated, or reused. Multiple editions or releases can also represent related works. A saved favorite must continue to identify the intended record after an editorial correction.

Readable fixture IDs such as book-kai-01 are suitable for the first milestone. A production ingestion process maps internal records to external identifiers. Our application ID is not automatically a Spotify track ID, Apple catalog ID, or Amazon identifier.

The first CatalogItem is a compact browsing projection. It does not claim every domain object will permanently have identical structure. Books can acquire edition/format records; episodes can belong to shows; songs can have multiple releases. Expand models when features need that information.

Avoid both extremes: twenty unused fields copied from a provider response, and an opaque JSON blob interpreted differently by every screen. A clear projection gives the interface a small, stable contract.

## 2.6 Separate public content and personal state

A favorite references a catalog item rather than duplicating all its metadata. A bookmark stores position for a particular work. An order retains an agreed snapshot, not a reference to a price table that may change tomorrow.

Account isolation applies on the device and server. Endpoints verify ownership. Local personal caches are scoped to an account. Sign-out, account switching, export, and deletion each require defined behavior.

MFA also has a lifecycle: enrollment, normal challenge, replacement factors, and recovery after device loss. We will choose a managed provider against those requirements rather than only the convenience of its first sign-in example.

An authentication cancellation must preserve the intended public journey. For a personal action, explain why authentication is needed and retain the action's context. These decisions become acceptance tests later.

## 2.7 Keep commercial rules trustworthy

The archived price table is versioned teaching data. Its three-minute vocal option is 179 dollars. Discounts apply separately to the second and third songs. Decimal arithmetic and tests express those rules without making the app authoritative.

A production server validates its own quote and stores the reviewed price snapshot. Client calculations improve responsiveness but do not determine what will be charged.

Likewise, returning from checkout does not prove payment. Trusted, verified sandbox events establish state in the payment chapter, including duplicates and delays. Before public release, the actual storefront requirements must be reviewed for this mix of content and custom services.

These boundaries allow a useful form to develop before live commerce exists. A draft can be saved and validated while checkout remains a clearly labeled future capability.

## 2.8 Write acceptance scenarios

Acceptance scenarios describe observable behavior without prescribing every class.

For search: given the bundled catalog, searching BERET with surrounding spaces returns Béret violet. A nonmatching query displays a helpful empty state. Clearing the query restores the list.

For draft recovery: given a completed and saved form step, restarting the process recovers the saved values. The requirement says when persistence occurs; “never lose anything” cannot replace a save strategy.

For ownership: given two customers, a request for another customer's order is denied by the server. Checking that the wrong item is absent from a client list is insufficient.

For discounts: three same-length/style songs receive factors of 1.0, 0.9, and 0.8. That is different from applying twenty percent to the entire order.

For uncertain submission: if the server accepted an operation but its response was lost, repeating the same operation identity returns the original result rather than creating another order.

## 2.9 Sequence the work by dependency

Bundled content teaches UI before networking. Local storage prepares offline behavior. A small API establishes contracts before accounts protect personal data. Authentication precedes customer orders. Device integration grows around a testable core.

Preparatory fixtures must remain labeled. A fake user context is not authentication. A fictitious episode is not a published show. A sandbox payment is not live commerce. A chapter should identify both the capability it adds and what remains unverified.

Comprehensiveness does not mean adding an unrelated social network, subscription platform, or enterprise administration suite. Each feature should advance the intended app or demonstrate a mobile capability with a credible use.

File/photo selection fits optional request attachments. Location-based song discovery can be an extension that teaches location without making it necessary for browsing. Watches remain a bounded companion discussion.

## Summary and exercises

We have a source inventory, user contexts, navigation map, identity strategy, and acceptance scenarios. The immediate milestone is small, while the finished application's service and device boundaries are explicit.

1. Write a scenario for preserving a draft when the user cancels sign-in.
2. Give two title changes that should not change a record's ID.
3. Specify how server and local storage prevent access to a previous account's delivered file.
4. Choose one feature to defer and explain how the app remains useful.

## Companion references and index terms

See src/GnazzosWorld.Core/Data/catalog.json and docs/acceptance-scenarios.md. Index: acceptance criteria; stable identifiers; projection; anonymous browsing; account isolation; quote snapshot; idempotency; sample data.
