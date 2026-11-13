"""Independent ATR review: execute actual skill snippets and fresh fixtures."""
from pathlib import Path
from contextlib import redirect_stdout
from copy import deepcopy
import hashlib
import io
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
names = {
    'ATR-001': 'audio-edit-frame-provenance',
    'ATR-002': 'audio-loop-edge-taper-comparison',
    'ATR-003': 'audio-stem-integer-offset-alignment',
}
loaded, records = {}, []
for sid, name in names.items():
    path = ROOT / 'skills' / 'ATR' / name / 'SKILL.md'
    raw = path.read_bytes()
    text = raw.decode('utf-8')
    scope, captured = {}, io.StringIO()
    with redirect_stdout(captured):
        for block in re.findall(r'```python\s*\n(.*?)```', text, re.S):
            exec(compile(block, str(path), 'exec'), scope)
    loaded[sid] = scope
    records.append((sid, hashlib.sha256(raw).hexdigest(), captured.getvalue().strip()))

cases = []
def record(sid, kind, request, actual, checks, response):
    cases.append(dict(skill=sid, kind=kind, request=request, actual=actual,
                      checks=checks, response=response))

def rejected(call, expected):
    try:
        call()
    except expected as exc:
        return {'exception': type(exc).__name__, 'message': str(exc)}
    raise AssertionError('expected rejection did not occur')

assemble = loaded['ATR-001']['assemble']
source = {'P': [(3,30),(4,40),(5,50)], 'Q': [(6,60),(7,70)]}
saved = deepcopy(source)
edits = [('P',0,2),('Q',1,2),('P',1,3)]
out, ledger = assemble(source, edits)
assert out == [(3,30),(4,40),(7,70),(4,40),(5,50)]
assert ledger == [('P',0,2,0,2),('Q',1,2,2,3),('P',1,3,3,5)]
assert source == saved
for sid,start,end,lo,hi in ledger:
    assert out[lo:hi] == source[sid][start:end] and end-start == hi-lo
record('ATR-001','ordinary',
       'Fictional Cedar supplies P/Q stereo arrays as recorded below on one confirmed common rate and channel order. Assemble P[0,2), Q[1,2), P[1,3); exact decoded arrays only.',
       {'sources':source,'edits':edits,'output':out,'ledger':ledger},
       ['five output frames','each output interval equals source slice','repeated P region retained','inputs unchanged'],
       'Construction: Cedar P/Q, confirmed common rate and stereo order. Edit ledger uses the exact source/output intervals below. Output: constructed array below. Checks: interval equality, total length and source preservation passed. Join review: not listened. Processing boundary: exact copies only, no encoding or fades.')

missing = rejected(lambda: assemble({'P':[(1,)]}, [('Absent',0,1)]), KeyError)
record('ATR-001','missing',
       'Fictional Cedar requests Absent[0,1), but provides only source P. Do not substitute another recording.',
       missing, ['missing source rejected','no returned constructed output'],
       'Construction: unresolved source Absent. Edit ledger: retain requested Absent[0,1) as pending. Output: none. Checks: code rejected the missing key. Join review: not performed. Processing boundary: no replacement or edit delivered. Please supply Absent with its frame basis and channel identity, or explicitly revise the edit decision.')

bad_indices = []
for bounds in [(-1,1),(1,1),(2,1),(0,4),(False,1)]:
    bad_indices.append({'bounds':bounds, 'result':rejected(lambda b=bounds: assemble(source,[('P',*b)]),ValueError)})
assert source == saved
record('ATR-001','edge',
       'Fictional Cedar asks to accept negative, empty, reversed, oversized and boolean frame bounds by permissive slicing. P has three frames.',
       bad_indices, ['all five malformed selections rejected','source unchanged'],
       'Construction: Cedar P supplied; requested bounds are invalid. Edit ledger: each rejected interval retained in the results below. Output: no shortened substitute. Checks: every malformed selection rejected. Join review: not performed. Processing boundary: ask the edit owner for valid integer boundaries rather than silently clipping.')

