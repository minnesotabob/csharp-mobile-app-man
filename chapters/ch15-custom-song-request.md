# Chapter 15
# Building the Custom-Song Request Form

A catalog asks a visitor to choose something that already exists. A custom-song request asks the customer to describe something that does not exist yet. That difference changes the interface. The customer may know the occasion but not the genre, have a long story to tell, or decide halfway through that an instrumental would work better. A useful form helps the customer make those decisions without losing earlier work.

Our example begins on the home page and opens a three-step request builder. The first step describes the music. The second collects the story. The third collects contact details and produces a review. This chapter stops at review: it does not create an order, calculate a final quote, send email, or charge a customer. Chapter 16 establishes the submission contract and pricing rules; later chapters connect that contract to an authenticated service.

## What You'll Learn

You will learn to break a complex customer request into manageable steps; keep draft state independent of controls; use conditional inputs without losing information; validate at the moment a decision requires it; invalidate an outdated review; and distinguish an explicit saved draft from unsaved in-process edits.

**Prerequisites:** The Chapter 14 navigation patterns, portable test project, and a development build of the sample app. **Deliverable:** A three-step request builder whose progress can be tested independently of the native keyboard.

## Begin with the customer's decisions

A long form is easier to build than a good short journey. Before adding controls, group fields according to the decision the customer is making. The music step contains supported lengths, vocal versus instrumental treatment, genre, occasion, and permission for explicit content. Optional vocal notes appear only when vocals are selected. The story step gives the customer room for names, memories, tone, and details they want included. The contact step collects a name and a single email address, then offers review.

| Step | Inputs | Gate before continuing |
| --- | --- | --- |
| Music | Length, vocals, genre, occasion, explicit preference, optional vocal notes | Supported length and required descriptive fields |
| Story | Customer's description | Nonblank story within the size limit |
| Contact and review | Name and email | All earlier rules plus valid contact fields |

Clean content is the default: AllowExplicit begins false. A switch labeled with the question makes its meaning clearer than an unexplained checkbox. “Allow explicit content” records permission, rather than promising that the resulting song will contain explicit material.

Do not assume the customer understands musical terminology. Genre is free text in this teaching milestone; it accepts “folk with a little country” as well as “country.” A production service might provide suggestions while retaining an Other field. Validation should reject unusable input, not reject a reasonable creative description merely because it is absent from a drop-down list.

Length uses a picker with the six supported values from the archived example: 1, 2, 3, 4, 6, and 8 minutes. Those choices are teaching data, not a statement about the current commercial offering. Displaying an input control never removes the need to validate its value in application logic.

## Keep editable state outside the controls

The portable SongRequest record lives under Core/Orders. Its properties use init accessors, and each edit creates a new record with a with expression. Controls show that record; they do not own it. SongRequestViewModel owns the current draft, step number, errors, saved status, and optional review snapshot.

```csharp
vm.Edit(vm.Draft with { Genre = text });
```

This small expression matters. If the customer changes Genre, every other property remains present. Moving to another step rebuilds the visible controls from the same record. Hiding the vocal-note control does not destroy what the customer previously wrote. Returning to vocals makes those notes available again.

Keep the draft and the review as separate concepts. A draft may be incomplete. A review must represent values that passed the current rules. The Edit method therefore clears Review on every change. A customer who reviews the request and then edits an email address should not continue seeing an authoritative-looking summary of the old address.

For an instrumental review, ForReview returns a copy with empty vocal notes. The original draft keeps them. This gives us two useful behaviors at once: reversible editing for the customer and an unambiguous proposed request. ForReview also trims outer whitespace from text fields. It leaves the story's internal spaces and line breaks alone.

```csharp
var review = draft.ForReview();
// Instrumental reviews omit vocal instructions.
// The editable draft still retains those notes.
```

The record owns local editing state. A customer API must separately validate submitted values, ownership, current quote terms and payment state.

### Trace edit and review in the view model

Open `src/GnazzosWorld.Core/Presentation/SongRequestViewModel.cs`. These methods connect an edit to the review step:

```csharp
public void Edit(SongRequest value)
{
    Draft = value; Review = null; IsDirty = true;
    Status = "Unsaved changes."; Errors = ""; Changed();
}
public bool Next()
{
    var errors = SongRequestRules.Validate(Draft, Step);
    Errors = string.Join("\n", errors.Select(e => e.Message));
    if (errors.Count != 0) { Changed(); return false; }
    if (Step < 2) Step++;
    else Review = Draft.ForReview();
    Changed(); return true;
}
```

