---
id: SEQ-003
name: dependency-critical-path-slack
domain: Dependency Schedule Computation
subdomain: Duration propagation
version: 1.0
description: Compute earliest and latest task times and total slack from supplied durations when a dependency-only completion baseline is needed.
triggers: ["calculate dependency critical paths", "compute task total slack", "show earliest and latest task times", "explain the longest prerequisite chain", "recompute finish after a duration change"]
not_for: ["choosing dispatch priority [SEQ-002]", "negotiating initiative dependencies [BPL-002]", "resource-constrained scheduling", "calendar date commitments"]
requires: []
risk_level: medium
---

# Dependency Critical Path Slack

## Purpose
Calculate a reproducible elapsed-time baseline for a directed acyclic task graph using forward and backward duration propagation. Identify tasks and connected edges that constrain the earliest project finish while keeping resource availability, calendar conversion and delivery promises outside the arithmetic claim.

## Inputs to collect
1. **Task graph** — obtain unique string identifiers and explicit prerequisite sets, including empty sets for roots. This establishes the completion-before-start relation. Default: none; an omitted prerequisite list is unresolved.
2. **Durations** — obtain a nonnegative duration for every task with its estimation basis. This supplies the weights used by the calculation. Default: none; missing duration is not zero.
3. **Time unit and resolution** — establish one elapsed-time unit and an exact integer representation for the reference implementation. Default: none; ask the owner to choose an appropriate unit rather than silently rounding fractional durations.
4. **Model assumptions** — confirm that tasks may start as soon as all prerequisites finish, independent tasks may overlap, and there are no lags, release dates or resource conflicts. Default: findings remain conditional until these assumptions are accepted.
5. **Completion boundary** — confirm that all scoped tasks must finish and all roots are eligible at time zero. Default: no excluded branch or implicit external prerequisite.
6. **Change request** — obtain any proposed duration or edge adjustment as a separate scenario. Default: calculate the supplied baseline only, preserving its revision.

If a required input is missing and has no safe default, ask in one message with at most three questions. Group graph scope, duration units and scheduling assumptions into those questions.

## Procedure
1. Freeze the graph, duration table and unit as a named scenario. Preserve the original if a later scenario changes an estimate.
2. Validate references and duration coverage before computing. ⚠️ Reject negative, unknown or silently rounded durations instead of producing a plausible finish from altered inputs.
3. Produce a prerequisite-first topological order. Reject a cyclic graph; use a cycle-witness procedure when the user needs the exact contradictory path.
4. Run the forward pass: each earliest start is the largest earliest finish among its prerequisites, or zero for a root; earliest finish is earliest start plus duration.
5. Set project finish to the largest earliest finish across all tasks. This includes disconnected components because the declared boundary requires every task to finish.
6. Run the backward pass in reverse order: each latest finish is the smallest latest start among its successors, or project finish for a terminal task; latest start is latest finish minus duration.
7. Calculate total slack as latest start minus earliest start. ⚠️ Distinguish this allowance relative to project finish from permission to delay successors; total slack is not necessarily free slack.
8. Identify zero-slack tasks and tight edges between them, where the predecessor earliest finish equals the successor earliest start. Retain all such branches rather than selecting one convenient longest chain.
9. Verify every precedence inequality and duration subtraction before reporting. Re-run both passes after an accepted change because another branch can become controlling.

The following Python 3 reference accepts dictionaries with string task identifiers, prerequisite sets and integer elapsed-time durations. It uses exact integer arithmetic, not calendar dates. Run the complete snippet and record the actual interpreter version; do not label a proposed execution as a passed test.

```python
def critical_times(pred, duration):
    tasks = set(pred)
    if set(duration) != tasks:
        raise ValueError("duration coverage mismatch")
    if any(type(d) is not int or d < 0 for d in duration.values()):
        raise ValueError("nonnegative integer durations required")
    if any(p not in tasks for ps in pred.values() for p in ps):
        raise ValueError("unknown prerequisite")
    succ = {t: set() for t in tasks}
    for t, ps in pred.items():
        for p in ps:
            succ[p].add(t)
    remaining, order = set(tasks), []
    while remaining:
        ready = sorted(t for t in remaining if not (pred[t] & remaining))
        if not ready:
            raise ValueError("cyclic graph")
        order.extend(ready)
        remaining.difference_update(ready)
    es, ef, ls, lf = {}, {}, {}, {}
    for t in order:
        es[t] = max((ef[p] for p in pred[t]), default=0)
        ef[t] = es[t] + duration[t]
    finish = max(ef.values(), default=0)
    for t in reversed(order):
        lf[t] = min((ls[s] for s in succ[t]), default=finish)
        ls[t] = lf[t] - duration[t]
    table = {t: (es[t], ef[t], ls[t], lf[t], ls[t]-es[t])
             for t in sorted(tasks)}
    critical = [t for t in sorted(tasks) if ls[t] == es[t]]
    edges = [(p, t) for t in critical for p in sorted(pred[t])
             if p in critical and ef[p] == es[t]]
    assert all(ef[p] <= es[t] and lf[p] <= ls[t]
               for t in tasks for p in pred[t])
    assert all(ls[t] >= es[t] and ef[t]-es[t] == lf[t]-ls[t] == duration[t]
               for t in tasks)
    return {"finish": finish, "table": table,
            "critical_tasks": critical, "critical_edges": edges}

g = {"A": set(), "B": {"A"}, "C": {"A"}, "D": {"B", "C"}}
d = {"A": 2, "B": 5, "C": 3, "D": 1}
r = critical_times(g, d)
assert r["finish"] == 8
assert r["table"]["C"] == (2, 5, 4, 7, 2)
assert r["critical_edges"] == [("A", "B"), ("B", "D")]
assert critical_times(g, dict(d, C=5))["critical_tasks"] == ["A", "B", "C", "D"]
assert critical_times({}, {})["finish"] == 0
print("critical time checks passed")
```

