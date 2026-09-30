#!/usr/bin/env python3
"""Static files-only audit. Never imports/executes upstream code or uses a simulator."""
import hashlib
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit():
    errors = []
    manifest = json.loads((BASE / 'case-manifest.json').read_text(encoding='utf8'))
    ids = re.findall(r'^id = "([^"]+)"',
                     (BASE / 'sources/upstream/tasks/benchmark.toml').read_text(), re.M)
    cases = manifest['cases']
    if len(ids) != 50 or [c['task_id'] for c in cases] != ids:
        errors.append('Frozen task list does not match 50 case records')
    provenance_matches = 0
    astra_passes = 0
    for c in cases:
        task = BASE / 'sources/upstream/tasks' / c['task_id']
        ref = json.loads((task / 'results/reference.json').read_text())
        for key, file in [('circuit_sha256', 'solution/circuit.spi'),
                          ('instruction_sha256', 'instruction.md'),
                          ('task_toml_sha256', 'task.toml')]:
            if digest(task / file) == ref['provenance'][key]:
                provenance_matches += 1
            else:
                errors.append(c['task_id'] + ': provenance mismatch: ' + file)
        ar = json.loads((BASE / 'sources/astra' / c['task_id'] / 'result.json').read_text())
        if ar.get('pass') is True and ar['result'].get('binary_pass') == 1 and all(
                g.get('status') == 'passed' for g in ar['result']['gates']):
            astra_passes += 1
        else:
            errors.append(c['task_id'] + ': unexpected website pass/gate status')
        note = BASE / c['case_path']
        if not note.is_file():
            errors.append('Missing note: ' + c['case_path'])
        else:
            text = note.read_text(encoding='utf8')
            for section in ['场景与测试边界', 'Reference 拓扑', '工程认识',
                            '不能由 pass', '检查摘要', 'Testbench 查阅索引']:
                if section not in text:
                    errors.append(c['case_path'] + ': missing section ' + section)
    tree = json.loads((BASE / 'sources/upstream-git-tree.json').read_text())
    if tree.get('truncated'):
        errors.append('Git tree is truncated')
    blob_matches = 0
    expected = set()
    for item in tree['tree']:
        if item['type'] != 'blob':
            continue
        expected.add(item['path'])
        p = BASE / 'sources/upstream' / item['path']
        if not p.is_file():
            errors.append('Missing upstream file: ' + item['path'])
            continue
        raw = p.read_bytes()
        actual = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        if actual != item['sha']:
            errors.append('Git blob mismatch: ' + item['path'])
        else:
            blob_matches += 1
    actual_paths = {p.relative_to(BASE / 'sources/upstream').as_posix()
                    for p in (BASE / 'sources/upstream').rglob('*') if p.is_file()}
    if actual_paths != expected:
        errors.append('Upstream file set differs from recorded Git tree')
    source_manifest = json.loads((BASE / 'sources/sha256-manifest.json').read_text())
    source_matches = 0
    for row in source_manifest['files']:
        p = BASE / row['path']
        if not p.is_file() or digest(p) != row['sha256']:
            errors.append('Source SHA-256 mismatch: ' + row['path'])
        else:
            source_matches += 1
    source_paths = {p.relative_to(BASE).as_posix() for p in (BASE / 'sources').rglob('*')
                    if p.is_file() and p.name != 'sha256-manifest.json'}
    if source_paths != {r['path'] for r in source_manifest['files']}:
        errors.append('Source file set differs from SHA-256 manifest')
    authored = list(BASE.glob('*.md')) + list((BASE / 'cases').glob('*.md')) + list(
        (BASE / 'topics').glob('*.md')) + [BASE / 'sources/README.md']
    links = 0
    for p in authored:
        text = p.read_text(encoding='utf8')
        if re.search(r'\[\[\d+\]\]', text):
            errors.append(str(p) + ': unresolved case placeholder')
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            if re.match(r'^[a-zA-Z]+://', target) or target.startswith('#'):
                continue
            path = target.split('#', 1)[0]
            links += 1
            if path and not (p.parent / path).exists():
                errors.append('{}: broken link {}'.format(p.relative_to(BASE), target))
    return dict(check_kind='static-files-only-not-circuit-verification',
                local_simulations_run=0, upstream_scripts_executed=0,
                task_count=len(cases), case_notes=len(list((BASE / 'cases').glob('*.md'))),
                topic_notes=len(list((BASE / 'topics').glob('*.md'))),
                reference_provenance_hashes_matched=provenance_matches,
                upstream_git_blobs_matched=blob_matches,
                source_sha256_matched=source_matches,
                astra_r1_website_pass_records=astra_passes,
                astra_detailed_static_comparisons=sum(c['astra_detailed_static_review'] for c in cases),
                bench_inventory_entries=sum(len(c['bench_files']) for c in cases),
                local_markdown_links_checked=links, errors=errors,
                status='passed' if not errors else 'failed')


if __name__ == '__main__':
    result = audit()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if not result['errors'] else 1)
