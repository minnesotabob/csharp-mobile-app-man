"""Validate the Chapters 12–21 revision against its historical code checkpoints.

This checks printed source and instructional structure, not app execution.
"""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--code-repo', type=Path, required=True)
args = parser.parse_args()
record = json.loads((ROOT / 'planning/part34-excerpt-provenance.json').read_text())
cache = {}
normalize = lambda value: re.sub(r'\s+', '', value)
for entry in record['excerpts']:
    chapter = next((ROOT / 'chapters').glob(f"ch{entry['chapter']:02d}-*.md"))
    text = entry['text']
    assert text in chapter.read_text(), (entry['chapter'], entry['source'])
    assert hashlib.sha256(text.encode()).hexdigest() == entry['sha256']
    key = (entry['source_ref'], entry['source'])
    if key not in cache:
        cache[key] = subprocess.check_output(
            ['git', 'show', ':'.join(key)], cwd=args.code_repo, text=True)
    assert normalize(text) in normalize(cache[key]), key
    assert all(len(line) <= 80 for line in text.splitlines()), key

ordered = ['## Guided Lab', '## Worked Example', '## Troubleshooting',
           '## Chapter Summary', '## Exercises']
for number in range(12, 22):
    path = next((ROOT / 'chapters').glob(f'ch{number:02d}-*.md'))
    text = path.read_text()
    for heading in ["## What You'll Learn", '**Prerequisites:**', '**Deliverable:**', *ordered]:
        assert text.count(heading + ('\n' if heading.startswith('##') else '')) == 1, (number, heading)
    positions = [text.index(heading + '\n') for heading in ordered]
    assert positions == sorted(positions), number
    assert not re.search(r'\b[a-f0-9]{40}\b', text), number

print(f"PASS: {len(record['excerpts'])} source-checked excerpts; ten ordered chapter templates; "
      'no commit hashes in reader chapters. No fresh app execution claimed.')
