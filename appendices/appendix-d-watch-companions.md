# Appendix D
# Watch Companions and Future Extensions

A watch is useful when a person wants one small action while their phone is out of reach. It is a poor place to reproduce the full custom-song form or a long catalog. This appendix outlines an optional extension; no watch project, device build, data channel or store package is implemented by the companion.

## D.1 Begin with the smallest useful promise

For Gnazzo's World, a plausible first experiment is a playback status and pause action for media already selected on the phone. Another is an innocuous status summary that opens the phone application for detail. Both preserve the principle that personal story entry, quote review, payment and account recovery belong in an interface that can explain them adequately.

A watch display must distinguish confirmed state from a last-known snapshot. If communication is unavailable, the interface should not announce that a command succeeded merely because a tap was recorded. Define what is useful while disconnected before adding a transport.

| Proposed feature | Useful boundary | Work still required |
| --- | --- | --- |
| Pause existing phone playback | Send a narrow intent; observe actual player state | Native system/media and device acceptance |
| Last-known progress | Identify item/revision and observation age | Data transfer, stale presentation and privacy |
| Generic order notification | Show limited information; open phone for detail | Provider delivery and authorized navigation |
| Full request editing | High input and review burden | Separate product design; not proposed here |
| Watch-only commerce | New identity/payment/offline surface | Independent design, provider and store work |

This is a product-selection table, not a promise that an existing MAUI page can be resized into a watch application.

## D.2 Choose the platform path explicitly

Microsoft's supported-platform documentation describes MAUI's phone/desktop targets and additional Tizen support. It does not establish a supported MAUI watchOS application target. Do not invent a net11.0-watchos target or assume the current project compiles a watch bundle.

For Apple Watch, investigate Apple's native watchOS application architecture and the selected iPhone relationship. Apple documents Watch Connectivity for communication between paired iOS and watchOS applications, including transfers whose delivery is managed by the system. A particular transport or callback still needs its own implementation and device observations.

For Wear OS, Google's guidance emphasizes focused watch tasks and describes Compose for Wear OS as its recommended UI approach. The phone's Android target is not evidence that its UI, dependencies or lifecycle are suitable for a watch. Select and verify the actual watch tooling before planning shared code.

Some portable domain rules may remain useful: stable identities, bounded message shapes and stale-result rejection. Reuse those rules when a real shared build boundary exists. Keep native presentation, capabilities, packaging, pairing and lifecycle work explicit. Existing C# source does not remove the need to evaluate the platform's supported implementation route.

## D.3 Keep authority on the correct side

A message saying pause is an intent. The current phone playback owner decides whether it applies to the current session. Include a bounded content/session identity in a proposed protocol so an old delayed action cannot control a newly selected item by accident.

For a customer-specific action, the server still owns authorization. Do not copy a long-lived confidential credential onto another device simply because pairing exists. Define account switching, lost-device behavior, sign-out and data removal for each endpoint. Treat the watch's cached display as another privacy surface.

Avoid sending a customer's full song story, contact information or private delivery URL to a generic glanceable view. Decide what can appear on a wrist or notification preview while another person can see it. A friendly label is not a substitute for the same ownership checks used by the phone and API.

## D.4 Rehearse delay and disconnection

A proposed protocol needs at least these cases: the phone is reachable; the phone is temporarily unreachable; a queued message arrives after selection changes; either application restarts; the customer changes account; the watch is removed or replaced. Do not assume an immediate live channel is always available.

A useful design exercise is to sketch the pause journey. The watch shows a last-known item. The user taps Pause. While the message is delayed, the phone selects a different item. When the old intent arrives, should it affect that item? A conservative design checks the intended session identity and reports a stale or unconfirmed result instead of acting on an unrelated session. The final choice should be explicit and tested on the selected native path.

For each observation, record watch model/OS, paired phone, both build identities, communication mode and actual outcome. A portable message-policy test cannot establish watch delivery timing, energy behavior or background execution. Preserve those pending rows until they have been observed.

## D.5 Decide whether the extension earns its maintenance

A watch companion adds a second release and support surface. It needs accessibility review, supported OS/tooling, data retention, compatibility with older phone builds, diagnostic handling and actual distribution checks. Its value must justify that continuing work.

Start with a prototype that proves one useful task. Stop if the result mostly duplicates existing system media controls or creates a confusing source of stale state. The phone application and its reliable customer journeys remain the main project; a watch extension is an independently scoped future decision.

## References

Primary sources checked November 17, 2026. No watch implementation or platform build is claimed.

- Microsoft supported platforms: https://learn.microsoft.com/dotnet/maui/supported-platforms
- Apple Watch Connectivity: https://developer.apple.com/documentation/watchconnectivity
- Google Wear OS app design and tooling: https://developer.android.com/training/wearables/apps
