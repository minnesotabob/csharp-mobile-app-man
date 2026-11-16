from pathlib import Path
from html import escape
import re
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
            result.append(Paragraph(fmt(' '.join(paragraph)),styles['reference'] if reference_mode else styles['body'])); paragraph.clear()
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
            result.append(KeepTogether([Preformatted('\n'.join(code),styles['code'])])); i+=1;continue
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
            if result and isinstance(result[-1], Paragraph) and result[-1].style.name == 'h2':
                group.insert(0, result.pop())
            result.extend([KeepTogether(group),Spacer(1,12)]);continue
        if line.startswith('# '):
            flush();result.append(Paragraph(fmt(line[2:]),styles['h1']))
        elif line.startswith('### '):
            flush();result.append(Paragraph(fmt(line[4:]),styles['h3']))
        elif line.startswith('## '):
            flush();reference_mode = line[3:].lower().startswith(('references', 'sources', 'companion references', 'official references'));result.append(Paragraph(fmt(line[3:].replace(' and index terms','')),styles['h2']))
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
    c.drawRightString(right,696,'OPENING DRAFT')
    c.setLineWidth(.4);c.line(left,686,right,686)
    c.drawString(left,30,'8 × 10 in  |  11 pt body  |  9.5 pt code  |  November 16, 2026')
    c.drawRightString(right,30,str(doc.page));c.restoreState()

class BookDoc(BaseDocTemplate):
    section_prefix=''
    def handle_pageBegin(self):
        # multiBuild and split flowables must not drift mirrored body margins.
        self.pageTemplate = self.pageTemplates[self.page % 2]
        super().handle_pageBegin()
    def afterFlowable(self, flowable):
        if not isinstance(flowable,Paragraph) or flowable.style.name!='h1': return
        text=flowable.getPlainText()
        if text in ['Contents','About This Draft'] or self.page==1: return
        if re.fullmatch(r'(Chapter \d+|Part [IVX]+)',text):
            self.section_prefix=text;return
        if self.section_prefix:
            text=self.section_prefix+' - '+text;self.section_prefix=''
        key='heading-'+re.sub(r'[^a-z0-9]+','-',text.lower())
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(text,key,level=0)
        self.notify('TOCEntry',(0,text,self.page,key))