`Edit` changes the draft, clears the old review and announces unsaved changes. `Next` checks every rule applicable to the current step. A failed check keeps the customer at that step; the final successful check produces `ForReview()` rather than advancing to a nonexistent fourth step.

Use a breakpoint in each method while changing only the email address after review. The story remains in `Draft`, but the old review must disappear immediately.

## Validate at meaningful boundaries

SongRequestRules.Validate returns field/message pairs. It accepts the draft and the step being completed. Step zero checks music choices; step one checks those choices and the story; step two checks everything, including contact details. Rechecking earlier fields at the final boundary prevents an invalid restored or programmatically modified draft from bypassing a rule merely because a previous screen was once visited.

The portable rules reject unsupported lengths, blank required fields, oversized text, and an email value that cannot be parsed as one address. Email parsing checks shape, not mailbox ownership or deliverability. Do not show “email verified” after this check. Verification requires a separate service workflow.

The example limits genre to 80 characters, occasion and contact name to 120, vocal notes to 500, story to 4,000, and email to 254. These are explicit teaching limits that **a customer-request API must enforce independently**. The Chapter 18 API checkpoint provides public catalog reads; it does not include order writes. Chapter 32 later adds separately enabled, authenticated synthetic quote/order routes with server-side validation. The controls expose the same limits to discourage accidental excess, while portable validation protects callers that do not use the controls.

```csharp
var errors = SongRequestRules.Validate(Draft, Step);
Errors = string.Join("\n",
    errors.Select(error => error.Message));
if (errors.Count != 0) return false;
```

A failed Next leaves both the step and the draft intact. It does not clear fields, navigate away, or return a generic “invalid request” toast. The error summary names the input to fix. Only successful validation advances the step or creates the review.

Do not validate every keystroke with aggressive errors. An email address is necessarily incomplete while it is being typed. This milestone validates when the customer chooses Next or Review request. Editing clears the previous error summary; the next boundary evaluates the current values. Later refinements can show unobtrusive field-level feedback after a field loses focus.

## Build controls that work with a keyboard

SongRequestPage creates native MAUI controls in C# and places them in a ScrollView containing a VerticalStackLayout. Earlier chapters used XAML; this code-built page makes the relationship between a step and its current controls particularly visible. Both styles use the same MAUI layout and binding system. The choice does not change where business rules belong.

Use an Entry for short fields and an Editor for the story. The email Entry requests Keyboard.Email. That setting selects an appropriate soft keyboard; it does not validate the resulting text. Editor uses automatic height adjustment with a minimum height so the initial empty story field is discoverable.

The Field helper adds a visible label before each input and sets a semantic hint. It does not set SemanticProperties.Description on Entry or Editor. Microsoft's accessibility guidance warns that descriptions on editable controls can interfere with their normal text announcements on Android. Keep the typed value available to the accessibility system and test the actual interaction with TalkBack and VoiceOver.

The page uses a heading for the step indicator and an announcement when validation fails. Review content appears as a single text summary, including story and contact details, so it can be read in order. Editing after review hides that summary immediately. The current implementation has a summary-level error experience; field-specific focus routing and translated strings are explicit follow-up work.

With the keyboard open, scroll to the story and final contact fields. Repeat with large text and narrow landscape. Check Back and keyboard dismissal using the same invented inputs on each target device.

### Build one field and connect its edit callback

`src/GnazzosWorld.App/Pages/SongRequestPage.cs` uses this helper for short entries and the multiline story:

```csharp
private void Field(string label, string value, int limit,
    Action<string> update, bool multiline = false, bool email = false)
{
    panel.Children.Add(new Label { Text = label });
    InputView input = multiline
        ? new Editor { AutoSize = EditorAutoSizeOption.TextChanges,
            MinimumHeightRequest = 120 }
        : new Entry { Keyboard = email ? Keyboard.Email : Keyboard.Default };
    input.MaxLength = limit; input.Text = value;
    SemanticProperties.SetHint(input, label);
    input.TextChanged += (_, args) => update(args.NewTextValue ?? "");
    panel.Children.Add(input);
}
```

