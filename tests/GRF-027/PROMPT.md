Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-027
name: bounded-graph-isomorphism-witness-search
domain: Graph Engineering Foundations
subdomain: Structural graph correspondence
version: 1.0
description: Search for exact structural bijections between two finite directed graphs and report mapping witnesses or bounded uncertainty when names differ but relationship structure must be compared.
triggers: ["compare graphs despite renamed nodes", "find structural graph mappings", "check directed graph isomorphism", "explain symmetric graph mappings", "distinguish search cutoff from nonisomorphism"]
not_for: ["deciding real entity identity [GRF-002]", "maximum bipartite assignment [GRF-011]", "executing a supplied migration mapping [GRF-017]", "approximate graph similarity scoring", "large graph solver selection"]
requires: []
risk_level: medium
---

# Bounded Graph Isomorphism Witness Search

## Purpose
Find bijections that preserve an explicitly selected graph structure when node identifiers differ. Return concrete mapping witnesses and a separate search-completeness statement so a truncated search cannot become a false impossibility claim. Structural correspondence alone does not establish real-world entity identity or authorize a merge.

## Inputs to collect
1. **Frozen graph pair** — obtain both revisions, node inventories and directed edge records. Why: changing inputs invalidate a comparison. Default: none; both inventories required, including isolated nodes.
2. **Preserved semantics** — identify direction, edge labels, parallel multiplicity, loops and node attributes that must match. Why: different projections answer different questions. Default: preserve direction, labels, multiplicities and loops; request the required node attribute policy.
3. **Compatibility encoding** — obtain a shared exact node-class key and edge-label vocabulary. Why: unrelated local labels cannot be compared without a declared mapping. Default: unresolved keys block a semantic verdict; explicitly untyped graphs may use one shared class key.
4. **Search budget** — obtain the permitted number of candidate bijections and output storage boundary. Why: exhaustive enumeration can become impractical. Default: propose a bounded rehearsal, with execution pending until the limit is supplied.
5. **Witness purpose** — identify whether the user needs one mapping, all mappings or a nonexistence decision. Why: one witness proves existence but cannot establish uniqueness. Default: retain every witness within the declared search budget and report completeness separately.
6. **Excluded properties** — inventory omitted identity, provenance, temporal or business fields. Why: structural equivalence applies only to the selected representation. Default: omitted fields remain outside the conclusion, never silently declared equal.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze both graph revisions and record the exact representation projection being compared.
2. Validate node identities and edge endpoints, retaining invalid input as an exception rather than creating missing nodes.
3. Encode the selected node attributes and edge labels into shared compatibility keys, preserving original records separately.
4. Check node totals and label-specific edge multiplicities as necessary conditions; a mismatch rules out a bijection under this contract.
5. Enumerate candidate node bijections in a recorded deterministic order, counting each examined candidate against the budget.
6. Reject a candidate when any mapped node has an incompatible class key.
7. Transform every source edge through the candidate and compare the complete directed labeled edge multiset with the target multiset.
8. ⚠️ Retain only candidates passing full edge comparison; equal degrees or counts alone do not establish correspondence.
9. Verify each retained witness against the original selected projection, including isolated nodes, self-loops and parallel edges.
10. Record whether enumeration exhausted all candidates or stopped at the budget; keep this independent of whether witnesses were found.
11. Deliver mapping witnesses, completeness and excluded semantics, routing any later identity or migration action to its own evidence process.

This Python 3 reference uses small, already materialized graphs. Nodes are dictionaries from nonempty string IDs to shared string class keys; edges are `(source, label, target)` tuples with string labels. Prevalidate those shapes and ensure the original node ledger has no duplicate IDs before dictionary construction. Edge IDs are deliberately excluded from structural equality: edge label, direction and multiplicity are preserved. Include additional properties in an explicit encoding before using the method for a broader contract. Record the actual interpreter version when executing.

```python
from collections import Counter
from itertools import permutations

def search(left, le, right, re, budget):
    if type(budget) is not int or budget < 0:
        raise ValueError("invalid candidate budget")
    for nodes, edges in ((left, le), (right, re)):
        if any(s not in nodes or t not in nodes for s, label, t in edges):
            raise ValueError("unknown endpoint")
    if len(left) != len(right):
        return [], 0, True
    if Counter(label for s, label, t in le) != Counter(label for s, label, t in re):
        return [], 0, True
    source, target = sorted(left), sorted(right)
    expected = Counter(re)
    witnesses, tested = [], 0
    for order in permutations(target):
        if tested >= budget:
            return witnesses, tested, False
        tested += 1
        mapping = dict(zip(source, order))
        if any(left[s] != right[mapping[s]] for s in source):
            continue
        mapped = Counter((mapping[s], label, mapping[t]) for s, label, t in le)
        if mapped == expected:
            witnesses.append(mapping)
    return witnesses, tested, True

left = {"A": "Unit", "B": "Unit"}
right = {"X": "Unit", "Y": "Unit"}
w, tested, complete = search(left, [], right, [], 2)
assert w == [{"A": "X", "B": "Y"}, {"A": "Y", "B": "X"}]
assert tested == 2 and complete
partial, tested, complete = search(left, [], right, [], 1)
assert len(partial) == 1 and tested == 1 and not complete
print("symmetry witnesses and bounded completeness checked")
```

