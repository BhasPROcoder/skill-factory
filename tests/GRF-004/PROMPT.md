Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-004
name: rooted-forest-contract-validation
domain: Graph Engineering Foundations
subdomain: Structural invariant validation
version: 1.0
description: Validate a declared parent-to-child forest against explicit roots, parent cardinality and whole-snapshot reachability, returning defect witnesses and evidence-bound repair proposals.
triggers: ["validate this graph is a rooted forest", "check hierarchy structural invariants", "find nodes outside declared roots", "audit parent graph integrity", "validate a proposed hierarchy repair"]
not_for: ["designing graph entity and role semantics [GRF-001]", "reconciling edge-list imports [GRF-003]", "finding a prerequisite cycle or ordering tasks [SEQ-001]", "choosing archival provenance groups [ARC-002]"]
requires: []
risk_level: medium
---

# Rooted Forest Contract Validation

## Purpose
Determine whether an existing directed parent relation satisfies a supplied rooted-forest contract. Return local violation witnesses and the complete set outside declared-root reachability, then separate proposed corrections from verified repaired snapshots. Structural success does not establish that the chosen parents are true in the real domain.

## Inputs to collect
1. **Graph snapshot** — obtain unique node IDs, uniquely identified parent edges and revision. Why: disconnected nodes must be checked too. Default: no full-snapshot verdict without the node inventory.
2. **Relation meaning** — confirm that each selected edge means parent to child, and isolate it from other relationship types. Why: cross-references need not belong to the forest. Default: unresolved; do not infer meaning from arrow layout.
3. **Root contract** — obtain the complete allowed root set and whether one tree or several trees are expected. Why: inventing roots conceals missing parents. Default: no inferred root approval; require explicit treatment of an empty graph.
4. **Completeness boundary** — obtain whether all relevant nodes and parent edges are included for the stated time/version. Why: missing extraction data can imitate broken structure. Default: findings apply to the supplied extract only; full-graph validity remains unknown.
5. **Repair evidence and owner** — collect source records, authorized parent changes and retained originals. Why: the validator cannot select the correct parent. Default: diagnosis and conditional repair proposal only.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the revision, node inventory, selected relation and declared root set, including a precise completeness statement.
2. Check input identities and endpoint references before structural evaluation. Retain invalid records as input exceptions; do not silently add nodes or deduplicate edges to obtain a passing graph.
3. Write the invariants: declared roots have no incoming parent edges; every other node has exactly one; every node is reachable from a declared root by parent-to-child edges. If one tree is required, also require exactly one declared root.
4. Count incoming parent edges for every inventory node and record offending edge IDs beside each failed count.
5. Traverse outward from all declared roots with a visited set and collect the complete unreachable-node set, including inventory-only nodes.
6. ⚠️ Compare local and global results separately. One incoming edge per non-root can still hide a disconnected directed cycle; never replace the reachability check with degree counts or aggregate edge totals.
7. Label each finding as an observed extract defect, an unresolved completeness issue, or a confirmed full-snapshot defect under supplied coverage evidence.
8. Propose an evidence-dependent repair for each defect group, naming exact additions, removals or root changes and the owner decision required. Do not select an arbitrary incoming edge or promote unreachable nodes to roots to force success.
9. Apply an approved alternative only to a separate preview; rerun every invariant across the full scope, retaining both snapshots and change identifiers.
10. Deliver the verdict, witnesses, proposed actions and rerun evidence. Mark absent execution as unrun and report domain-semantic verification separately.

This Python 3 reference validates a nonempty finite snapshot with string node/edge IDs, parent-to-child triples and explicit nonempty roots. Run it with the available interpreter and record its version. It reports structural findings, not semantic repairs; malformed tuple shapes or non-string fields must be rejected before calling it.

```python
def check_forest(nodes, edges, roots):
    if not nodes or len(nodes) != len(set(nodes)):
        raise ValueError("nonempty unique node inventory required")
    known = set(nodes)
    if not roots or len(roots) != len(set(roots)) or not set(roots) <= known:
        raise ValueError("explicit unique known roots required")
    if len({eid for eid, s, t in edges}) != len(edges):
        raise ValueError("edge identities must be unique")
    if any(s not in known or t not in known for eid, s, t in edges):
        raise ValueError("unknown endpoint")
    incoming = {n: [] for n in nodes}
    children = {n: [] for n in nodes}
    for eid, source, target in edges:
        incoming[target].append(eid)
        children[source].append(target)
    root_set = set(roots)
    local = {n: incoming[n] for n in nodes
             if len(incoming[n]) != (0 if n in root_set else 1)}
    visited, pending = set(), list(roots)
    while pending:
        node = pending.pop()
        if node not in visited:
            visited.add(node)
            pending.extend(children[node])
    return {"parent_violations": local,
            "unreachable": sorted(known - visited)}

nodes = ["r", "a", "x", "y"]
bad = [("e1", "r", "a"), ("e2", "x", "y"),
       ("e3", "y", "x")]
assert check_forest(nodes, bad, ["r"]) == {
    "parent_violations": {}, "unreachable": ["x", "y"]}
# Fictional owner evidence replaces e3 with r -> x; no live mutation.
fixed = bad[:2] + [("e4", "r", "x")]
assert check_forest(nodes, fixed, ["r"]) == {
    "parent_violations": {}, "unreachable": []}
multiple = fixed + [("e5", "a", "x")]
assert check_forest(nodes, multiple, ["r"])["parent_violations"] == {
    "x": ["e4", "e5"]}
print("disconnected-cycle, repaired-preview and multiple-parent checks passed")
```

