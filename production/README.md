# Reproduce the opening typography specimen

The opening PDF is an editorial draft, not the final paperback or accessible EPUB. It tests 8 × 10 pages, mirrored 0.95-inch inner/0.65-inch outer margins, 11/14-point body text, 9.5/12.5-point code, tables, and new-page starts. Short code examples stay together. Final illustrations and verified app screenshots are pending.

Install Python/reportlab, download the following static TTFs into production/fonts, then run python production/render_opening.py from this repository. The renderer reads the Markdown sources; fonts/PDF are excluded from Git by the production .gitignore. This is a specimen renderer, not the final ebook or print production pipeline.

Fonts and provenance:
- SourceSerif4-Regular.ttf: https://raw.githubusercontent.com/adobe-fonts/source-serif/release/TTF/SourceSerif4-Regular.ttf
- SourceSans3-Regular.ttf: https://raw.githubusercontent.com/adobe-fonts/source-sans/release/TTF/SourceSans3-Regular.ttf
- SourceCodePro-Regular.ttf: https://raw.githubusercontent.com/adobe-fonts/source-code-pro/release/TTF/SourceCodePro-Regular.ttf

These Adobe font repositories provide the respective SIL Open Font License notices. Review/preserve those notices if redistributing font files. The sample embeds subsets of all three fonts.

The rendered PDF has been visually inspected. It is not tagged for accessibility; the planned EPUB and final production checks remain separate. Part artwork appears only as a clearly labeled brief in this draft.
