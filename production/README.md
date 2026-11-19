# Reproduce the opening typography specimen

The PDF is an editorial proof, not the final paperback. A separately validated reflowable EPUB proof is also available. It tests 8 × 10 pages, mirrored 0.95-inch inner/0.65-inch outer margins, 11/14-point body text, 9.5/12.5-point code, tables, and new-page starts. Short code examples stay together. The eight Part illustrations and introductions, the Part IV planning diagram/introduction, Chapters 1–40, PDF bookmarks, and a linked table of contents are included. All eight Part illustrations are included; verified native app screenshots remain pending.

Install Python/reportlab, download the following static TTFs into production/fonts, then run python production/render_opening.py from this repository. The renderer reads the Markdown sources; fonts/PDF are excluded from Git by the production .gitignore. This is a specimen renderer, not the final ebook or print production pipeline.

Fonts and provenance:
- SourceSerif4-Regular.ttf: https://raw.githubusercontent.com/adobe-fonts/source-serif/release/TTF/SourceSerif4-Regular.ttf
- SourceSans3-Regular.ttf: https://raw.githubusercontent.com/adobe-fonts/source-sans/release/TTF/SourceSans3-Regular.ttf
- SourceCodePro-Regular.ttf: https://raw.githubusercontent.com/adobe-fonts/source-code-pro/release/TTF/SourceCodePro-Regular.ttf

These Adobe font repositories provide the respective SIL Open Font License notices. Review/preserve those notices if redistributing font files. The sample embeds subsets of all three fonts.

The rendered PDF has been visually inspected. It is not tagged for accessibility; the planned EPUB and final production checks remain separate. Part I uses assets/illustrations/part-01-desktop-to-mobile.jpg and Part II uses assets/illustrations/part-02-native-interface.jpg at 300 DPI. The original artwork is an editorial illustration, not a runtime screenshot or an exact architecture diagram. See assets/illustrations/provenance.md.


## Authored technical figures

Forty-two grayscale technical diagrams/recaps are under `assets/figures`. Their complete
reproducible source is `production/draw_editorial_figures.py` (Python/Pillow plus
DejaVu Sans fonts at the documented Linux paths). The assets are 1800x1200 pixels
with 300-DPI metadata, placed at 6.4x4.267 inches in the print proof. They are authored
architecture/planning figures, not native screenshots. Existing Part art keeps its
original 5.12-inch width. Figure and caption stay together.


Chapter 38 adds two signing/update diagrams and an expanded instructional draft. Table subheadings stay with their tables; new Part/chapter starts remain on separate pages.

Chapter 39 adds the iOS build-boundary and candidate-gate diagrams. Native iOS execution remains pending.

Chapter 40 adds candidate-evidence and incident-recovery diagrams plus the runnable synthetic release-packet lab.


The reference continuation adds four substantive appendices and an alphabetical
glossary. Appendix labels and titles share one bookmark/contents entry. The PDF
workflow watches appendix/back-matter changes and requires all five new sections.

## Subject index and reference audit

The publication continuation adds a draft notice, acknowledgments, reader/errata
resources, materials notices and a conservative author biography. ISBN/edition
assignment and final credits remain review work.

`planning/subject-index.json` curates 111 substantive section openings. The helper
`production/subject_index.py` validates unique source headings and collects actual
page locators through ReportLab multiBuild. Index terms and locators link to
internal destinations. This is a selected subject index, not a word concordance or
a claim that final indexing has been completed.

Run `python production/render_opening.py`, then
`python production/audit_navigation.py`. The audit checks the included source
inventory, numbered chapter references, relative Markdown targets, exact paginated
index headings, and the actual PDF destination page objects for both links per
entry. `proof-navigation.json` is generated/ignored and belongs to its matching PDF.
The existing proof workflow now renders and audits this navigation before upload.

## Reflowable EPUB proof

Install Pandoc 3.1.11.1 (or revalidate another version), Python with lxml, and run:

```bash
python production/build_epub.py
python production/audit_epub.py
```

The build uses the same included source inventory as the PDF, removes editorial
index metadata, combines chapter/Part/Appendix labels with their titles, assigns
unique anchors and generates a linked subject index without paperback page numbers.
It packages existing figures with their descriptions and semantic table headers.
Code has no syntax-highlighter rewrite, is checked exactly against the parsed source
blocks, and uses relative monospace styling with wrapping for narrow displays.
Raw HTML parsing is disabled so prose such as Task<TimeSpan> cannot become a broken
XML element. No fixed fonts, forced paper page sizes or unrelated cover art are added.

Output: production/Building-Mobile-Apps-CSharp15-proof.epub. Generated package,
content inventory and validation reports are ignored by Git. EPUBCheck 5.4.0 was run
locally with Java 21; use the official W3C distribution to repeat conformance checks:

```bash
java -jar /path/to/epubcheck.jar \
  production/Building-Mobile-Apps-CSharp15-proof.epub \
  -j production/epubcheck-report.json
```

Actual packaging/conformance and reflow observations are retained in
planning/epub-proof-review.md. EPUBCheck success does not certify screen-reader
acceptance, Kindle conversion, Apple Books behavior or store readiness. This is the
first editorial EPUB proof; its technical/native/publication gaps match the source.

## Complete source and artwork inventory

The current inventory includes all 40 chapters, all eight illustrated Part openers,
four appendices, glossary and reader/publication matter. There are 51 image
placements: eight conceptual Part illustrations, the separate Part IV planning
diagram and 42 technical figures/recaps. See assets/illustrations/provenance.md
for the restored artwork record. Existing generated files remain outside Git.

The navigation audit also requires Chapters 1–40 exactly once in order in the PDF
bookmarks, eight Parts, four appendices and a distinct existing original illustration
for every Part. These checks protect content completeness; they do not complete
editorial, native, accessibility or store acceptance. Current finishing status is
maintained in planning/finishing-checklist.md.

## Draft V2 Part II excerpt audit

Run `python production/audit_part02_excerpts.py --code-repo /path/to/companion-clone`.
The clone must contain the Part II checkpoint recorded in
`planning/part02-excerpt-provenance.json`. The audit checks 28 added excerpts against
that source, the complete XAML documents for well-formedness, six practical chapter
templates and printed code-line limits. This is source validation, not fresh app
compilation or runtime verification. Longer PDF listings may split at line boundaries;
short examples remain together, at the existing 9.5-point code size.

## Draft V3 Chapters 12–21 audit

Run `python production/audit_part34_excerpts.py --code-repo /path/to/companion-clone`.
This checks 19 printed excerpts against the historical source checkpoints in
`planning/part34-excerpt-provenance.json`, their line limits and ten consistently
ordered practical chapter templates. It is source verification, not new app
execution. Run the existing navigation and EPUB audits on the matching rebuilt
artifacts; run EPUBCheck separately.
