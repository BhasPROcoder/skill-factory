"""Independent forward checks by finish_tables; reads actual SEQ skill snippets."""
from pathlib import Path
import contextlib
import hashlib
import io
import platform
import re

ROOT = Path(__file__).resolve().parents[1]
report = ["# Independent SEQ forward review", "", "Reviewer: finish_tables; author: finish_schedule / earlier schedule agent.",
          f"Python: {platform.python_version()}. All fixtures below are fictional.",
          "These checks verify bounded reference behavior and task outputs, not actual task completion or resource feasibility."]

def load(name):
    path = ROOT / 'skills' / 'SEQ' / name / 'SKILL.md'
    text = path.read_text(encoding='utf-8')
    namespace = {}
    with contextlib.redirect_stdout(io.StringIO()) as captured:
        for block in re.findall(r'```python\n(.*?)```', text, re.S):
            exec(compile(block, str(path), 'exec'), namespace)
    report.extend(['', f"## {name}", f"Source SHA256: {hashlib.sha256(path.read_bytes()).hexdigest()}",
                   f"Embedded checks: {captured.getvalue().strip()}"])
    return namespace

def case(title, raw, output):
    report.extend(['', f'### PASS {title}', f'Input: {raw}', '```text', output, '```'])

def raises(fn, message):
    try:
        fn()
    except ValueError as exc:
        assert str(exc) == message, str(exc)
        return str(exc)
    raise AssertionError('invalid fixture accepted')

diagnose = load('prerequisite-cycle-witness')['diagnose']
graph = {'pack': {'inspect'}, 'ship': {'inspect'}, 'inspect': {'build'}, 'build': set()}
result = diagnose(graph)
assert result == {'cycle': None, 'order': ['build', 'inspect', 'pack', 'ship']}
case('SEQ001 normal shared ancestor', repr(graph),
     'Graph scope: Fictional Birch G; each task lists required completion predecessors.\n'
     'Input exceptions: None.\nResult: acyclic.\n'
     f"Witness or order: {result['order']}.\n"
     'Edge evidence: build precedes inspect, and inspect precedes pack and ship. All four identities appear once.\n'
     'Repair handoff: None required for this graph; no edge changed.\n'
     'Verification limit: Reference order and every edge checked. Durations, capacity and actual completions untested.')
error = raises(lambda: diagnose({'pack': {'inspect'}}), 'unknown prerequisite')
case('SEQ001 missing node', "pack needs undeclared inspect",
     'Graph scope: Fictional Birch missing-node snapshot.\n'
     f'Input exceptions: {error}: inspect has no declared node.\nResult: unresolved input.\n'
     'Witness or order: Withheld.\nEdge evidence: pack references inspect, but its scope and prerequisites are absent.\n'
     'Repair handoff: Owner must provide inspect or correct the reference; no automatic insertion.\n'
     'Verification limit: Missing reference rejected. No whole-graph orderability or capacity claim.')
graph = {'a': {'b'}, 'b': {'a'}, 'x': {'y'}, 'y': {'x'}, 'z': set()}
first = diagnose(graph)
assert first['cycle'] == ['a', 'b', 'a']
repaired = {key: set(value) for key, value in graph.items()}
repaired['b'] = set()
second = diagnose(repaired)
assert second['cycle'] == ['x', 'y', 'x'] and second['order'] is None
case('SEQ001 disconnected cycle after supplied repair',
     repr(graph) + '; separate caller-authorized scenario removes b needs a',
     'Graph scope: Fictional Birch two-cycle snapshot and explicitly supplied repaired scenario.\n'
     'Input exceptions: None.\nResult: cycle found in both scenarios.\n'
     f"Witness or order: Original {first['cycle']}; supplied repair {second['cycle']}.\n"
     'Edge evidence: Original a needs b and b needs a; repair retains x needs y and y needs x.\n'
     'Repair handoff: Owner must still resolve the x/y relationship; no further edge removed.\n'
     'Verification limit: Both full snapshots executed. Removing one witness did not establish acyclicity.')

