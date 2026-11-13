---
id: GRF-011
name: bipartite-matching-certificate
domain: Graph Engineering Foundations
subdomain: Matching and assignment
version: 1.0
description: Compute a maximum-cardinality one-to-one assignment from explicit bipartite eligibility and verify optimality with an equal-size vertex cover when greedy allocation can strand feasible requests.
triggers: ["maximize eligible one-to-one assignments", "check whether greedy matching missed a solution", "prove this matching is maximum", "explain unmatched nodes in bipartite assignment", "produce a matching optimality certificate"]
not_for: ["rental custody and serial readiness reconciliation [RNT-001]", "weighted or preference-ranked assignment", "capacitated scheduling with time constraints", "automatic eligibility judgments or real-world allocation approval"]
requires: []
risk_level: medium
---

# Bipartite Matching Certificate

## Purpose
Find as many eligible one-to-one pairs as possible in a supplied bipartite graph and provide a checkable optimality certificate. Preserve every unmatched entity and separate a mathematical maximum from fairness, cost, readiness or authorization decisions. A feasible greedy assignment alone does not establish maximum cardinality.

## Inputs to collect
1. **Two inventories** — obtain unique left and right entity IDs, including entities without candidates. Why: omitted isolates conceal unmet demand. Default: no complete assignment claim without both inventories; namespace equal labels by side.
2. **Eligibility edges and evidence** — obtain each permitted left/right pair with its source record and exclusions. Why: optimization cannot establish whether a pair is actually allowed. Default: unresolved eligibility stays outside the confirmed graph, with a separate uncertainty ledger.
3. **Objective and capacities** — confirm maximum number of pairs and at most one partner per entity. Why: weights, quotas, precedence and repeated capacity require another model. Default: ask rather than treating a preference score as eligibility.
4. **Existing commitments** — identify fixed pairs versus assignments that may be rearranged in a proposal. Why: augmenting paths can replace existing choices. Default: no assumed permission to change commitments; resolve this before optimizing an operational allocation.
5. **Snapshot and coverage** — obtain revision, time scope and completeness of eligibility evidence. Why: new or omitted edges can change the maximum. Default: mathematical claims apply only to the supplied confirmed graph.
6. **Execution scope** — obtain runtime and scale, and whether implementation or a proposal is requested. Why: a transparent small reference is not a production scheduler. Default: offline calculation and certificate only.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the two inventories and eligibility ledger, preserving source locators for every included and unresolved pair.
2. Confirm unit capacity on both sides and a cardinality-only objective; route additional coupled constraints to an appropriate formulation before claiming an optimum.
3. Validate identities, side membership and fixed commitments. For supported fixed pairs, remove their occupied endpoints, solve the residual graph, and state that optimality is conditional on those commitments.
4. Initialize an empty residual matching and seek an augmenting path from an unmatched left node: alternate unused eligibility edges toward the right with matched edges back toward the left.
5. Flip matched status along a found path, retaining the displaced and replacement pairs in the proposal; each successful augmentation adds one pair.
6. Repeat until no unmatched left node has an augmenting path. Use a tested implementation appropriate to scale; record actual completion rather than assuming a time-limited search finished.
7. Build alternating reachability from all unmatched left nodes, using unmatched edges left-to-right and matched edges right-to-left. Let the reached sides be ZL and ZR.
8. Form a vertex cover from the unreached left nodes together with reached right nodes. Verify every eligibility edge touches that cover, every matched pair is eligible, and no endpoint is reused.
9. ⚠️ Compare matching and cover sizes. Equal sizes certify maximum cardinality because any matching can use each cover vertex at most once. If coverage or equality fails, report an unverified feasible result and investigate instead of claiming optimality.
10. Explain unmatched entities by their confirmed candidate neighborhoods and the certificate; do not imply a particular unmatched individual is impossible to match in every alternative optimum.
11. Deliver pairs, unmatched inventories, certificate and evidence limits; operational reassignment requires the separate supplied authority and current eligibility checks.

This Python 3 reference accepts disjoint lists of nonempty string IDs and unique `(left, right)` pairs. Pair tuples locate eligibility records in the fictional fixture; retain a separate source mapping in practice. Validate tuple shapes before calling. The recursive augmenting search is for small inputs; use a tested iterative implementation for larger or deep instances rather than changing recursion limits. Run the full snippet and record the actual interpreter version.

```python
def matching(left, right, edges):
    if any(not isinstance(x, str) or not x for x in left + right):
        raise ValueError("nonempty string IDs required")
    L, R = set(left), set(right)
    if len(L) != len(left) or len(R) != len(right) or L & R:
        raise ValueError("unique disjoint inventories required")
    if len(set(edges)) != len(edges):
        raise ValueError("duplicate eligibility pair")
    if any(a not in L or b not in R for a, b in edges):
        raise ValueError("wrong side or unknown endpoint")
    adj = {a: sorted(b for x, b in edges if x == a) for a in left}
    owner = {}
    def augment(a, seen):
        for b in adj[a]:
            if b in seen:
                continue
            seen.add(b)
            if b not in owner or augment(owner[b], seen):
                owner[b] = a
                return True
        return False
    for a in sorted(left):
        augment(a, set())
    pairs = {(a, b) for b, a in owner.items()}
    matched_left = {a for a, b in pairs}
    zl, zr = L - matched_left, set()
    pending = list(zl)
    while pending:
        a = pending.pop()
        for b in adj[a]:
            if (a, b) not in pairs and b not in zr:
                zr.add(b)
                if b in owner and owner[b] not in zl:
                    zl.add(owner[b])
                    pending.append(owner[b])
    cover_left, cover_right = L - zl, zr
    assert pairs <= set(edges)
    assert len({a for a, b in pairs}) == len(pairs)
    assert len({b for a, b in pairs}) == len(pairs)
    assert all(a in cover_left or b in cover_right for a, b in edges)
    assert len(pairs) == len(cover_left) + len(cover_right)
    return pairs, L - matched_left, R - set(owner), cover_left, cover_right

edges = [("A", "x"), ("A", "y"), ("B", "x")]
result = matching(["A", "B", "C"], ["x", "y"], edges)
assert result == ({("A", "y"), ("B", "x")}, {"C"}, set(),
                  {"A", "B"}, set())
assert matching(["A", "B"], ["x"],
                [("A", "x"), ("B", "x")])[4] == {"x"}
print("greedy-trap, isolate and shared-neighbor certificates passed")
```

