# Chapter 10
# Design Systems, Accessibility, and Localization

A coherent interface is a set of decisions that continues to work when its conditions change. A dark theme, large text, a different language, keyboard navigation, and a screen reader can each reveal assumptions hidden by the default appearance.

This chapter connects shared styles with meaningful interaction and resource-based strings. The implementation includes English/Spanish application resources and portable lookup tests. Full translation review and native accessibility verification remain separate tasks.

## What You'll Learn

By the end of this chapter, you will be able to distinguish visual style from task accessibility; test text scaling and semantic descriptions; find and edit RESX resources; explain culture-specific result summaries and pluralization; and design real-device checks for screen readers, contrast, focus and translated text expansion.

**Prerequisites:** Chapters 1–9 and the Part II interface checkpoint linked in the companion repository’s `docs/milestones.md`. All application paths below are relative to `src/GnazzosWorld.App`; core paths are relative to `src/GnazzosWorld.Core`.

**Deliverable:** English/Spanish UI labels and result summaries, plus a repeatable accessibility review of the browsing journey.

## 10.1 Define roles before individual colors

App.xaml groups background, foreground, action, and selection colors. These roles allow us to evaluate a change across the application instead of hunting for scattered literal values.

A role-based palette should account for normal, selected, disabled, focused, and error states. The starter covers shared backgrounds/text, action styling, and selected rows. Focused/disabled/native-control appearance must still be inspected on each platform.

A design system also includes spacing, type, control sizing, and content conventions. A button's wording and location matter as much as its fill color. Keep names and action patterns consistent across the home, browser, and details.

Do not assume that a shared style forces native controls to render identically. The goal is a coherent experience that respects platform behavior.

## 10.2 Preserve text scaling

Body labels use automatic text scaling. Headings have explicit base sizes but still need large-text testing. Fixed heights for multiline content can defeat an otherwise appropriate text setting.

At large text sizes, the catalog's automatic toolbar rows occupy more height. Verify that a useful list region remains and that the Open selection action stays reachable. A more compact control arrangement may be necessary on a short landscape display.

Check translated text as well as English. Labels that fit in one language may wrap in another, and truncation can remove the distinction between actions.

A successful compile cannot establish these outcomes. Record the system text setting, viewport, language, and device when reviewing them.

## 10.3 Treat semantics as structure

Headings identify meaningful sections. Controls need names that communicate actions, and information should be encountered in an understandable order. SemanticProperties provides a supported way to supply native accessibility information.

The home title and detail title are headings. The catalog thumbnail is decorative because the adjacent text communicates the record. Excluding that image should reduce noise, but the actual reading sequence needs confirmation.

Avoid applying a description to a whole container that makes its child actions inaccessible or repeats their text. Listen to the result on each native screen reader before deciding that more labels are better.

Selection, validation feedback, and navigation changes should remain understandable without relying solely on color or position.

### Read the heading and decorative-image markup

Home’s first label supplies a main heading:

```xml
      <Label Text="Gnazzo's World" FontSize="32"
             SemanticProperties.HeadingLevel="Level1" />
```

The catalog card’s thumbnail uses `AutomationProperties.IsInAccessibleTree="False"`, while the adjacent title and creator remain text. The image is a decorative placeholder, so the title already carries the useful information. A meaningful illustration elsewhere needs its own treatment.

When reviewing Home, listen for the product heading, introductory text and browse action in a useful order. When reviewing a catalog row, listen for its identity and selected state without a redundant placeholder announcement. Correct the observed task rather than adding the same long description to every parent.

## 10.4 Verify complete tasks with assistive technology

Enable TalkBack on Android and VoiceOver on iOS. Start from Home, reach Discover, edit the query, change the filter, select an item, activate Open selection, and return.

Record focus order, spoken name/role/state, whether selection is announced, and where focus goes after navigation. If a no-match message appears, determine whether a person knows that the results changed.

An error label bound to a view model does not automatically prove that an error is announced at the right time. A later implementation may need a deliberate native announcement or focus action. That should follow measured behavior, not an assumption.

Test with hardware keyboard or switch-related navigation where available. A touch gesture that works visually does not establish access through other input methods.

## 10.5 Move interface strings into resources

The core has Strings.resx for English and Strings.es.resx for Spanish. UiText wraps ResourceManager lookups and exposes simple properties used by XAML and the view models.

