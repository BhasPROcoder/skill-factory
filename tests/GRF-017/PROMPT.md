Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-017
name: reversible-graph-identity-migration
domain: Graph Engineering Foundations
subdomain: Schema and identity migration
version: 1.0
description: Build and verify a reversible graph representation migration with a complete identity map, preserved relationship evidence and version-scoped consumer aliases before cutover.
triggers: ["migrate graph identifiers without merging entities", "verify a reversible graph schema change", "preserve parallel edges during graph migration", "test graph migration rollback", "handle identifier swaps across graph versions"]
not_for: ["deciding same-entity merges [GRF-002]", "new empty storage implementation [GRF-014]", "general producer compatibility planning [TDE-004]", "live database rollout without environment-specific controls"]
requires: []
risk_level: medium
---

# Reversible Graph Identity Migration

## Purpose
Produce a separate migrated snapshot with an explicit inverse, proving which graph facts survive the representation change. Keep entity renaming distinct from entity merging, and expose consumer or revision ambiguities before switching readers. A passing offline round-trip is not proof of live rollback under concurrent writes.

## Inputs to collect
1. **Frozen source snapshot** — obtain revision, full node inventory, identified edges, properties and provenance. Why: a moving or incomplete source cannot establish migration parity. Default: supplied snapshot only; complete-system coverage unverified.
2. **Source and target contracts** — specify field meanings, required properties, multiplicity, nulls and identity namespaces. Why: moving a field must not silently change its meaning. Default: no guessed coercions or discarded fields.
3. **Identity mapping** — obtain one target identity for every source node, including unchanged identities. Why: checking changed nodes alone misses collisions with retained nodes. Default: unresolved mapping blocks transformation.
4. **Consumer references** — collect queries, external IDs, caches and readers/writers with their version boundaries. Why: one string can mean different entities before and after a rename. Default: consumer compatibility pending; no cutover approval.
5. **Cutover and recovery policy** — obtain authority, source freeze or write-capture mechanism, checkpoints and rollback scope. Why: restoring an old snapshot can lose writes made after cutover. Default: preview only, originals retained.
6. **Execution environment** — identify runtime, target storage and constraints. Why: an in-memory result does not establish database behavior. Default: portable reference only; [VERIFY: current target migration, transaction and recovery documentation before implementation].

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the source revision and inventory every field and relationship identity that the migration must preserve.
2. Define the target representation and inverse field mapping; mark lossy transformations as separately approved exceptions rather than calling them reversible.
3. Check mapping coverage and target uniqueness across all source nodes. Stop many-to-one mappings for identity adjudication; this procedure does not authorize merges.
4. Validate original edge identities and both endpoint references before transformation; preserve defects for correction rather than inventing missing nodes.
5. Transform into a separate target snapshot, preserving edge IDs, direction, parallel relationships, self-loops, properties and source locators.
6. ⚠️ Apply identity swaps simultaneously through the frozen mapping. Do not rename one node in place and then mistake its new ID for an unprocessed original.
7. Compare full source-to-target records under the mapping, not just totals; rerun representative queries with their parameters translated into the target namespace.
8. Apply the inverse to the target preview and compare the reconstructed source records with the frozen original. Investigate any mismatch before accepting reversibility.
9. Define version-scoped aliases and reader/writer compatibility checks. An alias must identify the source revision or namespace when an old string is also a different current identity.
10. Prepare cutover gates and a recovery rehearsal for the actual environment. Reconcile captured changes or re-freeze if the source revision moved; specify how post-cutover writes would survive recovery.
11. Deliver preview artifacts, executed checks and unresolved consumer/operational gates; do not mark a database migrated from an offline fixture.

This Python 3 reference transforms source tuples into a different named-field representation. IDs are nonempty strings; properties are caller-validated plain dictionaries containing copied data. Source tuples have shapes `(id, properties)` and `(edge_id, source, target, properties)`; validate tuple shapes before calling. The target is a new artifact, not an existing database. Run the full snippet and record the installed interpreter version.

```python
from copy import deepcopy

def migrate(nodes, edges, mapping):
    ids = [n for n, props in nodes]
    if any(not isinstance(n, str) or not n for n in ids):
        raise ValueError("invalid node identity")
    if len(set(ids)) != len(ids) or set(mapping) != set(ids):
        raise ValueError("duplicate node or incomplete mapping")
    targets = list(mapping.values())
    if any(not isinstance(n, str) or not n for n in targets):
        raise ValueError("invalid target identity")
    if len(set(targets)) != len(targets):
        raise ValueError("mapping would merge nodes")
    edge_ids = [e for e, s, t, p in edges]
    if any(not isinstance(e, str) or not e for e in edge_ids):
        raise ValueError("invalid edge identity")
    if len(set(edge_ids)) != len(edge_ids):
        raise ValueError("duplicate edge identity")
    if any(s not in mapping or t not in mapping for e, s, t, p in edges):
        raise ValueError("dangling source reference")
    if any(not isinstance(p, dict) for n, p in nodes) or any(
            not isinstance(p, dict) for e, s, t, p in edges):
        raise ValueError("property dictionary required")
    target = {
        "vertices": [{"key": mapping[n], "attributes": deepcopy(p)}
                     for n, p in nodes],
        "links": [{"key": e, "from": mapping[s], "to": mapping[t],
                   "attributes": deepcopy(p)} for e, s, t, p in edges]
    }
    return target, {new: old for old, new in mapping.items()}

def restore(target, inverse):
    nodes = [(r["key"], r["attributes"]) for r in target["vertices"]]
    edges = [(r["key"], r["from"], r["to"], r["attributes"])
             for r in target["links"]]
    checked, _ = migrate(nodes, edges, inverse)
    return ([(r["key"], r["attributes"]) for r in checked["vertices"]],
            [(r["key"], r["from"], r["to"], r["attributes"])
             for r in checked["links"]])

nodes = [("A", {"name": "first", "source": "n0"}),
         ("B", {"name": "second", "source": "n1"}), ("I", {})]
edges = [("x", "A", "B", {"source": "e0", "tags": ["one"]}),
         ("y", "A", "B", {"source": "e1"}),
         ("z", "B", "B", {"source": "e2"})]
before = deepcopy((nodes, edges))
mapping = {"A": "B", "B": "A", "I": "I"}
target, inverse = migrate(nodes, edges, mapping)
assert [(r["key"], r["from"], r["to"]) for r in target["links"]] == [
    ("x", "B", "A"), ("y", "B", "A"), ("z", "A", "A")]
assert restore(target, inverse) == before
assert (nodes, edges) == before
target["links"][0]["attributes"]["tags"].append("preview")
assert edges[0][3]["tags"] == ["one"]
print("swap, parallel edges, loop, inverse and copy isolation passed")
```

