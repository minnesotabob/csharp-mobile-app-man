# Chapter 12
# Modeling Books, Artists, Songs, and Episodes

A catalog can look correct while carrying unreliable meaning. A song title might identify two recordings. A book may have several editions. A missing content advisory may be mistaken for a clean rating. An artist can change a display name without becoming a different artist.

The first eleven chapters needed a small list that could drive a native interface. This chapter gives that list a more explicit contract. We retain the five bundled records, add a related creator fixture, and validate both as one snapshot. The application still works without a network connection or account.

The files for this chapter are in src/GnazzosWorld.Core/Catalog, with fixtures under Data and regression cases in CatalogMetadataTests.cs. The changes are a first catalog model, not an import of every book, recording, artist, or podcast on the author's website.

## What You'll Learn

By the end of this chapter, you will be able to:

- distinguish a catalog item from its creator, edition, and delivery service;
- design stable identifiers that survive title and display-name changes;
- represent optional dates and content advisories without inventing facts;
- validate a whole bundled catalog, including relationships between files;
- test both successful imports and deliberately malformed fixtures.

**Prerequisites:** Complete Chapters 1–11 and have the companion portable test project available. **Deliverable:** A validated local catalog snapshot whose records and creator references remain stable as display metadata changes.

### Guided lab: trace one catalog record

1. Open the companion solution and locate the catalog model, bundled JSON files, loader, and metadata tests. Use the Chapter 12 source milestone documented in the companion repository rather than assuming a later checkout is identical.
2. Choose the bundled song *Northern Lights*. Record its item ID, creator ID, content kind, and optional fields. Do not infer that missing metadata means a negative answer.
3. Follow the creator ID into the bundled creator fixture. Confirm that the relationship is made by ID rather than the artist's display name.
4. Run the portable test suite using the instructions in the companion README. Note the actual result before changing fixture data.
5. Temporarily replace the song's creator ID with an unknown ID and run the relevant validation tests. Expect the snapshot to be rejected. Restore the original ID and run the tests again.

**Expected result:** A correctly linked snapshot loads; an unknown creator reference causes validation failure. This is a reproducible contract exercise, not a claim that a native device has been tested.

### Why the relationship matters

Imagine changing the artist's display name on a promotional page. If the application used display text as a foreign key, every linked song would need to change at the same moment. By using an immutable creator ID, the content model can change presentation independently of identity. The same reasoning applies to book editions, revised titles, and external streaming-provider metadata.

## 12.1 Decide what one record represents

Our ContentKind enum has three values: Book, Song, and Podcast. In this small catalog, a Podcast item represents an episode. A future show directory needs a separate show identity and an episode-to-show relationship. We do not overload one record with both meanings.

An artist is also a different entity from a song. The artist has a name and identity that can be reused across recordings. For that reason, this chapter introduces CatalogCreator rather than adding Artist as a fourth selectable content kind.

The model also includes authors and hosts. That makes one relationship useful across the three existing content kinds:

| Catalog record | Related creator in this fixture | Meaning |
|---|---|---|
| Northern Lights | artist-minnesota-bob | Artist associated with the song |
| Béret violet | artist-minnesota-bob | The same artist, a different item |
| Kai the Ninja | author-john-gnazzo | Author associated with the book |
| Mastering Modern C# | author-john-gnazzo | The same author, a different book |
| Inside the Studio — Demo Episode | host-demo | A fictitious host used only for development |

This is a single primary-creator relationship. It does not represent coauthors, duet credits, composers, publishers, contributors, or ownership. Those requirements would need explicit relationship records rather than a comma-separated identity field.

## 12.2 Keep identity independent of display text

CatalogItem already has a stable Id. Routes and selection use that identifier rather than Title. We apply the same rule to creators:

```csharp
public enum CreatorKind { Artist, Author, Host }

public sealed record CatalogCreator(
    [property: JsonRequired] string Id,
    [property: JsonRequired] string Name,
    [property: JsonRequired] CreatorKind Kind);
```

The name Minnesota Bob is readable text. The ID artist-minnesota-bob is an opaque application identity. Its spelling resembles a name for convenient fixtures, but the program must not generate a new ID every time someone edits the name.

Suppose an editor changes capitalization or adds an accent. Existing songs should retain their relationship to the creator. The regression test Renaming_display_text_preserves_identity demonstrates this with a record copy whose Name changes while its Id remains the same.

Do not use a list index as an identity. Inserting another record at the beginning of a JSON array would then change every later link. An external provider's identifier can be stored as provider metadata later; it does not need to become our only internal identity.

Identifiers are compared with StringComparer.Ordinal. That choice makes them case-sensitive and culture-independent. User searches follow a different policy because people reasonably expect accent-insensitive matching. Identity equality and text discovery solve different problems.

## 12.3 Add optional metadata without guessing

