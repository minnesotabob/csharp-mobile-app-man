# Chapter 5
# Establishing Testable Application Foundations

A useful test identifies a broken promise. A second copy of a method's algorithm may simply reproduce its mistake. An expected result grounded in the application's requirements is a stronger check.

Our first promises are concrete: catalog IDs are unique, an unaccented query can match an accented title, and discounts apply to separate songs. These behaviors need no emulator. This chapter explains their portable boundary, tests, and automated execution, while keeping native verification distinct.

## 5.1 Choose an observable boundary

The core targets net11.0 without referencing MAUI controls. A test supplies values and inspects results without constructing a page. The application references core and adds startup, views, and platform configuration.

A separate assembly helps because portable tests do not require mobile tooling and cannot accidentally depend on a page's fields. More projects are not automatically better: add infrastructure and service boundaries when features need them.

Initially, application depends on core and tests depend on core. The core neither resolves global application services nor asks Android objects for state. That keeps its requirements and failures understandable.

## 5.2 Configure the runner intentionally

The executable test project uses the xUnit v3 framework family with package version 4.0.0. Version-family and package-version names are different.

```xml
<ItemGroup>
  <PackageReference Include="xunit.v3" Version="4.0.0" />
  <ProjectReference
    Include="../../src/GnazzosWorld.Core/GnazzosWorld.Core.csproj" />
</ItemGroup>
```

The project targets net11.0 and sets OutputType to Exe. Test tooling generates the runner entry point. Our command invokes that executable rather than relying on an unconfigured VSTest adapter:

```powershell
$tests = "tests/GnazzosWorld.Core.Tests/GnazzosWorld.Core.Tests.csproj"
dotnet build $tests -c Release
dotnet run --project $tests -c Release --no-build
```

Use --no-build only after a successful matching build. An old binary is not evidence for new source. CI stops at a failing build instead of continuing silently.

## 5.3 Test observable search behavior

A parameterized example supplies meaningful input and checks the identity of a single result:

```csharp
[Theory]
[InlineData(" beret VIOLET ",
    "song-minnesota-bob-beret-violet")]
[InlineData("KAI", "book-kai-01")]
public void Search_handles_case_whitespace_and_accents(
    string term, string id)
    => Assert.Equal(id, Assert.Single(
        CatalogSearch.Find(
            CatalogLoader.LoadBundled(), term)).Id);
```

The theory covers whitespace, case, and diacritics. Assert.Single also catches unexpected extra matches. The expected ID is not computed by repeating the production comparison.

Use the bundled fixture for a contract check of sample content. For a focused sorting test, supply two handmade records with equal titles and reversed IDs. An already sorted fixture could conceal missing tie-breaking.

A test should allow a correct implementation change. Replacing LINQ with a loop should not fail tests when observable results remain the same.

## 5.4 Distinguish blank, filtered, and empty results

The core combines optional kind filtering with title/creator matching. Test the interaction: “Minnesota Bob” restricted to Song returns matching songs, while restricted to Book returns none.

Blank query means all records within the filter. A valid nonmatching query means an empty result. Neither means a failed network source, because this function performs no I/O.

Later view models distinguish loading, empty, error, and success. Keep the search function's contract simpler instead of inventing transport states it cannot experience.

Also consider whether search mutates its source. Producing a separately ordered result should preserve the supplied collection. Test meaningful source state rather than prescribing a particular internal method.

## 5.5 Validate at the serialization boundary

Deserialization does not make incoming data valid. An entry can have blank required values, duplicate IDs, or a non-HTTPS external link.

CatalogLoader distinguishes parser/serialization failures from semantic metadata errors. Malformed JSON must not become a silent empty list. An empty but valid array can remain a legitimate empty catalog.

An omitted enum field illustrates a subtle bug. If Book is numeric zero, a missing kind can otherwise default to Book. Checking Enum.IsDefined after deserialization cannot distinguish omission from intention.

The updated model marks required JSON properties explicitly. The serializer now rejects an otherwise complete entry with no kind field. Compile-time nullable analysis still helps, but it does not validate untrusted JSON.

The regression suite covers omitted kind, undefined enum, null entry, blank metadata, duplicate ID, malformed document, and unsupported link scheme. Each case protects a specific assumption. Do not claim that it proves every conceivable input is safe.

We did not observe a local red/green test cycle for the omission fix. The new regression case is verified in CI against the changed model. Record that actual sequence rather than inventing evidence.