```csharp
private static readonly ResourceManager Resources = new(
    "GnazzosWorld.Core.Localization.Strings",
    typeof(UiText).Assembly);
public static string Get(
    string key, CultureInfo? culture = null)
    => Resources.GetString(key, culture) ?? key;
```

The base resource name must match the compiled resource location. The core's NeutralLanguage is en. A missing translation can fall back to the neutral value; a missing key displays the key in this teaching helper to expose the defect.

That fallback is a debugging aid, not a finished translation-quality policy. Production checks should identify missing keys before a user sees internal resource names.

### Follow one key through both resource files

Open `Localization/Strings.resx` and `Localization/Strings.es.resx` in the core project. In Visual Studio’s resource editor, edit the value column while preserving the key. These equivalent XML entries show the mapping for Discover:

```xml
<data name="Discover" xml:space="preserve"><value>Discover</value></data>
```

```xml
<data name="Discover" xml:space="preserve"><value>Explorar</value></data>
```

Each entry belongs inside its file’s existing `root`, alongside the RESX headers and other keys. The neutral file supplies English. The Spanish file supplies the same key with a different value. Keep `Discover` as the key in both files; translating the key would break lookup.

`UiText` exposes the property used by the UI:

```csharp
    public static string Discover => Get(nameof(Discover));
```

The Shell uses `UiText.Discover` as its visible tab title. Its route remains `discover` in either language. Home uses the same mechanism through XAML’s `x:Static` expression. One resource key can therefore serve both C# composition and markup without copying English text into either.

## 10.6 Separate interface language and content language

Translating Browse, Search, and error messages does not translate song titles or book descriptions. Those are catalog content with their own editorial and availability rules.

The application keeps proper names and supplied catalog metadata. A future content service can supply localized descriptions where available, but should distinguish that from automatic interface resource lookup.

Currency, dates, and numeric formatting also need deliberate culture choices. CurrentCulture influences formatting; CurrentUICulture selects interface resources. They often align on a device but serve different purposes.

Avoid concatenating a translated fragment with an English noun or assuming the same word order in every language. Resource formats should represent a complete message where practical.

## 10.7 Handle singular and plural results

The browser originally had only a plural result format. A one-item query exposed the problem: “1 results” or “1 resultados” is incorrect.

The updated implementation selects a singular resource for one result and the general format otherwise:

```csharp
public string ResultSummary => string.Format(
    CultureInfo.CurrentCulture,
    Items.Count == 1 ? UiText.OneResult : UiText.ResultsFormat,
    Items.Count);
```

Tests run the one-result scenario in English and Spanish. They restore the test's previous UI culture rather than change a global default for other tests.

This two-form rule is appropriate for the sample's two languages. Other languages can need different plural categories and number rules. A multilingual production design must support those requirements instead of extending an English conditional indefinitely.

### Verify the message the reader actually sees

The singular-summary test lives in `PresentationTests.cs`:

```csharp
    [Theory]
    [InlineData("en", "1 result")]
    [InlineData("es", "1 resultado")]
    public void One_match_has_a_localized_singular_summary(
        string culture, string expected)
    {
        var previous = CultureInfo.CurrentUICulture;
        try
        {
            CultureInfo.CurrentUICulture = CultureInfo.GetCultureInfo(culture);
            var vm = new CatalogBrowserViewModel(
            CatalogLoader.LoadBundled(), new Navigation());
            vm.Query = "Kai";
            Assert.Equal(expected, vm.ResultSummary);
        }
        finally { CultureInfo.CurrentUICulture = previous; }
    }
```

Run it after editing the singular resource. `Kai` has one matching record in the bundled catalog, so the expected result includes the localized singular word. The `finally` block restores the previous UI culture even if an assertion fails.

Compare this with a zero-match query and a multi-match query. Each result count should use a complete resource message rather than concatenate an English suffix. If you add a language with more plural categories, replace this two-form policy with a suitable localization design.

## 10.8 Understand when strings refresh

XAML's static resource-property references are evaluated when the relevant view is created. Filter labels are captured when the view model is created. Changing a culture variable does not automatically update every existing object.

The sample supports language selection through the device/app environment when the application is started; it does not implement an in-app language-switching service. Runtime switching would need observable resource values or controlled view recreation and careful state preservation.

The iOS project also declares English and Spanish in its localization metadata. When adding a language, update platform declarations as well as managed resource files and check language selection on the target platform.

## 10.9 Plan right-to-left and expansion testing

