from pathlib import Path
from html import escape
import re
import json
from subject_index import load_targets, SubjectIndex
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak, Preformatted, Table, TableStyle, KeepTogether, Image

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = ROOT / 'production/fonts'
OUT = ROOT / 'production/opening-draft-8x10.pdf'
INDEX_TARGETS = load_targets(ROOT)
for name, filename in [('Body', 'SourceSerif4-Regular.ttf'), ('Head', 'SourceSans3-Regular.ttf'), ('Code', 'SourceCodePro-Regular.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / filename)))
    pdfmetrics.registerFontFamily(name, normal=name, bold=name, italic=name, boldItalic=name)

styles = {
    'list': ParagraphStyle('list', fontName='Body', fontSize=11, leading=14, leftIndent=16, firstLineIndent=-16, spaceAfter=4),
    'body': ParagraphStyle('body', fontName='Body', fontSize=11, leading=14, spaceAfter=6),
    'h1': ParagraphStyle('h1', fontName='Head', fontSize=26, leading=29, spaceBefore=12, spaceAfter=18, keepWithNext=True),
    'h3': ParagraphStyle('h3', fontName='Head', fontSize=12, leading=15, spaceBefore=6, spaceAfter=4, keepWithNext=True),
    'h2': ParagraphStyle('h2', fontName='Head', fontSize=17, leading=20, spaceBefore=9, spaceAfter=6, keepWithNext=True),
    'small': ParagraphStyle('small', fontName='Head', fontSize=9, leading=12, spaceAfter=7),
    'reference': ParagraphStyle('reference', fontName='Head', fontSize=8.6, leading=10.5, spaceAfter=3),
    'cell': ParagraphStyle('cell', fontName='Body', fontSize=9.5, leading=12),
    'code': ParagraphStyle('code', fontName='Code', fontSize=9.5, leading=12.5, spaceBefore=6, spaceAfter=12, backColor=colors.HexColor('#f1f1f1'), borderPadding=8),
}

def fmt(text):
    text=escape(text)
    text=re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>', text)
    text=re.sub(r'`([^`]+)`', r'<font name="Code">\1</font>', text)
    return text

def markdown(text, source=None):
    result=[]; lines=text.splitlines(); i=0; paragraph=[]; reference_mode=False
    def flush():
        if paragraph:
            formatted = fmt(' '.join(paragraph))
            if source is not None and source.name == 'glossary.md':
                formatted = re.sub(r'<b>(.*?)</b>', r'<font name="Head">\1</font>', formatted)
            result.append(Paragraph(formatted,styles['reference'] if reference_mode else styles['body'])); paragraph.clear()
    while i<len(lines):
        line=lines[i]
        if line.startswith(('## Editorial index terms', 'Editorial index terms:')):
            flush(); break
        if line.startswith('Index:'):
            flush(); i+=1; continue
        if line.startswith('!['):
            flush()
            match = re.fullmatch(r'!\[(.*?)\]\((.*?)\)',line)
            if not match or source is None: raise ValueError('Image needs a source document')
            path=(source.parent/match.group(2)).resolve()
            if not path.is_relative_to(ROOT): raise ValueError('Image outside manuscript')
            width = 460.8 if path.parent.name == 'figures' else 368.64
            height = width * 2 / 3
            group = [Image(str(path),width=width,height=height,hAlign='CENTER'), Paragraph(fmt(match.group(1)),styles['small'])]
            if result and isinstance(result[-1], Paragraph) and result[-1].style.name in ('h2', 'h3'):
                group.insert(0, result.pop())
            result.append(KeepTogether(group))
            i+=1;continue
        elif line.startswith('```'):
            flush(); i+=1; code=[]
            while i<len(lines) and not lines[i].startswith('```'):
                code.append(lines[i]); i+=1
            block = Preformatted('\n'.join(code), styles['code'])
            # Long worked listings can continue at a line boundary rather than
            # force a large empty region on the preceding page.
            result.append(KeepTogether([block]) if len(code) <= 24 else block)
            i+=1;continue
        if line.startswith('|'):
            flush(); rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                cells=[x.strip() for x in lines[i].strip('|').split('|')]
                if not all(re.fullmatch(r'[-: ]+',c) for c in cells):
                    rows.append([Paragraph(fmt(c),styles['cell']) for c in cells])
                i+=1
            n=len(rows[0]); widths=[460.8/n]*n
            table=Table(rows,colWidths=widths,repeatRows=1,hAlign='LEFT')
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e4e4e4')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LINEBELOW',(0,0),(-1,0),0.75,colors.black),('LINEBELOW',(0,1),(-1,-1),0.35,colors.HexColor('#bbbbbb'))]))
            # Keep a table's immediate heading with the complete table.
            group = [table]
            if result and isinstance(result[-1], Paragraph) and result[-1].style.name in ('h2', 'h3'):
                group.insert(0, result.pop())
            result.extend([KeepTogether(group),Spacer(1,12)]);continue
        if line.startswith('# '):
            flush();result.append(Paragraph(fmt(line[2:]),styles['h1']))
        elif line.startswith('### '):
            flush();result.append(Paragraph(fmt(line[4:]),styles['h3']))
        elif line.startswith('## '):
            flush();reference_mode = line[3:].lower().startswith(('references', 'sources', 'companion references', 'official references'))
            heading = line[3:].replace(' and index terms','')
            flow = Paragraph(fmt(heading),styles['h2'])
            if source is not None:
                flow._subject_entries = INDEX_TARGETS.get((source.relative_to(ROOT).as_posix(), heading), [])
            result.append(flow)
        elif line.startswith('*Illustration brief:') or line.startswith('*Editorial status:'):
            flush();result.append(Paragraph(fmt(line.strip('*')),styles['small']))
        elif line.startswith('- ') or re.match(r'^\d+\.\s', line):
            flush();result.append(Paragraph(fmt(line),styles['reference'] if reference_mode else styles['list']))
        elif not line.strip():flush()
        else:paragraph.append(line.split(' Index:')[0])
        i+=1
    flush()
    for k, flow in enumerate(result):
        if isinstance(flow, Paragraph) and flow.getPlainText().lower().startswith(('official references', 'companion references', 'references', 'sources')):
            tail = result[k:]
            if len(tail) <= 14:
                result[k:] = [KeepTogether(tail)]
            break
    # Keep a chapter-summary heading with its first paragraph, not with every
    # following exercise/reference. Entire-section KeepTogether can exceed a page.
    for j, flow in enumerate(result[:-1]):
        if isinstance(flow, Paragraph) and flow.getPlainText() == 'Chapter Summary':
            result[j:j+2] = [KeepTogether(result[j:j+2])]
            break
    return result

