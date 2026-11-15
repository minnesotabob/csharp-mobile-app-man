# Teaching and sample standard

Approved direction — November 15, 2026

John's instruction: "Keep the current sophistication level, but provide enough
documentation and working samples to make it a valuable resource and learning tool."

## Scope and length

Retain the current C# 15 / .NET 11 / MAUI 11 audience, 40-chapter progression and
intermediate/advanced engineering scope. Architecture, cancellation and result
ownership, idempotency, API contracts, storage/migrations, offline synchronization,
identity/MFA, media, payments and release engineering remain in the plan. No split
into volumes or removal of advanced subjects has been approved.

The former 800-page figure is a historical planning estimate, not a production quota.
No replacement page target has been approved. Estimate length from representative
expanded chapters after they meet the teaching standard. Preserve the 8x10 format,
11-point body and readable code; add instruction where the reader needs it.

## Chapter acceptance criteria

A topic draft and a passing build do not establish a finished teaching chapter.
Before calling a chapter ready for reader review, provide:

1. A What You'll Learn opening with 3–5 specific outcomes, prerequisites, what the reader will build, starting source revision and tool setup. Keep the opening concise.
2. A plain explanation of the problem and the decisions/tradeoffs behind the design.
3. A numbered implementation walkthrough: actual file paths, project references,
   registrations/configuration, necessary permissions and complete runnable source.
4. Short explained listings linked to the complete surrounding implementation.
   Identify omissions and preconditions; avoid unexplained copy/paste fragments.
5. Reproducible build/run commands, expected output or visible behavior, and an
   explanation of what each verification establishes.
6. A happy path and meaningful failure/cancellation/recovery path. Preserve data
   ownership and distinguish simulated services from real integrations.
7. A troubleshooting table with observed symptom, likely cause, diagnostic check
   and corrective action. Link official references where platform behavior matters.
8. Necessary diagrams and verified screenshots, captions and accessible descriptions.
   Authored diagrams and conceptual images must not be labeled runtime observations.
9. A distinct Chapter Summary of roughly 100–150 words, followed by exercises.
   Recap key lessons and connect the next step without repeating the opening.
   Include at least one guided exercise with a worked answer/check, plus an independent
   extension exercise. Explain reasoning rather than only giving the final code.
10. Explicit verification status: compilation, portable tests, server integration,
    real socket/TLS, Android/iOS/device observations and release checks stay separate.
11. Cross-references, source/milestone mapping, terms for the index and current
    dependencies. Introduce a new abstraction only with an explained purpose.

Do not add low-value tests solely to increase test counts. A regression case should
exercise a boundary, failure or behavior that could realistically be wrong.

## Working-sample acceptance

- Keep one evolving application with complete source and explicit reader milestones.
- Use repeatable fictitious fixtures; document fixture versions and expected results.
- Record the tested source revision and dependency/toolchain versions.
- Provide a way to run portable rules without requiring a mobile workstation.
- Provide a way to run backend examples locally with cleanup and bounded waiting.
- Document native prerequisites and actual observations separately. Pending device
  work remains pending even after successful Android compilation.
- Keep credentials, private customer data and live payment/deployment configuration
  out of distributable samples. No production activation follows from a tutorial.
- A mock/fixture implementation is useful for learning when it is labeled and the
  transition to a real integration is explained and verified separately.

## Revision work

The earlier 158-page proof covered Chapters 1–18 after their initial
instructional revision. Chapter 19 now exists as a new draft with real SQLite
companion tests. The new 19-chapter layout must pass its own proof workflow.
Native observations and screenshots remain pending. Do not characterize the
manuscript as technically or publication ready from successful CI alone.

Continue verifying matching code and chapter revisions, build the new 19-chapter
print proof, and keep adding working labs and high-value troubleshooting. Continue
technical verification when code changes; documentation-only edits need editorial
and link/command review rather than identical test reruns.

The companion docs/learning-guide.md provides the current starting paths and sample
map. docs/labs/ch18-api.md is the first explicit guided lab with worked checks.
Those additions start the instructional pass; they do not certify every chapter.
