Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-035
name: dag-reachability-reduction-certificate
domain: Graph Engineering Foundations
subdomain: Directed reachability reduction
version: 1.0
description: Remove redundant directed edges from a complete acyclic graph snapshot while certifying that every node pair retains its reachability.
triggers: ["remove redundant graph edges", "reduce a dependency DAG", "preserve reachability while trimming links", "find a minimal reachability skeleton", "explain why this directed edge can be removed", "certify DAG transitive reduction"]
not_for: ["bounded seed traversal [GRF-006]", "strong component condensation [GRF-008]", "database query-plan tuning [GRF-015]", "business approval to delete source records", "ordering tasks or finding a prerequisite cycle [SEQ-001]"]
requires: []
risk_level: medium
---

# DAG Reachability Reduction Certificate

## Purpose
Construct a smaller directed edge inventory preserving all reachable node pairs in an acyclic snapshot. Return retained identities, removal witnesses, and pairwise verification for review.

## Inputs to collect
1. **Snapshot** — complete node IDs and directed edge records `(edge ID, source, target)` from one declared version. Why: omitted nodes or links change the reachability claim. Default: none, required.
2. **Projection** — which relationship types participate and how direction is interpreted. Why: a mixed or silently reversed relationship changes paths. Default: none, required when the source has types or ambiguous direction.
3. **Identity policy** — whether parallel edges represent separately required obligations or interchangeable structural links. Why: reachability alone cannot authorize dropping an obligation. Default: structural analysis only; retain source records outside the analysis projection.
4. **Boundary** — included nodes, excluded records, and whether isolated nodes remain in scope. Why: verification must cover the same universe. Default: include every supplied node and edge.
5. **Use of result** — analysis view, proposed cleanup, or downstream execution. Why: a graph witness is not a domain approval. Default: analysis view; any destructive application awaits its own owner review.

If a required input is missing without a safe default, ask in one message with at most three questions. Freeze the answer and record the snapshot identifier before calculation.

## Procedure
1. Record the node and edge inventory, the source version, and the projection rule without changing source data.
2. Validate unique nonempty node IDs, unique nonempty edge IDs, and known endpoints. Preserve isolated nodes in the declared node universe.
3. Check that the selected directed graph is acyclic, including self-loops. If it has a cycle, stop and route the cycle question to a suitable diagnostic; do not call the result a DAG reduction.
4. Define reachability as existence of a directed path of one or more edges between an ordered node pair. Record whether zero-length self-reachability is included in a separate application contract; it does not change edge removal here.
5. Compute the original reachability set over every declared node. Keep this as the independent reference, not merely a count of reachable pairs.
6. Visit edge identities in a stated deterministic order. For each current edge, temporarily exclude that identity and search for another directed source-to-target path in the current retained graph.
7. ⚠️ Remove an edge only when that alternate path exists, and record the actual path edge IDs as a removal witness. If two parallel edges exist, sequential testing may remove one but must retain a path for the other; removing both from independent original-graph tests is invalid.
8. After all decisions, independently recompute every reachable ordered pair from the retained graph. Compare the complete pair set with the original reference and reject any difference.
9. For each removed edge, replace the decision-time witness with a path in the final retained graph; reject a missing final witness. For each retained edge, temporarily exclude it and verify that its source can no longer reach its target. This establishes inclusion-minimality for this structural snapshot, not business necessity.
10. Deliver retained IDs, removed IDs and witness paths, complete-pair parity, and limitations. Keep original source records untouched until the responsible owner separately approves any operational change.

This Python 3 reference handles finite in-memory directed graphs with nonempty string IDs. It rejects cyclic input, validates its own inventory, and uses exhaustive reachability for inspectability rather than production-scale performance. Execute the entire snippet on the target interpreter and record that interpreter's version. A caller must choose the eligible projection before passing records in.