doc=BookDoc(str(OUT),pagesize=(576,720),leftMargin=68.4,rightMargin=46.8,topMargin=54,bottomMargin=51,title='Building Mobile Apps with C# 15 - Opening Draft',author='John F. Gnazzo')
doc.addPageTemplates([
    PageTemplate(id='odd',frames=[Frame(68.4,51,460.8,615,id='odd-frame',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=footer,autoNextPageTemplate='even'),
    PageTemplate(id='even',frames=[Frame(46.8,51,460.8,615,id='even-frame',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=footer,autoNextPageTemplate='odd')])
story=[Spacer(1,84),Paragraph('Building Mobile Apps<br/>with C# 15',styles['h1']),Spacer(1,16),Paragraph('.NET 11 and .NET MAUI 11',styles['h2']),Paragraph('A Windows Developer’s Guide to Android, iPhone, and Tablets',styles['body']),Spacer(1,36),Paragraph('John F. Gnazzo',styles['h2']),Paragraph('DGreatGnazzini Press LLC',styles['body']),Spacer(1,50),Paragraph('Opening manuscript and typography proof. First drafts; not a finished book. Final illustrations, screenshots, front matter, and index are still in development.',styles['small']),PageBreak()]
toc=TableOfContents()
toc.levelStyles=[ParagraphStyle('toc',fontName='Head',fontSize=10.5,leading=12,spaceBefore=0)]
story.extend([Paragraph('Contents',styles['h1']),toc,PageBreak()])
story.extend(markdown('# About This Draft\n\nThis editorial proof uses Source Serif 4, Source Sans 3 and Source Code Pro on an 8 × 10 page, with 11-point body text, 9.5-point code, mirrored binding margins and new-page starts for major divisions. It includes the preface, reader orientation, introduction, Parts I–VII introductions and Chapters 1–34. Thirty authored architecture/workflow figures and visual recaps accompany three original Part illustrations. Runtime app screenshots remain pending native capture.\n\nThe full plan retains 40 chapters and complete front/back matter. These chapters have an initial instructional revision with learning outcomes, explained source, guided work, troubleshooting, summaries and exercises. They remain editorial drafts; short first drafts are not final chapter lengths. Final Part artwork, index, accessible EPUB, publication date, ISBNs, legal notices, dedication, acknowledgments and author biography remain production work.\n\nThe companion develops catalog discovery and accessible interface foundations, saved custom-song drafts, historical teaching pricing, bounded public HTTP reads and an ASP.NET Core fixture API. Storage/offline/synchronization chapters use explicit durable policies and simulated service boundaries. Identity chapters add provider SDK composition, secure-session leases, signed-token API fixtures, MFA/recovery configuration and isolated profile/lifecycle labs. No live tenant is configured by default, and simulated lifecycle receipts do not perform remote account deletion.\n\nPart VI adds original audio fixtures, playback checkpoints, opt-in native background/system controls, verified public downloads, local notifications, bounded inbound links, explicit public sharing and a local capability/attachment lab. Native decoding, listening, focus, picker, permissions, image normalization and share grants require device observations. Local attachment staging is separate from customer upload/account attachment storage.\n\nPart VII adds server-owned quotes/orders, durable account/resource retry journals, restricted TEST checkout and signed-event reconciliation. Chapter 34 adds owned history, revision requests, in-app notices and short-lived private sample access. Accepted and TEST Paid do not authorize real work. Hosted provider execution, real administration/publication, native private playback, notifications, complete tracking/delivery operations and privacy lifecycle composition remain separate acceptance work.\n\nExact executed companion revisions, test counts and workflow links are recorded in docs/verification.md and planning/progress.md. This independently built print proof checks layout and content markers; it does not prove source compilation. Portable tests, signed in-process API tests and Android compilation establish different evidence from actual native behavior. Live identity/provider round trips, device acceptance and iOS compilation/signing remain unverified. Keep those acceptance rows separate from passing build/test counts.\n\nCopyright 2026 John F. Gnazzo. All rights reserved.'))
for rel in ['front-matter/preface.md','front-matter/how-to-use-this-book.md','front-matter/introduction.md','parts/part-01/introduction.md','chapters/ch01-mobile-landscape.md','chapters/ch02-defining-gnazzos-world.md','chapters/ch03-windows-environment.md','chapters/ch04-first-application.md','chapters/ch05-testable-foundations.md','parts/part-02/introduction.md','chapters/ch06-xaml-layouts-resources.md','chapters/ch07-bindings-commands-mvvm.md','chapters/ch08-navigation-state.md','chapters/ch09-collections-images-reuse.md','chapters/ch10-accessibility-localization.md','chapters/ch11-adaptive-layouts.md','parts/part-03/introduction.md','chapters/ch12-catalog-models.md','chapters/ch13-search-filters-favorites.md','chapters/ch14-content-details-samples-links.md','chapters/ch15-custom-song-request.md','chapters/ch16-pricing-reliable-submission.md','parts/part-04/introduction.md','chapters/ch17-http-resilient-networking.md','chapters/ch18-companion-aspnet-core-api.md','chapters/ch19-local-storage-migrations.md','chapters/ch20-offline-background-work.md','chapters/ch21-synchronization-conflicts.md','parts/part-05/introduction.md','chapters/ch22-native-authentication.md','chapters/ch23-sessions-storage-authorization.md','chapters/ch24-mfa-recovery.md','chapters/ch25-profiles-privacy-lifecycle.md','chapters/ch26-threat-modeling-security.md','parts/part-06/introduction.md','chapters/ch27-audio-playback-progress.md','chapters/ch28-background-system-controls.md','chapters/ch29-downloads-media-storage.md','chapters/ch30-notifications-links-sharing.md','chapters/ch31-native-capabilities-attachments.md','parts/part-07/introduction.md','chapters/ch32-quotes-orders-ownership.md','chapters/ch33-payment-boundaries-verified-events.md','chapters/ch34-order-tracking-revisions-delivery.md']:
    story.append(PageBreak());story.extend(markdown((ROOT/rel).read_text(),ROOT/rel))
doc.multiBuild(story)
print(OUT)

