# Chapter 27
# Audio Playback and Podcast Progress

A listener discovers Minnesota Bob in Gnazzo's World and starts an episode before leaving home. Halfway through, the listener pauses, opens a book page and later returns. The application should restore a useful position without unexpectedly starting sound. If the listener chooses another item while an old native event is waiting, that event must not rename the player, mark the wrong episode completed or restart old audio.

Those promises require three cooperating parts: playback policy, a native player and durable progress. We will keep their responsibilities separate, use original bundled timing files and build a foreground player before adding background/system controls in Chapter 28. The timing fixtures make the sample distributable; they are not recordings of Minnesota Bob or a real podcast.

## What You'll Learn

1. Separate an audio-service interface, playback policy and platform decoder observations.
2. Load, play, pause and seek within an explicit foreground lifecycle.
3. Prevent obsolete source events from changing the current queue item.
4. Save absolute-time checkpoints by stable media identity and revision.
5. Verify policy/storage behavior independently of actual decoding, seeking and audible output.

**Prerequisites:** Chapters 19, 20 and 26, the SDK in `global.json` and the documented native workload. The previous companion checkpoint is `7a32c46e1246352fcc275ebf52d920bb2a3ccefd`. Chapter 27 source begins at `d500294db4b3dead74ba7952fa6bf85b5071a973`; use the corrected revision and executed evidence recorded in `docs/verification.md`. The app adds `CommunityToolkit.Maui.MediaElement` 12.0.0. Its Android minimum becomes API 26; earlier checkpoints retain their own platform requirements. iOS compilation and native package/SDK compatibility remain separate Mac work.

**What you will build:** `PlaybackSession`, the `IAudioPlayer` port, `AudioProgressDatabase`, `ToolkitAudioPlayer`, a native `AudioLabPage`, original WAV resources and portable tests. Home opens the foreground audio lab. It uses anonymous installation-local progress, a manual bounded queue and no autoplay. It does not migrate account data, play a streaming-service catalog, download customer deliveries or enable background audio.

## 27.1 Begin with media you can actually play

A Spotify track page identifies a destination in another service. It is not an audio source that our native decoder can consume, and the ability to hear it in that service does not establish permission to redistribute it. The same distinction applies to a podcast listing and its authorized media file.

This sample includes two original mathematical timing fixtures: short, quiet tapered tones spaced two seconds apart. They are mono, 16-bit PCM WAV at 8000 Hz, lasting 10 and 14 seconds. The low sample rate and sparse signals keep teaching assets small. They are decoder/timeline fixtures, not a production mastering recommendation or a realistic spoken podcast.

`eng/generate_demo_audio.py` contains the complete generation formula. `samples/audio-fixtures.json` records provenance, format, duration and SHA-256 hashes. The resources live in the native project's `Resources/Raw` folder and are packaged as `MauiAsset` items. The distribution tests verify the committed source files against that manifest. They do not listen to the audio or prove a device found the packaged resource.

For a real episode, obtain a distributable file and its metadata, then verify the target device's decoder and timeline. Container, codec and platform support are separate considerations; a filename extension alone is insufficient. A WAV that a development machine reads may still expose a packaging or playback problem on a phone.

## 27.2 Choose the playback boundary

The core's `IAudioPlayer` describes what the page needs from a device adapter: open one item, observe state, read position, play, pause, seek and stop. It does not expose native view classes or claim that every source supports every capability.

```csharp
public interface IAudioPlayer
{
    event Action<PlaybackObservation>? Observed;
    TimeSpan Position { get; }
    Task<TimeSpan> OpenAsync(AudioItem item,
        PlaybackTicket ticket, CancellationToken ct);
    void Play();
    void Pause();
    Task SeekAsync(TimeSpan target, CancellationToken ct);
    void Stop();
}
```

`PlaybackSession` is the portable policy. `ToolkitAudioPlayer` owns the actual `MediaElement` instance and translates native observations. `AudioLabPage` composes controls, lifecycle and the local store. Tests can exercise the policy with supplied observations without pretending those observations came from a physical decoder.

The current resource contract accepts a bounded bundled WAV filename. A URL or arbitrary file path is rejected. That is a deliberate first implementation, not a claim that the interface implements streaming and downloads already. Remote/public and authenticated/private sources need their own transport, authorization, buffering and storage contracts.

