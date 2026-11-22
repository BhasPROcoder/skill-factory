Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-055
name: temporal-functional-edge-conflict-windows
domain: Graph Engineering Foundations
subdomain: Temporal relationship constraints
version: 1.0
description: Find effective-time windows where one subject has multiple distinct objects for an owner-declared functional graph relationship, preserving edge-ID evidence.
triggers: ["find overlapping graph relationship values", "check one manager at a time in graph records", "audit time-window edge conflicts", "show which edge IDs cause a temporal cardinality violation", "distinguish parallel evidence from conflicting objects"]
not_for: ["reconstructing two-clock edge revisions [GRF-005]", "checking point-in-time value counts [GRF-020]", "reconciling appointment resources [SVC-001]", "choosing a winning relationship or editing records"]
requires: []
risk_level: medium
---

# Temporal Functional Edge Conflict Windows

## Purpose
Find intervals where one subject has multiple distinct objects under an approved at-most-one rule. Report maximal conflict windows and changing edge-ID evidence. This frozen-view check does not correct sources or assert universal rules.

## Inputs to collect
1. **Selected view** — obtain revision and reconciled active edges. Why: competing edge versions need upstream resolution. Default: no live-data claim.
2. **Predicate rule** — obtain one directed predicate and owner approval for at most one distinct object per subject. Why: counting duplicate records differs from counting values. Default: no assumed functional rule.
3. **Window and interval convention** — obtain comparison unit and `[start,end)` bounds. Why: touching endpoints differ under other conventions. Default: integer ticks in the reference; no silent date conversion.
4. **Inventories** — obtain known nodes, target subjects and uniquely identified `(edge_ID, subject, predicate, object, start, end)` records. Why: each conflict needs source witnesses. Default: hold malformed or unknown records.
5. **Coverage** — obtain completeness for targets and window. Why: conflict-free certification needs complete evidence. Default: incomplete.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the selected view, target subjects, predicate, rule, window, comparison unit and coverage statement.
2. Validate IDs, endpoints and integer half-open intervals; reject duplicate edge IDs and empty or reversed intervals.
3. Keep different subjects separate. Retain parallel edge IDs for an equal object, but count that object once.
4. Collect the window boundaries and every clipped interval start/end for each target subject.
5. On every consecutive elementary segment, list active objects and all active edge IDs supporting each object.
6. Mark a segment conflicting when more than one distinct object is active. ⚠️ Do not mark parallel same-object records as a conflict.
7. Join adjacent conflicting segments into maximal conflict windows while retaining each original evidence subsegment.
8. Independently probe one interior point of every segment against original records and compare exact object/ID sets.
9. Treat nonconflicting segments as certified only with complete coverage; otherwise label one observed value or unresolved absence.
10. Deliver per-subject conflict windows, evidence segments, coverage limits and owner review action. Do not select an object or delete records.

This Python 3 reference uses finite integer ticks and half-open intervals. It scans a frozen in-memory edge view and verifies segments with exact rational interior probes against original records. Run the snippet and record the installed interpreter version. Timestamp parsing, source revision selection, live writes and performance claims are outside it.

