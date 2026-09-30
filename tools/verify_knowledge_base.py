"""Verify this published knowledge snapshot using only Python's standard library."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    files = json.loads((ROOT / 'publication/files.sha256.json').read_text())
    for rel, want in files.items():
        p = ROOT / rel
        assert p.is_file() and sha(p) == want, rel
        assert p.name not in {'hd_cells.scs', 'license.dat'} and p.suffix not in {'.lib', '.cdl', '.lic'}, rel
        assert p.stat().st_size < 50 * 1024**2, rel
    reports = ROOT / 'SMIC18-Benchmark-Reproduction/evidence'
    cases = sorted(reports.glob('[0-9][0-9]-*'))
    assert len(cases) == 50
    pages = 0
    diagrams = 0
    for c in cases:
        pp = json.loads((c / 'pdf_provenance.json').read_text())
        review = json.loads((c / 'markdown_readability.json').read_text())
        assert pp['sha256'] == sha(c / 'review.pdf')
        assert pp['circuit_sha256'] == sha(c / 'circuit.scs')
        assert pp['results_sha256'] == sha(c / 'latest_results.json')
        assert review['review_status'] == 'passed'
        assert review['markdown_sha256'] == sha(c / 'review_report.md')
        md = (c / 'review_report.md').read_text()
        assert not re.search(r'!\[[^\]]*\]\([^)]*(?:markdown_assets|pdf_review)/page-\d', md)
        assert '图内标注与坐标文字' not in md
        assert re.findall(r'```spectre\n(.*?)\n```', md, re.S) == [(c / 'circuit.scs').read_text().rstrip()]
        for fig in review['figures']:
            assert sha(c / fig['png']) == fig['png_sha256']
            assert sha(c / fig['svg']) == fig['svg_sha256']
        pages += pp['pages']
        if (c / 'system_block_diagram.mmd').exists():
            diagrams += 1
            assert '```mermaid\n' + (c / 'system_block_diagram.mmd').read_text() + '```' in md
    assert pages == 533 and diagrams == 28
    lessons = ROOT / 'Analog-Design-Bench-V2-Lessons'
    assert len(list((lessons / 'cases').glob('*.md'))) == 50
    assert len(list((lessons / 'topics').glob('*.md'))) == 8
    print(json.dumps(dict(status='passed',files=len(files),reproduction_reports=50,pdf_pages=pages,
                         system_diagrams=diagrams,case_notes=50,topics=8), indent=2))


if __name__ == '__main__':
    main()
