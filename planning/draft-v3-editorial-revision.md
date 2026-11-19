# Draft V3 editorial revision

November 18, 2026 (Central). This batch continues Draft V2; it preserves the full
forty-chapter scope and the existing technical sophistication.

## Completed scope

- Revised Chapters 12–21: catalog metadata, discovery/favorites, details/links,
  request forms, pricing, HTTP, public API, SQLite, offline refresh and sync.
- Added or replaced 19 printed excerpts checked against named historical source
  checkpoints, with source attribution stored in part34-excerpt-provenance.json.
  The full book now has 201 fenced code blocks, up from 183 in Draft V2.
- Standardized the ten chapters' prerequisites, deliverables, guided labs, worked
  examples, troubleshooting, summaries and exercises. Kept every curated index
  target and reordered practical sections consistently.
- Replaced repetitive process commentary with shorter task-focused explanations,
  comparison tables and worked outcomes. Kept security constraints, failure
  handling, simulation boundaries and meaningful pending-operation state.
- Removed all full commit hashes from these reader chapters. Historical build
  logs and exact source identities remain in companion/maintainer documentation.
- Repaired the companion milestone guide for Chapters 12, 14–16 and 20, including
  direct checkout links to the source used by the printed examples.
- Retained Draft V2's expanded Part II and the initial Chapter 1 edit. The other
  thirty chapter source files are unchanged by this batch.

## Verification

- The 19-excerpt audit passes source containment, hashes, eighty-character line
  limits and consistent chapter structure. The earlier 28-excerpt Part II audit
  also passes.
- PDF: 497 pages, 8 x 10 inches; all 40 chapters, eight Parts, four appendices,
  111 exact subject-index targets and 222 index links pass navigation checks.
- All text spans in the revised Chapters 12–21 fit their mirrored text frames.
  Representative code, table and lab pages were rendered and inspected.
- EPUB: 64 XHTML documents, 201 exact code blocks, 51 described image placements,
  111 subject links and 290 local package references pass the package audit.
  EPUBCheck reports zero errors or warnings.
- Application code did not change. No fresh application test/build, physical-device,
  iOS, provider, checkout or native-screen observation is claimed by this revision.

## Still open

Chapters 22–40 need their editorial/code-reference pass. C# 15 feature coverage,
actual screenshots, real-device journeys, hosted identity/MFA and checkout, iOS
signing, reading-system review and final publication details remain unfinished.
Draft V3 is a review proof, not a publication-ready interior.
