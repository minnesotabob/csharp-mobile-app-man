# Chapter 6
# XAML, Controls, Layouts, and Resources

A native interface is measured and arranged in an environment the application does not fully control. A phone can show a keyboard, a user can enlarge text, and a tablet can offer much less space in a split window. A page that looks correct at one fixed size has demonstrated only one case.

This chapter explains the XAML structure behind the new home and catalog pages. Its result is a readable interface with shared appearance rules, a bounded collection area, and a clear place for later adaptive behavior.

## What You'll Learn

By the end of this chapter, you will be able to read a XAML page as an object graph; predict Grid measurement behavior; distinguish static resources from theme-aware bindings; diagnose a missing control versus a missing binding value; and verify that larger text remains readable.

**Prerequisites:** Complete the preceding chapters and use the matching Part II source revision from `docs/milestones.md`. **Deliverable:** A testable improvement or diagnostic exercise in the Gnazzo's World application, without assuming native-device verification.

### Guided lab: make a page respond to constraints

1. Check out the Part II source milestone described in `docs/milestones.md`, then open the home page XAML and the shared resources in `App.xaml`.
2. Trace the page's root layout, its immediate children, and the location of its bounded collection. Write a one-sentence explanation of why the list needs a finite viewport.
3. In a disposable working copy, change a `Grid` row allocated with `*` sizing into an `Auto` row. Predict how a growing list or keyboard appearance could affect the measured content. Restore the original setting after inspecting it.
4. Find one color or spacing value supplied through a shared resource. Follow that resource to its declaration; compare it with a theme-aware resource and explain which should change in dark mode.
5. Temporarily break an XAML namespace and build to see a markup/type-resolution error. Restore it, then deliberately misspell a binding path. Distinguish build diagnostics from a view that exists but displays no data.
6. Record narrow-screen, large-text, and dark-theme results on an emulator or device when available. A code review alone cannot verify those interactions.

**Expected result:** The reader can identify the layout and binding ownership of each visible region, and can explain why compilation and runtime presentation failures require different investigations.

### Troubleshooting the walkthrough

A page that will not compile suggests a type, resource key, or XAML syntax issue. A page that compiles but has blank text suggests a binding context, property name, or missing notification. Content that disappears when the keyboard opens suggests a viewport and measurement problem. Tackle these separately rather than scattering fixed heights through the layout.

## 6.1 Read XAML as an object graph

XAML declares objects and their properties. A ContentPage contains a layout; the layout contains views. Namespaces identify framework and application types. The x:Class connects the document to a partial C# class, while x:Name identifies a generated field for a specific named object.

InitializeComponent constructs the declared tree and assigns its settings. It does not supply every binding value. A binding may obtain data later from the BindingContext. Keep those stages distinct when diagnosing an empty label: the control may exist while its data source is wrong.

The home page uses a heading, introductory text, and a browse action. Static branding remains ordinary text; localized interface labels come from UiText. This makes a small useful distinction between a product's proper name and translatable instructions.

## 6.2 Respect the content property

A page usually exposes one content value. To arrange several children, place them inside an appropriate layout. A VerticalStackLayout suits a short sequence whose natural heights should follow content. A Grid suits regions that must share or divide available space.

Do not solve a “more than one content” error by deleting an arbitrary label. Understand the parent object's contract. The same rule applies when a reusable ContentView contains several controls: give it a layout as its content.

A resource dictionary is another kind of collection. Its keyed values are looked up by resource keys; they are not extra visible children added to the page. Distinguish appearance configuration from the visual tree.

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

## 6.6 Use styles at the appropriate scope

An implicit Label style supplies body size, text color, and automatic text scaling. A Button style supplies an understandable minimum height, padding, foreground, and background. Pages use shared background styling.

An implicit style can affect many controls. ApplyToDerivedTypes determines whether relevant derived types inherit the style. Review the result when introducing custom pages rather than assuming every subclass looks identical.

