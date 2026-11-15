# Preface

A website gives a reader a place to discover a book, a listener a way to find a song, and a customer a route to request something personal. A mobile application can carry those experiences further. It can remember a favorite, restore a listening position, keep useful material available without a connection, and return someone to an unfinished request. Making those experiences dependable is the work this book explores.

The application we build grows from johngnazzo.com, a website for my books, music, podcasts, and custom-song service. That mix makes a useful teaching project because its features have reasons to exist. A book catalog gives us collections and detail pages. Music and podcasts introduce media controls and interruptions. Custom-song requests demand more careful forms, validation, and business rules. Customer accounts bring authentication, multifactor authentication, and authorization into an application that has personal data to protect.

You do not need to be an author or musician to use the techniques. A product catalog, training library, field-service application, or membership service faces many of the same questions. What happens when a connection disappears? Which data belongs on the device? How do you distinguish a canceled operation from a failed one? How do you verify that a customer can access only their own records? The examples use this particular creative business to make the questions concrete.

This book assumes you have written C# and are comfortable with intermediate desktop or web development. It does not assume that you know mobile application lifecycles, native navigation, device permissions, app signing, or store distribution. Those ideas receive their own explanations. Where a familiar C# technique becomes important in a new setting, we revisit it with a mobile example rather than sending you to another book.

Our development path begins on Windows. We use C# 15, .NET 11, and .NET MAUI 11, and explain the tools necessary to work with Android and iOS. A shared codebase does not remove platform requirements. In particular, the iOS build and signing process still involves Apple's tools on a Mac. The environment chapter makes that boundary explicit so readers can plan their equipment and follow the early Android exercises without confusion.

Testing accompanies implementation. We begin with small, portable tests of catalog data and business rules, then expand to storage, API behavior, authorization, and complete user journeys. We also distinguish those tests from emulator and physical-device checks. A calculation can be correct in a unit test while the keyboard hides the submit button; both problems matter to the person using the application.

The destination is a candidate for public release. That means we must discuss loading states, errors, accessibility, account recovery, deletion, deployment, and maintenance as seriously as the first successful screen. Those responsibilities shape the architecture from the beginning, but we introduce them in manageable steps.

You will see code that evolves. Early chapters use the smallest useful design, and later chapters explain why a more capable design becomes necessary. The companion repository records that progression. My aim is for you to understand what each abstraction buys you, when it becomes worthwhile, and how to verify the behavior behind it.

John F. Gnazzo
