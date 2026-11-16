# Reproduce the opening typography specimen

The opening PDF is an editorial draft, not the final paperback or accessible EPUB. It tests 8 × 10 pages, mirrored 0.95-inch inner/0.65-inch outer margins, 11/14-point body text, 9.5/12.5-point code, tables, and new-page starts. Short code examples stay together. The Part I and II illustrations, the Part III introduction, the Part IV planning diagram/introduction, Chapters 1–35, PDF bookmarks, and a linked table of contents are included. Other Part illustrations and verified app screenshots are pending.

Install Python/reportlab, download the following static TTFs into production/fonts, then run python production/render_opening.py from this repository. The renderer reads the Markdown sources; fonts/PDF are excluded from Git by the production .gitignore. This is a specimen renderer, not the final ebook or print production pipeline.

Fonts and provenance:
- SourceSerif4-Regular.ttf: https://raw.githubusercontent.com/adobe-fonts/source-serif/release/TTF/SourceSerif4-Regular.ttf
- SourceSans3-Regular.ttf: https://raw.githubusercontent.com/adobe-fonts/source-sans/release/TTF/SourceSans3-Regular.ttf
- SourceCodePro-Regular.ttf: https://raw.githubusercontent.com/adobe-fonts/source-code-pro/release/TTF/SourceCodePro-Regular.ttf

These Adobe font repositories provide the respective SIL Open Font License notices. Review/preserve those notices if redistributing font files. The sample embeds subsets of all three fonts.

The rendered PDF has been visually inspected. It is not tagged for accessibility; the planned EPUB and final production checks remain separate. Part I uses assets/illustrations/part-01-desktop-to-mobile.jpg and Part II uses assets/illustrations/part-02-native-interface.jpg at 300 DPI. The original artwork is an editorial illustration, not a runtime screenshot or an exact architecture diagram. See assets/illustrations/provenance.md.


## Authored technical figures

Thirty-two grayscale technical diagrams/recaps are under `assets/figures`. Their complete
reproducible source is `production/draw_editorial_figures.py` (Python/Pillow plus
DejaVu Sans fonts at the documented Linux paths). The assets are 1800x1200 pixels
with 300-DPI metadata, placed at 6.4x4.267 inches in the print proof. They are authored
architecture/planning figures, not native screenshots. Existing Part art keeps its
original 5.12-inch width. Figure and caption stay together.