taper = loaded['ATR-002']['edge_taper']
seam = loaded['ATR-002']['seam_difference']
frames = [(6,12),(6,12),(6,12),(8,16),(-8,-16),(-6,-12),(-6,-12),(-6,-12)]
saved_frames = deepcopy(frames)
candidate = taper(frames,3)
assert candidate == [(0,0),(3,6),(6,12),(8,16),(-8,-16),(-6,-12),(-3,-6),(0,0)]
assert candidate[3:5] == frames[3:5] and frames == saved_frames
assert seam(frames) == (12,24) and seam(candidate) == (0,0)
assert all(right == 2*left for left,right in candidate)
record('ATR-002','ordinary',
       'Fictional studio Hazel permits editing both outer three-frame windows of the stereo fixture below. Use the same taper in both channels and return decoded arrays only.',
       {'baseline':frames,'candidate':candidate,'baseline_seam':seam(frames),'candidate_seam':seam(candidate)},
       ['eight frames retained','stereo gain relation preserved','center unchanged','source unchanged'],
       'Baseline: Hazel eight stereo frames, supplied unchanged rate. Candidate: three-frame linear edge taper shown below. Comparison: endpoint differences become zero, center remains unchanged and duration is preserved. Listening: not performed. Disposition: keep for audition, not audibly approved. Remaining: actual playback review if perceptual acceptance is required.')

missing_taper = rejected(lambda: taper(frames,None),ValueError)
record('ATR-002','missing',
       'Fictional Hazel supplies valid arrays but no taper length or editable-region permission; requester asks to use a typical fade.',
       missing_taper, ['missing trial length rejected','no universal duration selected'],
       'Baseline: supplied arrays retained. Candidate: not constructed. Comparison: no authorized trial extent. Listening: not performed. Disposition: retain original pending scope. Remaining: please specify editable edge regions and a trial frame count; identify any protected attack and listening target. No typical duration is inferred.')

short = [(2,4),(3,6),(4,8),(5,10)]
adjacent = taper(short,2)
assert adjacent == [(0,0),(3,6),(4,8),(0,0)] and len(adjacent)==4
overlap = rejected(lambda:taper(short,3),ValueError)
record('ATR-002','edge',
       'Fictional Hazel expressly permits two-frame edge windows on a four-frame stereo loop. Compare the touching nonoverlapping windows, then try an unapproved three-frame window. No playback requested.',
       {'baseline':short,'two_frame_candidate':adjacent,'overlap_attempt':overlap},
       ['touching windows do not overlap','four frames retained','overlapping windows rejected'],
       'Baseline: four-frame stereo fixture. Candidate: authorized two-frame windows produce the array below; no unedited center interval exists. Comparison: inner endpoints retain unity and outer endpoints zero. Listening: not performed. Disposition: numeric candidate only. Remaining: larger overlapping windows require another approved method; endpoint equality does not establish an inaudible join.')

shift = loaded['ATR-003']['shift_stem']
stem = [(11,21),(12,22),(13,23),(14,24)]
saved_stem = deepcopy(stem)
delayed, delay_log = shift(stem,2,5)
advanced, advance_log = shift(stem,-1,5)
assert delayed == [(0,0),(0,0),(11,21),(12,22),(13,23)]
assert delay_log == (0,3,2,5,0,1)
assert advanced == [(12,22),(13,23),(14,24),(0,0),(0,0)]
assert advance_log == (1,4,0,3,1,0)
assert stem == saved_stem
record('ATR-003','ordinary',
       'Fictional Juniper uses supplied stereo source on one agreed frame basis. Construct separate +2 and -1 candidates of length five. Owner permits last-frame crop in +2 and first-frame crop in -1. No marker identity or listening claim requested.',
       {'source':stem,'delayed':delayed,'delay_ledger':delay_log,'advanced':advanced,'advance_ledger':advance_log},
       ['five frames per candidate','positive offset delays','negative offset advances','tail/head crops explicit','inputs unchanged'],
       'Grid: supplied common basis, five frames. Alignment ledger: +2 retains [0,3) to [2,5), tail crop one; -1 retains [1,4) to [0,3), head crop one. Constructed arrays: below. Marker check: not requested or inferred. Content decision: both stated crops permitted; listening not performed. Verification: exact retained frame placement and unchanged source passed; no phase or encoding conclusion.')

