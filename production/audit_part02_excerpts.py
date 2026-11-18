"""Check Part II's printed excerpts against their recorded companion checkpoint.

Run with --code-repo pointing to a clone containing that historical revision.
This checks source fidelity and structure; it does not compile or run the app.
"""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--code-repo', type=Path, required=True)
args = parser.parse_args()
record = json.loads((ROOT / 'planning/part02-excerpt-provenance.json').read_text())
chapters = [p for p in sorted((ROOT / 'chapters').glob('ch*.md'))
            if 6 <= int(p.name[2:4]) <= 11]
printed = '\n'.join(p.read_text() for p in chapters)
normalize = lambda value: re.sub(r'\s+', '', value)
source_cache = {}
for entry in record['excerpts']:
    text = entry['text']
    assert hashlib.sha256(text.encode()).hexdigest() == entry['sha256']
    assert text in printed, f"Excerpt missing from chapters: {entry['source']}"
    key = (entry['source_ref'], entry['source'])
    if key not in source_cache:
        source_cache[key] = subprocess.check_output(
            ['git', 'show', ':'.join(key)], cwd=args.code_repo, text=True)
    assert normalize(text) in normalize(source_cache[key]), key
    if entry['language'] == 'xml' and text.startswith('<?xml'):
        ElementTree.fromstring(text)

required = ["## What You'll Learn", '**Prerequisites:**', '**Deliverable:**',
            '## Guided Lab', '## Worked Example', '## Chapter Summary',
            '## Exercises', '## Troubleshooting']
counts = {}
for path in chapters:
    text = path.read_text()
    for heading in required:
        assert text.count(heading) == 1, (path.name, heading)
    assert text.index('## Chapter Summary') < text.index('## Exercises')
    blocks = re.findall(r'^```([^\n]*)\n(.*?)^```', text, re.M | re.S)
    for _, body in blocks:
        for line in body.splitlines():
            assert len(line) <= 80, (path.name, len(line), line)
    counts[path.name] = len(blocks)

print(json.dumps({'status': 'passed', 'source_checked_excerpts': len(record['excerpts']),
                  'chapter_code_blocks': counts,
                  'scope': 'Source fidelity, XML well-formedness and chapter structure; no fresh app execution.'},
                 indent=2))
