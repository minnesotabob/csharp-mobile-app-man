# Appendix A
# Targeted C# Refresher

This reference revisits the C# ideas that carry the application's mobile behavior. It assumes you can already read classes, methods and collections. Use it when a chapter's syntax is familiar but its ownership, lifetime or failure behavior is unclear.

Examples below are excerpts from the companion rather than a second application. Read the named complete files before changing them. No new C# feature is required simply because the book targets C# 15; choose language features for the clarity they bring to the boundary being implemented.

## A.1 Read a contract before reading its implementation

An interface describes the operations one part of the application may request from another. In src/GnazzosWorld.Core/Media/PlaybackSession.cs, IAudioPlayer includes these members; other members are omitted here:

```csharp
TimeSpan Position { get; }
Task<TimeSpan> OpenAsync(
    AudioItem item, PlaybackTicket ticket, CancellationToken ct);
void Play();
void Pause();
Task SeekAsync(TimeSpan target, CancellationToken ct);
void Stop();
```

OpenAsync produces a duration after asynchronous preparation. Play requests a transition without returning proof that sound is audible. Position is an observation supplied by the adapter. The full interface also publishes observations. This distinction lets portable policy reason about a player without pretending it implements native audio behavior.

An interface is useful when its alternatives matter: a deterministic player double for a policy test, and a platform player adapter for device execution. It does not remove the need to verify either implementation. Follow Chapter 27 for foreground ownership and Chapter 28 for background/system controls.

## A.2 Task and await describe completion, not a dedicated thread

A Task represents an operation's eventual completion. Task<TimeSpan> additionally carries a result. Await allows the method to continue when that operation completes; it does not promise that the operation ran on a new thread or that every continuation belongs on the UI thread.

The practical question is what may happen while a method is waiting. In the media owner, another user action or lifecycle event can make the selected source obsolete. In a page, navigation can end the visit. After an await, the code must still own the right to publish its result.

Keep asynchronous application operations awaitable. An unobserved task can fail after its caller has announced success or released a resource it still needs. An event handler may have a framework-required void signature; keep its asynchronous boundary short and handle outcomes deliberately. Do not turn every service operation into async void merely because the first caller was a button.

## A.3 Cancellation and result ownership answer different questions

Cancellation requests cooperation. It does not rewind a committed server transaction, guarantee that another process stopped, or by itself prove that an old callback cannot arrive. A version or generation check answers a second question: may this result still change the current state?

Open Presentation/DebouncedQuery.cs. This excerpt preserves the order of the actual statements:

```csharp
var current = ++revision;
active?.Cancel();
using var own = new CancellationTokenSource();
active = own;
```

The new revision invalidates earlier work. Cancel asks the previous delay to stop. Each invocation owns its own cancellation source, whose lifetime continues through its awaited work. The later publication check is:

```csharp
if (!own.IsCancellationRequested && current == revision)
    apply(text ?? "");
```

Both conditions matter. If an older operation ignores cancellation, its revision still prevents publication. Empty input applies immediately while invalidating older pending input. Finally clears the shared active reference only if that reference still names this invocation's source. Otherwise an old completion could erase a newer operation's cancellation handle.

The class explicitly assumes UpdateAsync and Cancel run from one serialized context, such as the page's UI thread. The revision counter is an ownership fence within that design, not a general replacement for synchronization between arbitrary threads. See Chapter 13 and the companion's deterministic debounce tests.

## A.4 Exceptions need a boundary and a meaning

An exception tells a caller that an operation did not return normally. It does not always tell the caller whether an external side effect occurred. If a server committed an order and the connection failed before the reply, catching an HTTP exception cannot settle whether another order should be created.

Use a boundary that can interpret the failure. The HTTP client distinguishes transport, deadline, cancellation and invalid-response outcomes. The order coordinator retains the original operation identity while reconciling uncertain acceptance. The screen chooses a useful message without copying arbitrary server details to the user.

A catch filter can make cancellation ownership precise. DebouncedQuery catches OperationCanceledException when its own cancellation source was canceled. That is different from labeling every exception canceled. Likewise, finally restores local lifecycle state even after a failure; it does not establish that remote work was rolled back.

For an exercise, trace a timeout after commit through Chapter 32. Name the last confirmed local state, durable operation key and next permitted action. The worked answer should preserve the key and reconcile the operation, rather than infer failure from a missing response.

## A.5 Nullable references are a model, not input validation

A question mark on a reference type communicates that null is an expected possibility. In CatalogItem.cs, ExternalUrl is Uri?, because an item may have no external destination. ReleaseDate is DateOnly?, representing an unknown date rather than an invented one. These choices let the interface explain absence honestly.

Compiler analysis helps track possible nulls in ordinary code. It does not establish that deserialized JSON, a database row or a platform callback satisfies the application's contract. Validate at those input boundaries. An identifier may be non-null and still empty, too long, duplicated or owned by another account.