The search counts incompatible class assignments too, so the budget has an unambiguous operational meaning. It stores every discovered witness and is intended for bounded fixtures, not a scale claim. A retained mapping proves existence even when the remaining enumeration is incomplete. An empty result proves nonexistence only when completeness is true and input semantics are valid. Necessary-condition rejection also returns complete because the contract already makes a bijection impossible. Two empty graphs have one empty bijection; a zero budget leaves that enumeration unperformed.

## Decision rules
- IF at least one fully checked mapping exists THEN report structural existence BECAUSE a witness suffices even without exhaustive enumeration.
- IF no witness exists and enumeration is incomplete THEN report unknown existence BECAUSE unexamined mappings may succeed.
- IF several witnesses exist THEN preserve their ambiguity BECAUSE symmetry does not identify which real entity corresponds to which.
- IF one witness was found before a cutoff THEN do not call it unique BECAUSE another valid mapping may remain unexamined.
- IF properties were omitted from the projection THEN exclude them from the conclusion BECAUSE matching selected structure does not compare discarded information.

## Output template
```text
Contract: <two revisions, projection, compatibility keys; maximum 80 words>
Input exceptions: <invalid records or none>
Search: <candidate order, budget, tested count, complete/incomplete, stopping reason>
Witnesses: <complete mapping list or attachment; explicitly identify any presentation subset>
Verification: <node/class/edge-multiset checks executed or pending>
Decision: <exists / no mapping under contract / unknown; uniqueness evidence>
Limits: <excluded semantics and operational limits; maximum 70 words>
Next action: <owner and one concrete step; maximum 40 words>
```

## Quality checklist
- [ ] Both revisions and selected properties are explicit.
- [ ] Every original node, including isolates, is represented.
- [ ] Candidate mappings are bijective and class compatible.
- [ ] Edge comparison preserves direction, labels, loops and multiplicity.
- [ ] Candidate budget and actual tested count are distinguished.
- [ ] Existence and completeness are reported separately.
- [ ] Multiple mappings or unproven uniqueness remain visible.
- [ ] Structural results do not authorize identity merges.

## Anti-patterns
- **Degree shortcut**: accept matching degree lists as proof. Fix: verify the full mapped edge multiset.
- **Cutoff becomes impossible**: no early witness is called no mapping. Fix: preserve unknown existence when incomplete.
- **First map becomes identity**: turn a structural witness into an entity merge. Fix: obtain separate identity evidence.
- **Set erases multiplicity**: collapse parallel edges before comparison. Fix: compare multisets under the declared projection.
- **Hidden projection loss**: omit properties then claim complete equivalence. Fix: list every excluded semantic field.

## Worked example
**Input:** Fictional graphs L1 and R1 each contain two isolated Unit nodes, A/B and X/Y. Compare their unweighted directed structure with a candidate budget of two; business identity is excluded.

**Output:**
```text
Contract: L1/R1; isolated directed Unit-node structure; shared Unit key; no edges or business identity comparison.
Input exceptions: None in the supplied fixture.
Search: Sorted source/target IDs and permutation order; budget 2; tested 2 when reference executes; complete after enumeration.
Witnesses: {A:X,B:Y}; {A:Y,B:X}.
Verification: Reference checks bijection, class equality and empty edge multisets; execution must be recorded by the runner.
Decision: Exists; two mappings demonstrate nonuniqueness under the contract.
Limits: Structural symmetry supplies no business identity evidence; no merge or scalable performance claim.
Next action: Owner reviews additional meaningful attributes if a unique correspondence is needed.
```

**Bad output:** “The first mapping proves A is X, so merge their records.”
This treats an arbitrary structural witness as identity evidence and hides the second valid mapping.

## Edge cases
- **Equal degree counts, different connectivity**: continue exact edge comparison; retain a rejecting witness or completed no-mapping result.
- **Zero budget**: report unexamined search unless a necessary-condition mismatch already rules out a mapping.
- **Loops and parallel edges**: preserve every occurrence in multiset comparison; do not silently simplify either graph.
- **Unsupported attributes**: request a shared encoding or limit the projection explicitly before comparison.
- **Many witnesses**: stop under the declared resource boundary and return incomplete enumeration; attach checked witnesses without implying a complete list.

## Test case
**Input:**
> Fictional graphs each contain two isolated Unit nodes. A budget of one examines and accepts the first bijection. Can we conclude the mapping is unique or that the corresponding nodes are the same real objects?

**Assertions:**
1. Reports structural existence from the accepted witness.
2. Reports incomplete enumeration and unproven uniqueness.
3. Does not infer real-object identity or authorize merging.
4. Records the one examined candidate and declared budget.
</skill>

<user_request>
Fictional graphs each contain two isolated Unit nodes. A budget of one examines and accepts the first bijection. Can we conclude the mapping is unique or that the corresponding nodes are the same real objects?
</user_request>
