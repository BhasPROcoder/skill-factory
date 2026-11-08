# Independent SEQ forward review

Reviewer: finish_tables; author: finish_schedule / earlier schedule agent.
Python: 3.14.6. All fixtures below are fictional.
These checks verify bounded reference behavior and task outputs, not actual task completion or resource feasibility.

## prerequisite-cycle-witness
Source SHA256: 7036a85bed49c838ea1b2fb11dab3a1d1af51bf8e0f1502b3eb1f69b8f71b4ce
Embedded checks: cycle witness checks passed

### PASS SEQ001 normal shared ancestor
Input: {'pack': {'inspect'}, 'ship': {'inspect'}, 'inspect': {'build'}, 'build': set()}
```text
Graph scope: Fictional Birch G; each task lists required completion predecessors.
Input exceptions: None.
Result: acyclic.
Witness or order: ['build', 'inspect', 'pack', 'ship'].
Edge evidence: build precedes inspect, and inspect precedes pack and ship. All four identities appear once.
Repair handoff: None required for this graph; no edge changed.
Verification limit: Reference order and every edge checked. Durations, capacity and actual completions untested.
```

### PASS SEQ001 missing node
Input: pack needs undeclared inspect
```text
Graph scope: Fictional Birch missing-node snapshot.
Input exceptions: unknown prerequisite: inspect has no declared node.
Result: unresolved input.
Witness or order: Withheld.
Edge evidence: pack references inspect, but its scope and prerequisites are absent.
Repair handoff: Owner must provide inspect or correct the reference; no automatic insertion.
Verification limit: Missing reference rejected. No whole-graph orderability or capacity claim.
```

### PASS SEQ001 disconnected cycle after supplied repair
Input: {'a': {'b'}, 'b': {'a'}, 'x': {'y'}, 'y': {'x'}, 'z': set()}; separate caller-authorized scenario removes b needs a
```text
Graph scope: Fictional Birch two-cycle snapshot and explicitly supplied repaired scenario.
Input exceptions: None.
Result: cycle found in both scenarios.
Witness or order: Original ['a', 'b', 'a']; supplied repair ['x', 'y', 'x'].
Edge evidence: Original a needs b and b needs a; repair retains x needs y and y needs x.
Repair handoff: Owner must still resolve the x/y relationship; no further edge removed.
Verification limit: Both full snapshots executed. Removing one witness did not establish acyclicity.
```

## ready-task-priority-frontier
Source SHA256: f8461a95d4e51c7891cb5ea5f9408667d124d78df8ba1193066d2e2f2489bf29
Embedded checks: ready frontier checks passed

### PASS SEQ002 normal eligible tie
Input: ({'done': set(), 'alpha': {'done'}, 'beta': {'done'}, 'urgent': {'alpha'}, 'busy': set(), 'held': set()}, {'done': 8, 'alpha': 2, 'beta': 2, 'urgent': 0, 'busy': 1, 'held': 1}); done complete, busy running, held held, one slot
```text
Snapshot: Fictional Willow graph and owner-supplied state observation W.
Policy: Lower integer rank, then ascending identifier; one additional interchangeable slot.
Selected: alpha.
Ready waiting: beta; tied rank with alpha, later identifier.
Blocked: urgent -> alpha.
Excluded states: completed done; running busy; held held.
Handoff: Dispatch owner receives proposal only; no task started.
Limits: State truth and interchangeable resources supplied, not externally verified.
```

### PASS SEQ002 missing rank
Input: Same Willow snapshot, with beta rank omitted
```text
Snapshot: Fictional Willow incomplete priority snapshot.
Policy: Lower rank and identifier tie-break supplied; beta rank missing; one equivalent slot.
Selected: None; proposal withheld pending required rank.
Ready waiting: Not ranked.
Blocked: urgent requires alpha; full dispatch result withheld.
Excluded states: completed done; running busy; held held.
Handoff: Owner must provide beta rank; reference rejected input: integer priority required for every task.
Limits: No default rank invented and no execution performed.
```

### PASS SEQ002 zero slots and state conflict
Input: Willow with zero slots; separately done marked both running and complete
```text
Snapshot: Fictional Willow zero-slot snapshot; separate conflicting-state probe.
Policy: Lower rank then identifier; zero additional equivalent slots.
Selected: None.
Ready waiting: alpha, beta; capacity unavailable.
Blocked: urgent -> alpha.
Excluded states: completed done; running busy; held held in valid zero-slot snapshot.
Handoff: Owner receives frontier without starts; separate conflicting-state snapshot rejected.
Limits: Running/complete conflict requires reconciliation. Selection never changes completion evidence.
```

## dependency-critical-path-slack
Source SHA256: b34248755df95a4db27ae203211665f740a867d0af883c01e2c3d062503ae5fd
Embedded checks: critical time checks passed

### PASS SEQ003 normal disconnected terminal and merge
Input: ({'a': set(), 'b': {'a'}, 'c': {'a'}, 'd': {'c', 'b'}, 'e': set()}, {'a': 3, 'b': 4, 'c': 1, 'd': 2, 'e': 2})
```text
Scenario: Fictional Alder V; elapsed ticks; all five tasks required.
Assumptions: Roots eligible at zero; finish-to-start edges; no lags/releases; unlimited compatible resources.
Input exceptions: None.
Earliest project finish: 9 ticks from zero.
Task times: a | 0 | 3 | 0 | 3 | 0
b | 3 | 7 | 3 | 7 | 0
c | 3 | 4 | 6 | 7 | 3
d | 7 | 9 | 7 | 9 | 0
e | 0 | 2 | 7 | 9 | 7
Critical structure: a,b,d; tight edges a->b and b->d.
Interpretation: a/b/d controls the finish. The disconnected e shares the project boundary and has 7 ticks total slack.
Verification: Independently expected all five time tuples and checked actual results. No calendar or resource feasibility claim.
```

### PASS SEQ003 missing duration
Input: Alder graph with no duration supplied for c
```text
Scenario: Fictional Alder incomplete-duration snapshot; elapsed ticks; all tasks required.
Assumptions: Same dependency-only conditions, pending duration completion.
Input exceptions: Duration for c missing.
Earliest project finish: unresolved.
Task times: Withheld.
Critical structure: Withheld.
Interpretation: Request c duration; no zero substituted.
Verification: Reference rejected input with duration coverage mismatch. No baseline computed.
```

### PASS SEQ003 tied branches and zero milestones
Input: ({'start': set(), 'left': {'start'}, 'right': {'start'}, 'end': {'right', 'left'}}, {'start': 0, 'left': 5, 'right': 5, 'end': 0}); separate zero-duration cycle and invalid-duration probes
```text
Scenario: Fictional Alder tied scenario; elapsed ticks; all four tasks required.
Assumptions: Roots eligible at zero; finish-to-start edges; no lags/releases; unlimited compatible resources.
Input exceptions: None in tied scenario; separate zero-duration cycle rejected.
Earliest project finish: 5 ticks from zero.
Task times: start | 0 | 0 | 0 | 0 | 0
left | 0 | 5 | 0 | 5 | 0
right | 0 | 5 | 0 | 5 | 0
end | 5 | 5 | 5 | 5 | 0
Critical structure: start,left,right,end; start->left->end and start->right->end.
Interpretation: Both branches constrain earliest finish; zero-duration milestones retain their dependencies.
Verification: Both tied branches retained; negative, boolean and fractional durations rejected; empty scope returns zero with empty tables. No delivery assurance.
```
