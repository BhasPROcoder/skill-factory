"""Independent fresh fixture executions; no production localization claims."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    path = ROOT / 'skills' / 'LRE' / name / 'SKILL.md'
    data = path.read_bytes()
    namespace = {}
    with redirect_stdout(StringIO()) as captured:
        for block in re.findall(r'```python\s*\n(.*?)```', data.decode('utf-8'), re.S):
            exec(compile(block, str(path), 'exec'), namespace)
    print('SOURCE', name, hashlib.sha256(data).hexdigest())
    print('EMBEDDED', captured.getvalue().strip())
    return namespace


def report(label, actual, expected):
    assert actual == expected, (label, actual, expected)
    print(label, json.dumps(actual, sort_keys=True), 'PASS')


print('Python', sys.version.split()[0])
check = load('localized-message-placeholder-contract')['check']
report('LRE001 ordinary', check('[[recipient]] receives [[parcel]] from [[sender]]',
       ['sender', 'recipient', 'parcel']), {'missing': [], 'unexpected': []})
report('LRE001 missing', check('[[parcel]] delivered to [[recipient]]',
       ['sender', 'recipient', 'parcel']), {'missing': ['sender'], 'unexpected': []})
report('LRE001 edge', check('[[sender]] [[sender]] [[parcel]] [[recipient]]',
       ['sender', 'recipient', 'parcel']), {'missing': [], 'unexpected': ['sender']})
report('LRE001 unsupported', check('[[parcel-name]]', ['parcel']),
       {'syntax': 'unsupported or malformed token'})

resolve = load('locale-fallback-resolution-trace')['resolve']
report('LRE002 ordinary', resolve('go', ['coast', 'island'],
       {'coast': {'go': 'Proceed'}, 'island': {'go': 'Fallback'}}, False),
       {'locale': 'coast', 'value': 'Proceed', 'trace': [('coast', 'selected')]})
report('LRE002 missing', resolve('go', ['coast', 'island', 'inland'],
       {'island': {}, 'inland': {'go': None}}, False),
       {'locale': None, 'value': None, 'trace': [('coast', 'bundle unavailable'),
        ('island', 'key absent'), ('inland', 'value missing by policy')]})
report('LRE002 edge', resolve('subtitle', ['coast', 'island'],
       {'coast': {'subtitle': ''}, 'island': {'subtitle': 'Extra'}}, True),
       {'locale': 'coast', 'value': '', 'trace': [('coast', 'selected')]})
try:
    resolve('go', ['coast', 'coast'], {}, False)
except ValueError as exc:
    print('LRE002 duplicate policy', str(exc), 'PASS')
else:
    raise AssertionError('duplicate order was accepted')

coverage = load('translation-source-revision-coverage')['coverage']
report('LRE003 ordinary', coverage({'save': 'context-D'},
       {'save': {'source_revision': 'context-D', 'approved': True}}),
       ({'save': 'ready by supplied metadata'}, []))
report('LRE003 missing', coverage({'save': 'D', 'close': 'E'}, {'save': {}}),
       ({'save': 'lineage unknown', 'close': 'missing'}, []))
report('LRE003 edge', coverage({'open': 'status-B', 'title.new': 'title-C'}, {
       'open': {'source_revision': 'command-A', 'approved': True},
       'title.new': {'source_revision': 'title-C', 'approved': False},
       'title.old': {'source_revision': 'title-C', 'approved': True}}),
       ({'open': 'stale', 'title.new': 'review pending'}, ['title.old']))
print('All independent mechanical cases passed; semantic and live-runtime review remain bounded.')
