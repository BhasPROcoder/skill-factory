---
id: GRF-048
name: knowledge-inference-retraction-support
domain: Graph Engineering Foundations
subdomain: Derived fact support maintenance
version: 1.0
description: Recompute licensed transitive facts after one source assertion is retracted, distinguishing genuinely lost facts from facts with surviving alternate support.
triggers: ["retract a knowledge graph assertion", "check whether an inferred fact survives deletion", "replace a stale derivation witness", "trace alternate support for a derived relationship", "audit inferred facts after source removal"]
not_for: ["designing relation meanings or inference permissions [GRF-018]", "reconstructing a two-clock source snapshot [GRF-005]", "applying an atomic graph patch [GRF-016]", "generic directed edge insertion reachability [GRF-039]"]
requires: []
risk_level: medium
---

# Knowledge Inference Retraction Support

## Purpose
Preview one source assertion's retraction under an approved transitive rule. Keep duplicate-triple records distinct, replace stale witnesses when alternate paths survive, and classify loss only after checking the complete after view. This preview neither authorizes deletion nor establishes source truth.

## Inputs to collect
1. **Frozen inventory** — obtain nodes, identified assertions, predicate and snapshot ID. Why: loss depends on complete scoped records. Default: none; never infer omitted records.
2. **Rule contract** — obtain approved transitivity and revision. Why: paths alone do not license facts. Default: unapproved; report unresolved.
3. **Proposed retraction** — obtain one existing source ID. Why: equal triples may have separate records. Default: no preview without an exact ID.
4. **Interpretation boundaries** — obtain direction, identity scope and cyclic self-fact policy. Why: zero-length or undirected paths change results. Default: directed nonempty paths for this reference.
5. **Execution bound** — obtain a finite exhaustible snapshot. Why: partial search cannot prove loss. Default: report pending when complete calculation is infeasible.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze inventory, rule revision and retraction ID; retain original assertions.
2. Validate unique node/source IDs, four-field records, endpoints and predicate; reject malformed rows.
3. Confirm explicit transitivity approval; stop on unresolved direction or revision.
4. Build before facts with nonempty source-ID paths, including direct one-record paths.
5. Build an isolated after view excluding only the named ID. ⚠️ Preserve equal triples from other records.
6. Compute complete before and after fact sets under one convention; require a nonempty cycle for self-facts.
7. Separate lost and retained facts; flag retained facts whose selected before witness used the retracted ID.
8. ⚠️ Verify every claimed loss against an independent complete after closure; a lost witness alone proves nothing.
9. Replay every path against its corresponding inventory, checking direction, continuity and endpoints; reject retracted IDs in after paths.
10. Deliver affected and unchanged fact ledgers with scope limits; distinguish preview from live deletion.

This Python 3 in-memory reference accepts directed `(source_ID, subject, predicate, object)` records for one approved transitive predicate. It selects deterministic shortest witnesses by breadth-first search and checks fact sets using separate relation closure. Run it and record the installed interpreter version; it makes no production-scale claim.