select = load('ready-task-priority-frontier')['select_ready']
pred = {'done': set(), 'alpha': {'done'}, 'beta': {'done'}, 'urgent': {'alpha'},
        'busy': set(), 'held': set()}
rank = {'done': 8, 'alpha': 2, 'beta': 2, 'urgent': 0, 'busy': 1, 'held': 1}
result = select(pred, {'done'}, {'busy'}, {'held'}, rank, 1)
assert result == {'selected': ['alpha'], 'ready_waiting': ['beta'], 'blocked': {'urgent': ['alpha']}}
case('SEQ002 normal eligible tie', repr((pred, rank)) + '; done complete, busy running, held held, one slot',
     'Snapshot: Fictional Willow graph and owner-supplied state observation W.\n'
     'Policy: Lower integer rank, then ascending identifier; one additional interchangeable slot.\n'
     'Selected: alpha.\nReady waiting: beta; tied rank with alpha, later identifier.\n'
     'Blocked: urgent -> alpha.\nExcluded states: completed done; running busy; held held.\n'
     'Handoff: Dispatch owner receives proposal only; no task started.\n'
     'Limits: State truth and interchangeable resources supplied, not externally verified.')
missing = dict(rank)
del missing['beta']
error = raises(lambda: select(pred, {'done'}, {'busy'}, {'held'}, missing, 1),
               'integer priority required for every task')
case('SEQ002 missing rank', 'Same Willow snapshot, with beta rank omitted',
     'Snapshot: Fictional Willow incomplete priority snapshot.\n'
     'Policy: Lower rank and identifier tie-break supplied; beta rank missing; one equivalent slot.\n'
     'Selected: None; proposal withheld pending required rank.\nReady waiting: Not ranked.\n'
     'Blocked: urgent requires alpha; full dispatch result withheld.\n'
     'Excluded states: completed done; running busy; held held.\n'
     f'Handoff: Owner must provide beta rank; reference rejected input: {error}.\n'
     'Limits: No default rank invented and no execution performed.')
zero = select(pred, {'done'}, {'busy'}, {'held'}, rank, 0)
assert zero == {'selected': [], 'ready_waiting': ['alpha', 'beta'], 'blocked': {'urgent': ['alpha']}}
raises(lambda: select(pred, {'done'}, {'done'}, set(), rank, 1), 'conflicting states')
case('SEQ002 zero slots and state conflict', 'Willow with zero slots; separately done marked both running and complete',
     'Snapshot: Fictional Willow zero-slot snapshot; separate conflicting-state probe.\n'
     'Policy: Lower rank then identifier; zero additional equivalent slots.\nSelected: None.\n'
     'Ready waiting: alpha, beta; capacity unavailable.\nBlocked: urgent -> alpha.\n'
     'Excluded states: completed done; running busy; held held in valid zero-slot snapshot.\n'
     'Handoff: Owner receives frontier without starts; separate conflicting-state snapshot rejected.\n'
     'Limits: Running/complete conflict requires reconciliation. Selection never changes completion evidence.')

critical = load('dependency-critical-path-slack')['critical_times']
graph = {'a': set(), 'b': {'a'}, 'c': {'a'}, 'd': {'b', 'c'}, 'e': set()}
durations = {'a': 3, 'b': 4, 'c': 1, 'd': 2, 'e': 2}
result = critical(graph, durations)
expected = {'a': (0, 3, 0, 3, 0), 'b': (3, 7, 3, 7, 0),
            'c': (3, 4, 6, 7, 3), 'd': (7, 9, 7, 9, 0), 'e': (0, 2, 7, 9, 7)}