```python
def check_input(nodes, edges):
    if any(type(n) is not str or not n for n in nodes):
        raise ValueError("invalid node ID")
    if len(set(nodes)) != len(nodes):
        raise ValueError("duplicate node ID")
    if any(type(e) not in (tuple, list) or len(e) != 3
           or any(type(x) is not str or not x for x in e)
           for e in edges):
        raise ValueError("invalid edge record")
    if len({e[0] for e in edges}) != len(edges):
        raise ValueError("duplicate edge ID")
    if any(a not in nodes or b not in nodes for _, a, b in edges):
        raise ValueError("unknown endpoint")

def path(edges, start, goal):
    adj = {}
    for eid, a, b in sorted(edges):
        adj.setdefault(a, []).append((b, eid))
    pending = [(start, ())]
    seen = {start}
    for node, route in pending:
        for other, eid in adj.get(node, ()):
            candidate = route + (eid,)
            if other == goal:
                return candidate
            if other not in seen:
                seen.add(other)
                pending.append((other, candidate))
    return None

def pairs(nodes, edges):
    return {(a, b) for a in nodes for b in nodes if path(edges, a, b)}

def reduce_dag(nodes, edges):
    check_input(nodes, edges)
    if any((n, n) in pairs(nodes, edges) for n in nodes):
        raise ValueError("cycle or self-loop: DAG required")
    original = pairs(nodes, edges)
    keep = {e[0]: e for e in edges}
    removed = {}
    for eid in sorted(keep):
        edge = keep[eid]
        remaining = [e for key, e in keep.items() if key != eid]
        witness = path(remaining, edge[1], edge[2])
        if witness is not None:
            removed[eid] = witness
            del keep[eid]
    result = list(keep.values())
    if pairs(nodes, result) != original:
        raise AssertionError("reachability changed")
    for eid, a, b in result:
        if path([e for e in result if e[0] != eid], a, b) is not None:
            raise AssertionError("retained edge is still redundant")
    for eid in removed:
        _, a, b = next(e for e in edges if e[0] == eid)
        removed[eid] = path(result, a, b)
        if removed[eid] is None:
            raise AssertionError("removed edge has no final witness")
    return sorted(keep), removed, original

n = ["A", "B", "C", "I"]
e = [("ab", "A", "B"), ("bc", "B", "C"),
     ("ac", "A", "C")]
kept, deleted, reach = reduce_dag(n, e)
assert kept == ["ab", "bc"]
assert deleted == {"ac": ("ab", "bc")}
assert reach == {("A", "B"), ("A", "C"), ("B", "C")}
assert reduce_dag(["A", "B"], [("e1", "A", "B"),
                                   ("e2", "A", "B")])[0] == ["e2"]
assert reduce_dag(["I"], [])[0] == []
try:
    reduce_dag(["A", "B"], [("ab", "A", "B"), ("ba", "B", "A")])
except ValueError:
    pass
else:
    raise AssertionError("cycle accepted")
try:
    reduce_dag(["A", "B"], ["eAB"])
except ValueError:
    pass
else:
    raise AssertionError("string edge record accepted")
print("DAG reduction, parallel identities, isolates and cycle rejection checked")
```

## Decision rules
- IF the snapshot is incomplete THEN return unresolved and request the missing inventory BECAUSE pairwise reachability cannot be certified over unknown records.
- IF a directed cycle or self-loop exists THEN stop the DAG procedure and return the cycle blocker BECAUSE this reduction contract assumes acyclicity.
- IF an alternate path exists only before another proposed removal THEN reassess against the current retained graph BECAUSE independent removal decisions may jointly destroy reachability.
- IF complete pair sets differ after reduction THEN reject the candidate regardless of equal pair counts BECAUSE equal totals can hide different lost and gained pairs.
- IF a retained edge remains removable without changing its endpoint reachability THEN mark the result unfinished BECAUSE the claimed structural minimum has not been shown.
- IF an edge represents a legal, operational, or semantic obligation THEN keep its source record pending owner review BECAUSE structural redundancy alone does not erase that obligation.

