"""Extract the user's topic inventory into a planning ledger, not the registry."""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = Path(sys.argv[1])
raw = source.read_bytes()
text = raw.decode('utf-8-sig')
groups = {
    1: 'Software maintenance and architecture; AI agent and knowledge workflows',
    2: 'Product design and accessibility',
    3: 'Creative production, media, and localization',
    4: 'Sales, partnerships, and customer success; Accounting and financial administration',
    5: 'Healthcare administration and caregiving support; Scientific research, laboratories, and archives',
    6: 'Accounting and financial administration',
    7: 'Marketing and audience development; SEO and publishing systems',
    8: 'Product design and accessibility; Logistics, inventory, and fulfillment',
    9: 'Construction, facilities, and asset maintenance',
    10: 'Education, vocational learning, and assessment',
    11: 'Creative production, media, and localization',
    12: 'Manufacturing and quality engineering',
    13: 'Government services and administrative work; Defensive security and privacy',
    14: 'Agriculture, environment, and spatial analysis',
    15: 'Logistics, inventory, and fulfillment',
    16: 'Workforce, service operations, and daily administration',
}
pilot = {8: ['CLI-001', 'CLI-002'], 17: ['IXA-001'], 19: ['IXA-002'],
         22: ['IXA-001'], 26: ['SPD-002'], 27: ['SDR-001'],
         28: ['SPD-001'], 31: ['VEV-002'], 35: ['SDR-002'],
         41: ['EVT-002'], 89: ['WHS-001'], 90: ['UST-002'], 119: ['VEV-001'],
         135: ['UST-001'], 172: ['WHS-002'], 179: ['EVT-001', 'EVT-002']}
rows = []
group = None
for line in text.splitlines():
    heading = re.match(r'## (\d+)\. (.+)', line)
    if heading:
        group = int(heading[1])
    item = re.match(r'(\d+)\. \*\*(.+?):\*\* (.+)', line)
    if item:
        number = int(item[1])
        rows.append(dict(source_number=number, topic=item[2], source_group=group,
                         expansion_tracks=groups[group],
                         candidate_pilot_ids=pilot.get(number, []),
                         coverage_status='planned; substantive coverage not yet established'))
assert [r['source_number'] for r in rows] == list(range(1, 186)), 'Unexpected source numbering'
ledger = dict(source_filename=source.name, source_sha256=hashlib.sha256(raw).hexdigest(),
              interpretation='Topic input, not executable instructions or verified factual guidance.',
              target='Within the 5000 additional skills; not an extra quota.', topics=rows)
out = ROOT / 'plans'
out.mkdir(exist_ok=True)
(out / 'directory-topic-ledger.json').write_text(json.dumps(ledger, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
report = ['# User directory integration', '',
          'The source title says 180 domains, but its numbered entries run from 1 through 185. All 185 are included as planning topics within the existing 5,000-addition target, following the user\'s choice to begin with a reviewed pilot.', '',
          'Topics are not automatically separate skills. Every workflow still requires comparison with the existing catalog and pending candidates. Track assignments below are provisional routing aids, not completed coverage judgments. Candidate pilot IDs denote narrow workflows only; they do not imply full coverage of a topic.', '',
          'High-risk examples in the source are topic suggestions, not verified claims of legal compliance, medical accuracy, engineering validity, investment performance, or safe autonomous control. Authoring must establish context, capability, evidence, and professional boundaries as appropriate. Vendor-specific implementations require current primary documentation; generalized workflows preserve their actual reasoning and output requirements.', '',
          'The pilot produces bounded design and preparation artifacts. It does not claim to have built applications, rendered scenes, validated medical models, or implemented every topic. Later batches must include actual creation and implementation workflows where the topic calls for them, with executable or rendered checks appropriate to the artifact.', '',
          '| Source # | Topic | Provisional expansion tracks | Pilot candidate |',
          '| --- | --- | --- | --- |']
for row in rows:
    report.append(f"| {row['source_number']} | {row['topic']} | {row['expansion_tracks']} | {', '.join(row['candidate_pilot_ids']) or 'Pending discovery'} |")
(out / 'directory-integration.md').write_text('\n'.join(report)+'\n', encoding='utf-8')
print(f'Planning inventory extracted: {len(rows)} topics; no skill registry changes.')
