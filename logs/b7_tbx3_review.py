from pathlib import Path
import re,contextlib,io,sys,hashlib
from collections import Counter
root=Path(__file__).resolve().parents[1]
p=root/'skills/TBX/numeric-interval-membership-assignment/SKILL.md'; data=p.read_bytes(); ns={}
with contextlib.redirect_stdout(io.StringIO()) as captured:
 for code in re.findall(r'```python\s*\n(.*?)```',data.decode(),re.S): exec(compile(code,str(p),'exec'),ns)
f=ns['assign']; defs=[('A','0','2',False,False),('B','2','4',False,True),('C','4','6',True,True)]
rows=[('x','2'),('y','4'),('z',None),('n','NaN'),('v','3')]; result=f(rows,defs)
assert result==[('x','2','unmatched',[]),('y','4','ambiguous',['B','C']),('z',None,'missing',[]),('n','NaN','invalid',[]),('v','3','assigned',['B'])]
probes=f([(str(i),str(i)) for i in (0,2,4,6)],defs)
assert [x[3] for x in probes]==[[],[],['B','C'],['C']]
def fails(fn):
 try: fn()
 except ValueError as e: return str(e)
 raise AssertionError('invalid contract accepted')
missing=fails(lambda:f([('x','1')],[('A','0','2',None,True)])); assert 'endpoint' in missing
for bad in [[('A','2','0',True,True)],[('A','1','1',True,False)],[('A','0','Infinity',True,True)],[('A','0','1',True,True),('A','2','3',True,True)]]: fails(lambda:f([],bad))
single=[('P','0.10000000000000000000000000001','0.10000000000000000000000000001',True,True)]
r=f([('a','0.1'),('b','0.10000000000000000000000000001')],single)
assert [x[2] for x in r]==['unmatched','assigned']
fails(lambda:f([('a','1'),('a','2')],defs))
reversed_result=f(rows,defs[::-1]); assert [x[2] for x in reversed_result]==[x[2] for x in result]
assert set(reversed_result[1][3])==set(result[1][3])
report=f'''# Independent TBX003 review
Coordinator separate from finish_tables author. Python {sys.version.split()[0]}; SHA256 {hashlib.sha256(data).hexdigest()}.
Embedded assertions: {captured.getvalue().strip()}

## Ordinary and shared-edge fixture
Fictional Larch request: classify 2,4,null,NaN,3 in A=(0,2), B=(2,4], C=[4,6]; retain all rows.
```text
Contract: Larch snapshot; common fictional units; decimal strings; explicitly supplied edges.
Membership: {result!r}
Endpoint probes: {probes!r}
Reconciliation: Five inputs and five outputs; {dict(Counter(x[2] for x in result))!r}; total five.
Disposition: Diagnostic accepted; single-label output withheld pending ambiguous and other nonassigned dispositions.
Limits: Exact supplied representation only; no measurement validity or intended-universe coverage finding.
```
Asserted all results, endpoints and statuses; PASS.

## Missing endpoint policy
Fictional Larch request supplies A lower endpoint without its inclusion flag.
```text
Contract: Incomplete inclusion definition for A.
Membership: Not calculated.
Endpoint probes: Blocked pending flag.
Reconciliation: No accepted classification output.
Disposition: Request whether A includes its lower endpoint; observed error: {missing}.
Limits: No default bracket convention inferred. Source unchanged.
```
Missing policy fails before classification; PASS.

## Exact singleton and interval-order edge
Fictional Larch supplies a closed singleton 0.10000000000000000000000000001 and observations a=0.1, b=that exact value.
```text
Contract: Finite decimal strings; closed singleton P; no quantization.
Membership: {r!r}
Endpoint probes: The supplied singleton endpoint matches P.
Reconciliation: Two inputs, two outputs; one unmatched and one assigned.
Disposition: Preserve differing representations and membership; do not round to merge.
Limits: No measurement-precision claim. Reversing interval order in the separate overlap fixture changes label order but not membership sets or statuses.
```
Exact-boundary and permutation assertions PASS. Additional reversed/empty/nonfinite/duplicate-label contracts and duplicate observation identities rejected.

## Substantive scope review
The procedure performs per-observation membership across all supplied intervals. TDQ004 range validity is a different output and judgment: unmatched does not mean invalid here. No thresholds are prescribed. Every number above is fictional input or asserted result. Endpoint probes do not certify exhaustive coverage; that limit is explicit. All three fresh fixture outputs follow the skill template. No external serialization or platform execution claimed.
'''
(root/'logs/b7-tbx3-tests.md').write_text(report,encoding='utf-8')
print('PASS three fresh TBX003 fixtures plus invalid-contract and permutation assertions')
