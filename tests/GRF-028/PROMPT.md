Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-028
name: analysis-graph-projection-contribution-ledger
domain: Graph Engineering Foundations
subdomain: Analysis projection contracts
version: 1.0
description: Materialize an explicitly approved graph analysis projection with contribution and exclusion ledgers when filtering or combining source relationships changes their analytical meaning.
triggers: ["build an analysis graph projection", "aggregate graph edges with provenance", "explain projected graph weights", "preserve isolated nodes in projection", "audit graph projection exclusions"]
not_for: ["designing the source graph model [GRF-001]", "preserving imported edge identities [GRF-003]", "reversible identity migration [GRF-017]", "computing graph ranks [GRF-012]", "choosing community partitions [GRF-013]"]
requires: []
risk_level: medium
---

# Analysis Graph Projection Contribution Ledger

## Purpose
Create a derived analysis graph whose aggregates can be recomputed from named source contributions. Expose filtering and information loss so downstream results can be interpreted against the projection actually used. Retain the source graph separately; an aggregate graph does not reconstruct every original relationship.

## Inputs to collect
1. **Source snapshot** — obtain stable node and edge identities, endpoints, relation kinds and weights. Why: contributions must reference an immutable input. Default: no materialization without the source inventory.
2. **Analysis question and consumer** — obtain the intended interpretation and required graph properties. Why: different projections answer different questions. Default: unresolved consumer suitability; no readiness claim.
3. **Node cohort and filters** — specify included nodes, relation kinds and treatment of isolated nodes. Why: edge-only output can silently remove eligible entities. Default: propose retaining the supplied node inventory, awaiting approval.
4. **Weight contract** — obtain quantity, unit, aggregation rule and treatment of invalid values. Why: numeric values are not automatically additive. Default: aggregation blocked until approved; never silently substitute one for missing weights.
5. **Direction and loop policy** — obtain directed or undirected interpretation and whether self-loops are meaningful. Why: collapsing direction and loops changes possible analyses. Default: preserve direction and request explicit loop treatment before materializing.
6. **Occurrence identity evidence** — establish whether parallel or inverse records represent distinct occurrences. Why: repeated representations can inflate sums. Default: unresolved equivalences require adjudication before combining their values.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze source revision, consumer question and projection contract under a named output revision.
2. Validate node identities, unique source edge IDs and endpoint membership before filtering.
3. Establish the approved node cohort, retaining nodes that may become isolated after filtering.
4. Classify each source edge as included or excluded using the relation, cohort and loop policy, recording a reason for each exclusion.
5. Check included weights against the approved quantity, unit and missing-value policy.
6. ⚠️ Resolve repeated representations of one occurrence before summing; do not assume opposite directions imply independent events.
7. Construct each contribution's grouping key using the approved direction convention and compatible relation grouping.
8. Aggregate each group while retaining every contributing source edge ID and its value.
9. Reconcile source IDs against the disjoint contribution and exclusion ledgers so every input edge is accounted for once.
10. Recompute each output aggregate from its listed contributions and compare the complete output mapping.
11. Identify source-isolated nodes separately from nodes made isolated by projection filters.
12. Deliver the derived graph, ledgers, semantic losses and consumer checks, marking unexecuted downstream runs pending.

This Python 3 reference implements an explicitly approved sum of nonnegative integer occurrence counts for one relation kind. Its cohort is the complete supplied node inventory. Self-loops are excluded with evidence. Undirected mode requires explicit permission to lose direction. Source edge tuples are `(ID, subject, predicate, object, count)`; prevalidate nonempty string IDs and tuple shapes. Execute the complete snippet and record the interpreter version. This code checks accounting, not whether the supplied records truly represent independent occurrences.

```python
def project(nodes, edges, relation, directed, allow_direction_loss):
    if type(directed) is not bool or type(allow_direction_loss) is not bool:
        raise ValueError("explicit direction policy required")
    if not directed and not allow_direction_loss:
        raise ValueError("direction loss not approved")
    inventory = set(nodes)
    if len(inventory) != len(nodes):
        raise ValueError("duplicate node ID")
    seen, groups, excluded = set(), {}, {}
    for eid, s, p, o, weight in edges:
        if eid in seen:
            raise ValueError("duplicate edge ID")
        seen.add(eid)
        if s not in inventory or o not in inventory:
            raise ValueError("unknown endpoint")
        if p != relation:
            excluded[eid] = "relation filter"
            continue
        if s == o:
            excluded[eid] = "loop policy"
            continue
        if type(weight) is not int or weight < 0:
            raise ValueError("invalid included occurrence count")
        key = (s, o) if directed else tuple(sorted((s, o)))
        groups.setdefault(key, []).append((eid, weight))
    aggregate = {key: sum(w for eid, w in items)
                 for key, items in groups.items()}
    included = [eid for items in groups.values() for eid, w in items]
    assert len(included) == len(set(included))
    assert set(included).isdisjoint(excluded)
    assert set(included) | set(excluded) == seen
    return sorted(inventory), aggregate, groups, excluded

nodes = ["A", "B", "I"]
edges = [("e1", "A", "visit", "B", 2),
         ("e2", "A", "visit", "B", 3),
         ("e3", "B", "visit", "A", 7),
         ("e4", "A", "other", "B", 9)]
out = project(nodes, edges, "visit", True, False)
assert out[0] == ["A", "B", "I"]
assert out[1] == {("A", "B"): 5, ("B", "A"): 7}
assert out[2][("A", "B")] == [("e1", 2), ("e2", 3)]
assert out[3] == {"e4": "relation filter"}
assert project(nodes, edges, "visit", False, True)[1] == {("A", "B"): 12}
print("projection contributions and exclusions checked")
```