## 27.3 Model selection and observed state

![Figure 27.1. A new selection receives a fresh ticket and enters Loading. Only an accepted open and any completed restore make it Ready. Playing/Paused/Buffering reflect observations; Ended or Failed is terminal for that source, and closing invalidates late work. Replay opens a fresh source.](../assets/figures/fig-27-source-ownership.png)

The queue contains at most 32 items with distinct stable IDs. Each `AudioItem` has an ID, a media revision, a title and an optional bundled resource. A missing resource represents the explicitly unavailable demonstration item. Selection clears the previous duration and position immediately, so unavailable media cannot inherit a previous item's apparent readiness.

The states are Empty, Loading, Unavailable, Ready, Playing, Paused, Buffering, Ended and Failed. They represent meaningful differences for controls and persistence. Loading is not Playing. A button press that requests playback is not an observation that sound is advancing. Buffering does not by itself indicate either completion or a new position.

`BeginSelection` increments a generation and returns a `PlaybackTicket`. Every observation carries the ticket captured when that native source was created. A different selection, including A-to-B-to-A, requires a new ticket. Closing also increments the generation. An old item ID matching the current ID does not revive an old source.

End and failure are terminal for a source. A queued Playing event arriving after Ended must not undo completion. Explicit replay creates a fresh source and ticket. This is more precise than trusting the arrival order of native callbacks or trying to infer whether an old event represented a new user command.

## 27.4 Add the maintained native player

The app project pins `CommunityToolkit.Maui.MediaElement` 12.0.0 alongside MAUI 11.0.10. `MauiProgram` initializes the toolkit with Android foreground-service support disabled. The chapter intentionally owns foreground playback only; no background service or iOS background-audio entitlement is added.

The installed package exposes the builder extension in `CommunityToolkit.Maui` and names its flag `isAndroidForegroundServiceEnabled`. Initial compilation caught both differences from the overview examples. The bootstrap uses:

```csharp
using CommunityToolkit.Maui;

var builder = MauiApp.CreateBuilder().UseMauiApp<App>()
    .UseMauiCommunityToolkitMediaElement(
        isAndroidForegroundServiceEnabled: false);
```

The Android activity uses the documented resize/single-task setup. Its minimum supported API rises from 24 to 26 for this media capability. That affects the current expanded app, not the requirements of an earlier reader checkpoint. Record the package, target frameworks, native workload and actual build outcome together. An older API-reference page can describe an earlier toolkit release, so do not assume every copied signature matches the pinned version.

`ToolkitAudioPlayer.OpenAsync` creates a fresh `MediaElement` and fresh event closures for every source. It disables autoplay, looping, native transport controls and screen-on behavior, sets fixture metadata, adds the element to the page host and applies `MediaSource.FromResource`. The control remains a real hosted native view even though the chapter supplies its own buttons.

Opening has a 20-second bound. `MediaOpened` supplies duration; `MediaFailed` produces a sanitized failure. The adapter does not copy raw native errors or resource paths into the customer's message. A zero or unsupported duration is refused by the policy because this sample expects bounded on-demand media, not live radio with an unknown timeline.

## 27.5 Reject obsolete native events twice

The adapter checks that the event belongs to its current element, then checks again inside the UI-dispatched action before publishing the observation. The portable session separately checks the ticket. These checks protect different ownership transitions: the adapter's native resource and the model's selected source.

```csharp
host.Dispatcher.Dispatch(() =>
{
    if (ReferenceEquals(current, element))
        Observed?.Invoke(new(ticket, signal,
            element.Position));
});
```

A callback can already be queued when the listener switches items. Disposing the old view does not prove that every queued callback vanished. Conversely, model fencing does not release a native decoder that still holds resources. The implementation needs both cleanup and rejection of obsolete results.

The policy and page are UI-thread-affine. Do not call them concurrently from arbitrary workers or attach one player to multiple windows. The sample's guard serializes page actions, while lifecycle cancellation invalidates unfinished work. A larger playback service will need an explicit owner beyond one page when background operation is introduced.

## 27.6 Restore a useful position without autoplay

Progress is stored as absolute timeline ticks, keyed by item ID and media revision. It does not reuse the earlier reading-percent field. A percentage loses the concrete seek position and can become misleading when media length changes.

