# First EPUB proof and milestone-scope review — November 17, 2026

## Editorial corrections

Targeted consistency pass across twelve documents, retaining historical chapter
milestones and actual integration boundaries. Clarified early public-only APIs
versus Chapter 32 commerce/Chapter 34 delivery; Chapter 8 navigation versus later
links; native collection pagination versus API paging; bundled catalog metadata
versus separate audio fixtures; preferences recovery versus SQLite; and Chapter 19
public storage versus Chapter 35 commerce backup/restore. Also clarified pending
remote iOS execution and the scope of later diagnostics/background-media labs.
This is a focused scope/continuity pass, not a completed line edit or native review.
No application C# or companion implementation changed.

## Reproducible tools and observed checks

- Pandoc 3.1.11.1; Python 3.12.14; lxml; Java 21.0.13.
- Official W3C EPUBCheck 5.4.0: zero fatals, errors, warnings or infos.
- 61 source documents produce 64 packaged XHTML documents with a complete manifest/spine.
- All 155 code blocks preserve exact parsed source text; highlighting is disabled.
- All 46 image placements have nonempty descriptions and packaged bytes.
- All 111 subject-index entries link to the selected actual section anchors.
- All 285 local package references resolve, including fragments. No script content.
- Chapter/Part/Appendix labels are combined into navigable top-level entries.
- No paperback page locators, fixed-font embedding or unrelated cover are imported.

Disabling raw HTML input parsing prevents prose generic types such as Task<TimeSpan>
from being misinterpreted as unclosed XHTML. Markdown smart punctuation is disabled
for faithful source/heading matching. Existing source typography is retained.

## Visual reflow and PDF observations

MuPDF 1.26.6 opened the actual EPUB and reflowed it at 390x780 and
820x1000 with a 12-point base. Title, chapter/appendix navigation, code and tables
were inspected. CSS requests short-block cohesion, but this reader can still split
a code block across screens; exact code preservation is checked independently. This is one
reader engine at two viewports, not actual iPhone/Apple Books/Kindle certification.
Screen-reader flow, target readers/dark mode, Kindle conversion, final cover metadata
and store acceptance remain pending. No accessibility conformance claim is added.

The corrected PDF remains 464 pages/61 bookmarks. Production trim/text/image checks
pass; navigation audit checks 61 source files, 442 numbered chapter-reference
expressions, 111 exact paginated headings and 222 matching index destinations.
Changed-statement pages 40, 83, 89, 108, 118, 134, 156, 178, 260, 267, 278 and 326
received contact-sheet review. Existing platform/provider gaps remain unchanged.

PDF SHA-256: 07e9e51fc34a2215613c6772a44f40a9a9a4c22bbbe1b4487b39022025942a97.
EPUB SHA-256: 35dd971b761de7e9752e20cd78d4fd2ec93a03b0ea3155a3b02af86383aec16a.

No GitHub push or new remote workflow run was attempted. Repository publication
remains pending explicit authorization after the earlier automatic-review blocks.
