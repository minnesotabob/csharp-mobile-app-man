# Draft V2 editorial revision

November 18, 2026. Preserve all forty chapters and the agreed technical depth.

## Review findings and revision order

1. Rebuild Part II instruction before polishing later prose. Chapter 6 currently has
   two fenced XML examples; Chapters 6–11 contain roughly 1,700–2,300 words each.
   Add coherent, explained XAML/C# walkthroughs drawn from the companion application,
   explicit file placement, expected screen behavior, guided labs and worked exercises.
   Measure usefulness by whether a reader can implement the feature, not code percentage.
2. Standardize the chapter template: learning goals, prerequisites, deliverable,
   guided lab, worked example, troubleshooting, summary and exercises. Keep conceptual
   chapters proportionate rather than inserting artificial code.
3. Move commit hashes, CI history, recorded test totals and editorial pending notes
   into maintainer verification records. Retain actionable reader prerequisites,
   supported limitations, security requirements and reproducible checkpoint access.
4. Audit the C# 15 title promise against official language documentation and the
   actual compiler/toolchain before adding feature instruction. Distinguish new
   language features from older C# features used on a C# 15 target. Unverified feature
   claims must not enter the manuscript. Reassess title wording if coverage remains weak.
5. Plan 50–75 purposeful native screenshots across catalog, search, navigation,
   forms, identity, media, downloads, notifications and publishing. Capture from a
   named working build with fictional data; diagrams are separate deliverables.
6. Track iOS signing, hosted identity, checkout and real-device journeys as open
   acceptance work. Editing and portable tests cannot close those checks. Complete
   authorized runnable checks where tools/accounts/hardware allow; report actual blockers.
7. Reduce density in Draft V1 pages 24–26, 133–147, 189–209 and 323–349; use their
   source sections as anchors because pagination will change. Remove repeated general
   cautions while preserving specific failure handling and security constraints.

## Work completed

- Chapter 1 release prose converted to a milestone comparison table.
- Chapter 1 verification guidance and worked-example transition shortened.
- Full PDF rebuild and navigation/index audit passed after those edits.
- Initial fenced-code inventory completed across all forty chapters. This inventory
  is a diagnostic only, not a validated measure of instructional completeness.

## Deliverable

Publish Building-Mobile-Apps-with-CSharp15-Draft-V2.pdf after a substantive revision
batch and layout checks. Keep Draft V1 as the comparison baseline. Do not describe
this plan or the initial Chapter 1 edit as a completed full-manuscript revision.

## Draft V2 delivered revision batch

- Chapters 6–11 now contain 43 fenced listings (15 at the Draft V1 baseline),
  including 28 additional excerpts tied to the original Part II code checkpoint.
- Each of those six chapters has prerequisites, a concrete deliverable, guided lab,
  worked example, troubleshooting, summary and exercises. Numbered/indexed section
  headings are retained for the current subject-index targets.
- Added complete Home markup and handler, theme resources, binding/notification
  flow, async command, Shell hierarchy, route receiver/parser, dependency setup,
  collection/card/visual-state/detail markup, localized resources and tests,
  and the complete resize adapter with boundary tests.
- Reduced repeated checkpoint commentary in the revised chapters. Consolidated
  the proof's opening acceptance notes and labeled its headers/title Draft V2.
- Retained the 11-point body and 9.5-point code sizes. Newly printed Part II code
  lines are at most 80 characters; whitespace-only reformatting preserves source.
- Rebuilt PDF: 484 pages at 8 x 10 inches; 40 chapters, eight Parts, four appendices,
  111 subject-index targets and 222 PDF index links. Representative revised pages
  were rendered and inspected; all Part II text spans fit their mirrored frames.
- Rebuilt EPUB: 64 XHTML documents, 183 exact code blocks, 51 described image
  placements, 111 subject links and 290 local package references pass the audit.
- Source fidelity checks compare the 28 excerpts to their recorded companion
  checkpoint and check complete XML documents for well-formedness. No application
  code changed; no fresh app compilation, device run or live-service check occurred.

This is a substantial Part II revision batch, not completion of the full editorial
pass. Native screenshots, C# 15 feature coverage, Chapters 12–40 prose/code review,
live identity/checkout, iOS and real-device acceptance, reader testing and final
publication decisions remain open. The 33 chapters outside the initial Chapter 1
edit and revised Chapters 6–11 retain their baseline source text.