## Decision rules
- IF a duration or prerequisite is missing THEN withhold the computed baseline BECAUSE inserting a zero changes the model.
- IF two branches tie for longest duration THEN retain both critical branches BECAUSE either can affect the earliest finish.
- IF a task has positive total slack THEN describe it relative to the project finish BECAUSE using it can still delay an immediate successor.
- IF a deadline, calendar or shared resource matters THEN request the additional model BECAUSE these passes do not encode those constraints.
- IF durations change THEN recompute the entire scenario BECAUSE the previous critical branch may no longer control completion.

## Output template
```text
Scenario: <revision, unit and completion boundary; up to three lines>
Assumptions: <up to four dependency-model conditions>
Input exceptions: <up to five unresolved items, or None>
Earliest project finish: <elapsed units from zero, or unresolved>
Task times: <task | ES | EF | LS | LF | total slack; twelve rows then attached continuation>
Critical structure: <zero-slack tasks and tight directed edges; continuation if needed>
Interpretation: <up to three sentences explaining controlling branches and slack>
Verification: <actual checks and remaining limits; up to three sentences>
```

## Quality checklist
- [ ] Every task has a supplied duration in the declared unit.
- [ ] Every prerequisite exists in the task universe.
- [ ] A topological order covers the entire graph.
- [ ] Every earliest start respects all prerequisite finishes.
- [ ] Every latest finish respects all successor latest starts.
- [ ] Slack equals latest start minus earliest start for every row.
- [ ] Tied critical branches are retained with connected edges.
- [ ] Resource or calendar feasibility is not implied by arithmetic success.

## Anti-patterns
- **Average predecessor time**: a merge starts before its slowest prerequisite finishes. Fix: take the maximum prerequisite finish.
- **Local terminal deadline**: each terminal receives its own earliest finish in the backward pass. Fix: use the shared project finish to measure total slack.
- **Slack as permission**: a task is delayed without checking successor effects. Fix: distinguish total slack from successor-specific scheduling decisions.
- **Single-path bias**: one tied branch is omitted. Fix: report all zero-slack tasks and their tight connecting edges.

## Worked example
**Input:**
> Fictional studio Birch supplies graph g and durations d from the snippet in elapsed hours. All tasks must finish; roots start at zero, dependencies are finish-to-start, and resources impose no restrictions. Compute the baseline using the reference.

**Output:**
```text
Scenario: Birch baseline; elapsed hours; all A/B/C/D tasks must finish.
Assumptions: Roots eligible at zero; finish-to-start links; no lags or release dates; independent work can overlap without resource limits.
Input exceptions: None.
Earliest project finish: 8 hours from zero.
Task times: A | 0 | 2 | 0 | 2 | 0
B | 2 | 7 | 2 | 7 | 0
C | 2 | 5 | 4 | 7 | 2
D | 7 | 8 | 7 | 8 | 0
Critical structure: Tasks A, B, D; tight edges A -> B and B -> D.
Interpretation: A/B/D controls the baseline. C has two hours of total slack relative to the common finish. Estimates and assumptions remain supplied inputs.
Verification: Reference assertions check durations and precedence inequalities. This is an elapsed-time calculation, not a calendar commitment or resource-feasibility test.
```

**Bad output:** “D starts after the average of B and C finishes, so finish is seven hours.”
This violates the B-to-D prerequisite: B finishes at seven, so the one-hour D cannot finish before eight.

## Edge cases
- **Zero-duration milestone**: retain its edges and calculate normally; a zero-duration cycle is still rejected as a graph contradiction.
- **Disconnected tasks**: include each component and use their shared maximum finish for the backward pass.
- **Empty scope**: return an empty table and zero elapsed finish, explicitly identifying that no tasks were supplied.
- **Fractional estimates**: obtain an exact common integer unit or adapt and test an exact rational implementation; never round silently.
- **Actual progress already underway**: obtain a newly scoped remaining-work model instead of mixing original durations with completed work.

## Test case
**Input:**
> Fictional graph has root A duration two, parallel successors B and C duration four each, and terminal D duration one needing both. Use elapsed ticks, all roots eligible at zero and no resource restrictions.

**Assertions:**
1. Reports earliest project finish seven ticks.
2. Reports zero total slack for all four tasks.
3. Includes A-to-B-to-D and A-to-C-to-D in the critical structure.
4. Does not turn the elapsed-time baseline into a delivery promise.
