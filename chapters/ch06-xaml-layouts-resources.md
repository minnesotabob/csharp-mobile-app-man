# Chapter 6
# XAML, Controls, Layouts, and Resources

A native interface is measured and arranged in an environment the application does not fully control. A phone can show a keyboard, a user can enlarge text, and a tablet can offer much less space in a split window. A page that looks correct at one fixed size has demonstrated only one case.

This chapter explains the XAML structure behind the new home and catalog pages. Its result is a readable interface with shared appearance rules, a bounded collection area, and a clear place for later adaptive behavior.

## What You'll Learn

By the end of this chapter, you will be able to read a XAML page as an object graph; predict Grid measurement behavior; distinguish static resources from theme-aware bindings; diagnose a missing control versus a missing binding value; and verify that larger text remains readable.

**Prerequisites:** Chapters 1–5 and the Part II interface checkpoint linked in the companion repository’s `docs/milestones.md`. All application paths below are relative to `src/GnazzosWorld.App`; core paths are relative to `src/GnazzosWorld.Core`.

**Deliverable:** A Home page you can read and modify, a mapped catalog grid, and theme-aware shared label styling.

## 6.1 Read XAML as an object graph

XAML declares objects and their properties. A ContentPage contains a layout; the layout contains views. Namespaces identify framework and application types. The x:Class connects the document to a partial C# class, while x:Name identifies a generated field for a specific named object.

InitializeComponent constructs the declared tree and assigns its settings. It does not supply every binding value. A binding may obtain data later from the BindingContext. Keep those stages distinct when diagnosing an empty label: the control may exist while its data source is wrong.

The home page uses a heading, introductory text, and a browse action. Static branding remains ordinary text; localized interface labels come from UiText. This makes a small useful distinction between a product's proper name and translatable instructions.

### Build the Home page from a complete file

Open `Pages/HomePage.xaml`. This is the complete Home page at this checkpoint. Keep its existing class name and code-behind; replacing only the inner layout in an unrelated page would leave `OnBrowse` without its handler.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<ContentPage xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:text=
  "clr-namespace:GnazzosWorld.Core.Localization;assembly=GnazzosWorld.Core"
             x:Class="GnazzosWorld.App.Pages.HomePage"
             Title="{x:Static text:UiText.Home}">
  <ScrollView>
    <VerticalStackLayout Padding="24" Spacing="20">
      <Label Text="Gnazzo's World" FontSize="32"
             SemanticProperties.HeadingLevel="Level1" />
      <Label Text="{x:Static text:UiText.Welcome}" FontSize="24" />
      <Label Text="{x:Static text:UiText.Intro}" />
      <Button Text="{x:Static text:UiText.Browse}" Clicked="OnBrowse" />
    </VerticalStackLayout>
  </ScrollView>
</ContentPage>
```

Read from the outside inward. `ContentPage` provides a screen. Its `Title` supplies the navigation label. The single `ScrollView` contains one `VerticalStackLayout`, whose children appear in order. The heading and introductory labels grow with their text; the browse button follows them.

The `x` prefix identifies XAML language features such as `x:Class` and `x:Static`. The `text` prefix maps to the core assembly’s localization namespace. `{x:Static text:UiText.Browse}` reads a static C# property; Chapter 10 follows that property into its language resource. It is separate from the view-model bindings introduced in Chapter 7.

| XAML setting | Effect on this page |
|---|---|
| `x:Class` | Connects this file to `GnazzosWorld.App.Pages.HomePage` |
| `Padding="24"` | Leaves space inside the stack’s edges |
| `Spacing="20"` | Separates each pair of neighboring children |
| `HeadingLevel="Level1"` | Identifies the main heading to assistive technology |
| `Clicked="OnBrowse"` | Connects the button event to the page’s C# method |

**Try it:** change the welcome label’s text temporarily to a sentence twice as long. The following controls should move down rather than overlap. Restore the resource reference after the experiment.

## 6.2 Respect the content property

A page usually exposes one content value. To arrange several children, place them inside an appropriate layout. A VerticalStackLayout suits a short sequence whose natural heights should follow content. A Grid suits regions that must share or divide available space.

Do not solve a “more than one content” error by deleting an arbitrary label. Understand the parent object's contract. The same rule applies when a reusable ContentView contains several controls: give it a layout as its content.

A resource dictionary is another kind of collection. Its keyed values are looked up by resource keys; they are not extra visible children added to the page. Distinguish appearance configuration from the visual tree.

### Connect the browse button

`Pages/HomePage.xaml.cs` contains the corresponding partial class:

```csharp
using GnazzosWorld.Core.Localization;
namespace GnazzosWorld.App.Pages;
public partial class HomePage : ContentPage
{
    public HomePage() => InitializeComponent();
    private async void OnBrowse(object? sender, EventArgs e)
    {
        try { await Shell.Current.GoToAsync("//main/discover/catalog"); }
        catch (Exception)
        {
            await DisplayAlertAsync(
                UiText.Error, UiText.NavigationError, UiText.Ok);
        }
    }
}
```

`InitializeComponent` constructs the XAML controls and wires the named event. The handler awaits navigation to Discover. Its `try`/`catch` turns a navigation failure into a localized alert. This small, page-specific event is a useful first connection between markup and C#; the reusable catalog action becomes a command in Chapter 7.

Keep the two filenames together when navigating your editor. If the handler is renamed in C# but not in XAML, the markup still refers to the old method. Fix the connection instead of adding a second button with different behavior.

## 6.3 Learn measurement before adding fixed sizes

A layout first measures what its children need, then arranges them within the space offered. Automatic sizing lets a heading occupy its natural height. Star sizing divides remaining space. Fixed values are useful for deliberate constraints, but can become assumptions that fail at large text sizes.

The catalog browser uses automatic rows for search, filter, result summary, command, and error text, followed by a star-sized collection row. That gives the collection a finite region in which to scroll.

```xml
<Grid RowDefinitions="Auto,Auto,Auto,Auto,Auto,*"
      RowSpacing="10">
    <!-- Search, filter, summary, action, feedback, list. -->