## 5.6 Respect stream ownership

LoadBundled opens and disposes its resource. Load(Stream) accepts the caller's stream and does not silently take ownership. Tests use MemoryStream with an explicit using declaration.

A future HTTP adapter remains responsible for its response lifetime. This convention avoids a loader unexpectedly closing a resource another component owns.

Null stream, malformed bytes, and a valid empty array deserve different outcomes. A broad catch that returns an empty result hides those distinctions and prevents useful recovery by the caller.

The mobile boundary can later translate a known load failure into a retryable state while retaining diagnostics. That does not require erasing the cause inside the core.

## 5.7 Ground price tests in customer rules

The archived pricing example uses decimal money and explicit allowed lengths/quantities. It is a snapshot, not a live offer.

For three identical-style/length songs, the factors are 1.0, 0.9, and 0.8. A three-minute vocal song at 179 dollars therefore totals 483.30 dollars:

```csharp
[Fact]
public void Third_song_gets_twenty_percent_discount_in_addition_to_second()
    => Assert.Equal(
        483.30m, SongPricing.Calculate(3, true, 3));
```

This expected amount comes from the stated rule. Calling another copy of the same factor calculation to obtain it would weaken the test.

The suite checks all snapshot base prices and rejects unsupported lengths and quantities. A version identifier makes future changes deliberate. Do not rewrite historical order prices merely because the current table changes.

Taxes, fees, mixed-length bundles, refunds, and revision charges are outside this calculator. Production quoting remains server-authoritative. A correct client total cannot establish payment.

## 5.8 Introduce doubles when dependencies arrive

Pure search/pricing functions need no mocking library. Later, fake clocks, controlled HTTP handlers, and test stores can isolate meaningful behavior.

Choose the double for the question. A fake clock makes expiration deterministic. A temporary real database checks migration behavior. A fake repository can support view-model state tests, but cannot prove a database rollback.

Likewise, a mocked sign-in response cannot prove provider-enforced MFA, and a fake payment callback cannot prove signature verification. Test at the boundary where a requirement actually operates.

Small interfaces should describe feature needs. Do not wrap an entire platform SDK merely to mock it.

## 5.9 Keep the suite understandable

Behavioral names communicate intent. Second_song_gets_ten_percent_discount is more useful than Calculate_test_2. Keep inputs and expected outcomes visible even when helpers remove repeated setup.

Add cases for relevant interactions and failure paths. Avoid tests that mirror generated properties or enforce incidental implementation structure. A useful suite protects freedom to improve the internals.

When practical, observe a failing regression before the fix. If tooling or environment prevents that sequence, state what was actually run. Truthful evidence is part of a technical book's reliability.

## 5.10 Automate the same sequence

The portable workflow checks out source, installs SDK 11.0.100, records the environment, restores, builds Release, and runs the executable tests. It uses read-only repository permissions and no project secrets.

A green result belongs to its commit SHA. Compare it with the version you intend to use. A passing run from before a logic change does not verify that change.

Keep mobile packaging separate so a missing Android dependency does not hide a pricing regression. Conversely, portable tests do not replace Android/iOS build checks, screen-reader journeys, or provider recovery tests.

Coverage can reveal gaps, but its percentage is not the goal. Protect concrete risks: incorrect totals, lost drafts, cross-account records, duplicate orders, and invalid updates.

## 5.11 Record the Part I checkpoint

Editorial draft, compilation, tests, device checks, and artwork are different dimensions of progress. Five chapter files alone do not establish a verified application.

A reader should be able to retrieve the source, run portable checks, explain startup, and attempt the documented launch. Identify remaining platform work precisely. Use docs/verification.md and docs/device-checks.md to show what happened and what remains.

## Summary and exercises

Portable logic makes application rules quick to exercise. Tests protect search, validation, and pricing contracts. Other boundaries require integration, provider, or device evidence, and CI results need a source revision and clear scope.

1. Test duplicate IDs with different titles.
2. Compare malformed JSON with a valid object missing kind.
3. Change the second-song discount locally, confirm failure, then restore it.
4. Design a fake clock for quote expiration and state what still needs integration testing.
5. Specify a device check that portable tests can never establish.

## References and index terms

xUnit runner: https://xunit.net/docs/getting-started/v3/getting-started  
Required JSON properties: https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/required-properties

Index: portable core; unit tests; xUnit; theory; fact; serialization; required properties; nullability; stream ownership; decimal; regression; test double; CI.