The inverse helper expects the generated target shape; validate extra or missing fields before accepting an externally edited artifact. No target edits are reconciled automatically into the original snapshot.

## Decision rules
- IF multiple source IDs map to one target THEN block this migration BECAUSE consolidation changes identity and is not an invertible rename.
- IF a target ID collides with an unchanged node THEN reject the complete mapping BECAUSE checking only renamed entries conceals an unintended merge.
- IF an old ID now names another entity THEN require a version-scoped alias BECAUSE an unqualified lookup cannot distinguish old and new meaning.
- IF the source changes after freezing THEN reconcile or rebuild the preview BECAUSE parity with an obsolete snapshot does not establish current correctness.
- IF post-cutover writes lack a recovery plan THEN leave rollback unproven BECAUSE restoring the old snapshot would discard later changes.

## Output template
```text
Scope: <source/target revisions, schema meanings and preview boundary; maximum 70 words>
Mapping: <old namespace/ID | new namespace/ID | inverse; full table>
Artifacts: <target snapshot, inverse map, original snapshot references>
Parity: <nodes, edge IDs/endpoints/properties, query results; executed or pending>
Recovery: <inverse comparison and treatment of later writes; maximum 90 words>
Consumers: <reader/writer | version-scoped alias or change | tested/pending>
Decision: <preview verified / blocked / incomplete; cutover gates, maximum 100 words>
```

## Quality checklist
- [ ] Mapping covers unchanged as well as changed identities.
- [ ] No target identity merges two source nodes.
- [ ] Both edge endpoints use the same frozen mapping.
- [ ] Parallel edge IDs, loops and isolated nodes survive.
- [ ] Complete properties and provenance survive round-trip comparison.
- [ ] Source records are unchanged by preview edits.
- [ ] Aliases identify their source and target namespaces or revisions.
- [ ] Offline inverse success is separate from live recovery evidence.

## Anti-patterns
- **Sequential swap**: overwrite B while renaming A. Fix: build a separate target using the complete map.
- **Counts prove parity**: accept equal totals with changed endpoints. Fix: compare mapped records and query witnesses.
- **Implicit merge**: reuse an occupied target ID. Fix: reject collisions across the entire inventory.
- **Timeless alias**: resolve old B as current B without version context. Fix: bind aliases to namespaces or revisions.
- **Snapshot rollback fantasy**: restore old data after new writes. Fix: rehearse preservation or reconciliation of those writes.

## Worked example
**Input:** Fictional team Birch supplies the snippet snapshot V1 and requests V2 with A/B swapped, I unchanged and the new field representation. Properties and all relationships must survive; no consumer or live-system evidence is supplied.

**Output:**
```text
Scope: Birch V1 to V2 named-field representation; separate offline preview.
Mapping: V1/A->V2/B, inverse B->A; V1/B->V2/A, inverse A->B; I unchanged within its versions.
Artifacts: Generated target plus inverse mapping; frozen V1 retained.
Parity: x/y become B->A; z becomes A->A; I retained. Reference assertions test complete inverse equality and copy isolation when executed.
Recovery: Offline inverse verified only after execution; post-cutover write handling unprovided.
Consumers: All pending; a V1/B reference must resolve to V2/A, not V2/B.
Decision: Preview conditionally verified by reference checks; cutover incomplete until consumers, source consistency and live recovery gates pass.
```

**Bad output:** “Rename A to B, then B to A; counts match, so deploy and keep B as an alias.”
This risks overwriting identities, lacks version context and invents operational readiness.

## Edge cases
- **Many-to-one requirement**: route to explicit entity-merge review; do not label it a reversible rename.
- **Partial mapping**: require explicit unchanged entries before checking collisions or rewriting endpoints.
- **Dangling original edge**: stop and preserve the defect; migration must not fabricate its endpoint.
- **Consumer caches old IDs**: require version-aware invalidation or translation evidence before cutover.
- **Lossy property change**: retain originals and document the loss separately; the inverse claim must exclude or recover it explicitly.

## Test case
**Input:**
> Fictional graph has nodes P/Q/R and separate edges u/v P->Q. Proposed mapping P->Q, Q->Q, R->R is called a rename. Produce a reversible migration assessment; no merge evidence is supplied.

**Assertions:**
1. Rejects the P/Q target collision rather than dropping either node.
2. Preserves original u/v identities and endpoints without a partial transformation.
3. Requests an injective mapping or a separate evidenced merge decision.
4. Makes no successful inverse, deployment or live rollback claim for the rejected proposal.
</skill>

<user_request>
Fictional graph has nodes P/Q/R and separate edges u/v P->Q. Proposed mapping P->Q, Q->Q, R->R is called a rename. Produce a reversible migration assessment; no merge evidence is supplied.
</user_request>
