# GRF-038 independent review

Reviewer `g32_reviewer`. Read SPEC, full draft and author evidence; inspected actual Procedure sections of GRF-003, GRF-006 and GRF-013. Those handle import identity, bounded traversal and partition comparison. GRF-038 separately enumerates three-distinct-vertex triangle/open-wedge motifs and preserves both structural triples and edge-identity combinations. This is a scoped distinction, not whole-library uniqueness proof. Registry untouched.

## Executed evidence

Executed the full Python 3 reference under Python 3.14.6; its built-in assertions printed `distinct triples, parallel witnesses, loop exclusion and isolates checked`. Independently enumerated all 729 four-node undirected multigraphs where each of six unordered endpoint pairs has zero, one or two identified edges. A separate bucket-size calculation matched both structural and edge-identity counts for every graph; witness lengths equaled instance totals. Explicit loop-plus-wedge, isolated-node and empty-graph cases passed. A loop was listed as excluded and did not supply a wedge arm. Unknown endpoint, repeated edge ID, malformed string edge and repeated node ID were rejected.

The reference verifies each generated witness against original edge endpoints and checks per-triple bucket-size products. For externally tampered output, I compared a forged structural count and a witness with an invented edge ID against independently recomputed results; both were rejected by that comparison. The reference does not expose a separate submitted-certificate verifier, so this demonstrates the review procedure rather than a callable import API. `sf.validate_text` returned zero errors and warnings.

## Ordinary scenario

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

## Missing-input scenario

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

## Edge/Test scenario

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

## Verdict

All four Test case assertions pass. The worked example's structural counts, edge-identity counts and arithmetic match the executed reference; examples are fictional. No changing external fact, invented citation or production-scale claim appears. Recommend acceptance under the finite undirected snapshot and explicit multiplicity policy. No required repair found.