The existing positional constructor remains usable. Its original required parameters are unchanged, and the additional parameters have defaults:

```csharp
Uri? ExternalUrl = null,
string? CreatorId = null,
DateOnly? ReleaseDate = null,
string? Edition = null,
int? DurationSeconds = null,
ContentAvailability Availability = ContentAvailability.Unknown,
ContentAdvisory Advisory = ContentAdvisory.Unknown
```

These declarations are the optional tail of CatalogItem's constructor. They are not a complete stand-alone record declaration. Open CatalogItem.cs to inspect the entire type.

ReleaseDate uses DateOnly because an editorial release date is a calendar value. It is not a timestamp showing the instant an API response arrived. If a later provider offers territory-specific release times, preserve that distinct meaning in a separate field.

DurationSeconds is an integer rather than formatted text such as “3:07.” Presentation can convert seconds into a localized duration. The fixture does not yet contain verified recording lengths, so it leaves durations absent.

Edition is available for books. Our sample labels Kai as Book One, preserving the source description without inventing an ISBN or publication date. The value is display metadata; it is not an identifier linking every edition of a work.

Unknown metadata remains absent or explicitly Unknown. We do not insert today's date to satisfy a sorting control, use zero as an unknown duration, or label a song Clean because its advisory is missing.

## 12.4 Give availability and advisories distinct meanings

ContentAvailability has Unknown, Listed, and Unavailable values. Listed means that this catalog includes a listing. It does not mean that an audio file is downloadable, an ebook is owned, a customer has purchased access, or an external provider will serve the content in every country.

The four real-title sample records use Listed. The fictitious podcast episode uses Unavailable because the development fixture includes no media. Existing native detail views still show their original text; this commit does not add an availability badge or prevent an external launch.

ContentAdvisory has Unknown, Clean, and Explicit values. Those labels describe editorial metadata, not permission to play content. All five bundled records retain Unknown because this exercise does not establish verified ratings.

These enums are independent. An unavailable item could have a known advisory, and a listed item could have an unknown advisory. A single boolean named IsAvailableAndSafe would lose both distinctions.

In Chapter 14, the detail experience can translate these values into useful text and actions. For now, the importer and tests establish what the values mean before controls depend on them.

## 12.5 Validate syntax and meaning separately

System.Text.Json reads JSON syntax and converts values into .NET types. Required-property annotations establish presence requirements. They do not establish that a present string contains useful text.

For example, a record with a missing Title property fails deserialization because of JsonRequired. A record whose Title is a single space reaches our validation and fails with InvalidDataException. Both reject the input, but they fail at different boundaries.

CatalogLoader continues to reject duplicate item IDs, undefined content kinds, empty required text, and non-HTTPS external links. It now rejects additional contradictions:

| Input | Reason for rejection |
|---|---|
| CreatorId containing only spaces | A supplied reference must be usable |
| Edition containing only spaces | A supplied edition must contain text |
| Edition on a Song or Podcast | This model reserves editions for books |
| DurationSeconds of zero or less | Unknown duration must be absent |
| DurationSeconds on a Book | This model treats duration as audio metadata |
| Undefined advisory or availability number | The application has no meaning for that value |

Unknown enum names and malformed dates fail during deserialization. Defined enum values that violate our domain rules fail in validation. A broad catch that returns an empty list for either failure would hide a broken bundled fixture.

These rules intentionally describe the current catalog. If audiobooks become a supported product, we should revisit the model and tests rather than placing audio duration on every book without explaining its meaning.

The generic JsonStringEnumConverter instances make fixture values readable. The loader still calls Enum.IsDefined because numeric enum input can otherwise deserialize to a value the application does not recognize.

## 12.6 Load related files as a coherent snapshot