</Grid>
```

A CollectionView placed in an unconstrained vertical scrolling region can undermine the finite viewport it needs. Avoid wrapping a scrolling list inside another vertical ScrollView merely to make every control move together. Decide which region owns scrolling.

The home page is different: a short content sequence in a ScrollView remains useful when text grows. That choice follows the content and interaction, not a rule that every page must use the same outer layout.

### Allocate the catalog’s available height

Open `Pages/CatalogPage.xaml`. Its inner grid divides the browser into six regions. This excerpt belongs inside the existing typed page; retain that page’s namespace declarations and outer `ContentGrid`.

```xml
<Grid RowDefinitions="Auto,Auto,Auto,Auto,Auto,*" RowSpacing="10">
      <SearchBar Placeholder="{x:Static text:UiText.SearchHint}"
                 Text="{Binding Query, Mode=TwoWay}" />
      <Picker Grid.Row="1" Title="{x:Static text:UiText.Filter}"
              ItemsSource="{Binding FilterLabels}"
              SelectedIndex="{Binding FilterIndex, Mode=TwoWay}" />
      <Label Grid.Row="2" Text="{Binding ResultSummary}" />
      <Button Grid.Row="3" Text="{x:Static text:UiText.OpenSelected}"
              Command="{Binding OpenDetails}" />
      <Label Grid.Row="4" Text="{Binding NavigationError}" />
```

The collection is the next child and sets `Grid.Row="5"`. Rows are zero-based: a child without `Grid.Row` occupies row zero. `Auto` asks for the content’s desired height; the final `*` gives the list the remaining height. The list’s own scrolling handles rows that exceed that region.

| Row | Content | Sizing reason |
|---|---|---|
| 0 | Search entry | Its native control determines a suitable height |
| 1 | Content-type picker | Its text and native chrome need their natural height |
| 2 | Result summary | May grow with language or text settings |
| 3 | Open selection | Keeps the primary action outside the scrolling list |
| 4 | Navigation feedback | Allows a message to wrap |
| 5 | Catalog collection | Uses remaining height and owns list scrolling |

**Try it:** put the collection in row four in a temporary copy. It now shares a cell with feedback because Grid permits overlapping children. The mistake is a row assignment, not a search failure. Restore row five before continuing.

## 6.4 Use spacing as a system

Padding separates content from its container edges. Margin separates one element from surrounding layout. Spacing on a stack or grid expresses a repeated relationship. Repeating several unrelated values makes later changes harder to reason about.

Our starter uses a modest family of values: page padding, row spacing, card padding, and gaps between an image and text. They are starting values to evaluate on devices, not measured proof of accessibility.

Avoid fixed row heights for descriptions and translated labels. The catalog card allows titles to wrap. Its small decorative thumbnail has a deliberate bounded size, while the text region uses the remaining width.

Spacing should remain understandable in a narrow window. A tablet design that allocates generous whitespace can become cramped when that same whitespace survives unchanged in a smaller viewport.

## 6.5 Separate resources from theme choices

App.xaml defines shared colors and styles. Keys such as PaperLight, PaperDark, TextLight, and TextDark describe roles within a theme pair. Accent supplies a consistent action color.

AppThemeBinding selects values for light or dark appearance:

```xml
<Setter Property="TextColor"
        Value="{AppThemeBinding
          Light={StaticResource TextLight},
          Dark={StaticResource TextDark}}" />
