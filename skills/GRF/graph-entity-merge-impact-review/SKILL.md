---
id: GRF-002
name: graph-entity-merge-impact-review
domain: Graph Engineering Foundations
subdomain: Entity identity and merge impact
version: 1.0
description: Review proposed graph entity merges against identity evidence and relationship consequences when duplicate-looking nodes could change graph meaning.
triggers: ["review graph entity merges", "resolve duplicate graph nodes", "check entity merge consequences", "merge graph identities safely", "audit graph entity resolution"]
not_for: ["checking tabular key uniqueness [TDQ-001]", "triaging duplicate business listings [MSL-008]", "automatic identity scoring without evidence", "redesigning the whole graph schema"]
requires: []
risk_level: medium
---

# Graph Entity Merge Impact Review

## Purpose
Produce a reversible proposal for consolidating graph nodes that represent the same entity, including the effects on their incident relationships. Distinguish identity approval from a similarity suggestion and identify groups whose apparently acceptable pairwise links create contradictory combined identities. This review prepares a change artifact; it does not mutate a database.

## Inputs to collect
1. **Identity definition and scope** — obtain what one node represents, source namespaces, entity type, and relevant time/version boundary. Why: an organization, branch, account, and historical version may be different entities. Default: unresolved until defined.
2. **Candidate pairs and evidence** — obtain stable node IDs, source records, proposed same-entity evidence and evidence that nodes must remain distinct. Why: similar names alone cannot approve a merge. Default: candidate only, no consolidation.
3. **Graph snapshot** — obtain node attributes and incident edges with edge IDs, type, direction, properties and provenance. Why: identity changes affect relationships. Default: incomplete impact assessment if only a sample is available.
4. **Merge policy** — obtain canonical-ID selection, conflicting-property handling, allowed self-loops, parallel-edge meaning and cardinality constraints. Why: graph mechanics cannot choose domain meaning. Default: preserve originals and flag each policy gap.
5. **Authority and recovery** — obtain approving owner, requested action scope, snapshot/version and rollback mechanism. Why: a correct proposal can still be unauthorized or irreversible. Default: proposal only.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the review snapshot and record its coverage, entity definition and candidate sources.
2. Classify each pair as supported same entity, supported distinct, or unresolved, citing the exact evidence and applicable identity rule.
3. Build proposed merge groups from supported same-entity links; keep unresolved suggestions outside the groups.
4. ⚠️ Check every proposed group for distinctness constraints and incompatible identity facts, including pairs not directly proposed. If a chain joins a forbidden pair, block the whole conflicting group pending adjudication instead of accepting links in arbitrary order.
5. Choose a canonical ID for each conflict-free group under the supplied policy, retaining the mapping from every original ID. Do not use an arbitrary sorting rule unless the owner explicitly accepts it.
6. Resolve properties into a proposal that retains original values, source and validity context. Conflicting values remain a documented owner decision; do not overwrite them silently.
7. Rewrite both endpoints of each incident edge in a separate preview, preserving original edge ID, type, properties, direction and source endpoints.
8. Classify new self-loops, coincident edges, changed cardinalities and newly reachable relationships. Distinguish repeated observations from duplicate storage before proposing edge consolidation.
9. Compare affected query results and contractual invariants before and after the preview. Use representative successful and failing examples, not only node-count reduction.
10. Package mapping, property decisions, edge dispositions, blocked groups and verification results for the approving owner. Require version consistency and a recoverable source snapshot before any later authorized execution.

The following fictional fixture runs with Python 3 using built-in language features. Save and execute it with the available interpreter, recording that interpreter's version. It checks identity-group conflicts and previews endpoint rewriting; it does not decide identity from names or prove that a merge is authorized. Adapt the facts and constraints before applying the method elsewhere.

```python
def groups(nodes, pairs):
    parent = {n: n for n in nodes}
    def root(n):
        while parent[n] != n:
            n = parent[n]
        return n
    for a, b in pairs:
        parent[root(b)] = root(a)
    return {n: root(n) for n in nodes}

nodes = {"a", "b", "c", "x"}
proposed = groups(nodes, [("a", "b"), ("b", "c")])
cannot_link = [("a", "c")]
conflicts = [(a, b) for a, b in cannot_link
             if proposed[a] == proposed[b]]
assert conflicts == [("a", "c")]
# A separate owner-approved alternative merges only a and b.
canonical = {"a": "a", "b": "a", "c": "c", "x": "x"}
edges = [("e1", "a", "x"), ("e2", "b", "x"),
         ("e3", "a", "b")]
preview = [(eid, canonical[s], canonical[t])
           for eid, s, t in edges]
assert preview == [("e1", "a", "x"), ("e2", "a", "x"),
                   ("e3", "a", "a")]
assert len(preview) == len(edges)
print("conflicting_pairs=1 preserved_edges=3 new_self_loops=1")
```