The current Spanish resources exercise language variation but do not establish right-to-left support. A future RTL locale requires direction-aware layouts, icons, alignment, navigation expectations, and content review.

Use long test strings or pseudolocalization to discover fixed-width assumptions. Preserve recognizable meaning so a reviewer can still complete a task. Do not “fix” expansion by reducing type below a readable size.

A directional icon may need mirroring while a brand or media artwork should not. Distinguish layout direction from indiscriminately flipping every image.

Keep a separate locale review for direction-aware layouts when adding an RTL language.

## 10.10 Maintain a release checklist rather than a claim

Check contrast in each state, text scaling, focus order, accessible names, keyboard interaction, localized formatting, missing resources, and navigation recovery. Test complete customer journeys when later features arrive.

Keep defects concrete. “Spanish filter label is clipped at large text in landscape” is actionable. “Localization works” is too broad to be evidence.

The final accessibility review will revisit the whole app. It should be a regression and integration pass, not the first time native assistive technology is used.

## Guided Lab

1. Open the two RESX files and locate `Discover`, `SearchHint`, `OneResult` and `ResultsFormat`. Compare keys and full-message values.
2. Run `One_match_has_a_localized_singular_summary` for English and Spanish. Search for zero and multiple matches in additional test cases or the debugger.
3. Set the device/app language to Spanish using its supported settings and restart the app. Discover should use its translated label while catalog proper names remain intact.
4. In a temporary copy, lengthen the Spanish filter label. Increase text size, rotate to landscape and inspect wrapping. Restore the label; fix a layout constraint if normal translations clip.
5. Enable TalkBack or VoiceOver on your target device. Travel from Home to Discover, edit a query, select a result, open details and return. Note names, roles, selected state and focus after navigation.
6. Compare the same journey with the keyboard visible and in dark appearance. Record a specific defect and the control that owns it rather than a general pass/fail claim.

**Expected result:** resource lookup and summary grammar are testable, and the native review identifies whether a reader can complete the entire task with their chosen input and display settings.

## Worked Example

A Spanish-speaking reader searches for Kai with enlarged text. The tab reads “Explorar,” the book retains its supplied title, and the result summary reads “1 resultado.” These are three different content decisions: translated UI, authored catalog content and a localized count message.

If the tab remains English after a culture change made inside the debugger, recreate the page or restart with the intended app language: the static label was read when the object was created. If the Spanish label appears but clips, correct layout. If the label is visible but absent from spoken navigation, inspect semantics and focus. Resource correctness alone cannot repair either of those presentation defects.

## Troubleshooting

| Symptom | First correction |
|---|---|
| A resource key appears on screen | Check the spelling and presence of that key in the neutral RESX file. |
| A translated label remains in the old language | Recreate the relevant objects or restart with the intended app language. |
| One result uses plural wording | Check OneResult and the summary’s count-based resource selection. |
| A label is correct but clips or is not spoken | Review layout or semantics on the native task; resource lookup is a separate step. |

## Chapter Summary

A design system is more than a palette, and accessibility is more than attaching labels. Shared resources establish consistent roles, while text scaling, focus, screen-reader semantics and complete journeys determine whether people can actually use the interface. This chapter introduces localized English/Spanish resources, explicit singular/plural messages and the difference between interface language and authored catalog content. The guided lab checks resource behavior in portable tests, creates a deliberate long translation and plans a complete assistive-technology journey. Existing tests support resource lookup, but they do not establish native screen-reader output, sufficient contrast in every state, right-to-left layout, or dynamic language refresh. Those outcomes must be measured on target devices.

## Exercises

The application now has a shared appearance foundation and real English/Spanish resources, with tests for fallback and singular result messages. Native language selection, screen-reader behavior, contrast, and expansion remain device-review work.

1. Query one item in English and Spanish and verify the summary.
2. Add a temporary long translation and inspect the filter/action area.
3. Trace why changing CurrentUICulture does not refresh an existing static label.
4. Record an entire screen-reader browsing journey.
5. Identify one image that should be described and one that should be decorative.

## References and index terms

Accessibility: https://learn.microsoft.com/en-us/dotnet/maui/fundamentals/accessibility  
Localization: https://learn.microsoft.com/en-us/dotnet/maui/fundamentals/localization

Index: design system; contrast; text scaling; semantic properties; focus; screen reader; RESX; ResourceManager; neutral language; pluralization; CurrentUICulture; RTL.