```python
from fractions import Fraction

def validate(nodes, subjects, records, predicate, window, complete, approved):
    if approved is not True or type(complete) is not bool:
        raise ValueError("rule approval or coverage flag required")
    if any(type(x) not in (list, tuple) for x in (nodes, subjects, records)):
        raise ValueError("invalid inventory shape")
    if type(predicate) is not str or not predicate:
        raise ValueError("invalid predicate")
    if type(window) not in (list, tuple) or len(window) != 2:
        raise ValueError("invalid window")
    lo, hi = window
    if type(lo) is not int or type(hi) is not int or lo >= hi:
        raise ValueError("invalid window bounds")
    if any(type(n) is not str or not n for n in nodes) or len(set(nodes)) != len(nodes):
        raise ValueError("invalid nodes")
    known = set(nodes)
    if any(type(s) is not str or s not in known for s in subjects) or len(set(subjects)) != len(subjects):
        raise ValueError("invalid targets")
    ids = set()
    for row in records:
        if type(row) not in (list, tuple) or len(row) != 6:
            raise ValueError("invalid edge record")
        rid, s, p, o, a, b = row
        if any(type(x) is not str or not x for x in (rid, s, p, o)):
            raise ValueError("invalid edge field")
        if rid in ids or s not in known or o not in known or p != predicate:
            raise ValueError("duplicate ID, endpoint or predicate mismatch")
        if type(a) is not int or type(b) is not int or a >= b:
            raise ValueError("invalid interval")
        ids.add(rid)

def active(records, subject, point):
    buckets = {}
    for rid, s, p, o, a, b in records:
        if s == subject and a <= point < b:
            buckets.setdefault(o, []).append(rid)
    return tuple((o, tuple(sorted(ids))) for o, ids in sorted(buckets.items()))

def analyze(nodes, subjects, records, predicate, window, complete, approved):
    validate(nodes, subjects, records, predicate, window, complete, approved)
    lo, hi = window
    output = {}
    for subject in subjects:
        relevant = [r for r in records if r[1] == subject and r[4] < hi and r[5] > lo]
        bounds = {lo, hi}
        for rid, s, p, o, a, b in relevant:
            bounds.add(max(lo, a)); bounds.add(min(hi, b))
        ordered = sorted(bounds)
        segments = []
        for a, b in zip(ordered, ordered[1:]):
            evidence = active(relevant, subject, a)
            status = ("conflict" if len(evidence) > 1 else
                      "one" if evidence and complete else
                      "observed-one" if evidence else
                      "none" if complete else "unresolved")
            segments.append((a, b, status, evidence))
        windows = []
        for a, b, status, evidence in segments:
            if status == "conflict":
                if windows and windows[-1][1] == a:
                    windows[-1] = (windows[-1][0], b)
                else:
                    windows.append((a, b))
        output[subject] = (segments, windows)
    verify(subjects, records, window, complete, output)
    return output

def verify(subjects, records, window, complete, output):
    lo, hi = window
    if set(output) != set(subjects):
        raise ValueError("target coverage mismatch")
    for subject in subjects:
        segments, windows = output[subject]
        if not segments or segments[0][0] != lo or segments[-1][1] != hi:
            raise ValueError("window coverage mismatch")
        bounds = {lo, hi}
        for rid, s, p, o, a, b in records:
            if s == subject and a < hi and b > lo:
                bounds.update((max(lo, a), min(hi, b)))
        ordered = sorted(bounds)
        if [(a, b) for a, b, _, _ in segments] != list(zip(ordered, ordered[1:])):
            raise ValueError("evidence boundary mismatch")
        expected_windows = []
        previous = lo
        for a, b, status, evidence in segments:
            if a != previous or a >= b:
                raise ValueError("segment gap or reversal")
            previous = b
            probe = Fraction(a + b, 2)
            expected = active(records, subject, probe)
            expected_status = ("conflict" if len(expected) > 1 else
                               "one" if expected and complete else
                               "observed-one" if expected else
                               "none" if complete else "unresolved")
            if evidence != expected or status != expected_status:
                raise ValueError("source replay mismatch")
            if status == "conflict":
                if expected_windows and expected_windows[-1][1] == a:
                    expected_windows[-1] = (expected_windows[-1][0], b)
                else:
                    expected_windows.append((a, b))
        if windows != expected_windows:
            raise ValueError("nonmaximal conflict windows")
    return True

nodes = ["A", "B", "M1", "M2", "M3"]
rows = [("e1", "A", "managedBy", "M1", 1, 8),
        ("e1b", "A", "managedBy", "M1", 3, 6),
        ("e2", "A", "managedBy", "M2", 5, 10),
        ("e3", "A", "managedBy", "M1", 10, 12),
        ("e4", "B", "managedBy", "M2", 6, 9)]
result = analyze(nodes, ["A", "B"], rows, "managedBy", (1, 12), True, True)
assert result["A"][1] == [(5, 8)] and result["B"][1] == []
assert result["A"][0][2][3] == (("M1", ("e1", "e1b")), ("M2", ("e2",)))
assert analyze(nodes, ["A"], rows + [("e5", "A", "managedBy", "M3", 7, 9)],
               "managedBy", (1, 12), True, True)["A"][1] == [(5, 9)]
print("distinct objects, changing witnesses and maximal windows checked")
```

## Decision rules
- IF two distinct objects overlap for one subject/predicate THEN report their maximal conflict window BECAUSE the approved rule permits at most one value.
- IF parallel records support the same object THEN retain all IDs but count one object BECAUSE source multiplicity differs from value multiplicity.
- IF intervals only touch at an end-exclusive boundary THEN report no overlap at that instant BECAUSE the ending record is inactive.
- IF coverage is incomplete THEN preserve observed conflicts but withhold conflict-free certification BECAUSE omitted edges may add values.
- IF the rule or interval convention is undeclared THEN stop at unresolved BECAUSE neither may be silently assumed.

