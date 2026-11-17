"""Independent fresh traces against Python blocks extracted from IPR skills."""
from pathlib import Path
import contextlib
import io
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
records = []

def load(name):
    path = ROOT / 'skills' / 'IPR' / name / 'SKILL.md'
    namespace = {}
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        for block in re.findall(r'```python\s*\n(.*?)```', path.read_text(encoding='utf-8'), re.S):
            exec(compile(block, str(path), 'exec'), namespace)
    records.append(('Embedded assertions: ' + name, output.getvalue().strip(), 'PASS'))
    return namespace

def record(label, result, condition):
    assert condition, (label, result)
    records.append((label, result, 'PASS'))

n = load('interrupted-form-draft-restoration')
offer, accept = n['offer'], n['accept']
current = dict(form='Notebook',record='Cedar',schema='S2',revision=7,values={},submitted=False)
saved = dict(form='Notebook',record='Cedar',schema='S2',values={'title':'Aster','secret':'omit'})
proposal = offer(saved,current,{'title'})
restored, status = accept(current,proposal)
record('IPR-001 ordinary: allowlisted title and no submission', (restored,status),
       restored['values']=={'title':'Aster'} and restored['submitted'] is False and current['values']=={})
result = accept(current,None)
record('IPR-001 missing: no eligible offer',result,result==(current,'review-required'))
switched = {}
for field in ('form','record','schema'):
    other = dict(current, **{field:'different'})
    result = accept(other,proposal)
    assert result==(other,'review-required')
    switched[field]=result
edited=dict(current,revision=8,values={'title':'Latest'})
assert accept(edited,proposal)==(edited,'review-required')
submitted=dict(current,revision=8,submitted=True)
assert accept(submitted,proposal)==(submitted,'review-required')
policy_changed=dict(current,revision=8)
assert accept(policy_changed,proposal)==(policy_changed,'review-required')
record('IPR-001 edge: same-revision identity switches and later edit', switched, True)

# The pre-repair shape held revision and values only. Reproduce the actual
# failure independently, without modifying the repaired skill.
def previous_accept(current, proposed):
    if proposed is None or proposed[0] != current['revision']:
        return current,'review-required'
    updated=dict(current)
    updated['values']=dict(proposed[1]); updated['revision']+=1
    updated['submitted']=False
    return updated,'restored-for-review'
wrong_record=dict(current,record='Maple')
before=previous_accept(wrong_record,(7,{'title':'Aster'}))
assert before[0]['values']=={'title':'Aster'}
record('Reproduction of original defect: Cedar values applied to Maple by old acceptance guard',before,True)

n=load('asynchronous-result-generation-ownership')
initial,begin,settle=n['initial'],n['begin'],n['settle']
s,token=begin(initial(),'violet')
s,verdict=settle(s,token,['v1','v2'])
record('IPR-002 ordinary: owning response settles once',(s,verdict),s['items']==('v1','v2') and verdict=='accepted')
assert settle(s,token,error='duplicate late callback')==(s,'ignored')
s,token=begin(initial(),'pending')
result=settle(s,None,['orphan'])
record('IPR-002 missing: response has no request token',result,result==(s,'ignored'))
s,a=begin(initial(),'red'); s,b=begin(s,'blue'); s,c=begin(s,'red')
assert settle(s,a,['obsolete'])==(s,'ignored')
assert settle(s,b,error='stale error')==(s,'ignored')
s,unused=begin(s,'')
result=settle(s,c,error='late current failure')
record('IPR-002 edge: repeated text then clear rejects stale success and errors',result,result==(s,'ignored') and s['status']=='idle')

n=load('transactional-edit-history-branching')
start,commit,undo,redo=[n[k] for k in ('start','commit','undo','redo')]
first=start('Cedar'); second=commit(first,'Maple'); third=commit(second,'Aster')
result=redo(undo(third))
record('IPR-003 ordinary: complete undo-redo round trip',result,result==third and first[1]=='Cedar')
try:
    commit(first,None)
except ValueError as error:
    result=str(error)
else:
    raise AssertionError('Missing snapshot accepted')
record('IPR-003 missing: no string snapshot supplied',result,result=='reference snapshots must be strings')
back=undo(third)
preview='Discard me'
preview=None
assert back==second[:2]+(('Aster',),)
assert commit(back,back[1])==back
branch=commit(back,'Juniper')
result=redo(branch)
record('IPR-003 edge: canceled preview/no-op retain redo; real edit clears it',result,result==branch and branch[2]==())

lines=['# Independent IPR executable review','',
       'Reviewer: recover_lre, separate from IPR author. Fresh fictional traces execute the actual fenced Python blocks. Interpreter observed: '+sys.version.split()[0]+'.', '',
       'Initial review identified an acceptance-time identity gap in IPR-001. The original revision-only guard is reproduced separately below; the coordinator repaired the actual skill to bind identity and revision. Tests below run the repaired skill and reject form, record and schema switches even when revision remains equal.', '']
for label,result,status in records:
    lines += ['## '+label,'','```json',json.dumps(result,ensure_ascii=False,indent=2),'```','',status,'']
lines += ['## Judgment and boundaries','',
    'IPR-001: Fresh normal, missing-offer and switched-context cases retain allowlist, identity and edit-version constraints. The original failure is a regression reproduction, not a current failure. Follow-up assertions reject offers after submission or policy changes when the caller advances revision as required. The inspected post-snippet contract limits the model to one editing lifetime and fixed allowlist; reopened records must discard old offers before revision reset or add a lifetime identity. This boundary is explicit, not implemented by the snippet. If the user provides no form identity or field policy, request form/record/schema and allowed fields before offering recovery; no browser persistence is inferred.', '',
    'IPR-002: Fresh response traces reject missing ownership, duplicate callbacks, repeated-text older generations and errors after clearing. A request whose non-query context is unspecified requires the actual context contract before integration; the sample only implements one query-owned view.', '',
    'IPR-003: Fresh traces preserve history through canceled preview and no-op commit, reject missing string content and invalidate the old future on a genuine branch edit. Grouped previews are modeled outside committed history as instructed, not inferred from timings.', '',
    'These are executable transition-model tests, not rendered UI, framework lifecycle, persistent storage, service, security or cross-model validation. No current external APIs, empirical claims or mutable policies were assumed. Fixture labels are fictional; arithmetic consists only of deterministic revision increments.', '',
    'No remaining blocker found in these tested paths after the identity repair. Usability of a production adaptation still requires its actual state schema and integration checks.']
(ROOT/'logs'/'b6-ipr-tests.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('IPR independent review PASS: nine fresh scenario groups; identity regression reproduced and repaired implementation passes')
print('Saved logs/b6-ipr-tests.md; interpreter',sys.version.split()[0])
