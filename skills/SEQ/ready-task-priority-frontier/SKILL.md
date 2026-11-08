---
id: SEQ-002
name: ready-task-priority-frontier
domain: Dependency Schedule Computation
subdomain: Dispatch selection
version: 1.0
description: Compute a deterministic next-task shortlist from completion evidence and explicit priority when blocked or already-running work must not consume available dispatch slots.
triggers: ["choose ready tasks by priority", "build a deterministic dispatch shortlist", "exclude blocked tasks from selection", "separate running from ready work", "explain why a task was not selected"]
not_for: ["choosing personal priorities [GPR-004]", "checking pipeline artifact readiness [TDE-008]", "optimizing staff allocation", "proving a graph acyclic [SEQ-001]"]
requires: []
risk_level: medium
---

# Ready Task Priority Frontier

## Purpose
Produce a reproducible shortlist of work whose direct prerequisites are recorded complete, using a supplied priority order and dispatch capacity. Keep eligibility, ranking and actual starting separate so a high-priority blocked task cannot be mistaken for executable work.

## Inputs to collect
1. **Dependency snapshot** — obtain task identifiers and direct prerequisite sets. These establish eligibility. Default: none; unknown prerequisite identifiers must be resolved before selection.
2. **Execution states** — collect completed, running and explicitly held task sets with an observation reference. These prevent redispatch and unsupported readiness. Default: missing state evidence is unresolved, not inferred from a planned finish time.
3. **Priority rule** — obtain integer ranks, lower first in this reference, and a stable tie-break convention. This makes selection reproducible. Default: no invented business ranking; request the rule.
4. **Available slots** — obtain the nonnegative number of additional tasks that may be proposed now. This controls shortlist size. Default: no dispatch proposal until supplied; existing running tasks are already accounted for by the owner.
5. **Capacity equivalence** — confirm that every eligible task consumes one equivalent slot and has no additional resource constraint in the model. Default: if this is false, provide only the ready frontier and request a resource-aware scheduler.
6. **Decision boundary** — establish whether the user wants a proposal or authorized execution. Default: proposed shortlist only; no task starts or state changes.

If a required input has no safe default, ask in one message with at most three questions. Consolidate graph/state, ranking and capacity assumptions rather than asking about each task separately.

## Procedure
1. Freeze the graph and state snapshot used for this selection. A changed completion event can change eligibility even if priorities remain unchanged.
2. Validate task references, state-set disjointness and priority coverage. ⚠️ A task listed both running and complete is an evidence conflict, not an opportunity to choose whichever status improves throughput.
3. Remove completed, running and held tasks from the candidate set. Retain the reason each excluded task is outside dispatch consideration.
4. Compute each remaining task's unsatisfied direct prerequisites against the completed set. A running prerequisite is not complete; a newly selected prerequisite cannot release its dependent in the same snapshot.
5. Build the ready frontier from candidates with no unsatisfied prerequisite. Record blocked candidates and their actual missing dependencies separately from ranking.
6. Sort ready candidates by the supplied integer rank and then their stable identifier. Use the identifier tie-break only when that convention is accepted; do not portray it as a fairness guarantee.
7. Take the first supplied number of slots and retain the rest as ready but unselected. A zero-slot request can still produce an informative frontier without any proposed starts.
8. Compare the result with resource and hold assumptions before handoff. If a required machine, permission or specialist is not represented by equivalent slots, label the output conditional rather than claiming dispatch feasibility.
9. Recompute from a new snapshot after an actual state change. Do not mutate the completed set merely because an item was proposed or started.

The Python 3 fixture below uses string task identifiers, prerequisite sets and integer ranks. The caller provides a reconciled snapshot; the function does not verify that a reported completion actually happened or detect every cycle. Run the snippet in the available Python 3 environment and retain the observed version with its results.

```python
def select_ready(pred, complete, running, held, rank, slots):
    tasks = set(pred)
    if type(slots) is not int or slots < 0:
        raise ValueError("nonnegative integer slots required")
    if any(p not in tasks for ps in pred.values() for p in ps):
        raise ValueError("unknown prerequisite")
    if not (complete | running | held) <= tasks:
        raise ValueError("unknown state task")
    if complete & running or complete & held or running & held:
        raise ValueError("conflicting states")
    if set(rank) != tasks or any(type(v) is not int for v in rank.values()):
        raise ValueError("integer priority required for every task")
    candidates = tasks - complete - running - held
    blocked = {t: sorted(pred[t] - complete) for t in sorted(candidates)
               if pred[t] - complete}
    ready = sorted(candidates - set(blocked), key=lambda t: (rank[t], t))
    return {"selected": ready[:slots], "ready_waiting": ready[slots:],
            "blocked": blocked}

pred = {"A": set(), "B": {"A"}, "C": set(), "D": {"B"}}
ranks = {"A": 4, "B": 2, "C": 2, "D": 0}
result = select_ready(pred, {"A"}, set(), set(), ranks, 1)
assert result == {"selected": ["B"], "ready_waiting": ["C"],
                  "blocked": {"D": ["B"]}}
assert select_ready(pred, {"A"}, {"B"}, set(), ranks, 1)["selected"] == ["C"]
assert select_ready(pred, {"A"}, set(), {"C"}, ranks, 0)["ready_waiting"] == ["B"]
try:
    select_ready(pred, {"A"}, {"A"}, set(), ranks, 1)
except ValueError:
    pass
else:
    raise AssertionError("conflicting state accepted")
print("ready frontier checks passed")
```