## Output template
```text
Scope: <snapshot, predicate, subjects, window and half-open convention>
Rule: <owner-approved at-most-one-distinct-object contract>
Coverage: <complete/incomplete for subjects and window>
Conflict windows: <subject | maximal [start,end) | active object IDs>
Evidence segments: <subject | [start,end) | status | object:edge IDs>
Independent check: <rational-point source replay and window parity>
Limits: <time-unit, source and execution limits; max 60 words>
Next action: <owner review or missing-input request>
```

## Quality checklist
- [ ] Snapshot and rule approval are named.
- [ ] Time unit and half-open boundaries are explicit.
- [ ] Edge IDs are unique and endpoints known.
- [ ] Parallel same-object records count once but remain visible.
- [ ] Conflict windows are maximal and evidence changes remain segmented.
- [ ] Cross-subject records do not create false conflicts.
- [ ] Independent point probes match every evidence segment.
- [ ] Incomplete coverage never certifies conflict-free intervals.

## Anti-patterns
- **Record count**: two IDs for M1 called a conflict. Fix: count distinct objects.
- **Touching overlap**: treating `[5,10)` and `[10,12)` as simultaneous. Fix: apply end-exclusive boundaries.
- **Merged subjects**: combining A and B edges. Fix: partition by subject and predicate.
- **Lost evidence**: returning `[5,8)` without subsegments. Fix: retain changing edge-ID witnesses.
- **Silent repair**: choosing a winner or deleting an edge. Fix: send the ledger to owners.

## Worked example
**Input:** Fictional C1 has the five records in the reference. The owner approves at most one distinct `managedBy` object per subject on integer ticks `[1,12)`, with complete coverage.

**Output:**
```text
Scope: Fictional C1; managedBy; A and B; integer ticks [1,12), end-exclusive.
Rule: Owner-approved at most one distinct object per subject.
Coverage: Complete for supplied C1 exercise.
Conflict windows: A | [5,8) | M1,M2; B | none.
Evidence segments: A | [3,5) | one | M1:e1,e1b; A | [5,6) | conflict | M1:e1,e1b M2:e2; A | [6,8) | conflict | M1:e1 M2:e2; A | [8,10) | one | M2:e2; A | [10,12) | one | M1:e3; remaining segments in attached full ledger.
Independent check: Exact rational-point source replay and full [1,12) coverage passed.
Limits: Fictional selected view; no date conversion, source truth or edit approval.
Next action: Owner reviews e1,e1b and e2 together before any correction.
```

**Bad output:** “A conflicts on `[3,8)` because e1 and e1b overlap.” The two IDs both name M1; the distinct-object conflict begins only when M2 becomes active at 5.

## Edge cases
- **Incomplete coverage**: `[5,8)` remains an observed conflict, while apparently single-valued or empty segments are provisional.
- **Touching intervals**: e3 begins at e2's end 10 and creates no simultaneous M1/M2 value.
- **Different subject**: e4 affects B only and cannot extend A's conflict.
- **Third object**: A→M3 on `[7,9)` extends A's maximal conflict to `[5,9)` with new evidence segments.
- **Malformed record**: reject duplicate IDs, unknown endpoints, string-shaped records, noninteger or reversed bounds.

## Test case
**Input:**
> In fictional C1, assess A and B on `[1,12)` using e1,e1b,e2,e3,e4. Then add A→M3 record e5 on `[7,9)` and repeat. Show both maximal conflict windows and changing source-ID subsegments.

**Assertions:**
1. Base A has one maximal conflict window `[5,8)` and B has none.
2. Base `[5,6)` evidence contains e1,e1b,e2, while `[6,8)` contains e1,e2; e1b alone never creates a conflict.
3. e2 and e3 touching at 10 do not overlap under `[start,end)`.
4. Adding e5 extends A's maximal conflict to `[5,9)` without merging B's records.
</skill>

<user_request>
In fictional C1, assess A and B on `[1,12)` using e1,e1b,e2,e3,e4. Then add A→M3 record e5 on `[7,9)` and repeat. Show both maximal conflict windows and changing source-ID subsegments.
</user_request>