## Decision rules
- IF parent counts pass but nodes remain unreachable THEN fail the forest contract BECAUSE local counts do not establish attachment to the declared roots.
- IF a reference is unknown or an identity is ambiguous THEN stop the structural verdict BECAUSE evaluating a silently altered graph hides the input defect.
- IF coverage is partial THEN limit absence-based findings to the extract BECAUSE an omitted parent edge can explain an apparent orphan.
- IF several parents are present THEN retain their edge evidence and request adjudication BECAUSE structure alone cannot identify the truthful relationship.
- IF a proposed repair passes THEN report only the tested preview as structurally valid BECAUSE acceptance does not prove deployment or domain correctness.

## Output template
```text
Scope: <revision, relation direction, completeness; maximum 70 words>
Contract: <roots, tree/forest, empty-graph policy; maximum 50 words>
Input exceptions: <ID/reference issues or none; attach complete table>
Local witnesses: <node | expected incoming count | edge IDs observed; complete table>
Global witnesses: <unreachable IDs; attach complete list>
Verdict: <pass / fail / unresolved; extract versus full-snapshot scope>
Repair proposal: <edge/root changes | supporting evidence | owner/state; up to 8 rows, attach remainder>
Rerun: <snapshot | local/global results | executed/unrun; maximum 100 words>
Limits: <semantic and deployment checks not established; maximum 60 words>
```

## Quality checklist
- [ ] Direction and selected parent relation are explicit.
- [ ] Roots come from the declared contract, not algorithmic convenience.
- [ ] Every inventory node participates in both checks.
- [ ] Failed parent counts include original edge IDs.
- [ ] Unreachable nodes remain visible even when local counts pass.
- [ ] Partial coverage limits absence-based conclusions.
- [ ] Repair evidence and authorization are separate from structural preference.
- [ ] Rerun results identify the exact tested snapshot.

## Anti-patterns
- **Degree-only approval**: every non-root has one parent, so the graph passes. Fix: also check declared-root reachability.
- **Invented root repair**: declare each disconnected node a root. Fix: obtain a supported root-policy change.
- **Convenient parent deletion**: keep the first incoming edge. Fix: retain all witnesses for evidence-based adjudication.
- **Mixed relation graph**: cross-reference edges become extra parents. Fix: select the contracted relation explicitly.
- **Preview becomes production**: a passing copy is called a deployed repair. Fix: report its revision and unperformed deployment separately.

## Worked example
**Input:** Fictional team Willow supplies complete snapshot W1 from the snippet: r→a, x→y, y→x with root r. Exactly one tree is required. No repair evidence or mutation authorization is supplied.

**Output:**
```text
Scope: W1; parent-to-child edges; supplied complete fictional snapshot.
Contract: Root r; one tree; nonempty snapshot.
Input exceptions: None.
Local witnesses: None; r has zero incoming edges, a/x/y each have one.
Global witnesses: x, y are unreachable from r.
Verdict: Fail for complete W1 despite passing local counts.
Repair proposal: No approved change. Owner must supply parent evidence for x/y before selecting a replacement edge or changing roots.
Rerun: W1 reference check identifies x/y as unreachable when executed; repaired W1 rerun unrun because no correction was supplied.
Limits: No semantic parent decision or live change established. The snippet's separate fictional repaired preview is not an authorized W1 correction.
```

**Bad output:** There are four nodes and three edges, so W1 is a tree; remove any troublesome edge if needed.
This ignores the disconnected cycle and invents permission to alter relationships.

## Edge cases
- **Isolated declared root**: valid as a one-node tree in a forest; a single-tree contract still forbids additional declared roots.
- **Self-parent edge**: preserve its ID; at a root it breaks the zero-parent rule, while an otherwise isolated non-root self-loop fails reachability.
- **Parallel parent edges**: count both identified relationships; do not collapse them before applying an exactly-one-edge contract.
- **Empty snapshot**: require the owner's empty-forest policy; the reference intentionally rejects it and cannot prove that policy satisfied.
- **Time-sliced hierarchy**: validate one explicitly supplied interval/version at a time; do not combine historical parents into a simultaneous graph.

## Test case
**Input:**
> Fictional complete snapshot has roots R and S, edges p:R→A, q:S→B and t:B→A. A forest is allowed. Produce defect evidence; no source supports choosing between p and t.

**Assertions:**
1. Reports A's two incoming edge IDs p and t against expected count one.
2. Reports all nodes reachable without treating that as a passing forest verdict.
3. Preserves both conflicting edges and requests parent evidence rather than choosing one.
4. Keeps any repair and rerun unperformed unless actually executed on a supplied alternative.
</skill>

<user_request>
Fictional complete snapshot has roots R and S, edges p:R→A, q:S→B and t:B→A. A forest is allowed. Produce defect evidence; no source supports choosing between p and t.
</user_request>
