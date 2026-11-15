from pathlib import Path
from html import escape
import re
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
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
    'body': ParagraphStyle('body', fontName='Body', fontSize=11, leading=14, spaceAfter=8),
    'h1': ParagraphStyle('h1', fontName='Head', fontSize=26, leading=29, spaceBefore=12, spaceAfter=18, keepWithNext=True),
    'h2': ParagraphStyle('h2', fontName='Head', fontSize=17, leading=20, spaceBefore=13, spaceAfter=8, keepWithNext=True),
    'small': ParagraphStyle('small', fontName='Head', fontSize=9, leading=12, spaceAfter=7),
    'cell': ParagraphStyle('cell', fontName='Body', fontSize=9.5, leading=12),
    'code': ParagraphStyle('code', fontName='Code', fontSize=9.5, leading=12.5, spaceBefore=6, spaceAfter=12, backColor=colors.HexColor('#f1f1f1'), borderPadding=8),
}

def fmt(text):
    text=escape(text)
    text=re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text=re.sub(r'`([^`]+)`', r'<font name="Code">\1</font>', text)
    return text

def markdown(text, source=None):
    result=[]; lines=text.splitlines(); i=0; paragraph=[]; reference_mode=False
    def flush():
        if paragraph:
            result.append(Paragraph(fmt(' '.join(paragraph)),styles['small'] if reference_mode else styles['body'])); paragraph.clear()
    while i<len(lines):
        line=lines[i]
        if line.startswith('## Editorial index terms'):
            flush(); break
        if line.startswith('Index:'):
            flush(); i+=1; continue
        if line.startswith('!['):
            flush()
            match = re.fullmatch(r'!\[(.*?)\]\((.*?)\)',line)
            if not match or source is None: raise ValueError('Image needs a source document')
            path=(source.parent/match.group(2)).resolve()
            if not path.is_relative_to(ROOT): raise ValueError('Image outside manuscript')
            result.append(Image(str(path),width=368.64,height=245.76,hAlign='CENTER'))
            result.append(Paragraph(fmt(match.group(1)),styles['small']))
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
            result.extend([table,Spacer(1,12)]);continue
        if line.startswith('# '):
            flush();result.append(Paragraph(fmt(line[2:]),styles['h1']))
        elif line.startswith('## '):
            flush();reference_mode = 'reference' in line.lower() or 'source' in line.lower() or 'index terms' in line.lower();result.append(Paragraph(fmt(line[3:].replace(' and index terms','')),styles['h2']))
        elif line.startswith('*Illustration brief:') or line.startswith('*Editorial status:'):
            flush();result.append(Paragraph(fmt(line.strip('*')),styles['small']))
        elif not line.strip():flush()
        else:paragraph.append(line.split(' Index:')[0])
        i+=1
    flush();return result

def footer(c,doc):
    c.saveState();c.setFont('Head',8);c.setFillColor(colors.HexColor('#555555'))
    left=68.4 if doc.page%2 else 46.8
    right=left+460.8
    c.drawString(left,696,'BUILDING MOBILE APPS WITH C# 15')
    c.drawRightString(right,696,'OPENING DRAFT')
    c.setLineWidth(.4);c.line(left,686,right,686)
    c.drawString(left,30,'8 × 10 in  |  11 pt body  |  9.5 pt code  |  November 14, 2026')
    c.drawRightString(right,30,str(doc.page));c.restoreState()

doc=BaseDocTemplate(str(OUT),pagesize=(576,720),leftMargin=68.4,rightMargin=46.8,topMargin=54,bottomMargin=51,title='Building Mobile Apps with C# 15 - Opening Draft',author='John F. Gnazzo')
doc.addPageTemplates([
    PageTemplate(id='odd',frames=[Frame(68.4,51,460.8,615,id='odd-frame',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=footer,autoNextPageTemplate='even'),
    PageTemplate(id='even',frames=[Frame(46.8,51,460.8,615,id='even-frame',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=footer,autoNextPageTemplate='odd')])
story=[Spacer(1,84),Paragraph('Building Mobile Apps<br/>with C# 15',styles['h1']),Spacer(1,16),Paragraph('.NET 11 and .NET MAUI 11',styles['h2']),Paragraph('A Windows Developer’s Guide to Android, iPhone, and Tablets',styles['body']),Spacer(1,36),Paragraph('John F. Gnazzo',styles['h2']),Paragraph('DGreatGnazzini Press LLC',styles['body']),Spacer(1,50),Paragraph('Opening manuscript and typography proof. First drafts; not a finished book. Final illustrations, screenshots, front matter, and index are still in development.',styles['small']),PageBreak()]
story.extend(markdown('# About This Draft\n\nThis specimen uses the selected Source Serif 4, Source Sans 3, and Source Code Pro fonts. It demonstrates the 8 × 10 page, 11-point body text, 9.5-point code, a generous binding margin, and new-page starts for major divisions.\n\nIncluded: preface, reader orientation, introduction, Part I overview with its original illustration, and Chapters 1–5. These chapters are first drafts; device checks remain separate from compilation. The full book retains its planned 40 chapters and complete front and back matter.\n\nPortable code and tests passed the GitHub-hosted Windows workflow. The Android starter compiles on Windows CI and all 37 portable tests pass. Emulator/physical-device launch and iOS compilation remain unverified.\n\nCopyright 2026 John F. Gnazzo. All rights reserved. Publication date, ISBNs, final legal notices, dedication, acknowledgments, and author biography will be completed during production.'))
for rel in ['front-matter/preface.md','front-matter/how-to-use-this-book.md','front-matter/introduction.md','parts/part-01/introduction.md','chapters/ch01-mobile-landscape.md','chapters/ch02-defining-gnazzos-world.md','chapters/ch03-windows-environment.md','chapters/ch04-first-application.md','chapters/ch05-testable-foundations.md']:
    story.append(PageBreak());story.extend(markdown((ROOT/rel).read_text(),ROOT/rel))
doc.build(story)
print(OUT)