## Decision rules
- IF evidence supports similarity but not identity THEN retain separate nodes and request discriminating evidence BECAUSE a merge asserts sameness, not resemblance.
- IF a proposed transitive group contains a supported distinct pair THEN block that group for adjudication BECAUSE individually plausible links can create a contradictory combined identity.
- IF endpoint rewriting creates coincident edges THEN preserve edge IDs until relationship semantics justify consolidation BECAUSE two events can legitimately share endpoints.
- IF a merge produces a forbidden self-loop or cardinality violation THEN hold execution and resolve the identity or relationship policy BECAUSE dropping the edge hides a consequence rather than repairs it.
- IF an attribute conflicts across sources THEN retain provenance and route the conflict under the supplied policy BECAUSE selecting a convenient value invents certainty.
- IF graph coverage or snapshot freshness is unknown THEN label impact incomplete BECAUSE unseen or changed relationships may alter the decision.

## Output template
```text
Scope: <snapshot, entity meaning, coverage; maximum 60 words>
Identity decisions: <pair/group | evidence | same/distinct/unresolved; up to 10 rows>
Mapping: <original ID | proposed canonical ID | approval/state; up to 10 rows>
Properties: <field | original values/sources | proposed treatment; up to 8 rows>
Edges: <edge ID | old endpoints | proposed endpoints | disposition/reason; up to 12 rows>
Checks: <constraint/query | before/after observation | pass/fail/unrun; up to 8 rows>
Recovery: <snapshot and reverse mapping availability; maximum 60 words>
Decision: <ready for owner approval / blocked / incomplete; reason and next evidence>
```

## Quality checklist
- [ ] Entity meaning, namespace and snapshot are explicit.
- [ ] Same, distinct and unresolved decisions cite evidence.
- [ ] Entire merge groups were checked for conflicting distinctness constraints.
- [ ] Original IDs, properties and edge identities remain recoverable.
- [ ] Both edge endpoints were included in the preview.
- [ ] New self-loops and coincident edges have explicit dispositions.
- [ ] Query and cardinality consequences were checked or marked unrun.
- [ ] Execution authorization is separate from identity evidence.

## Anti-patterns
- **Name equality**: merge records with matching labels. Fix: apply evidenced identity criteria.
- **Greedy conflict hiding**: accept the first pair and ignore later contradictory links. Fix: inspect the full proposed group before execution.
- **Edge collapse**: deduplicate every rewritten edge. Fix: preserve event identity and relationship provenance.
- **Property winner by convenience**: keep the first source's value. Fix: use an approved conflict policy or leave unresolved.
- **Irreversible cleanup**: discard originals once the preview looks tidy. Fix: preserve snapshot, mapping and change history.

## Worked example
**Input:** Fictional archive Linden has nodes a, b and x. An approved identity record establishes a and b as the same organization; the owner selects a as canonical. Edges e1:a→x and e2:b→x are distinct dated participation events; e3:a→b is an affiliation relation that forbids self-links. Property conflict review and query execution are unavailable. This is a proposal only.

**Output:**
```text
Scope: Linden supplied snapshot; organization identity; complete listed incident edges only.
Identity decisions: {a,b} | approved identity record | same.
Mapping: a→a; b→a | canonical selection supplied; execution pending.
Properties: Not supplied; property reconciliation unrun.
Edges: e1 a→x becomes a→x, retain event; e2 b→x becomes a→x, retain distinct event; e3 a→b becomes a→a, blocked forbidden self-link.
Checks: edge identities 3→3 preserved; self-link constraint fails for e3; query checks unrun.
Recovery: Original snapshot and complete property history must be retained before execution; supplied mapping alone is insufficient recovery evidence.
Decision: Blocked; owner must resolve e3's identity/relationship meaning and complete property/query checks before execution.
```

**Bad output:** Merge a and b, discard e2 as duplicate, and delete e3 because self-links look wrong.
This loses a legitimate event and conceals a failed constraint without authority.

## Edge cases
- **A–B and B–C match but A–C must differ**: preserve all evidence and block the group; request adjudication of the conflicting links.
- **Missing incident-edge coverage**: deliver identity decisions with an incomplete impact label; request the missing scope before execution.
- **Historical identity change**: distinguish temporal versions from aliases under the supplied entity policy; do not retroactively rewrite history automatically.
- **External IDs still referenced**: retain resolvable alias mappings and identify consumers requiring an approved migration.

## Test case
**Input:**
> Fictional graph has proposed same-entity links A–B and B–C, but an authoritative record requires A and C to remain distinct. All have edges to X. The user asks to merge the group and collapse repeated edges.

**Assertions:**
1. Blocks the transitive merge group and cites the A–C conflict.
2. Preserves original nodes and edges while requesting adjudication.
3. Does not assume shared endpoints imply duplicate events.
4. Separates a preview from authorized execution and identifies recovery evidence.