The loading sequence reads a saved checkpoint, opens the native source, validates the reported duration and computes a restore target. A completed checkpoint reopens at zero. Another item or revision does not inherit the position. A saved position at or beyond the new duration also restarts at zero rather than asking for an invalid seek.

```csharp
var saved = progress.Read(item);
var duration = await player.OpenAsync(item, ticket, ct);
var resume = session.ResumeTarget(ticket, duration, saved);
if (resume > TimeSpan.Zero)
    await player.SeekAsync(resume, ct)
        .WaitAsync(TimeSpan.FromSeconds(10), ct);
```

The surrounding method checks cancellation and current ownership, then marks Ready using the player's observed position. It does not publish the desired target as if the device had reached it. A device may round a seek, and a failed/canceled seek must not become a success checkpoint.

No autoplay follows restoration. The customer chooses Play after the app shows the loaded item and observed position. This makes a return to an episode predictable and avoids unexpected sound when a page is merely reopened.

## 27.7 Play, pause and seek deliberately

The Play button requests native playback only from an eligible state. Playing is confirmed through the adapter's state observation. Pause requests native pause, captures the last observed position and attempts a local save. The page's status distinguishes playback state from whether persistence succeeded.

Back/Forward move five seconds within the known duration. `SeekTarget` clamps the requested target but does not mutate the recorded position. After the native seek completes, the page reads actual position and saves that observation. Explicit seek waits are bounded to ten seconds. On a failed/timed-out action, the page makes the source unusable until reload and requests native cleanup, preventing another control from racing the same unresolved source operation.

The short timing fixtures are intentionally useful for boundary checks. A backward seek near the start should clamp to zero. A forward seek near the end should stay within duration. Listen to the timing pattern while comparing the displayed position; a changing label does not establish audible seek behavior.

Completed playback produces a completed checkpoint at duration. A late Position or Paused event cannot turn it back into partial playback. Replay reloads the same item with a new ticket, restores the completed checkpoint to zero and then responds to the explicit Play action. Completion does not automatically start the next queue item in this chapter.

## 27.8 Save only what has been observed and committed

`AudioProgressDatabase` uses a separate SQLite file named `anonymous-audio-progress.sqlite3`. One small row contains item/revision, position ticks, duration ticks and completed status. The schema does not contain credentials or a signed-in account. It is installation-local anonymous progress and is not encrypted or synchronized.

The store validates bounds before writing. A completed checkpoint must have position equal to duration. One upsert commits the new row atomically. A rewind is allowed to save a lower position; choosing the maximum position would undo the listener's deliberate return to an earlier passage.

The page attempts periodic saves every five seconds and at meaningful boundaries: pause, successful seek, selection/navigation and foreground suspension. A save message appears only after the SQLite call succeeds. If writing fails, the earlier confirmed row remains the recovery point. This is a checkpoint contract, not a guarantee that the latest audible sample survives arbitrary termination.

These are small synchronous SQLite operations in a teaching UI. A lock serializes one instance's connection; it does not eliminate storage latency or provide cross-process coordination. Observe native responsiveness and contention before extending the database or moving it into a long-lived service. Do not assume an Async suffix would make SQLite work nonblocking without checking the adapter's actual behavior.

## 27.9 Stop when the foreground contract ends

Navigation away and `Window.Stopped` both request pause/save, invalidate the model generation and stop/disconnect the native element. Canceling the pending action prevents an unfinished open/seek from publishing Ready later. On return, the listener explicitly loads and plays again; the app does not claim continued background playback.

Cleanup first removes current-element ownership so queued native events are refused. It then stops playback, clears the source and disconnects the handler, with cleanup attempted even if an earlier step fails. If cleanup cannot be confirmed, the page does not claim that the device was silent. Actual native disposal and audible stop behavior remain device observations.

This foreground rule does not implement every interruption. A phone call, audio-focus loss, a headphone change and a locked screen involve platform behavior that Chapter 28 will address. The lifecycle worksheet records these separately. A passed policy test cannot tell us whether a particular phone routed audio correctly after a call.

The Forget selected progress action suspends playback before removing the row. Otherwise a timer could immediately recreate the checkpoint the listener just removed. A later deliberate playback may save new progress. This action removes one local checkpoint, not a provider account, downloaded file or another device's listening history.