```

This is a shortened extract from the application resource style. Read the complete XAML for its namespaces and target type.

StaticResource resolves a keyed resource. DynamicResource is useful when the resource dictionary value itself changes at runtime. AppThemeBinding addresses a related but distinct problem: selecting according to the current app theme. Do not treat these mechanisms as interchangeable names for “styling.”

The implementation supplies theme-aware text and backgrounds. It still needs real-device contrast and native-control inspection. A chosen palette is a design input, not a completed accessibility result.

### Put the shared label appearance in App.xaml

These entries are inside `Application.Resources`. Keep the palette entries before the style that references them:

```xml
    <Color x:Key="PaperLight">#FAFAF7</Color>
    <Color x:Key="PaperDark">#15212A</Color>
    <Color x:Key="TextLight">#15212A</Color>
    <Color x:Key="TextDark">#F5F5F0</Color>
    <Color x:Key="Accent">#22566B</Color>
    <Color x:Key="SelectionLight">#DCEBF0</Color>
    <Color x:Key="SelectionDark">#244A5B</Color>
```

```xml
    <Style TargetType="Label">
      <Setter Property="FontSize" Value="16" />
      <Setter Property="FontAutoScalingEnabled" Value="True" />
      <Setter Property="TextColor"

        Value="{AppThemeBinding
          Light={StaticResource TextLight},
          Dark={StaticResource TextDark}}" />
    </Style>