The null-forgiving operator suppresses a compiler warning at a point where the programmer claims the value is present. It does not perform a runtime check. Before copying Current! from a state machine, inspect the transition that guarantees a selected item exists. If that guarantee does not hold in your new code, fix the state model rather than suppressing the warning.

## A.6 Records, identity and mutable collections

CatalogItem is a sealed record with stable Id separate from Title. A record provides useful value-oriented behavior, but the application's identity rule still comes from its contract. Two items with identical titles can be different works; a spelling correction need not create a new favorite identity.

A record is not automatically deeply immutable. If it contains a reference to a mutable list, other code may still change that list. Similarly, IReadOnlyList<T> restricts what a caller can do through that interface; it does not prove that no other owner can mutate the underlying collection.

PlaybackSession demonstrates an explicit snapshot decision. Its constructor materializes the supplied sequence with ToArray, validates the bounded queue and exposes Array.AsReadOnly. Later changes to the caller's original list do not redefine that session's queue. Follow the complete constructor for unique-ID and size checks.

Choose identity comparison deliberately. The catalog uses stable IDs, while presentation text has its own search rules. Do not replace an ordinal identifier comparison with a user-language comparison just because both operands happen to be strings. Chapters 12-13 explain the domain distinction.

## A.7 Delegates and events create ownership relationships

A delegate references code to call and can retain the object needed to call it. A lambda can also capture state. An event publisher that outlives a subscriber may therefore keep the subscriber and captured objects reachable.

BackgroundPlaybackOwner subscribes player.Observed += Observe. Its Dispose method cancels pending work, closes the session, removes that subscription and clears its Changed callbacks. The exact sequence matters; use the full source when studying failure handling and the disposed guard.

Garbage collection does not replace this cleanup. An object still reachable through a publisher is not garbage merely because the page is no longer visible. Conversely, a lower process-memory counter is not proof that private bytes were physically erased. Chapter 37's controlled retention investigation distinguishes subscription invariants from diagnostic reachability observations.

For a guided check, locate each subscription in the background lab and name its owner and release point. If you cannot identify a release point, investigate before adding a finalizer or a weak reference as a shortcut.

## A.8 IDisposable, using and asynchronous lifetime

Using arranges deterministic cleanup when execution leaves its scope. In DebouncedQuery, using var own remains alive across the await because the scope has not ended. If code instead starts work and returns without awaiting it, the scope may end while that work still uses the resource.

Dispose is not an operating-system shutdown promise. A mobile process can end without executing a final application callback. Save valuable customer state at explicit dependable boundaries. The request form confirms a save only after storage succeeds; an in-memory property or an intended Dispose call cannot provide that guarantee.

For an asynchronously disposable resource, use the supported await using pattern when cleanup itself must be awaited. Do not introduce it mechanically into synchronous types. Read the actual interface and lifetime requirements of the resource you own.

## A.9 Dependency injection and lifetime

Dependency injection makes construction and ownership visible. A view model can receive an external-browser interface rather than construct a platform browser itself. The composition root chooses the platform adapter. Portable tests can supply a controlled implementation that reproduces cancellation or failure.

Registration lifetime affects behavior. A process-shared request view model may preserve edits during navigation while still losing them on process termination. A transient page can own visit cancellation. An app-lifetime HTTP client has a different responsibility from a request-specific cancellation source. Registering a component as singleton is not a persistence strategy or a blanket guarantee of thread safety.

Start at src/GnazzosWorld.App/MauiProgram.cs when tracing the current application. Then follow the constructor dependency into its interface and selected implementation. Earlier source milestones can have different startup arrangements, so use docs/milestones.md rather than assuming the latest composition matches Chapter 4.

## A.10 A quick reasoning checklist

| When you see | Ask |
| --- | --- |
| await | What may become obsolete before continuation? |
| CancellationToken | Who owns cancellation, and what side effect can already have happened? |
| nullable property | Is absence valid, and where is external input validated? |
| record or read-only interface | What is the stable identity, and who owns referenced collections? |
| event subscription | Which object retains the subscriber, and who unsubscribes? |
| using or Dispose | Does all dependent work finish within this lifetime? |
| singleton registration | Which state survives navigation, and which survives a new process? |
| catch | Is this failure definitive, canceled, or still uncertain? |

Use these questions to read the implementation, not as a substitute for its tests. Chapters 5, 13, 17, 27-28 and 32 provide concrete examples of the resulting behavior.

## References

- C# statements and using: https://learn.microsoft.com/dotnet/csharp/language-reference/language-specification/statements
- Deterministic resource cleanup: https://learn.microsoft.com/dotnet/standard/garbage-collection/using-objects
- Companion source: https://github.com/minnesotabob/csharp-mobile-app-code
