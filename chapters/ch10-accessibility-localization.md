# Chapter 10
# Design Systems, Accessibility, and Localization

A coherent interface is a set of decisions that continues to work when its conditions change. A dark theme, large text, a different language, keyboard navigation, and a screen reader can each reveal assumptions hidden by the default appearance.

This chapter connects shared styles with meaningful interaction and resource-based strings. The implementation includes English/Spanish application resources and portable lookup tests. Full translation review and native accessibility verification remain separate tasks.

## What You'll Learn

By the end of this chapter, you will be able to distinguish visual style from task accessibility; test text scaling and semantic descriptions; find and edit RESX resources; explain culture-specific result summaries and pluralization; and design real-device checks for screen readers, contrast, focus and translated text expansion.

**Prerequisites:** Complete the preceding chapters and use the matching Part II source revision from `docs/milestones.md`. **Deliverable:** A testable improvement or diagnostic exercise in the Gnazzo's World application, without assuming native-device verification.

### Guided lab: test one user journey in two languages

1. Open the shared appearance resources and the English/Spanish RESX files. Find the browser filter label and result-summary strings in both.
2. Run the portable localization tests for zero, one and multiple results. Explain why a translated label cannot be built by blindly appending an English plural suffix.
3. Add a longer temporary Spanish label in a development checkout. Inspect the layout at increased text size; restore the fixture after observing wrapping and clipping.
4. Follow the resource lookup path from a view-model label to the current UI culture. Explain why changing `CurrentUICulture` at runtime may not update a static label already assigned on screen.
5. Identify a decorative thumbnail and a meaningful action. Describe which should receive semantic text and which could create noise if both parent and child announce the same content.
6. On a device, navigate catalog, selection and details with TalkBack or VoiceOver. Record device, OS, source revision, focus order, announcements and any clipped content. Leave results pending if these checks were not performed.

**Expected result:** Portable tests demonstrate resource selection and summary grammar; native checks are separately required to establish a genuinely accessible end-to-end experience.

### Troubleshooting the walkthrough

An untranslated word usually points to a missing resource or incorrect lookup, not to a layout defect. A string that changes only after page recreation suggests resource refresh semantics. A visually correct control that a screen reader cannot discover suggests an accessibility or focus problem. Check the full task, not just the presence of semantic properties.

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

## 10.8 Understand when strings refresh

XAML's static resource-property references are evaluated when the relevant view is created. Filter labels are captured when the view model is created. Changing a culture variable does not automatically update every existing object.

The sample supports language selection through the device/app environment when the application is started; it does not implement an in-app language-switching service. Runtime switching would need observable resource values or controlled view recreation and careful state preservation.

The iOS project declares English and Spanish in its localization metadata, but iOS build/launch is not yet verified. Check platform declarations as well as managed resource files before claiming a supported-language experience.

Tests prove that resources can be found and formatted. They do not prove that native platform settings select them correctly on every device.

## 10.9 Plan right-to-left and expansion testing

The current Spanish resources exercise language variation but do not establish right-to-left support. A future RTL locale requires direction-aware layouts, icons, alignment, navigation expectations, and content review.

Use long test strings or pseudolocalization to discover fixed-width assumptions. Preserve recognizable meaning so a reviewer can still complete a task. Do not “fix” expansion by reducing type below a readable size.

A directional icon may need mirroring while a brand or media artwork should not. Distinguish layout direction from indiscriminately flipping every image.

Record these checks as pending until an actual locale/device combination is exercised.

## 10.10 Maintain a release checklist rather than a claim

Check contrast in each state, text scaling, focus order, accessible names, keyboard interaction, localized formatting, missing resources, and navigation recovery. Test complete customer journeys when later features arrive.

Keep defects concrete. “Spanish filter label is clipped at large text in landscape” is actionable. “Localization works” is too broad to be evidence.

The final accessibility review will revisit the whole app. It should be a regression and integration pass, not the first time native assistive technology is used.

## Checkpoint and exercises

The application now has a shared appearance foundation and real English/Spanish resources, with tests for fallback and singular result messages. Native language selection, screen-reader behavior, contrast, and expansion remain device-review work.

1. Query one item in English and Spanish and verify the summary.
2. Add a temporary long translation and inspect the filter/action area.
3. Trace why changing CurrentUICulture does not refresh an existing static label.
4. Record an entire screen-reader browsing journey.
5. Identify one image that should be described and one that should be decorative.

## Chapter Summary

A design system is more than a palette, and accessibility is more than attaching labels. Shared resources establish consistent roles, while text scaling, focus, screen-reader semantics and complete journeys determine whether people can actually use the interface. This chapter introduces localized English/Spanish resources, explicit singular/plural messages and the difference between interface language and authored catalog content. The guided lab checks resource behavior in portable tests, creates a deliberate long translation and plans a complete assistive-technology journey. Existing tests support resource lookup, but they do not establish native screen-reader output, sufficient contrast in every state, right-to-left layout, or dynamic language refresh. Those outcomes must be measured on target devices.

## References and index terms

Accessibility: https://learn.microsoft.com/en-us/dotnet/maui/fundamentals/accessibility  
Localization: https://learn.microsoft.com/en-us/dotnet/maui/fundamentals/localization

Index: design system; contrast; text scaling; semantic properties; focus; screen reader; RESX; ResourceManager; neutral language; pluralization; CurrentUICulture; RTL.