```

The implicit style applies to labels without an explicit style. A heading can override its base `FontSize` locally while still receiving the shared text color and scaling behavior. `TextLight` is the dark foreground used on the light background; `TextDark` is the light foreground used on the dark background. The names identify the active theme, not the brightness of the color itself.

Change the appearance at its owner. To adjust all body text, edit this style. To change only the Home heading’s hierarchy, edit its label. To change the translated instruction, edit the string resource rather than the color dictionary.

## 6.6 Use styles at the appropriate scope

An implicit Label style supplies body size, text color, and automatic text scaling. A Button style supplies an understandable minimum height, padding, foreground, and background. Pages use shared background styling.

An implicit style can affect many controls. ApplyToDerivedTypes determines whether relevant derived types inherit the style. Review the result when introducing custom pages rather than assuming every subclass looks identical.

Use explicit styles when controls have different roles. A section heading, metadata label, and error message should not acquire their distinction through scattered inline values that are difficult to find later.

Keep content-specific settings near the content. A title's semantic heading level describes its role, while the shared text color describes appearance. A style should not accidentally give every metadata label the same heading level.

## 6.7 Understand units and text scaling

MAUI layout values use device-independent measurements. They do not specify a physical pixel count shared across every screen. Display density determines how those values map to pixels.

Text scaling is a user preference that can expose assumptions in the layout. Leaving FontAutoScalingEnabled on allows that preference to participate. It does not guarantee a usable page if fixed heights or overlays still clip the resulting text.

Test long titles and translations at large text settings. Check the result action, filter picker, list, and any inline detail pane with the keyboard visible. If vertical space is scarce, reconsider which controls remain outside the scrolling region.

The first implementation intentionally exposes that tradeoff: several automatic toolbar rows precede the list. A compact screen with very large text needs runtime review, and may need a more concise toolbar. Use the keyboard-open exercise below to decide whether to simplify that toolbar.

## 6.8 Add semantics without duplicating information

A main heading provides structure to assistive technology. A meaningful button name describes its action. Native search and picker controls have useful built-in behavior, but still need testing in the actual hierarchy.

The placeholder image in a catalog row is decorative. It does not provide information beyond the adjacent title, so the sample excludes it from the accessibility tree. Verify that exclusion on each target rather than assume the property behaves identically everywhere.

Avoid assigning a verbose description to a container that hides or repeats its children's useful text. Accessibility is about a navigable sequence of information and actions, not maximizing the number of descriptions in XAML.

The later design-system chapter expands this into a test plan. Start with semantic structure now, then test actual focus and announcements when the application runs.

## 6.9 Make a useful first debugging distinction

A XAML compilation error, runtime binding error, and visual measurement defect are different failures. A misspelled type may stop compilation. A wrong BindingContext may leave a correctly created control empty. A valid control can still receive too little space.

Inspect the earliest relevant failure. For layout, outline regions temporarily or inspect the live visual tree in supported tooling. For data, use a breakpoint and binding diagnostics. Remove temporary visual/debug instrumentation after the experiment.

The complete Part II application replaces the original startup with Shell. Use the Part I milestone when following the earlier startup code. Source history is a teaching aid when changes are explicit.

## Guided Lab

1. Open the Part II interface checkpoint and locate `Pages/HomePage.xaml`, its `.xaml.cs` file, `Pages/CatalogPage.xaml` and `App.xaml`. Keep an unchanged copy or use version control so you can restore each experiment.
2. Run the app on your configured Android emulator or device. Home should show the product heading, introductory text and browse button. Activate Browse; Discover should show the search/filter controls and catalog.
3. Change Home’s stack spacing from 20 to 8. Observe the relationship between controls, then restore 20. Change padding separately so you can distinguish outer space from gaps between children.
4. Switch the system between light and dark appearance. Inspect the shared label color and page background. Temporarily change `TextDark` to an unmistakable color to trace the resource, then restore it.
5. In the catalog grid, identify rows zero through five. Increase system text size and open the search keyboard. Check whether results remain reachable and whether the feedback label can wrap.
6. Temporarily change the collection’s row from five to four, reproduce the overlap, then restore it. Finally rename `OnBrowse` in only one file, inspect the build diagnostic and restore the matching names.

**Expected result:** you can explain each visible region, the file that owns it, and how a resource or layout change affects it. Keep the original application behavior after the experiments.

## Worked Example

A customer enlarges text before browsing Minnesota Bob’s songs. Home becomes taller, but its short content sequence can scroll. Discover must keep a bounded list beneath its search controls.

| Symptom | First inspection | Appropriate change |
|---|---|---|
| Home’s browse action is below the fold | ScrollView and child content | Preserve scrolling rather than fixing the heading height |
| Discover results overlap feedback | `Grid.Row` values | Give feedback and collection distinct rows |
| Body text is unreadable in dark mode | Label style and theme color keys | Correct the foreground/background pairing |
| Browse does not compile after a rename | `Clicked` and method name | Restore the XAML/C# event connection |

This is the basic debugging order: identify the region, find its owner, change one setting, and repeat the same action. It is faster than adding fixed heights until one screenshot looks right.

## Troubleshooting

| Symptom | First correction |
|---|---|
| A XAML type cannot be resolved | Inspect the namespace prefix, CLR namespace and assembly; restore the original declaration. |
| Browse fails to compile | Match the XAML Clicked handler name to the method in HomePage.xaml.cs. |
| The collection overlaps feedback | Check zero-based Grid.Row assignments and restore the list to row five. |
| Dark text disappears into its background | Follow the label style’s light/dark resource keys before changing individual labels. |

## Chapter Summary

This chapter turns a declarative XAML file into an understandable object graph and measurement system. Rows, columns, scroll containers, resource lookup, and styles each solve different responsibilities. Star-sized regions and bounded collections matter because mobile screens do not provide unlimited height. Theme resources and typography choices must remain responsive to system appearance and text scaling. The guided lab traces actual source files, changes a measurement rule temporarily, and compares XAML compilation faults with data-binding symptoms. The complete Home page, browse handler and shared label style give you concrete files to change, run and inspect.

## Exercises

The application now has a home introduction, search/filter browser, shared theme settings, and layout regions ready for selection/detail behavior. The following checks still need emulator or device evidence: narrow width, large text, keyboard occlusion, light/dark controls, and screen-reader structure.

1. Explain why the list receives a star-sized row while the home content uses a ScrollView.
2. Increase text size and record which automatic rows consume the available height.
3. Move a repeated color into a resource and verify light/dark behavior.
4. Deliberately break a namespace and a binding separately; compare their diagnostics.

## References and index terms

Layouts: https://learn.microsoft.com/en-us/dotnet/maui/user-interface/layouts/  
Styles: https://learn.microsoft.com/en-us/dotnet/maui/user-interface/styles/xaml  
Themes: https://learn.microsoft.com/en-us/dotnet/maui/user-interface/system-theme-changes

Index: XAML; object graph; content property; measurement; Grid; star sizing; ScrollView; resource dictionary; styles; AppThemeBinding; text scaling.