This helper belongs inside the existing page, where `panel` is the step’s vertical layout. It creates the label first, chooses an `Editor` or `Entry`, assigns the current text, then attaches the change callback. Initial text is assigned before subscription, so constructing a field does not itself mark the draft edited.

The caller supplies the field-specific update. Story uses `multiline: true`; email uses `email: true`. Those settings change the control or keyboard while the portable rules still decide whether the entered value is acceptable.

## Distinguish open edits from saved drafts

Customers need a precise answer to “Will this still be here?” The example makes two promises. A shared view model retains open edits when the customer leaves the form and returns during the same application process. Choosing Save draft on this device writes a local copy that can be loaded by a new process. Unsaved edits are not promised to survive process termination.

SongRequestViewModel is registered as a singleton. SongRequestPage remains transient. Consequently, navigating away may create a new page later, but the editing session stays in the shared model. Restore reads storage only once after a successful load and never replaces unsaved edits. A page appearing is not permission to overwrite newer in-memory values with an older saved copy.

The IRequestDraftStore interface keeps persistence out of the view model. It supplies Load, Save, and Delete. FileRequestDraftStore places a versioned JSON envelope in MAUI's app-data directory, using a fixed application-controlled filename. It writes a temporary file before replacing the saved file. This avoids directly truncating the saved copy before serialization completes, although it is not a database transaction or a guarantee against every power-loss failure.

```csharp
var temporary = PathName + ".tmp";
File.WriteAllText(temporary, json);
File.Move(temporary, PathName, overwrite: true);
```

These synchronous operations are deliberately limited to a small local draft. They must not grow into large attachment writes on the UI thread. Chapter 19 revisits storage, migrations, and stronger persistence boundaries. If this feature expands, move serialized writes behind an asynchronous interface with ordered operations; taking a snapshot before an await prevents later edits from silently changing the intended save.

The envelope includes schema version 1. Load rejects an unknown version, a missing draft, and null text fields. Malformed data stays on disk when reading fails, and the view model reports that it could not read the saved draft. It does not silently delete a customer's story. A subsequent explicit save can replace that file; a fuller recovery interface can offer export before replacement.

Save may accept an incomplete draft. Requiring a complete contact step before saving would defeat the purpose of saving unfinished work. A failed save keeps the open draft dirty and displays a retry message. A failed discard keeps the open values as well. Status text says “saved” only after the storage operation returns successfully.

### Confirm saving before changing the status

The view model’s save boundary is:

```csharp
public bool Save()
{
    try
    {
        store.Save(Draft); IsDirty = false;
        Status = "Draft saved on this device."; Changed(); return true;
    }
    catch (Exception ex) when (ex is IOException or UnauthorizedAccessException)
    {
        Status = "Could not save. Your edits are still open; try again.";
        Changed(); return false;
    }
}
```

A successful write clears `IsDirty`. The handled file errors leave the editable draft intact and keep the status specific about what failed. `Restore` separately protects current unsaved edits from being overwritten when a page reappears.

## Handle personal information deliberately

The story and contact fields can contain personal information. The demonstration uses a local, anonymous JSON draft; it provides no application-level encryption, account isolation, cloud synchronization, or backup exclusion configuration. Do not describe the app-data directory as encrypted storage merely because it is application-specific. Operating-system sandboxing and application encryption solve different problems.

The customer chooses when to save and can explicitly discard. The discard button asks before removing both open and saved values. This is a real product decision because discarding destroys customer input. Normal Back navigation does not require such a prompt: it preserves the shared in-memory session.

Use synthetic names and addresses when testing. Avoid logging the record, the JSON body, or the full story. When accounts arrive later, define which account owns a draft, what sign-out clears, what operating-system backups may retain, and whether anonymous drafts can migrate to a signed-in account. Do not ship account switching on top of a single anonymous filename without adding that boundary.

## Verify behavior before presentation details

The new SongRequestTests cover allowed and rejected lengths, final revalidation of earlier fields, incomplete contact data on earlier steps, story length boundaries, instrumental normalization, invalid email shape, and review invalidation. Store doubles demonstrate successful restoration and failed save/discard behavior without relying on a device filesystem.

A particularly useful test saves one draft, changes the story, then makes the next save fail. The expected result is threefold: the old saved draft remains unchanged, the new story stays in the open model, and the model remains dirty. A test that merely asserts that Save was called would miss the customer's actual requirement.

