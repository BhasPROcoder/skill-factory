Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-003
name: graph-edge-list-import-reconciliation
domain: Graph Engineering Foundations
subdomain: Graph import reconciliation
version: 1.0
description: Convert an explicit node inventory and edge list into a traceable graph import while preserving direction, relationship identity, parallel edges and rejected-row evidence.
triggers: ["import an edge list without losing edges", "reconcile graph import counts", "preserve isolated nodes during import", "check missing edge endpoints", "why did graph loading collapse relationships"]
not_for: ["deciding which entities are identical", "designing a graph model from business requirements", "general tabular key uniqueness [TDQ-001]", "database deployment or live graph mutation"]
requires: []
risk_level: medium
---

# Graph Edge List Import Reconciliation

## Purpose
Prepare a graph import artifact whose nodes and relationships can be traced back to source records. Detect semantic losses that row-count checks alone miss, including dropped isolated nodes, collapsed parallel relationships and silently reversed endpoints. The result is an import proposal and reconciliation, not evidence that a live database was changed.

## Inputs to collect
1. **Source snapshot** — collect the node inventory, edge rows and stable source-row locators; why: the import must have a reproducible boundary. Default: supplied snapshot only, with missing inventories flagged.
2. **Graph contract** — obtain directed or undirected semantics, edge identity, permitted parallel relationships and self-loops; why: the same rows can encode different graphs. Default: no invented contract; ask before transforming.
3. **Identifier policy** — obtain node namespaces, types, normalization and approved aliases; why: coercion can merge distinct entities. Default: preserve exact source strings; do not trim or convert identifiers automatically.
4. **Endpoint policy** — identify whether nodes must already exist or may be created from endpoints; why: an absent node could be a data defect or intended creation. Default: quarantine unresolved endpoints when a complete inventory is supplied; otherwise report incomplete node coverage.
5. **Destination capabilities** — obtain target format, importer behavior and version from the actual environment; why: an exporter can support multiple edges that a loader collapses. Default: produce a neutral node/edge table and mark destination verification pending.
6. **Acceptance scope** — obtain expected semantics and who can approve losses or corrections; why: rejected rows may block release. Default: no silent discard and no live import.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the source revision and assign a source locator to every node and edge record, including malformed records.
2. Write the graph contract explicitly, distinguishing an edge's identity from its endpoint pair.
3. Validate node identifiers against the declared namespace and type policy; preserve originals alongside any approved mapped values.
4. Validate the node inventory for repeated identifiers and conflicting attributes; stop ambiguous mappings before rewriting edges.
5. Classify every edge row as accepted or quarantined with all observed reasons, retaining original fields and locator.
6. ⚠️ Resolve both endpoints against the inventory before output. Do not create a node merely to make a dangling reference disappear unless the contract explicitly authorizes that creation.
7. Preserve distinct edge identities even when endpoint pairs match; quarantine repeated edge IDs rather than selecting whichever row was encountered first.
8. For undirected graphs, apply a declared canonical endpoint ordering only to the output representation; preserve original order and edge identity in provenance. For directed graphs, retain endpoint order.
9. Retain inventory nodes with no accepted incident edges. Distinguish declared isolated nodes from nodes made isolated because their incident rows were quarantined.
10. Reconcile accepted and quarantined source locators to the entire input, and compare output relationship identities and endpoint mappings, not just counts.
11. Round-trip a representative target export when tools are available, checking node IDs, edge IDs, endpoint direction and properties. Verify current importer options in official documentation before relying on target behavior.
12. Deliver the tables, exceptions and release decision; unresolved semantic loss blocks a claim that the import preserves the contract.

The following Python 3 reference uses string IDs, a complete unique node inventory, directed relationships, and allowed parallel edges/self-loops. It intentionally rejects all occurrences of a repeated edge ID. It does not implement attribute validation, alias mapping or database loading; apply the corresponding procedure checks separately. Run it with the available interpreter and record its actual version.

```python
from collections import Counter

def prepare(nodes, rows):
    if any(not isinstance(n, str) or n == "" for n in nodes):
        raise ValueError("invalid node ID")
    if len(set(nodes)) != len(nodes):
        raise ValueError("duplicate node ID")
    known = set(nodes)
    ids = Counter(row["id"] for row in rows)
    accepted, rejected = [], []
    for pos, row in enumerate(rows):
        reasons = []
        if not isinstance(row["id"], str) or row["id"] == "":
            reasons.append("invalid edge ID")
        if ids[row["id"]] != 1:
            reasons.append("repeated edge ID")
        if row["src"] not in known or row["dst"] not in known:
            reasons.append("unknown endpoint")
        if reasons:
            rejected.append((pos, dict(row), reasons))
        else:
            accepted.append((pos, dict(row)))
    assert len(accepted) + len(rejected) == len(rows)
    return list(nodes), accepted, rejected

nodes = ["A", "B", "C"]
rows = [dict(id="e1", src="A", dst="B"),
        dict(id="e2", src="A", dst="B"),
        dict(id="e3", src="B", dst="B"),
        dict(id="e4", src="A", dst="Z")]
n, accepted, rejected = prepare(nodes, rows)
assert n == nodes
assert [r["id"] for _, r in accepted] == ["e1", "e2", "e3"]
assert rejected[0][0] == 3
assert rejected[0][2] == ["unknown endpoint"]
print(len(n), len(accepted), len(rejected))
```

