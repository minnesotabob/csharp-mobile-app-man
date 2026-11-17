"""Audit selected manuscript references and generated proof index destinations."""
import ast
import json
import re
from pathlib import Path
import fitz
from subject_index import load_targets

ROOT=Path(__file__).resolve().parents[1]
tree=ast.parse((ROOT/'production/render_opening.py').read_text())
source_list=next(node.iter for node in ast.walk(tree) if isinstance(node,ast.For)
                 and isinstance(node.target,ast.Name) and node.target.id=='rel')
sources=[ROOT/p for p in ast.literal_eval(source_list)]
sources.append(ROOT/'front-matter/publication-notice.md')
chapters={int(re.search(r'ch(\d+)',p.name).group(1)) for p in sources if p.parent.name=='chapters'}
assert chapters==set(range(1,41))
references=0
for source in sources:
    assert source.is_file(),source
    text=source.read_text()
    # Editorial metadata is not rendered and need not be interpreted as prose.
    text=text.split('## Editorial index terms')[0]
    for match in re.finditer(r'\bChapters?\s+(\d+)(?:\s*[-–]\s*(\d+))?',text):
        first=int(match[1]);last=int(match[2] or first)
        assert first<=last and set(range(first,last+1))<=chapters,(source.name,match[0])
        references+=1
    for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',text):
        if re.match(r'^[a-z]+://',target) or target.startswith('#'):continue
        resolved=(source.parent/target.split('#',1)[0]).resolve()
        assert resolved.is_relative_to(ROOT) and resolved.exists(),(source.name,target)

plan=json.loads((ROOT/'planning/subject-index.json').read_text())['entries']
load_targets(ROOT)  # each curated term has exactly one existing source heading
report=json.loads((ROOT/'production/proof-navigation.json').read_text())['index']
assert len(report)==len(plan)
assert len({row['term'] for row in report})==len(plan)
assert [r['term'].casefold() for r in report]==sorted(r['term'].casefold() for r in report)
by_term={row['term']:row for row in plan}
pdf=fitz.open(ROOT/'production/opening-draft-8x10.pdf')
toc=pdf.get_toc()
assert all(1<=row[2]<=len(pdf) for row in toc)
normalize=lambda s:' '.join(s.split())
for row in report:
    assert 1<=row['page']<=len(pdf)
    heading=by_term[row['term']]['heading']
    assert normalize(heading) in normalize(pdf[row['page']-1].get_text()),(row['term'],row['page'],heading)
index_start=next(row[2] for row in toc if row[1]=='Subject Index')
index_links=[link for page in list(pdf)[index_start-1:] for link in page.get_links()]
# Some PyMuPDF versions expose /Fit destinations as named page strings.
# Resolve the actual PDF destination page object instead of assuming LINK_GOTO.
page_by_xref={page.xref:i for i,page in enumerate(pdf)}
internal=[]
for link in index_links:
    raw=pdf.xref_object(link['xref'])
    target=re.search(r'/Dest\s*\[\s*(\d+)\s+0\s+R',raw)
    assert target is not None,'Subject index link lacks an internal page destination'
    internal.append(page_by_xref[int(target[1])])
assert len(internal)==2*len(plan),'Each index term and locator must link'
assert all(0<=page<index_start-1 for page in internal),'Index destination outside preceding content'
assert internal==[row['page']-1 for row in report for _ in range(2)],'Index term/locator destination mismatch'
print(f'PASS: {len(sources)} source documents, {references} numbered chapter references, '
      f'{len(plan)} exact paginated subject headings and {len(internal)} index links')