## 27.10 Explain unavailable media and recovery

An unavailable queue entry never opens the native adapter. A missing packaged file, unsupported codec or native failure is a different condition: the attempted source becomes Failed and controls require explicit reload. Neither case should display the previous episode's duration or report the current one completed.

A corrupt checkpoint is refused rather than silently treated as a valid resume. The page gives an actionable message and the explicit Forget selected progress reset. A controlled storage error leaves saving unconfirmed. Do not erase all listening history just because one record failed to load, and do not replace the error with a successful “saved” message.

The resources and messages are deliberately small English-language lab UI. Full localization, screen-reader announcements, large-text focus and recovery usability require the native pass. Even with simple vertical controls, verify the complete journey on a narrow phone and tablet rather than judging accessibility from a screenshot alone.

## 27.11 Extend to streaming and account progress only after defining the boundary

A public remote episode needs a reviewed HTTPS media endpoint, buffering/seek behavior and an actual native network test. A network connection hint cannot establish that the media host is reachable or that its timeline supports seeking. Redirect, caching and timeout behavior in the native player must be reviewed independently of the earlier JSON client.

A private customer delivery also needs authorization at the service/storage boundary. Do not attach a customer access token to a public streaming-service URL or assume the `ProtectedRequestClient` configures the media control's transport. The chapter's player has no private HTTP adapter, range-download implementation or authenticated cache.

Account-owned listening progress needs another deliberate step. Derive its owner from the accepted session, decide whether synchronization is optional, fence old-account writes and define sign-out/deletion behavior. The current anonymous file must not be assigned to whoever next signs in. Chapter 25's lifecycle contract and Chapter 26's threat model provide the questions, not an automatic migration.

Keep source revision and content identity distinct. Changing the app build does not necessarily change an episode's media revision. Replacing audio bytes or changing their timeline should prompt a new media revision and an explicit resume policy. Stable IDs help find the same item; revisions protect the meaning of a saved position.

## Guided Lab: hear, pause and return

Use `docs/labs/ch27-audio-progress.md`. Portable checks run without a mobile workload:

```powershell
dotnet build tests/GnazzosWorld.Core.Tests -c Release
dotnet run --project tests/GnazzosWorld.Core.Tests `
    -c Release --no-build