def footer(c,doc):
    c.saveState();c.setFont('Head',8);c.setFillColor(colors.HexColor('#555555'))
    left=68.4 if doc.page%2 else 46.8
    right=left+460.8
    c.drawString(left,696,'BUILDING MOBILE APPS WITH C# 15')
    c.drawRightString(right,696,'DRAFT V3')
    c.setLineWidth(.4);c.line(left,686,right,686)
    c.drawString(left,30,'8 × 10 in  |  11 pt body  |  9.5 pt code  |  November 18, 2026')
    c.drawRightString(right,30,str(doc.page));c.restoreState()

class BookDoc(BaseDocTemplate):
    section_prefix=''
    def handle_pageBegin(self):
        # multiBuild and split flowables must not drift mirrored body margins.
        self.pageTemplate = self.pageTemplates[self.page % 2]
        super().handle_pageBegin()
    def afterFlowable(self, flowable):
        for term, anchor in getattr(flowable, '_subject_entries', []):
            self.canv.bookmarkPage(anchor)
            self.notify('SubjectIndexEntry', (0, term, self.page, anchor))
        if not isinstance(flowable,Paragraph) or flowable.style.name!='h1': return
        text=flowable.getPlainText()
        if text in ['Contents','About This Draft','Publication Notice'] or self.page==1: return
        if re.fullmatch(r'(Chapter \d+|Part [IVX]+|Appendix [A-D])',text):
            self.section_prefix=text;return
        if self.section_prefix:
            text=self.section_prefix+' - '+text;self.section_prefix=''
        key='heading-'+re.sub(r'[^a-z0-9]+','-',text.lower())
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(text,key,level=0)
        self.notify('TOCEntry',(0,text,self.page,key))