Data/catalog.json holds the content items. Data/creators.json holds three creator records. The project embeds both with an EmbeddedResource include for Data/*.json.

CatalogSnapshot.Load accepts two streams and returns Items and Creators together. It first uses CatalogLoader for the item rules. It then validates creator metadata and duplicate creator IDs. Finally, every supplied CreatorId must resolve:

```csharp
foreach (var item in items)
    if (item.CreatorId is { } id && !ids.Contains(id))
        throw new InvalidDataException(
            $"Unknown creator ID: {id}");
```

A missing relationship rejects the snapshot. We do not quietly delete the song, attach it to the first artist, or publish half the import.

Legacy item arrays may omit CreatorId. That keeps earlier chapter fixtures working. However, every current bundled item supplies a resolvable reference, and a dedicated test establishes that stronger fixture guarantee.

The display Creator string remains on CatalogItem for compatibility with the existing cards and search. CreatorId provides identity; Creator provides display text. The loader does not require that Creator match CatalogCreator.Name, so an importer remains responsible for refreshing display text after a creator rename. Chapter 13 can use CreatorId for filtering without confusing display equality with identity.

For a larger application, derive display projections from related records and represent attribution roles explicitly. Keeping the current compatibility field is a deliberate transitional choice.

## 12.7 Preserve stream ownership

CatalogSnapshot.Load borrows streams. It does not close them. Its caller decides their lifetime, including when validation throws.

CatalogSnapshot.LoadBundled opens its own embedded-resource streams with using declarations and therefore disposes those streams. That is a different responsibility from closing a stream received as a parameter.

CatalogLoader.LoadBundled now delegates to CatalogSnapshot.LoadBundled().Items. Existing callers keep their familiar method while gaining creator-reference validation for the bundled data. CatalogSnapshot itself calls CatalogLoader.Load on the item stream, so this delegation does not create recursion.

The tests inspect CanRead after both successful loading and a failed creator-reference check. Resource ownership is observable behavior, and a later file or network adapter should not need to guess it.

## 12.8 Treat imports as boundaries

The local records currently serve two jobs: a small JSON input contract and the read-only data displayed by the app. That is acceptable for a controlled bundled fixture. It does not mean that a future external provider should deserialize straight into our application model.

When a remote source arrives, define a provider-specific DTO, validate it, and map it into the catalog. A provider may use different kinds, missing creator information, duration units, or content-rating vocabulary. That translation belongs at the import boundary.

The original website informs the sample data and archived pricing rules. The mobile app does not download and scrape the production HTML on every launch. Bundled fixtures provide predictable development input while the later API chapters build an explicit connected contract.

Also separate imported text from instructions. A description is content to display. It must not become executable HTML, a command, or a navigation destination merely because it arrived in a catalog file.

## 12.9 Verify the failure cases

CatalogMetadataTests adds cases for valid optional values, malformed dates, unsupported enum values, inappropriate book/audio fields, duplicate creators, missing references, preserved stream ownership, and the current bundled relationships.

These tests complement CatalogTests, which already covers missing kinds, malformed JSON, duplicate item IDs, empty catalogs, and search behavior. The entire suite runs through the existing portable Windows workflow.

A test that reads a three-minute duration proves the importer preserves 180 seconds. It does not prove the actual recording is three minutes long. A passing reference test proves the fixture has a related creator; it does not prove the attribution is commercially authoritative.

No mobile APIs changed in this chapter. Portable tests establish import behavior. Device execution, native rendering of the new metadata, and iOS builds remain separate verification tasks.

## 12.10 Hands-on exercise: break a relationship

Work in a local checkout and keep the original fixture available for restoration.

1. Run the portable tests using the commands in the companion README.
2. In Data/catalog.json, change one song's CreatorId to artist-does-not-exist.
3. Run the tests again. The bundled-snapshot checks should fail at the import boundary.
4. Restore the valid ID and rerun the suite.
5. In a test fixture, add a second creator with the same name and a different ID. Loading should remain valid because names are not unique identities.
6. Add a duplicate creator ID with a different name. Loading should fail.

For a second exercise, provide a known release date only inside a test fixture. Compare a valid ISO calendar date with February 30. Observe which case preserves DateOnly and which throws JsonException. Leave unverified real release dates absent.

Do not “fix” the failing relationship exercise by changing the loader to ignore unknown references. The purpose is to make broken import data visible before the browser renders it.

## 12.11 Review questions

- Why does an artist need an identity separate from the songs credited to that artist?
- What is the difference between a missing property and a present but blank string?
- Why does Listed fail to prove playback or purchase access?
- When should an absent advisory remain Unknown?
- Which method owns the streams in the bundled-loading path?
- Why should future provider DTOs be translated before they reach the app?

The next chapter builds on these identities to extend search and filtering, define sorting behavior, and introduce favorites. Stable IDs let those features survive renamed titles and reordered records.

## Chapter Summary

A useful mobile catalog starts with trustworthy identities and explicit meaning. This chapter separates content records from creators, keeps stable IDs independent of display names, and treats absent values as unknown rather than inventing dates or advisories. The bundled loader validates both individual records and relationships across files so broken references fail at the import boundary instead of surfacing later as confusing user-interface behavior. The guided lab demonstrates this contract by deliberately introducing an invalid creator reference, observing the expected failure, and restoring the fixture. These rules also prepare the application for provider imports, discovery, navigation and eventual synchronization. The result is intentionally a validated offline teaching snapshot, not a production content-ingestion service or a guarantee of native-device behavior.

## Official references

- Microsoft Learn, Required properties: https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/required-properties
- Microsoft Learn, JSON property and enum customization: https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/customize-properties

Editorial index terms: catalog; artist identity; author identity; podcast episode; stable identifier; optional metadata; DateOnly; content advisory; availability; JsonRequired; JsonStringEnumConverter; validation; DTO; stream ownership; bundled fixture.