Use explicit styles when controls have different roles. A section heading, metadata label, and error message should not acquire their distinction through scattered inline values that are difficult to find later.

Keep content-specific settings near the content. A title's semantic heading level describes its role, while the shared text color describes appearance. A style should not accidentally give every metadata label the same heading level.

## 6.7 Understand units and text scaling

MAUI layout values use device-independent measurements. They do not specify a physical pixel count shared across every screen. Display density determines how those values map to pixels.

Text scaling is a user preference that can expose assumptions in the layout. Leaving FontAutoScalingEnabled on allows that preference to participate. It does not guarantee a usable page if fixed heights or overlays still clip the resulting text.

Test long titles and translations at large text settings. Check the result action, filter picker, list, and any inline detail pane with the keyboard visible. If vertical space is scarce, reconsider which controls remain outside the scrolling region.

The first implementation intentionally exposes that tradeoff: several automatic toolbar rows precede the list. A compact screen with very large text needs runtime review, and may need a more concise toolbar. We do not claim that compilation has answered the design question.

## 6.8 Add semantics without duplicating information

A main heading provides structure to assistive technology. A meaningful button name describes its action. Native search and picker controls have useful built-in behavior, but still need testing in the actual hierarchy.

The placeholder image in a catalog row is decorative. It does not provide information beyond the adjacent title, so the sample excludes it from the accessibility tree. Verify that exclusion on each target rather than assume the property behaves identically everywhere.

Avoid assigning a verbose description to a container that hides or repeats its children's useful text. Accessibility is about a navigable sequence of information and actions, not maximizing the number of descriptions in XAML.

The later design-system chapter expands this into a test plan. Start with semantic structure now, then test actual focus and announcements when the application runs.

## 6.9 Make a useful first debugging distinction

A XAML compilation error, runtime binding error, and visual measurement defect are different failures. A misspelled type may stop compilation. A wrong BindingContext may leave a correctly created control empty. A valid control can still receive too little space.

Inspect the earliest relevant failure. For layout, outline regions temporarily or inspect the live visual tree in supported tooling. For data, use a breakpoint and binding diagnostics. Remove temporary visual/debug instrumentation after the experiment.

The complete Part II application replaces the original startup with Shell. Use the Part I milestone when following the earlier startup code. Source history is a teaching aid when changes are explicit.

## Checkpoint and exercises

The application now has a home introduction, search/filter browser, shared theme settings, and layout regions ready for selection/detail behavior. The following checks still need emulator or device evidence: narrow width, large text, keyboard occlusion, light/dark controls, and screen-reader structure.

1. Explain why the list receives a star-sized row while the home content uses a ScrollView.
2. Increase text size and record which automatic rows consume the available height.
3. Move a repeated color into a resource and verify light/dark behavior.
4. Deliberately break a namespace and a binding separately; compare their diagnostics.

## Chapter Summary

This chapter turns a declarative XAML file into an understandable object graph and measurement system. Rows, columns, scroll containers, resource lookup, and styles each solve different responsibilities. Star-sized regions and bounded collections matter because mobile screens do not provide unlimited height. Theme resources and typography choices must remain responsive to system appearance and text scaling. The guided lab traces actual source files, changes a measurement rule temporarily, and compares XAML compilation faults with data-binding symptoms. It closes by separating what source inspection proves from what only a device can show: keyboard occlusion, large-text behavior, native appearance, and assistive-technology reading order.

## References and index terms

Layouts: https://learn.microsoft.com/en-us/dotnet/maui/user-interface/layouts/  
Styles: https://learn.microsoft.com/en-us/dotnet/maui/user-interface/styles/xaml  
Themes: https://learn.microsoft.com/en-us/dotnet/maui/user-interface/system-theme-changes

Index: XAML; object graph; content property; measurement; Grid; star sizing; ScrollView; resource dictionary; styles; AppThemeBinding; text scaling.
