"""Build a reflowable editorial EPUB from the same source inventory as the PDF."""
import ast
import collections
import json
import re
import subprocess
import tempfile
import uuid
import zipfile
from pathlib import Path
from lxml import etree

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'production/Building-Mobile-Apps-CSharp15-proof.epub'
TREE=ast.parse((ROOT/'production/render_opening.py').read_text())
source_list=next(n.iter for n in ast.walk(TREE) if isinstance(n,ast.For)
                 and isinstance(n.target,ast.Name) and n.target.id=='rel')
sources=['front-matter/publication-notice.md',*ast.literal_eval(source_list)]
plan=json.loads((ROOT/'planning/subject-index.json').read_text())['entries']


def inlines(text):
    return [{'t':'Str','c':text}]


def plain(value):
    if isinstance(value,list):return ''.join(plain(x) for x in value)
    if not isinstance(value,dict):return ''
    if value.get('t') in ('Str','Code'):return value['c'] if value['t']=='Str' else value['c'][1]
    if value.get('t') in ('Space','SoftBreak','LineBreak'):return ' '
    return plain(value.get('c',[]))


def walk(value):
    if isinstance(value,dict):
        yield value
        for child in value.values():yield from walk(child)
    elif isinstance(value,list):
        for child in value:yield from walk(child)


blocks=[];target_ids={};old_ids={};code_blocks=[];image_count=0;api_version=None
for i,rel in enumerate(sources):
    source=ROOT/rel
    text=source.read_text().split('## Editorial index terms')[0]
    text=text.split('Editorial index terms:')[0]
    text='\n'.join(line.split(' Index:')[0] for line in text.splitlines() if not line.startswith('Index:'))
    text=re.sub(r'^# (Chapter \d+|Part [IVX]+|Appendix [A-D])\n# ([^\n]+)',r'# \1 — \2',text)
    if source.name=='how-to-use-this-book.md':
        text=text.replace("The subject index in this proof links to selected substantive section openings and uses this proof's page numbers. It is regenerated during typesetting; the final paperback index will be reviewed again after pagination stabilizes. The ebook will use linked targets.","The subject index in this EPUB links directly to selected substantive section openings. Reflowable text has no fixed paperback pagination. Use the chapter navigation, glossary and linked index when returning by task.")
    document=json.loads(subprocess.run(['pandoc','--from=markdown-smart-raw_html','--to=json'],input=text,text=True,capture_output=True,check=True).stdout)
    api_version=document['pandoc-api-version']
    heading_number=0
    for node in walk(document['blocks']):
        if node.get('t')=='Header':
            level,attrs,content=node['c'];old=attrs[0]
            anchor=f'document-{i:03d}' if heading_number==0 else f'section-{i:03d}-{heading_number:03d}'
            attrs[0]=anchor
            old_ids[(rel,old)]=anchor
            target_ids[(rel,plain(content))]=anchor
            heading_number+=1
        if node.get('t')=='CodeBlock':code_blocks.append(node['c'][1])
        if node.get('t')=='Image':
            image_count+=1
            path=(source.parent/node['c'][2][0]).resolve()
            assert path.is_relative_to(ROOT) and path.is_file(),path
            node['c'][2][0]=str(path)
    # Links are resolved after all document/header targets are known.
    for node in walk(document['blocks']):
        if node.get('t')=='Link':node['_source']=rel
    blocks.extend(document['blocks'])

for node in walk(blocks):
    if node.get('t')!='Link':continue
    rel=node.pop('_source');target=node['c'][2][0]
    if re.match(r'^[a-z]+:',target):continue
    if target.startswith('#'):
        node['c'][2][0]='#'+old_ids[(rel,target[1:])]
    else:
        file,_,fragment=target.partition('#')
        resolved=((ROOT/rel).parent/file).resolve()
        assert resolved.is_relative_to(ROOT),target
        other=resolved.relative_to(ROOT).as_posix()
        if other in sources:
            anchor=old_ids[(other,fragment)] if fragment else f'document-{sources.index(other):03d}'
            node['c'][2][0]='#'+anchor
        else:
            assert resolved.is_file(),target
            node['c'][2][0]='https://github.com/minnesotabob/csharp-mobile-app-man/blob/main/'+other

# EPUB locators point directly to sections; paper page numbers are not imported.
index_items=[]
for row in sorted(plan,key=lambda row:row['term'].casefold()):
    anchor=target_ids[(row['source'],row['heading'])]
    index_items.append([{'t':'Plain','c':[{'t':'Link','c':[['',[],[]],inlines(row['term']),['#'+anchor,'']]}]}])
blocks.extend([{'t':'Header','c':[1,['subject-index',[],[['epub:type','index']]],inlines('Subject Index')]},
               {'t':'Para','c':inlines('Selected substantive section openings. These links follow the reflowable text and do not use paperback page numbers.')},
               {'t':'BulletList','c':index_items}])
meta={
 'title':{'t':'MetaString','c':'Building Mobile Apps with C# 15'},
 'subtitle':{'t':'MetaString','c':'.NET 11 and .NET MAUI 11: A Windows Developer’s Guide to Android, iPhone, and Tablets'},
 'author':{'t':'MetaList','c':[{'t':'MetaString','c':'John F. Gnazzo'}]},
 'lang':{'t':'MetaString','c':'en-US'},
 'date':{'t':'MetaString','c':'2026-11-18'},
 'rights':{'t':'MetaString','c':'Copyright 2026 John F. Gnazzo. All rights reserved. Editorial proof.'},
 'description':{'t':'MetaString','c':'Editorial reflowable proof. Native/platform/provider acceptance and final publication review remain incomplete.'},
 'identifier':{'t':'MetaString','c':'urn:uuid:'+str(uuid.uuid5(uuid.NAMESPACE_URL,'https://johngnazzo.com/books/building-mobile-apps-csharp15/editorial-proof'))}
}
document={'pandoc-api-version':api_version,'meta':meta,'blocks':blocks}
with tempfile.TemporaryDirectory(prefix='mobile-epub-') as directory:
    raw=Path(directory)/'raw.epub'
    subprocess.run(['pandoc','--from=json','--to=epub3','--standalone','--toc','--toc-depth=1',
                    '--split-level=1','--no-highlight','--css='+str(ROOT/'production/epub.css'),
                    '--output='+str(raw)],input=json.dumps(document),text=True,check=True)
    # Preserve semantic table headers and normalize package metadata without
    # embedding fonts or claiming accessibility conformance from structure alone.
    xhtml='http://www.w3.org/1999/xhtml'
    with zipfile.ZipFile(raw) as source_zip,zipfile.ZipFile(OUT,'w') as dest_zip:
        for info in source_zip.infolist():
            data=source_zip.read(info.filename)
            if info.filename.endswith('.xhtml'):
                root=etree.fromstring(data)
                for th in root.findall('.//{'+xhtml+'}thead/{'+xhtml+'}tr/{'+xhtml+'}th'):
                    th.set('scope','col')
                data=etree.tostring(root,xml_declaration=True,encoding='UTF-8',doctype='<!DOCTYPE html>')
            dest_zip.writestr(info,data)
(ROOT/'production/epub-inventory.json').write_text(json.dumps({
    'schema':1,'sources':sources,'code_blocks':code_blocks,'image_placements':image_count,
    'index_entries':len(plan),'target_ids':[target_ids[(row['source'],row['heading'])] for row in plan]
},indent=2)+'\n')
print(OUT)
print(f'{len(sources)} source documents; {len(code_blocks)} code blocks; {image_count} image placements; {len(plan)} linked index entries')