The test double does not prove file replacement, native navigation, screen-reader output, or restart behavior on Android or iOS. Run the portable suite first, compile the Android app, then complete the device scenarios in docs/device-checks.md. Record toolchain, source revision, platform, and actual result. See the current verification log for the recorded portable run and native compilation results; device behavior must still be observed independently.

## Guided Lab

Save, edit and recover.

1. Start a new request with an instrumental choice. Observe which vocal fields are hidden and whether their stored values are intentionally retained or cleared.
2. Enter the story and contact details, advance to review, then edit the story. Verify that the earlier review is invalidated rather than displayed as current.
3. Save a draft explicitly. Change the story again without saving and navigate away and back during the same process. Observe the in-memory state.
4. Restart the app and reload the draft. The expected persisted result is the last *saved* version, not an uncommitted edit.
5. Inject a draft-store failure. Confirm that the interface does not report success and does not discard the editable request.
6. Repeat the journey with a large font and screen reader on a real device; record the observed result.

**Expected result:** Review reflects the most recently validated input, explicit save controls persistence, and a failed save cannot masquerade as success. No part of this exercise submits a real customer order.

### Before you begin: saved and editable are separate states

Users reasonably expect an unfinished composition to survive moving between form steps. That does not automatically mean every keystroke should be written to permanent storage, particularly when the story contains personal details. Separate the live editing model from the saved snapshot, make the save action explicit, and explain which data survives process termination.

### Running journey: an anniversary at Long Lake

Use an invented customer throughout this lab: someone requesting a clean folk song for an anniversary at Long Lake. They choose vocals, add a family memory, then decide an instrumental may suit the occasion better. Preserve their written story while the relevant fields change. Use fictitious contact details and avoid putting a real family story into a shared fixture or screenshot.

## Worked Example

Use the anniversary request at Long Lake. Save the story as “An evening by the lake,” then edit it to “Our anniversary at the cabin” without saving.

| Action | Current editor | Last confirmed saved draft |
|---|---|---|
| Save the lake version | Lake story | Lake story |
| Edit to the cabin version | Cabin story | Lake story |
| Move to another step in the same process | Cabin story | Lake story |
| Restart and load | Lake story | Lake story |
| Save cabin version successfully | Cabin story | Cabin story |

If saving the cabin version fails, keep it visible as unsaved text. Recovery should not claim that the last confirmed disk value changed.

## Troubleshooting

- **A customer loses edits while changing steps:** Check whether the form controls write to shared editable state and whether any page recreates the view model unexpectedly.
- **An old review stays visible after editing:** Verify that changing validated input invalidates the review snapshot rather than presenting it as approved.
- **A saved draft differs from the latest typing:** Distinguish explicitly saved disk state from unsaved in-process edits. A failed save must not display a success message.

## Chapter Summary

The request builder separates editing, validation, persistence, and review. Customers can change musical direction, navigate between steps, and save an incomplete draft. Failures preserve their work. A review is a validated snapshot that becomes invalid when input changes; it is not an order confirmation.

## Exercises

1. Save a draft, edit its story without saving, leave the form, and return. Confirm that the unsaved story remains during the same process. Then restart the app and distinguish the last saved story from unsaved edits.
2. Add field-level focus routing for validation errors. Verify the first invalid field with TalkBack and VoiceOver, including the announcement and the next navigation gesture.
3. Replace the English form strings with localization resources. Check a long translation at large system text size and retain the same portable validation rules.
4. Add a failing-file-store integration test around a temporary directory when the storage abstraction is expanded in Chapter 19. Verify the previously saved bytes, rather than only an exception message.

## References

- Microsoft Learn, Entry: https://learn.microsoft.com/dotnet/maui/user-interface/controls/entry
- Microsoft Learn, Editor: https://learn.microsoft.com/dotnet/maui/user-interface/controls/editor
- Microsoft Learn, Accessibility: https://learn.microsoft.com/dotnet/maui/fundamentals/accessibility
- Microsoft Learn, File-system helpers: https://learn.microsoft.com/dotnet/maui/platform-integration/storage/file-system-helpers

## Editorial index terms

Custom-song requests; forms; conditional inputs; validation; draft preservation; process termination; email keyboard; Editor; semantic hints; file replacement; JSON envelopes; personal information; review snapshots.