```python
from collections import deque

def validate(nodes, records, predicate, retracted, approved):
    if approved is not True:
        raise ValueError("transitive rule not approved")
    if type(nodes) not in (list, tuple) or type(records) not in (list, tuple):
        raise ValueError("invalid inventory shape")
    if type(predicate) is not str or not predicate:
        raise ValueError("invalid predicate")
    if any(type(n) is not str or not n for n in nodes) or len(set(nodes)) != len(nodes):
        raise ValueError("invalid node inventory")
    known, ids = set(nodes), set()
    for row in records:
        if type(row) not in (tuple, list) or len(row) != 4:
            raise ValueError("invalid assertion record")
        rid, s, p, o = row
        if any(type(x) is not str or not x for x in row):
            raise ValueError("invalid assertion field")
        if rid in ids or s not in known or o not in known or p != predicate:
            raise ValueError("duplicate ID, endpoint or predicate mismatch")
        ids.add(rid)
    if retracted not in ids:
        raise ValueError("unknown retraction ID")

def witnesses(nodes, records):
    adj = {n: [] for n in nodes}
    for rid, s, p, o in records:
        adj[s].append((rid, o))
    for n in adj:
        adj[n].sort()
    found = {}
    for start in nodes:
        queue = deque([(start, ())])
        expanded = {start}
        while queue:
            at, path = queue.popleft()
            for rid, nxt in adj[at]:
                candidate = path + (rid,)
                found.setdefault((start, nxt), candidate)
                if nxt not in expanded:
                    expanded.add(nxt)
                    queue.append((nxt, candidate))
    return found

def closure(nodes, records):
    pairs = {(s, o) for _, s, _, o in records}
    while True:
        added = pairs | {(a, d) for a, b in pairs for c, d in pairs if b == c}
        if added == pairs:
            return pairs
        pairs = added

def replay(pair, path, records):
    by_id = {rid: (s, o) for rid, s, _, o in records}
    if not path:
        return False
    at = pair[0]
    for rid in path:
        if rid not in by_id or by_id[rid][0] != at:
            return False
        at = by_id[rid][1]
    return at == pair[1]

def preview(nodes, records, predicate, retracted, approved):
    validate(nodes, records, predicate, retracted, approved)
    after = [r for r in records if r[0] != retracted]
    before_paths, after_paths = witnesses(nodes, records), witnesses(nodes, after)
    before_facts, after_facts = set(before_paths), set(after_paths)
    lost = before_facts - after_facts
    replaced = {f for f in before_facts & after_facts
                if retracted in before_paths[f]}
    result = (before_paths, after_paths, lost, replaced)
    verify(nodes, records, after, retracted, result)
    return result

def verify(nodes, before, after, retracted, result):
    bp, ap, lost, replaced = result
    if set(bp) != closure(nodes, before) or set(ap) != closure(nodes, after):
        raise ValueError("fact set differs from independent closure")
    if lost != set(bp) - set(ap):
        raise ValueError("incorrect lost facts")
    if replaced != {f for f in set(bp) & set(ap) if retracted in bp[f]}:
        raise ValueError("incorrect replacement ledger")
    if any(not replay(f, path, before) for f, path in bp.items()):
        raise ValueError("invalid before witness")
    if any(retracted in path or not replay(f, path, after)
           for f, path in ap.items()):
        raise ValueError("invalid after witness")
    return True

nodes = ["A", "B", "C", "D", "E"]
rows = [("r1", "A", "contains", "B"), ("r2", "B", "contains", "D"),
        ("r3", "A", "contains", "C"), ("r4", "C", "contains", "D"),
        ("r5", "D", "contains", "E"), ("r6", "A", "contains", "B")]
bp, ap, lost, replaced = preview(nodes, rows, "contains", "r2", True)
assert lost == {("B", "D"), ("B", "E")}
assert ("A", "D") in replaced and ap[("A", "D")] == ("r3", "r4")
assert ("A", "E") in replaced and ap[("A", "E")] == ("r3", "r4", "r5")
assert ("A", "B") in ap and "r2" not in ap[("A", "B")]
assert ("A", "B") in preview(nodes, rows, "contains", "r1", True)[1]
cyclic = [("x", "A", "contains", "B"), ("y", "B", "contains", "A")]
assert ("A", "A") in preview(["A", "B"], cyclic, "contains", "y", True)[0]
assert ("A", "A") in preview(["A", "B"], cyclic, "contains", "y", True)[2]
print("retraction, alternate support, duplicate source and cycle checks passed")
```

## Decision rules
- IF the rule is unapproved or its revision is unknown THEN stop at unresolved BECAUSE traversal alone does not license inference.
- IF another source ID asserts an equal triple THEN retain that assertion after one ID is retracted BECAUSE source records are separate evidence.
- IF the selected old witness disappears but another valid after path remains THEN classify the fact as retained with replacement support BECAUSE witness loss is not fact loss.
- IF a fact is absent from the complete independently checked after closure THEN classify it lost for this frozen scope BECAUSE no licensed after path supports it.
- IF full inventory or computation is unavailable THEN report pending, not a global loss claim BECAUSE unobserved support may exist.

