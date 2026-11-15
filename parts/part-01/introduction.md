# Part I
# From Desktop and Web to Mobile

*Illustration brief: a Windows workstation linked visually to a phone and tablet, with a restrained book/music motif. Grayscale, generous negative space, and no generated code or tiny labels. Final illustration pending.*

A mobile application often begins with familiar work: a project, a model, a screen, and a way to get data onto that screen. It is tempting to treat everything that follows as a variation in controls. This Part starts with the operating environment because that environment determines what the controls and their supporting code must do.

The five chapters establish a common foundation. We first compare development approaches and investigate the assumptions that stop holding when software lives on a phone. We then turn the existing website into requirements for a native application, identifying which content is public, which state is personal, and where services become necessary.

Once the requirements are concrete, we prepare a Windows workstation, explain the additional iOS build boundary, and run an initial MAUI application. The first screen is intentionally small. Its value is that you can trace the project structure, startup, data flow, and debugging process without an elaborate framework hiding each step.

Testing completes the foundation. Catalog validation and pricing do not need a device to prove their basic behavior. By placing that logic in a portable library, we gain fast feedback and a useful boundary for later features. Device checks remain separate and become increasingly important as the application acquires lifecycle-sensitive behavior.

## The chapters in this Part

**Chapter 1, Understanding the Mobile Development Landscape,** compares native, cross-platform, hybrid, and browser-based approaches. It explains lifecycle, permissions, unreliable connectivity, touch, accessibility, and distribution through the application's intended journeys.

**Chapter 2, Defining Gnazzo's World,** maps the website's books, artists, songs, podcasts, and custom-song service into an application plan. It defines stable content identities and acceptance scenarios, and separates public discovery from signed-in customer features.

**Chapter 3, Preparing a Windows Development Environment,** sets up a repeatable toolchain and explains the relationship between Visual Studio, the .NET SDK, workloads, Android tools, and Apple build requirements. Its output is an environment record rather than a collection of unexplained installations.

**Chapter 4, Building and Debugging the First Application,** introduces startup, resources, pages, lifecycle observation, logging, and debugging. Readers run the first catalog screen and learn how to investigate a failure rather than simply replace code until it disappears.

**Chapter 5, Establishing Testable Application Foundations,** gives the application a small portable core and meaningful automated tests. It introduces service boundaries and test doubles only where they remove an actual dependency or make a behavior observable.

## What you will have at the end

You will have a defined application scope, a documented development environment, a starter that runs on a verified target, and portable tests for the first behaviors. You will also have a list of device checks that remain to be executed. That distinction matters: a foundation is dependable when its evidence is explicit, including the work that is not yet verified.