## Output template
```text
Scope: <snapshot ID, node/edge inventory, projection, direction; max 3 lines>
Eligibility: <DAG confirmed | unresolved | cycle blocker and witness>
Retained: <edge IDs, or none>
Removed: <edge ID -> alternate path edge IDs, one line each, or none>
Verification: <original and retained reachable-pair sets match or exact difference; essential-edge check>
Decision: <certified analysis reduction | rejected | unresolved>
Limits: <semantic obligations, source retention and unexamined records; max 2 lines>
Next action: <owner or analyst action; one line>
```

## Quality checklist
- [ ] Snapshot version, projection, direction and node universe are explicit.
- [ ] Node IDs, edge IDs and endpoints passed validation.
- [ ] Acyclicity was checked before removal.
- [ ] Every removed edge has an alternate path using final retained edge identities.
- [ ] Parallel edges were processed sequentially, not removed together from separate tests.
- [ ] Original and retained complete reachable-pair sets match.
- [ ] Each retained edge failed the endpoint alternative-path test.
- [ ] Isolated nodes remain in the node inventory.
- [ ] The result does not authorize source deletion or infer semantic equivalence.

## Anti-patterns
- **Endpoint count comparison**: equal reachability counts can conceal different pairs. Fix: compare exact ordered-pair sets.
- **Independent parallel deletion**: each parallel edge appears unnecessary when the other remains. Fix: test against the current retained set after each decision.
- **Original-only witness**: a path recorded before later removals might not survive. Fix: rebuild each removal witness from the final retained graph.
- **Silent direction flip**: reversing a dependency changes reachability. Fix: freeze arrow meaning and use directed paths only.
- **Cycle laundering**: applying DAG language to a cyclic projection. Fix: reject and route the cycle issue separately.
- **Business deletion claim**: treating structural redundancy as approval to erase a contract or event. Fix: confine the result to an analysis view until owner review.

## Worked example
**Input:**
> Fictional Atlas project has complete directed snapshot S1: nodes A, B, C, I; edges ab A→B, bc B→C, ac A→C. I is isolated. Produce an analysis reduction.

**Output:**
```text
Scope: Fictional Atlas S1; nodes A,B,C,I; directed edges ab,bc,ac; all eligible.
Eligibility: DAG confirmed.
Retained: ab,bc.
Removed: ac -> ab,bc.
Verification: Original and retained pairs both {(A,B),(A,C),(B,C)}; each retained edge essential.
Decision: Certified analysis reduction.
Limits: I remains isolated; no source record deletion or semantic-equivalence claim.
Next action: Use the retained IDs in the analysis view; ask the record owner before any source change.
```

**Bad output:** "Delete ac from Atlas because it is unnecessary." This fails because the witness supports only structural reachability in S1 and gives no authority over source-record meaning.

## Edge cases
- **No edges**: retain every declared node, return empty edge sets and an empty reachable-pair set.
- **Parallel edges**: process stable edge IDs sequentially; one may remain to preserve the endpoint pair, and the other receives a one-edge witness.
- **Self-loop**: reject as a cyclic input even when other edges form a DAG.
- **Disconnected DAG**: compare all ordered pairs across components; unreachable cross-component pairs stay absent.
- **Missing endpoint or duplicate ID**: reject inventory before computing paths; never synthesize a missing node or silently collapse identities.

## Test case
**Input:**
> Fictional Beacon snapshot T1 has nodes P,Q,R,I and directed edges p P→Q, q Q→R, r P→R, plus isolated I. Provide a certified analysis reduction. Then state what happens if edge s R→P is added.

**Assertions:**
1. The ordinary T1 result retains p and q and removes r with witness p,q.
2. The result lists exactly the reachable pairs (P,Q), (P,R), and (Q,R), unchanged after reduction.
3. I remains in scope as an isolated node and no source deletion is authorized.
4. Adding s is reported as a cycle blocker; the skill does not certify a DAG reduction for that changed snapshot.
</skill>

<user_request>
Fictional Beacon snapshot T1 has nodes P,Q,R,I and directed edges p P→Q, q Q→R, r P→R, plus isolated I. Provide a certified analysis reduction. Then state what happens if edge s R→P is added.
</user_request>
