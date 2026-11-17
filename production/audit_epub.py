"""Verify packaged navigation, exact code text and semantic EPUB structure."""
import collections
import json
import posixpath
import urllib.parse
import zipfile
from pathlib import Path
from lxml import etree

ROOT=Path(__file__).resolve().parents[1]
EPUB=ROOT/'production/Building-Mobile-Apps-CSharp15-proof.epub'
inventory=json.loads((ROOT/'production/epub-inventory.json').read_text())
NS={'x':'http://www.w3.org/1999/xhtml','o':'http://www.idpf.org/2007/opf',
    'c':'urn:oasis:names:tc:opendocument:xmlns:container','dc':'http://purl.org/dc/elements/1.1/'}
with zipfile.ZipFile(EPUB) as z:
    names=set(z.namelist())
    assert z.infolist()[0].filename=='mimetype' and z.infolist()[0].compress_type==zipfile.ZIP_STORED
    assert z.read('mimetype')==b'application/epub+zip'
    container=etree.fromstring(z.read('META-INF/container.xml'))
    opf_name=container.find('.//c:rootfile',NS).get('full-path')
    opf=etree.fromstring(z.read(opf_name))
    assert opf.get('version').startswith('3')
    assert opf.find('.//dc:language',NS).text=='en-US'
    manifest={i.get('id'):i for i in opf.findall('.//o:manifest/o:item',NS)}
    base=posixpath.dirname(opf_name)
    for item in manifest.values():
        assert posixpath.normpath(posixpath.join(base,urllib.parse.unquote(item.get('href')))) in names
    spine=opf.findall('.//o:spine/o:itemref',NS)
    assert all(i.get('idref') in manifest for i in spine)
    docs={name:etree.fromstring(z.read(name)) for name in names if name.endswith('.xhtml')}
    ids={name:{e.get('id') for e in doc.iter() if e.get('id')} for name,doc in docs.items()}
    codes=[];image_count=0;link_count=0;index_links=[]
    for name,doc in docs.items():
        for element in doc.findall('.//x:pre/x:code',NS):
            codes.append(''.join(element.itertext()).rstrip('\n'))
        for image in doc.findall('.//x:img',NS):
            assert image.get('alt','').strip(),(name,'missing image alt')
            image_count+=1
        for element in doc.iter():
            attribute='src' if etree.QName(element).localname=='img' else 'href'
            value=element.get(attribute)
            if not value:continue
            parsed=urllib.parse.urlsplit(value)
            if parsed.scheme:
                assert parsed.scheme in ('https','http','mailto'),(name,value)
                continue
            target=posixpath.normpath(posixpath.join(posixpath.dirname(name),urllib.parse.unquote(parsed.path))) if parsed.path else name
            assert target in names,(name,value)
            if parsed.fragment:
                assert target in ids and urllib.parse.unquote(parsed.fragment) in ids[target],(name,value)
            link_count+=1
        if doc.find('.//*[@id="subject-index"]') is not None:
            index_links=doc.findall('.//x:a',NS)
    assert collections.Counter(codes)==collections.Counter(s.rstrip('\n') for s in inventory['code_blocks']),'Code text changed'
    assert image_count==inventory['image_placements']
    assert len(index_links)==inventory['index_entries']
    assert {urllib.parse.urlsplit(link.get('href')).fragment for link in index_links}==set(inventory['target_ids'])
    assert not any(doc.findall('.//x:script',NS) for doc in docs.values())
    assert not any('editorial index terms' in ''.join(doc.itertext()).lower() for doc in docs.values())
    print(f'PASS: {len(docs)} XHTML documents; {len(codes)} exact code blocks; '
          f'{image_count} described images; {inventory["index_entries"]} subject links; '
          f'{link_count} local package references; complete manifest/spine')