## Decision rules
- IF the graph contract does not specify direction THEN ask before canonicalizing endpoints BECAUSE endpoint order may carry meaning.
- IF two rows share endpoints but have different edge identities THEN preserve both unless an approved aggregation rule applies BECAUSE parallel edges can represent distinct relationships.
- IF a node ID is absent from the supplied complete inventory THEN quarantine its edge row BECAUSE adding an invented node hides a reference defect.
- IF edge identity repeats THEN quarantine the whole conflicting group until resolved BECAUSE first-row selection depends on input order.
- IF the destination drops edge identities or isolated nodes THEN report the loss and block a preservation claim BECAUSE matching total counts cannot restore the missing semantics.

## Output template
```text
Scope: <snapshot, target, contract; up to 100 words>
Node output: <ID, source locator, properties, incident-edge status; attach full table>
Edge output: <edge ID, source, target, properties, source locator; attach full table>
Exceptions: <source locator, original values, reason, owner action; every rejected row>
Reconciliation: <input rows = accepted + quarantined; node inventory comparison>
Semantic checks: <direction, edge identity, parallel edges, loops, isolated nodes>
Destination evidence: <executed round-trip result or pending check>
Disposition: <ready for authorized import / blocked; next action, maximum 80 words>
```

## Quality checklist
- [ ] Direction and relationship identity are explicit.
- [ ] Original identifiers survive normalization or mapping.
- [ ] Every input edge locator appears exactly once in acceptance or quarantine.
- [ ] Repeated edge IDs are resolved or all occurrences quarantined.
- [ ] Parallel edges and self-loops follow the declared contract.
- [ ] Inventory-only nodes remain represented.
- [ ] Dangling endpoints are visible with original row evidence.
- [ ] Destination checks are distinguished from offline transformation checks.

## Anti-patterns
- **Pair deduplication**: collapse rows by endpoints. Fix: use relationship identity and approved semantics.
- **Endpoint invention**: create a node for every typo. Fix: quarantine unresolved references.
- **Edge-only node discovery**: build nodes solely from accepted edges. Fix: include the declared inventory.
- **String coercion**: merge `01` with `1`. Fix: retain exact IDs unless an approved mapping proves equivalence.
- **Count-only success**: accept matching totals despite changed endpoints. Fix: compare edge identity and mappings.

## Worked example
**Input:** Fictional workshop Juniper supplies the exact node/edge fixture in the snippet. Its directed multigraph permits parallel edges and self-loops. Inventory A/B/C is complete; Z is not authorized. No destination loader was tested.

**Output:**
```text
Scope: Juniper supplied fixture; directed multigraph; neutral tables only.
Node output: (ID, source locator, properties, incident-edge status)
  A | node:0 | {} | accepted incident edges
  B | node:1 | {} | accepted incident edges
  C | node:2 | {} | no source incident edge
Edge output: (edge ID, source, target, properties, source locator)
  e1 | A | B | {} | edge:0
  e2 | A | B | {} | edge:1
  e3 | B | B | {} | edge:2
Exceptions: row position 3, e4 A→Z; unknown endpoint Z; owner must resolve identity.
Reconciliation: 4 input edges = 3 accepted + 1 quarantined; all 3 inventory nodes retained.
Semantic checks: direction unchanged; e1/e2 remain distinct; e3 self-loop retained; C preserved.
Destination evidence: offline reference assertions pass; target round-trip pending.
Disposition: Blocked for full import until e4 is resolved or exclusion is explicitly approved.
```

**Bad output:** “Load A–B once and B–B; ignore the bad row and C.”
This drops a legitimate parallel edge, a declared node and exception evidence.

## Edge cases
- **No node inventory**: report endpoint-derived coverage only; isolated-node completeness cannot be established.
- **Undirected reciprocal rows**: do not merge until evidence establishes whether they are duplicate encodings or separate edges.
- **Target cannot represent parallel edges**: propose another representation or explicit aggregation with preserved provenance; require owner approval.
- **Missing required fields or unhashable values**: validate/quarantine before the illustrative function; its input contract expects row dictionaries with scalar IDs.

## Test case
**Input:**
> Fictional nodes are P, Q and R. Directed edges x P→Q and y P→Q are separate events; z Q→Q is allowed. Two further rows reuse edge ID t, one P→R and one Q→R. Inventory is complete. Prepare import evidence.

**Assertions:**
1. Preserves x and y as separate edges and z as a self-loop.
2. Quarantines both t rows rather than choosing one.
3. Retains R and explains its isolation follows quarantining its incident rows.
4. Reconciles five source edge rows to three accepted and two quarantined.
5. Does not claim any destination import occurred.
</skill>

<user_request>
Fictional nodes are P, Q and R. Directed edges x P→Q and y P→Q are separate events; z Q→Q is allowed. Two further rows reuse edge ID t, one P→R and one Q→R. Inventory is complete. Prepare import evidence.
</user_request>