## Decision rules
- IF a high-priority task has an incomplete prerequisite THEN retain it as blocked BECAUSE priority does not satisfy a dependency.
- IF a prerequisite is selected now THEN leave its dependents blocked in this snapshot BECAUSE a dispatch proposal is not completion evidence.
- IF ready tasks tie on priority THEN use the supplied stable tie-break BECAUSE iteration order is not an agreed selection policy.
- IF no slots are available THEN return the ready frontier without selected tasks BECAUSE readiness and immediate capacity are distinct states.
- IF capacity is not interchangeable THEN withhold an unconditional dispatch claim BECAUSE a scalar slot count does not encode resource compatibility.

## Output template
```text
Snapshot: <graph/state revision and observation basis; up to three lines>
Policy: <rank direction, tie-break, additional slots and resource assumption>
Selected: <ordered task identifiers, or None>
Ready waiting: <ordered identifiers with reason; first twelve then continuation>
Blocked: <task -> missing direct prerequisites; first twelve then continuation>
Excluded states: <completed, running and held lists; reference full ledger if large>
Handoff: <one sentence naming owner and proposal versus execution>
Limits: <up to three unverified state or resource assumptions>
```

## Quality checklist
- [ ] Every referenced prerequisite exists in the scoped graph.
- [ ] State sets are disjoint and contain only known tasks.
- [ ] Each task has a supplied priority rank.
- [ ] Selected tasks have all direct prerequisites in the completed set.
- [ ] Already-running and held tasks are not selected.
- [ ] Selection count does not exceed additional available slots.
- [ ] Ready but unselected work is distinguished from blocked work.
- [ ] Proposed selection is not described as task execution or completion.

## Anti-patterns
- **Priority overrides logic**: a blocked urgent task displaces ready work. Fix: filter eligibility before ranking.
- **Instant completion**: selecting B immediately unlocks its dependent D. Fix: recompute only after new completion evidence.
- **Arbitrary tie**: dictionary insertion order determines equal-ranked work. Fix: state and implement the accepted tie-break.
- **Double dispatch**: a running task is selected again. Fix: exclude reconciled running states before building the frontier.
- **Capacity laundering**: one slot count hides incompatible resource types. Fix: report the frontier and request the actual resource model.

## Worked example
**Input:**
> Fictional studio Ash uses the snippet's A/B/C/D graph and ranks. A is complete, nothing is running or held, and one additional interchangeable slot is available. Lower rank wins; identifier ascending breaks ties. Return a proposal, not execution.

**Output:**
```text
Snapshot: Ash supplied graph and current state; A completion accepted as supplied evidence.
Policy: Lower integer first, then identifier ascending; one additional equivalent slot.
Selected: B.
Ready waiting: C; same rank as B, later identifier, no remaining slot.
Blocked: D -> B; D's rank zero cannot replace completion evidence.
Excluded states: complete A; running None; held None.
Handoff: Dispatch owner reviews proposed B; no work started or completed by this selection.
Limits: Completion evidence and equivalent-slot capacity supplied, not independently observed; no resource-specific optimization performed.
```

**Bad output:** “Select D because it is most urgent, then count B complete to justify it.”
This fabricates prerequisite completion and reverses the eligibility-before-ranking procedure.

## Edge cases
- **All work blocked**: return the blockers and request completion or graph review; do not invent a root task.
- **Priority changes mid-selection**: recompute against a new labeled snapshot and preserve the earlier proposal for comparison.
- **Running task fails**: obtain its reconciled state and recovery policy before making it eligible again; failure is not automatic completion.
- **Resource-specific holds**: represent the confirmed hold explicitly or supply a richer resource model rather than hiding it in rank.

## Test case
**Input:**
> Fictional task Z has highest priority but needs running task Y. Task X has lower priority and no prerequisites. One additional equivalent slot is supplied; no completion event for Y exists.

**Assertions:**
1. Selects X and retains Z blocked on Y.
2. Does not redispatch Y.
3. Does not call Y complete because it is running.
4. Labels the result as a proposal based on the supplied snapshot.