## Decision rules
- IF an eligible greedy choice blocks another entity THEN search for alternating reassignment BECAUSE an earlier choice may be replaceable without losing a pair.
- IF matching and verified cover have equal sizes THEN certify maximum cardinality for that graph BECAUSE the cover is an upper bound attained by the matching.
- IF weights or fairness preferences matter THEN withhold a best-assignment claim BECAUSE equal cardinality does not compare those objectives.
- IF an unmatched entity has candidates THEN describe competition within this optimum BECAUSE another maximum matching may leave a different entity unmatched.
- IF eligibility coverage is incomplete THEN qualify optimality to confirmed edges BECAUSE missing allowed pairs can increase the attainable size.

## Output template
```text
Scope: <snapshot, inventories, objective, fixed commitments; maximum 80 words>
Matching: <left | right | eligibility evidence; full table>
Unmatched: <left IDs and right IDs; complete lists>
Certificate: <cover-left IDs, cover-right IDs, matching/cover sizes>
Checks: <eligibility, unique endpoints, every edge covered, equal size; executed/pending>
Explanation: <unmatched neighborhoods and alternate-optimum limits; maximum 100 words>
Disposition: <certified scoped maximum / feasible unverified / unresolved input>
Limits: <coverage, preferences, fixed commitments and unperformed actions; maximum 80 words>
```

## Quality checklist
- [ ] Both inventories include isolated entities.
- [ ] Eligibility evidence is distinct from preference or prediction.
- [ ] No endpoint appears in two matched pairs.
- [ ] Every matched pair exists in the confirmed graph.
- [ ] Every eligibility edge touches the certificate cover.
- [ ] Matching and cover sizes are checked explicitly.
- [ ] All unmatched entities remain visible.
- [ ] Maximum cardinality is not called fair, cheapest or deployed.

## Anti-patterns
- **Greedy equals optimal**: stop after taking the first eligible pair. Fix: search augmenting paths and verify a certificate.
- **Invented eligibility**: add a pair to satisfy every request. Fix: preserve the evidence boundary and unmatched list.
- **Unmatched means impossible**: label one leftover entity inherently infeasible. Fix: distinguish this optimum from alternative assignments.
- **Certificate by count alone**: report equal totals without checking cover edges. Fix: verify every eligibility edge touches the cover.
- **Commitment overwrite**: reroute a binding assignment silently. Fix: model fixed pairs separately and report conditional optimality.

## Worked example
**Input:** Fictional workshop Maple supplies A/B/C and resources x/y. Confirmed pairs are A-x, A-y and B-x; C has none. Each entity can have one partner, no commitment is fixed, and the goal is maximum pair count. This is an offline proposal.

**Output:**
```text
Scope: Maple supplied complete fixture; unit capacities; maximum cardinality; no fixed pairs.
Matching: A | y | A-y record; B | x | B-x record.
Unmatched: Left C; right none.
Certificate: Cover-left A,B; cover-right none; matching size 2, cover size 2.
Checks: Reference assertions verify eligible pairs, unique endpoints, all three eligibility edges covered, and equal size when executed.
Explanation: A-x alone strands B despite A-y being available; alternating reassignment reaches two pairs. C has no confirmed candidate in this fixture.
Disposition: Certified scoped maximum of two pairs when checks execute successfully.
Limits: No fairness or cost objective, live allocation or current readiness verification performed.
```

**Bad output:** “Assign A-x; B and C cannot be served, so one pair is optimal.”
This misses the supported two-pair reassignment and supplies no optimality certificate.

## Edge cases
- **Shared only neighbor**: return one pair and a cover containing that right node; identify the competing left set without inventing priority.
- **Empty side or no edges**: return empty matching and cover, retaining all unmatched inventory IDs.
- **Same display label on both sides**: namespace identities explicitly; equal labels need not represent one entity.
- **Several slots per entity**: use a capacity-aware formulation or evidenced distinct slots; do not silently duplicate an entity.
- **Interrupted search**: return the feasible partial pairs as unverified; do not fabricate a completed certificate.

## Test case
**Input:**
> Fictional left nodes P/Q/R and right nodes u/v permit P-u, P-v and Q-u; R has no edge. Unit capacity, no fixed commitments and cardinality only. Find a maximum and certify it.

**Assertions:**
1. Returns P-v and Q-u, leaving R unmatched.
2. Gives a valid two-vertex cover and checks its size equals the two matched pairs.
3. Preserves all unmatched inventory entries and original eligibility evidence.
4. Makes no fairness, cost-optimality or operational allocation claim.