missing_offset = rejected(lambda:shift(stem,None,5),ValueError)
fractional = rejected(lambda:shift(stem,0.5,5),ValueError)
record('ATR-003','missing',
       'Fictional Juniper asks for an aligned result but supplies neither approved offset nor confirmed corresponding marker. A suggested half-frame approximation is not authorized.',
       {'missing_offset':missing_offset,'fractional_offset':fractional},
       ['missing and fractional offsets rejected','no silent rounding'],
       'Grid: output request known, offset unresolved. Alignment ledger: pending. Constructed arrays: none. Marker check: identity and desired location required if deriving offset. Content decision: no crop accepted. Verification: reference rejects missing/fractional offsets. Please provide approved integer offset or confirmed marker indices and an approved alternative method for fractional placement.')

protected, protected_log = shift(stem,-3,4)
assert protected == [(14,24),(0,0),(0,0),(0,0)]
assert protected_log == (3,4,0,1,3,0)
no_overlap = rejected(lambda:shift(stem,4,4),ValueError)
record('ATR-003','edge',
       'Fictional Juniper proposes -3 on a four-frame grid. The first three source frames are protected speech and no crop is authorized. Also test +4, which would place all material outside the grid.',
       {'proposed_candidate':protected,'crop_ledger':protected_log,'no_overlap':no_overlap},
       ['three head frames would be removed','only final frame retained','zero-overlap rejected'],
       'Grid: four frames. Alignment ledger: proposed -3 retains [3,4) at [0,1), crops three protected head frames and pads three trailing frames. Constructed arrays: diagnostic candidate only below. Marker check: arithmetic cannot authorize removal. Content decision: reject delivery under supplied protection; request grid or offset revision. Verification: source placement passed, zero-overlap alternative rejected; no phase or listening acceptance.')

report = ['# Independent ATR execution review', '',
          'Reviewer: review_atr, independent of author recover_atr. All cases are new fictional fixtures. The script executes the actual embedded snippets, asserts new results and records outputs. Narrative responses below are the reviewer’s application of the full skill; permission, missing-input and perceptual judgments are not claimed as automated by the snippets.', '',
          'Observed Python interpreter: ' + sys.version.split()[0], '',
          '## Reviewed source fingerprints', '']
for sid,digest,output in records:
    report.extend([f'- {sid}: SHA256 `{digest}`; embedded output: `{output}`'])
for case in cases:
    report.extend(['',f"## {case['skill']} {case['kind']}",'',
                   'Request: '+case['request'],'','Actual numerical result:', '```json',
                   json.dumps(case['actual'],indent=2),'```','',
                   'Reviewer response:', '```text',case['response'],'```','',
                   'Checks passed: '+ '; '.join(case['checks'])+'.'])
report.extend(['','## Scope, claims and uniqueness', '',
    'Nine fresh cases passed their executed assertions; no blocker found in these paths. Finite numeric arrays, rate agreement and channel order remain preconditions as stated by the skills. These checks are not production decoders, listening tests or proof of perceptual quality. The missing/protected-input responses apply the written workflow rather than claiming the functions enforce approval.', '',
    'Routing and selected procedures compared through sf.py: TAM-004 chooses dialogue meaning and pacing; ATR-001 constructs exact source-frame correspondence. TAM-005 is a noise-reduction audition plan; ATR-002 constructs a bounded edge-taper candidate and reports its numerical alteration. TAM-009 defines stem delivery requirements and reimport checks; ATR-003 implements integer placement with explicit crops and padding. The new artifacts and decision rules are distinct from those neighbors; this is a substantive comparison, not a universal uniqueness proof.', '',
    'Arithmetic in fixtures is asserted against literal expected arrays, interval lengths and crop ledgers. Names and numeric inputs are explicitly fictional. No rate, production threshold, legal rule, current software API, source citation or audibility statistic is invented. Review covers decoded arrays and procedural decisions only.', ''])
(ROOT/'logs'/'b6-atr-tests.md').write_text('\n'.join(report),encoding='utf-8')
print(f'PASS {len(cases)} fresh ATR cases; embedded snippets passed; report logs/b6-atr-tests.md')
