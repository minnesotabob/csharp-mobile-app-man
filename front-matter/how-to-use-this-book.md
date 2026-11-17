# How to Use This Book

## Who this book is for

You should be able to read ordinary C# classes and methods, work with collections, and recognize asynchronous code. Intermediate experience building desktop or web software will help you connect familiar concepts to mobile examples. Prior MAUI, Android, or iOS knowledge is not required. Appendix A provides targeted refreshers rather than a second introduction to the C# language.

The material is independent of Mastering Modern C#. Owning that book is not a prerequisite. No chapter requires AI services or AI-development tools.

## Follow the application, then revisit by task

On a first reading, follow Parts I and II in order. They establish the environment, application boundaries, XAML, navigation, and test structure used later. Subsequent Parts develop catalogs and forms, connected/offline data, identity and MFA, media, customer workflows, and release engineering.

Each chapter identifies the capability it delivers, the earlier material it relies on, and the verification that makes its result credible. When a chapter includes an advanced topic, the explanation will identify what changes and why. Advanced sections should deepen the application rather than introduce a separate unexplained system.

Use the glossary, cross-references, and index when returning to a specific task. The subject index in this proof links to selected substantive section openings and uses this proof's page numbers. It is regenerated during typesetting; the final paperback index will be reviewed again after pagination stabilizes. The ebook will use linked targets.

## Code and examples

The companion repository is https://github.com/minnesotabob/csharp-mobile-app-code. Follow its README and tested-version record before building a milestone. Chapter tags and edition tags will be created only when their code is ready; a tag mentioned as planned is not evidence that a complete example already exists.

Listings in the manuscript focus on the code being discussed. Refer to the repository for complete projects and surrounding configuration. Sample data is deliberately small. An episode labeled demonstration is fictitious, and a link to a streaming service is not an audio file for our player. Media used for playback and downloads must be supplied with permission to distribute it.

Prices in teaching examples are snapshots with a version identifier. A production server remains responsible for validating a request and producing an authoritative quote. Do not copy sample settings into a live business without configuring and verifying the actual service.

## Choose the matching source checkpoint

Chapters 1–5 follow the Part I starter checkpoint recorded in the companion's docs/milestones.md. It displays a simple MainPage and has a recorded 37-case portable suite. Later source adds Shell navigation, forms, HTTP and an API; the Chapter 18 portable suite has 245 cases. Both can be valid milestones while showing different screens and totals.

Use Chapter 3's dedicated exercise checkout instead of changing an existing working copy blindly. Read the source ID before following a listing. The companion docs/labs/part01-foundation.md provides a consolidated guided lab, while docs/learning-guide.md maps later source and tests. A chapter tag is still a promise only after it is actually created and verified.

The chapter drafts include What You'll Learn and a separate Chapter Summary. Guided exercises explain expected outcomes and worked reasoning; independent exercises ask you to extend that understanding. Their first instructional passes still need final consistency and technical acceptance review. An expected device result is labeled as an expectation until it has been observed, and an exercise's proposed failure/restoration sequence is not presented as a test run performed by the author.

## Equipment and verification

The early portable examples need the documented .NET SDK and can be tested without a mobile workload. Android development additionally needs a compatible workload, SDK/JDK, and emulator or device. iOS builds and signing require compatible Apple tooling on a Mac, whether accessed through a supported remote workflow or used directly.

We record compilation, test execution, emulator checks, hardware checks, and store submission as separate kinds of evidence. A successful unit-test run does not imply that an iPad layout or MFA recovery process has been tested. Environment and verification records accompany the code so that readers can see these boundaries.

## Working safely with your own application

Keep secrets out of source control and screenshots. Use demonstration customers and sandbox payments while learning. When the identity chapters arrive, use the selected provider's supported enrollment and recovery features; do not replace them with a password or one-time-code implementation improvised for the sample.

Exercises encourage you to change a rule, explore a failure, or extend a feature. Save a known working milestone first. Understanding how the application recovers when a step is canceled is as valuable as seeing its happy path complete.