```

1. Inspect `DemoAudio`, the WAV manifest and generation script. Verify that the sample ships original resources and that the unavailable item has no resource. Do not substitute an external music-service page.
2. On the supported Android setup, build and launch the app. Record source, SDK, toolkit, device/OS and volume. Choose Home > Open foreground audio lab.
3. Load timing chimes. Expected: Loading then Ready, with no sound until Play. Verify actual audible output and advancing native position.
4. Pause/save midway and reload. Compare the observed position with the last confirmed checkpoint; choose Play explicitly. Exercise backward/forward seeks and listen to the timing pattern.
5. Let the item end, then replay it. Expected: a new source/ticket and zero-position start. Change items and load the unavailable entry; no previous source should reappear.
6. Navigate away and background the app separately, including during loading/seeking. Expected: cancellation, checkpoint attempt and native stop; return requires an explicit action. Record actual audible behavior, not just status labels.
7. Forget selected progress and reload. Use a controlled development write failure to verify the earlier-save message and recovery. Never damage a real customer's database to create a tutorial failure.
8. Repeat the supported native scenarios on iOS after its Mac build is established. Record pending cells honestly until those observations exist.

## Troubleshooting

| Symptom | Diagnostic check and corrective action |
|---|---|
| Ready appears but no sound after Play | Check volume/output route and real decoder state; a label is insufficient evidence |
| Media fails before Ready | Verify packaged resource, pinned toolkit initialization and reported duration; keep errors sanitized |
| Old item completes the current one | Inspect fresh-element ownership, ticket capture and dispatcher recheck |
| Seek displays an exact target immediately | Separate requested target from native observed position after completion |
| Resume uses an older location | Inspect last confirmed write, item/revision key and save failure; do not promise an unsaved sample |
| Forget progress appears ineffective | Stop timer/source before removal, then distinguish deliberate later playback from resurrection |
| Playback continues after leaving | Review native stop/disconnect and lifecycle observation; background behavior is not enabled by policy labels |
| Android workload or toolkit fails to build | Compare the exact SDK/package/platform versions and Chapter 27 API-26 minimum with the verification record |

## Verification record

At corrected source `c73f3cd25e175d7e89de84f3cbdaa9bacdd86af6`, the portable Release build has zero warnings/errors and all 394 cases pass, including 34 new playback/storage/fixture cases. The matching API/probe builds are clean and 46 API cases pass, as do the public loopback smoke and both earlier console labs. The toolkit bootstrap corrections and native failure/close cleanup are included in this source; matching Android compilation succeeds with zero final compiler warnings/errors. The earlier SDK dependency-setup warning remains documented separately in `docs/verification.md`. The portable suite supplies observations to the policy and exercises real SQLite files for restart persistence, revision isolation, corruption, rewind and failed-write recovery. It also verifies the source fixtures' PCM headers, durations and hashes. These are not decoding or listening tests. `docs/verification.md` records the executed source, totals, API regression and Android build separately.

The native adapter/page is subject to its own compilation and device evidence. Actual audible playback, packaged resource lookup, seek rounding/cancellation, foreground stop, memory/resource cleanup, accessibility, iOS and screenshots remain pending until observed on the documented platforms. Background/system controls, remote streaming, downloads and account synchronization remain outside this milestone.

## Chapter Summary

A dependable player separates commands, native observations and durable progress. The audio port hides the platform control, while the portable session gives each selected source a fresh ticket and refuses obsolete events. Opening and restore complete before Ready, and neither loading nor returning to a checkpoint starts playback automatically. Absolute-time checkpoints belong to a media ID and revision; the last successful write defines recovery after interruption. Completion is terminal for that source, replay opens a new one, and leaving the foreground requests save and cleanup. Original timing fixtures make the lab reproducible without borrowing a streaming catalog. Chapter 28 extends the ownership model beyond one visible page to background playback, system controls and platform audio interruptions.

## Exercises

### Worked exercise: an old episode ends late

The listener loads timing pulses after timing chimes. A delayed Ended callback from chimes arrives. Both assets are valid. Should the new item become completed?

**Worked answer:** No. The old native element fails the adapter ownership check, and its ticket fails the policy check. Completion belongs to that source instance, not merely to a valid file or familiar item ID. The A-to-B-to-A test also requires a new ticket on the return to A. Native cleanup still matters even when the model refuses the event.

### Worked exercise: a successful seek followed by failed saving

The device reaches 7.8 seconds, but the checkpoint write fails. The earlier confirmed save is 4 seconds. What can reopening promise?

**Worked answer:** It can restore 4 seconds, provided that row and media revision remain valid. Native seek completion established the current observed position, not durable persistence. Report saving as unconfirmed and retain the earlier row. The injected SQLite-failure test verifies preservation and retry, while actual device storage failures require separate observation.

### Independent extensions

1. Design a real spoken-episode fixture with permission to distribute it. Specify content identity, media revision, format, timeline and device acceptance evidence.
2. Define a future queue auto-advance policy. Include cancellation during the next open, an unavailable next item, repeat behavior and whether the listener explicitly enabled continuous playback.
3. Design account progress migration without implementing it. Decide which anonymous values may be offered for import, how the customer confirms the owner and what sign-out/deletion must clear.

## Official references

- Microsoft, MediaElement overview, sources and native setup: https://learn.microsoft.com/dotnet/communitytoolkit/maui/views/mediaelement
- Toolkit bootstrap source: https://github.com/CommunityToolkit/Maui/blob/main/src/CommunityToolkit.Maui.MediaElement/AppBuilderExtensions.shared.cs
- Toolkit package 12.0.0 and target dependencies: https://www.nuget.org/packages/CommunityToolkit.Maui.MediaElement/12.0.0
- Microsoft, MAUI lifecycle: https://learn.microsoft.com/dotnet/maui/fundamentals/app-lifecycle
- Microsoft, SQLite transactions and failure handling: https://learn.microsoft.com/dotnet/standard/data/sqlite/transactions

The overview and API-reference pages can target different toolkit releases. The pinned sample's matching build and actual platform observations are the evidence for its implemented behavior.

Index: audio service; MediaElement; foreground playback; source ticket; queue; seek; buffering; absolute progress; media revision; checkpoint; WAV fixture; native disposal.