doc=BookDoc(str(OUT),pagesize=(576,720),leftMargin=68.4,rightMargin=46.8,topMargin=54,bottomMargin=51,title='Building Mobile Apps with C# 15 - Draft V3',author='John F. Gnazzo')
doc.addPageTemplates([
    PageTemplate(id='odd',frames=[Frame(68.4,51,460.8,615,id='odd-frame',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=footer,autoNextPageTemplate='even'),
    PageTemplate(id='even',frames=[Frame(46.8,51,460.8,615,id='even-frame',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=footer,autoNextPageTemplate='odd')])
story=[Spacer(1,84),Paragraph('Building Mobile Apps<br/>with C# 15',styles['h1']),Spacer(1,16),Paragraph('.NET 11 and .NET MAUI 11',styles['h2']),Paragraph('A Windows Developer’s Guide to Android, iPhone, and Tablets',styles['body']),Spacer(1,36),Paragraph('John F. Gnazzo',styles['h2']),Paragraph('DGreatGnazzini Press LLC',styles['body']),Spacer(1,50),Paragraph('Draft V3. Expanded practical instruction through Chapter 21. Editorial manuscript for review.',styles['small']),PageBreak()]
story.extend(markdown((ROOT/'front-matter/publication-notice.md').read_text(),ROOT/'front-matter/publication-notice.md'))
story.append(PageBreak())
toc=TableOfContents()
toc.levelStyles=[ParagraphStyle('toc',fontName='Head',fontSize=10.5,leading=12,spaceBefore=0)]
story.extend([Paragraph('Contents',styles['h1']),toc,PageBreak()])
story.extend(markdown('# About This Draft\n\nDraft V3 continues the practical revision through Chapter 21. Chapters 6–11 retain the expanded UI instruction; Chapters 12–21 add source-grounded walkthroughs, worked examples and consistent practical sections while shortening repeated process commentary. It retains all forty chapters, eight illustrated Parts, four appendices, glossary and subject index. The remaining chapters continue through editorial review.\n\nUse the companion repository’s milestone guide to retrieve the code for each chapter. Detailed build results, source history and technical acceptance records belong in the companion verification documents. The examples distinguish bundled data, local simulations and configured services at the relevant implementation steps.\n\nThis manuscript is not publication-ready. Native screenshots, full real-device journeys, hosted sign-in and checkout, iOS signing, final editorial and index review, and print/ebook reader proofing remain unfinished. Examples using test payment events do not perform live checkout. A configured identity provider is required for hosted sign-in. The C# 15 feature-coverage review is also still open.\n\nCopyright 2026 John F. Gnazzo. All rights reserved.'))
for rel in ['front-matter/preface.md','front-matter/acknowledgments.md','front-matter/how-to-use-this-book.md','front-matter/introduction.md','parts/part-01/introduction.md','chapters/ch01-mobile-landscape.md','chapters/ch02-defining-gnazzos-world.md','chapters/ch03-windows-environment.md','chapters/ch04-first-application.md','chapters/ch05-testable-foundations.md','parts/part-02/introduction.md','chapters/ch06-xaml-layouts-resources.md','chapters/ch07-bindings-commands-mvvm.md','chapters/ch08-navigation-state.md','chapters/ch09-collections-images-reuse.md','chapters/ch10-accessibility-localization.md','chapters/ch11-adaptive-layouts.md','parts/part-03/introduction.md','chapters/ch12-catalog-models.md','chapters/ch13-search-filters-favorites.md','chapters/ch14-content-details-samples-links.md','chapters/ch15-custom-song-request.md','chapters/ch16-pricing-reliable-submission.md','parts/part-04/introduction.md','chapters/ch17-http-resilient-networking.md','chapters/ch18-companion-aspnet-core-api.md','chapters/ch19-local-storage-migrations.md','chapters/ch20-offline-background-work.md','chapters/ch21-synchronization-conflicts.md','parts/part-05/introduction.md','chapters/ch22-native-authentication.md','chapters/ch23-sessions-storage-authorization.md','chapters/ch24-mfa-recovery.md','chapters/ch25-profiles-privacy-lifecycle.md','chapters/ch26-threat-modeling-security.md','parts/part-06/introduction.md','chapters/ch27-audio-playback-progress.md','chapters/ch28-background-system-controls.md','chapters/ch29-downloads-media-storage.md','chapters/ch30-notifications-links-sharing.md','chapters/ch31-native-capabilities-attachments.md','parts/part-07/introduction.md','chapters/ch32-quotes-orders-ownership.md','chapters/ch33-payment-boundaries-verified-events.md','chapters/ch34-order-tracking-revisions-delivery.md','chapters/ch35-hosting-diagnostics-operations.md','parts/part-08/introduction.md','chapters/ch36-testing-complete-application.md','chapters/ch37-performance-reliability-accessibility.md','chapters/ch38-android-signing-google-play.md','chapters/ch39-ios-signing-app-store.md','chapters/ch40-automated-releases-maintenance.md','appendices/appendix-a-csharp-refresher.md','appendices/appendix-b-environment-troubleshooting.md','appendices/appendix-c-contracts-data-configuration.md','appendices/appendix-d-watch-companions.md','back-matter/glossary.md','back-matter/companion-and-errata.md','back-matter/materials-and-notices.md','back-matter/about-author.md']:
    story.append(PageBreak());story.extend(markdown((ROOT/rel).read_text(),ROOT/rel))
story.extend([PageBreak(),Paragraph('Subject Index',styles['h1']),
    Paragraph('Selected substantive section openings. Locators and links refer to this editorial proof and regenerate during typesetting; final index review follows stable pagination.',styles['small'])])
subject_index=SubjectIndex()
subject_index.levelStyles=[ParagraphStyle('subject-index',fontName='Head',fontSize=10.5,leading=13,spaceBefore=1)]
subject_index.tableStyle=TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)])
story.append(subject_index)
doc.multiBuild(story)
expected=sum(len(rows) for rows in INDEX_TARGETS.values())
assert len(subject_index._entries)==expected, 'Missing or duplicated paginated index target'
(ROOT/'production/proof-navigation.json').write_text(json.dumps({
    'schema':1,'index':[{'term':text,'page':page,'anchor':key}
    for _,text,page,key in sorted(subject_index._entries,key=lambda row:row[1].casefold())]},indent=2)+'\n')
print(OUT)