Filtered relation and loop records keep their exclusion reasons even though their weights are not included in the sum. A zero-valued included occurrence remains a contribution; removing zero edges is a different consumer policy requiring an explicit transformation. Consumers needing other aggregation rules, mixed units or selected node cohorts must use separately specified and tested implementations rather than reinterpret this reference's output.

## Decision rules
- IF weight meanings or units differ THEN block their aggregation BECAUSE arithmetic compatibility does not establish semantic compatibility.
- IF direction loss is unapproved THEN retain directed grouping BECAUSE reverse relationships can answer different questions.
- IF a source ID appears twice THEN reject ambiguous accounting BECAUSE contributions must identify source records uniquely.
- IF all incident edges are filtered THEN retain the node under the approved cohort policy BECAUSE filtering relationships does not remove entity eligibility.
- IF an aggregate disagrees with its contributions THEN reject the derived artifact BECAUSE unchanged totals or edge counts cannot prove correct grouping.

## Output template
```text
Contract: <source/output revisions, consumer, quantity/unit, aggregation, direction, loops, cohort; maximum 100 words>
Projection: <node inventory and complete aggregate mapping or attachment>
Contributions: <output key | source edge IDs and values>
Exclusions: <source edge ID | reason>
Isolation: <originally isolated nodes | projection-isolated nodes>
Checks: <accounting, aggregate recomputation and consumer checks; observed/pending>
Decision: <ready within approved contract / blocked; semantic losses and unresolved items; maximum 80 words>
```

## Quality checklist
- [ ] Source and output revisions are distinguished.
- [ ] Quantity, unit and aggregation have explicit approval.
- [ ] Direction and loop policies appear in the contract.
- [ ] Every source edge is included once or excluded with a reason.
- [ ] Every aggregate recomputes from its named contributions.
- [ ] Eligible isolated nodes remain in the node inventory.
- [ ] Repeated representations have an occurrence-identity decision.
- [ ] Information loss and pending consumer checks are visible.

## Anti-patterns
- **Numeric means additive**: sum unrelated scores. Fix: establish quantity and unit semantics first.
- **Default weight invention**: replace a missing count with one. Fix: apply an approved missing-value rule or block.
- **Direction erasure**: collapse reverse links without approval. Fix: record direction conversion explicitly.
- **False reversibility**: promise original records from aggregates alone. Fix: retain the original graph and contribution ledger separately.
- **Silent isolation loss**: emit nodes only from retained edges. Fix: preserve the approved node cohort.

## Worked example
**Input:** Fictional inventory A/B/I and the snippet edges represent distinct occurrences. Owner approves directed visit-count sums, exclusion of other relations and loops, and retention of all nodes. Consumer execution is pending.

**Output:**
```text
Contract: Fictional source F1/output P1; visit-count analysis; occurrence counts summed; directed; loops excluded; all A/B/I retained.
Projection: Nodes A,B,I; A->B 5; B->A 7.
Contributions: A->B | e1=2,e2=3; B->A | e3=7.
Exclusions: e4 | relation filter.
Isolation: Originally isolated I; projection-isolated I; no additional isolated nodes.
Checks: Reference accounting and aggregate checks available to execute; downstream consumer run pending.
Decision: Ready for reference verification within supplied contract; occurrence detail is collapsed in aggregates, source records retained separately; no downstream result claimed.
```

**Bad output:** “The projection has weight 21, so it preserves all source meaning.”
This includes the excluded value and mistakes a total for semantic preservation.

## Edge cases
- **No retained edges**: emit the approved node inventory and complete exclusion ledger; no fabricated relationship.
- **Missing weight**: block an included contribution unless a separately approved handling exists.
- **Inverse records of one event**: adjudicate event identity before counting either as independent occurrence.
- **Unknown endpoint**: reject malformed source input before treating it as a normal filtered edge.
- **Changed consumer requirements**: create a new projection revision and rerun contributions; do not silently reuse incompatible weights.

## Test case
**Input:**
> Fictional A->B visit edges have counts 2 and 3; I is isolated. A reverse record may describe the same event, and direction loss has not been approved. Build the projection decision.

**Assertions:**
1. Blocks aggregation involving unresolved repeated-event identity.
2. Does not collapse direction without approval.
3. Retains I under the declared all-node cohort, or asks for cohort approval.
4. Provides contribution/exclusion accounting requirements without claiming an executed result.
</skill>

<user_request>
Fictional A->B visit edges have counts 2 and 3; I is isolated. A reverse record may describe the same event, and direction loss has not been approved. Build the projection decision.
</user_request>
