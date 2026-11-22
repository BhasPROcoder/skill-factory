# GRF-038 author evidence

Read AGENTS.md, SPEC.md and GOLD example; queried sf.py for motif, triangle and wedge. Inspected actual GRF-003, GRF-006 and GRF-013 procedures. They reconcile edge import, traverse from a seed, and compare community assignments respectively. None performs a three-distinct-vertex triangle/open-wedge census with separate structural and parallel-edge identity-instance counts. This is a scoped distinction, not a whole-library uniqueness proof. No registry mutation or push.

Draft: `skills/GRF/undirected-motif-witness-census/SKILL.md`; manifest: `staging/graph_g38.json`. `sf.validate_text(text, path)` returned zero errors/warnings. Executed the full embedded Python 3 snippet: `distinct triples, parallel witnesses, loop exclusion and isolates checked`. Additional calls returned:

```text
parallel wedge A-B two IDs, B-C one ID: structural triangle=0 wedge=1; identity triangle=0 wedge=2
closed triangle A-B one ID, B-C one ID, A-C two IDs: structural triangle=1 wedge=0; identity triangle=2 wedge=0
one isolated node with no edges: all counts zero
unknown endpoint: REJECT unknown endpoint
duplicate edge ID: REJECT duplicate edge ID
string edge record: REJECT invalid edge record
```

Ordinary scenario:
```text
Scope: Fictional Grove S1; undirected complete supplied exercise; nodes A,B,C,D,I; six edge IDs.
Policy: Three distinct vertices; parallel IDs separate for instances; loop excluded.
Structural: 1 triangle triple (A,B,C); 2 open-wedge triples (A,C,D),(B,C,D).
Instances: 2 triangle combinations; 2 open-wedge combinations.
Witnesses: (A,B,C), center none, (ab1,ac,bc); (A,B,C), center none, (ab2,ac,bc); (A,C,D), center C, (ac,cd); (B,C,D), center C, (bc,cd).
Exclusions: loop.
Verification: All IDs replayed; products 2×1×1=2 and 1×1+1×1=2.
Limits: I is isolated; motif counts do not explain the relationships.
Next action: Retain this witness ledger with S1 for comparison to a later snapshot.
```

Missing-input scenario:
```text
Scope: Node count and edge count supplied, but no endpoint records or undirected projection.
Policy: Three distinct vertices and identity witnesses requested; source contract unresolved.
Structural: Not computed.
Instances: Not computed.
Witnesses: None.
Exclusions: Unknown; loop IDs not supplied.
Verification: Not run because pair buckets cannot be constructed.
Limits: Counts alone cannot establish triangles, wedges or parallel identities.
Next action: Request full node/edge records, projection and snapshot boundary together.
```

Edge scenario:
```text
Scope: Fictional three-node A,B,C extract; ab1 and ab2 join A-B; bc joins B-C; no A-C record in the supplied extract.
Policy: Three distinct vertices; parallel IDs separate; no loops.
Structural: 0 triangle triples; 1 open-wedge triple (A,B,C).
Instances: 0 triangles; 2 open-wedge combinations.
Witnesses: (A,B,C), center B, (ab1,bc); (A,B,C), center B, (ab2,bc).
Exclusions: None.
Verification: Both IDs replay; product 2×1=2.
Limits: If the extract omits an A-C edge, the wider graph may close this wedge.
Next action: Confirm inventory completeness before calling this a whole-graph census.
```

Claim audit: all numerical example counts and products were checked against executable output. General claims are finite endpoint-pair and combinatorial operations under a stated undirected multigraph policy. No changing value, external source, API version, law or statistic was asserted. Fictional examples only. Independent review required before acceptance.
