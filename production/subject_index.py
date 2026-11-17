"""Curated section locators, resolved by ReportLab's multi-pass pagination."""
import json
from pathlib import Path
from reportlab.platypus.tableofcontents import TableOfContents


def load_targets(root: Path):
    plan = json.loads((root / 'planning/subject-index.json').read_text())
    if set(plan) != {'schema', 'entries'} or plan['schema'] != 1:
        raise ValueError('Invalid subject-index plan')
    targets, terms = {}, set()
    for i, row in enumerate(plan['entries']):
        if set(row) != {'term', 'source', 'heading'} or row['term'].casefold() in terms:
            raise ValueError('Duplicate or invalid index term')
        terms.add(row['term'].casefold())
        source = (root / row['source']).resolve()
        if not source.is_relative_to(root.resolve()) or not source.is_file():
            raise ValueError('Index source is missing or outside manuscript')
        headings = [line.lstrip('#').strip() for line in source.read_text().splitlines()
                    if line.startswith(('# ', '## ', '### '))]
        if headings.count(row['heading']) != 1:
            raise ValueError('Index target must identify exactly one heading: ' + row['term'])
        targets.setdefault((row['source'], row['heading']), []).append((row['term'], f'subject-{i:03d}'))
    return targets


class SubjectIndex(TableOfContents):
    """A separate notification channel prevents contents/index cross-contamination."""
    def notify(self, kind, stuff):
        if kind == 'SubjectIndexEntry':
            self.addEntry(*stuff)

    def beforeBuild(self):
        self._entries.sort(key=lambda row: row[1].casefold())
        super().beforeBuild()

    def isSatisfied(self):
        return sorted(self._entries, key=lambda row: row[1].casefold()) == self._lastEntries