## Output template
```text
Scope: <snapshot, node/record population, predicate and rule revision; max 60 words>
Retraction: <one source ID; preview only>
Before facts: <complete ledger or attached ID; count>
Lost: <fact | old source-ID path; every lost fact>
Retained with replacement: <fact | old path | current path; every affected fact>
Other retained: <fact IDs or attached ledger>
Verification: <independent closure and path replay result, or pending>
Limits: <inventory, rule and execution limits; max 60 words>
Next action: <source owner review or missing-input request>
```

## Quality checklist
- [ ] Snapshot and licensed rule revision are named.
- [ ] Retraction identifies one existing source record, not a triple label.
- [ ] Duplicate direct records remain distinguishable by source ID.
- [ ] Before and after fact sets use the same direction and nonempty-path convention.
- [ ] Every affected retained fact has a current after witness.
- [ ] Every lost fact is absent from an independent complete after closure.
- [ ] All displayed witness IDs replay continuously against their own inventory.
- [ ] No output claims source truth, a live deletion or whole-graph completeness without evidence.

## Anti-patterns
- **Witness equals fact**: dropping a fact when its first witness vanishes. Fix: recompute all after support before classifying loss.
- **Triple-wide deletion**: removing every equal assertion. Fix: remove only the named source ID.
- **Unlicensed closure**: turning any path into an entailed relation. Fix: require the approved predicate rule revision.
- **Empty self-path**: reporting `(A,A)` merely because A exists. Fix: require a nonempty directed cycle.
- **Count-only comparison**: accepting equal before and after totals. Fix: compare exact fact sets and paths.
- **Live-edit wording**: treating a preview as committed deletion. Fix: state owner decision and execution separately.

## Worked example
**Input:** Fictional Grove snapshot G1 has nodes A, B, C, D, E and the six source records in the reference snippet. Its owner has approved transitivity of `contains` for G1 and asks what would happen if record r2 alone were retracted.

**Output:**
```text
Scope: Fictional G1; five nodes and six source records; approved contains transitivity for this exercise.
Retraction: r2; preview only.
Before facts: A,B; A,C; A,D; A,E; B,D; B,E; C,D; C,E; D,E (nine).
Lost: B,D | r2; B,E | r2,r5.
Retained with replacement: A,D | r1,r2 | r3,r4; A,E | r1,r2,r5 | r3,r4,r5.
Other retained: A,B; A,C; C,D; C,E; D,E. See the full path ledger.
Verification: Independent closure and source-ID path replay passed.
Limits: G1 is fictional and scoped; source truth and wider omitted support unexamined.
Next action: Owner reviews the proposed retraction before any source change.
```

**Bad output:** “A,D is lost because its recorded derivation used r2.” This fails because the surviving r3,r4 path still proves the fact under the approved rule.

## Edge cases
- **Duplicate direct records**: retracting r1 leaves A,B supported by r6; show the surviving record ID.
- **Cyclic self-fact**: a directed nonempty cycle may support A,A; removing its only closing record removes that self-fact.
- **Multiple alternate paths**: one current path is enough to show survival, but retain the full source ledger for later retractions.
- **Malformed assertion**: reject string-shaped records and unknown endpoints before computing; do not guess fields.
- **Incomplete extract**: label loss unresolved outside the supplied scope, even when the finite local closure is complete.

## Test case
**Input:**
> In the fictional G1 exercise, preview retracting r2. Also preview retracting r1 alone. Keep the six source records distinct, use the approved transitive contains rule, and show what happens to A,D, A,E, B,D, B,E and A,B.

**Assertions:**
1. The r2 preview loses B,D and B,E but retains A,D and A,E with paths through r3 and r4.
2. No after witness for the r2 preview contains r2.
3. The r1-only preview retains direct A,B support from r6.
4. The answer states that the calculation is a preview for the fictional scoped ledger and requires owner review before deletion.