assert result['table'] == expected and result['finish'] == 9
assert result['critical_tasks'] == ['a', 'b', 'd']
assert result['critical_edges'] == [('a', 'b'), ('b', 'd')]
case('SEQ003 normal disconnected terminal and merge', repr((graph, durations)),
     'Scenario: Fictional Alder V; elapsed ticks; all five tasks required.\n'
     'Assumptions: Roots eligible at zero; finish-to-start edges; no lags/releases; unlimited compatible resources.\n'
     'Input exceptions: None.\nEarliest project finish: 9 ticks from zero.\n'
     'Task times: a | 0 | 3 | 0 | 3 | 0\nb | 3 | 7 | 3 | 7 | 0\n'
     'c | 3 | 4 | 6 | 7 | 3\nd | 7 | 9 | 7 | 9 | 0\ne | 0 | 2 | 7 | 9 | 7\n'
     'Critical structure: a,b,d; tight edges a->b and b->d.\n'
     'Interpretation: a/b/d controls the finish. The disconnected e shares the project boundary and has 7 ticks total slack.\n'
     'Verification: Independently expected all five time tuples and checked actual results. No calendar or resource feasibility claim.')
missing = dict(durations)
del missing['c']
error = raises(lambda: critical(graph, missing), 'duration coverage mismatch')
case('SEQ003 missing duration', 'Alder graph with no duration supplied for c',
     'Scenario: Fictional Alder incomplete-duration snapshot; elapsed ticks; all tasks required.\n'
     'Assumptions: Same dependency-only conditions, pending duration completion.\n'
     'Input exceptions: Duration for c missing.\nEarliest project finish: unresolved.\n'
     'Task times: Withheld.\nCritical structure: Withheld.\n'
     'Interpretation: Request c duration; no zero substituted.\n'
     f'Verification: Reference rejected input with {error}. No baseline computed.')
tie_graph = {'start': set(), 'left': {'start'}, 'right': {'start'}, 'end': {'left', 'right'}}
tie_durations = {'start': 0, 'left': 5, 'right': 5, 'end': 0}
tied = critical(tie_graph, tie_durations)
assert tied['finish'] == 5
assert all(values[4] == 0 for values in tied['table'].values())
assert set(tied['critical_edges']) == {('start', 'left'), ('start', 'right'), ('left', 'end'), ('right', 'end')}
raises(lambda: critical({'x': {'y'}, 'y': {'x'}}, {'x': 0, 'y': 0}), 'cyclic graph')
for bad in (-1, True, 1.5):
    raises(lambda: critical({'x': set()}, {'x': bad}), 'nonnegative integer durations required')
assert critical({}, {}) == {'finish': 0, 'table': {}, 'critical_tasks': [], 'critical_edges': []}
case('SEQ003 tied branches and zero milestones', repr((tie_graph, tie_durations)) + '; separate zero-duration cycle and invalid-duration probes',
     'Scenario: Fictional Alder tied scenario; elapsed ticks; all four tasks required.\n'
     'Assumptions: Roots eligible at zero; finish-to-start edges; no lags/releases; unlimited compatible resources.\n'
     'Input exceptions: None in tied scenario; separate zero-duration cycle rejected.\n'
     'Earliest project finish: 5 ticks from zero.\n'
     'Task times: start | 0 | 0 | 0 | 0 | 0\nleft | 0 | 5 | 0 | 5 | 0\n'
     'right | 0 | 5 | 0 | 5 | 0\nend | 5 | 5 | 5 | 5 | 0\n'
     'Critical structure: start,left,right,end; start->left->end and start->right->end.\n'
     'Interpretation: Both branches constrain earliest finish; zero-duration milestones retain their dependencies.\n'
     'Verification: Both tied branches retained; negative, boolean and fractional durations rejected; empty scope returns zero with empty tables. No delivery assurance.')

(ROOT / 'logs/b7-seq-tests.md').write_text('\n'.join(report) + '\n', encoding='utf-8')
print('PASS: SEQ001/002/003 nine independent cases plus embedded assertions; report saved')
