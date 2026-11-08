from pathlib import Path
import re, io, contextlib, hashlib, sys
from collections import Counter
root=Path(__file__).resolve().parents[1]
report=['# Independent TBX review','Reviewer: coordinator, separate from table authors. Fictional fixtures; in-memory Python only.', 'Python '+sys.version.split()[0]]
def load(name):
 p=root/'skills/TBX'/name/'SKILL.md'; data=p.read_bytes(); ns={}
 with contextlib.redirect_stdout(io.StringIO()) as out:
  for code in re.findall(r'```python\s*\n(.*?)```',data.decode(),re.S): exec(compile(code,str(p),'exec'),ns)
 report.extend([name+' SHA256 '+hashlib.sha256(data).hexdigest(),'Embedded: '+out.getvalue().strip()]); return ns
def case(name,output): report.extend(['## '+name,'```text',output,'```','Fresh assertions PASS.'])
def fails(fn,kind):
 try: fn()
 except kind as e: return str(e)
 raise AssertionError('invalid input accepted')
n=load('reversible-wide-long-cell-mapping'); melt,rebuild=n['melt'],n['rebuild']
rows=[('B',{'x':None,'y':''}),('A',{'x':0,'y':7})]; ids,cols,cells=melt(rows,['y','x'])
r=rebuild(ids,cols,cells[::-1]); assert r==rows and list(r[0][1])==cols
case('TBX001 ordinary','Boundary: Fictional Fir snapshot, scalar rectangle.\nIdentity manifests: B,A; y,x.\nLong records: '+repr(cells)+'\nReconstruction: '+repr(r)+'\nChecks: Four unique coordinates; null, empty text, zero and order retained after record reversal.\nLimits: In-memory only; no serialization tested.')
error=fails(lambda:melt([('A',{'x':1})],['x','y']),ValueError)
case('TBX001 missing input','Boundary: Fictional Fir incomplete rectangle.\nIdentity manifests: A; x,y.\nLong records: Not emitted.\nReconstruction: '+error+'\nChecks: Absent y rejected; not converted to null.\nLimits: Request actual y cell or corrected selection; no source mutation.')
cells=[('A','p',1),('A','p',1),('A','q',2),('B','p',3)]
counts=Counter((a,b) for a,b,_ in cells); expected={(a,b) for a in ['A','B'] for b in ['p','q']}
duplicates={k for k,v in counts.items() if v>1}; missing=expected-set(counts)
assert duplicates=={('A','p')} and missing=={('B','q')}; fails(lambda:rebuild(['A','B'],['p','q'],cells),ValueError)
assert rebuild(['A','B'],[],[])==[('A',{}),('B',{})]
case('TBX001 duplicate masks missing','Boundary: Fictional Fir corrupt four-record export preserved.\nIdentity manifests: A,B; p,q.\nLong records: '+repr(cells)+'\nReconstruction: Rejected duplicate A/p and missing B/q; request corrected export.\nChecks: Separate coordinate tally finds both defects; total four is insufficient. Zero-column sidecars reconstruct two empty rows.\nLimits: Constructor fails fast; complete defect inventory comes from separate tally. No aggregation.')
n=load('paired-list-positional-expansion'); expand=n['expand']
rows=[{'id':'P','names':['same','same',None],'values':[0,None,8]},{'id':'E','names':[],'values':[]}]
children,empty=expand(rows); assert children==[('P',0,'same',0),('P',1,'same',None),('P',2,None,8)] and empty==['E']
assert [c[2] for c in children]==rows[0]['names'] and [c[3] for c in children]==rows[0]['values']
case('TBX002 ordinary','Pairing contract: Fictional Larch declares shared positions.\nChildren: '+repr(children)+'\nEmpty parents: E.\nRejected parents: None.\nReconciliation: Expected 3+0=3; actual 3; both lists reconstruct, duplicates and null retain position.\nLimits: No exported table; parent context remains separate.')
error=fails(lambda:expand([{'id':'S','names':[]}]),KeyError)
case('TBX002 missing input','Pairing contract: Fictional Larch, S missing values field.\nChildren: No accepted batch.\nEmpty parents: Not established for S.\nRejected parents: S missing '+error+'; request actual list and positional contract.\nReconciliation: Missing is not empty; no invented child or list.\nLimits: KeyError is caught at caller boundary; no source mutation.')
error=fails(lambda:expand([{'id':'E','names':[],'values':[]},{'id':'Q','names':['oak','elm','ash'],'values':[2,5]}]),ValueError)
fails(lambda:expand([{'id':'N','names':[],'values':None}]),ValueError)
fails(lambda:expand([rows[0],rows[0]]),ValueError)
case('TBX002 unequal and invalid batch','Pairing contract: Fictional Larch Q claims positional alignment.\nChildren: No complete accepted batch returned.\nEmpty parents: E observed in input; preserved separately.\nRejected parents: Q '+error+'; retain original three names and two values for correction.\nReconciliation: No truncation; explicit null list and duplicate identity also rejected in fresh checks.\nLimits: Fail-fast function is not a complete defect collector. No external writes.')
report.extend(['## Scope and claim review','TBX001 preserves cell-coordinate bijection and identity sidecars, distinct from TDQ008 join cardinality. TBX002 preserves paired nested positions, distinct from Cartesian joins and semantic matching. Arithmetic and concrete assertions executed above. Source snippets have explicit scalar/string-identity preconditions; no general serializer guarantee. Third skill requires separate review.'])
(root/'logs/b7-tbx-tests.md').write_text('\n\n'.join(report)+'\n',encoding='utf-8')
print('PASS six fresh TBX cases plus embedded assertions')
