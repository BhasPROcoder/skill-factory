# GRF-008 independent review

Reviewed 2026-11-13 by g08_review_resume. Decision: complete draft; accept for coordinator ingestion and validation, with no blocking finding. Only this review log was changed; no registry status or skill mutation performed.

## Scope and neighboring procedures

Read AGENTS.md, SPEC.md, the complete GRF-008 draft and manifest, SEQ-001, and the pertinent GRF-006/007 procedures and output contracts. SEQ-001 returns one cycle witness or a prerequisite order, not the full maximal strong-component partition and inter-region provenance. GRF-006 computes bounded reachability from one seed with minimum-hop and stopping evidence. GRF-007 partitions an undirected projection and diagnoses filter boundaries; it deliberately cannot establish return reachability. GRF-008 instead returns the full mutual-reachability equivalence classes, internal/crossing edge ledgers, cyclic singleton classification and acyclic condensed view. These are distinct artifacts and decision rules. This is selected-neighbor comparison, not an exhaustive semantic proof about the whole library.

The draft has the required frontmatter and all ten sections, runnable example, fictional worked example, bad-output explanation and test case. Direct `tools.sf.validate_text` returned errors=[] and warnings=[] in this review. That is a draft check, not registry acceptance.

## Mathematical and specific-claim audit

Mutual directed reachability is an equivalence relation when a node reaches itself by a zero-edge path. Its equivalence classes are maximal strongly connected components, including isolated nodes. A component with multiple nodes necessarily contains a directed cycle. A singleton is cyclic exactly when it has a self-loop; the helper's nonempty internal-edge test is equivalent for a singleton.

Any directed cycle among distinct condensed components would provide return reachability among their members, contradicting maximality. Thus a correctly constructed condensation is acyclic. Keeping original crossing-edge IDs in one list per ordered component pair preserves parallel source evidence while presenting one summary arrow. The helper's adjacency sets collapse endpoint repetition only for reachability; original edge IDs are retained in the second pass.

The reachability-from-every-node reference is expressly limited to manageable finite inputs; no unsupported production complexity or scale claim is made. Malformed tuple shapes require prevalidation. Component labels are snapshot-local, not durable entities. Partial history or projection coverage limits maximality claims to the supplied graph. A structural order follows arrows and is not an authorized execution schedule; contraction is not a repair.

The worked fictional graph has five inventory nodes, six edges, three components, two cyclic regions and an isolated noncyclic singleton. Its internal ledger has four edge IDs and its crossing ledger has two; all six survive. No changing external platform behavior, invented citation, threshold or legal/financial/medical claim occurs. Python 3 denotes the reference language; the execution version below records the observed interpreter only.

## Actual executed checks

Extracted and ran the exact Python fenced block under Python 3.14.6. Observed output:

```text
partition, provenance, condensed order and singleton checks passed
test-case ({'W': ['W'], 'X': ['X', 'Y'], 'Z': ['Z']}, {'W': [], 'X': ['a', 'b'], 'Z': ['d']}, {('X', 'Z'): ['c']}, {'W': False, 'X': True, 'Z': True}, ['W', 'X', 'Z'])
parallel, empty, isolate, no-mutation passed
rejected duplicate node ID
rejected duplicate edge or unknown endpoint
rejected duplicate edge or unknown endpoint
rejected invalid node ID
rejected invalid edge field
512 exhaustive graph cases matched independent closure/edge/order checks
```

The published test fixture produced X/Y together, Z and W separate, a/b/d internal and c crossing, with W noncyclic and Z cyclic. Parallel one-way edges p/q from A to B remained two crossing IDs without merging A/B. Empty input returned empty structures. An isolated node was noncyclic. A deep-copy assertion confirmed the input node and edge lists were unchanged. The five rejected inputs were repeated node identity, unknown endpoint, repeated edge identity, blank node ID and blank edge ID.

Independently enumerated all 512 directed edge subsets on three nodes, including loops. A Floyd-style transitive closure oracle checked that helper membership equality exactly matched mutual reachability for every pair. Each run also checked that every original edge ID appeared exactly once in internal/crossing ledgers and that every condensed arrow respected the returned order. All assertions passed. These bounded fixtures support the reference behavior; they do not establish production-scale performance or external-data completeness.

## Independent procedural scenarios

These are reviewer applications of the written procedure, not a separate model benchmark or live database test.

### Ordinary complete snapshot

Input: fictional complete snapshot S1 with W/X/Y/Z and edges a:X->Y, b:Y->X, c:Y->Z, d:Z->Z. Arrows are supplied directed relationships, not a confirmed scheduling convention. No mutation requested.

```text
Scope: S1; directed relationship arrows; no filters; supplied complete fictional inventory.
Components: W | W | noncyclic; X | X,Y | cyclic; Z | Z | cyclic.
Internal evidence: W | none; X | a:X->Y,b:Y->X; Z | d:Z->Z. IDs locate S1 records.
Condensed edges: X | Z | c:Y->Z.
Checks: Executed reference; full partition, edge coverage and acyclic order pass. X/Y mutually reach; no reverse path from Z joins it to X/Y.
Interpretation: X precedes Z in the arrow-respecting structural order. No operational schedule or cyclic-group execution policy is established.
Limits: S1 only; no production scale, live mutation or domain repair tested.
```

All published test assertions hold, including singleton-loop detection and retained crossing evidence.

### Required information missing

Input: "Group these dependencies" with pairs A/B and B/C but no node inventory, directed meaning or coverage contract.

Response: "Please provide the node inventory and snapshot revision, including isolated nodes. What does each directed edge mean, and which relations belong in this analysis? Is that projection complete for the requested time/version? Until these are supplied, I cannot claim a complete strong-component partition or interpret pair order as direction."

This is one message with three questions and no inferred direction, invented isolated-node coverage or provisional partition promoted to a result.

### Partial one-way extract with parallel evidence

Input: fictional partial extract P1 has nodes A/B and two directed edges p:A->B, q:A->B; return-path coverage outside the extract is unknown. The user asks whether B can never return to A and whether duplicate-looking arrows can be deleted.

```text
Scope: P1 partial directed extract; supplied A/B inventory and p/q relationships only.
Components: A | A | noncyclic; B | B | noncyclic, within P1.
Internal evidence: A | none; B | none.
Condensed edges: A | B | p:A->B,q:A->B; both original IDs retained.
Checks: Executed parallel fixture; separate components, both crossing IDs and acyclic order pass for P1.
Interpretation: One summary arrow represents both supplied relationships. No return path exists in P1; unseen records could change the full-graph partition. No deletion authorized or justified by endpoint equality.
Limits: Partial coverage prevents claiming B can never reach A in the wider graph. No source changes performed.
```

The response preserves multiplicity and limits the negative reachability claim. The code returns the projected result; the procedure supplies the necessary wider-scope qualification.

## Conclusion and limits

No blocking finding. The interrupted author left a complete, mechanically valid draft with an internally consistent executable fixture. Independent execution and scenario application now supply review evidence. Coordinator must still ingest serially, validate against the registry, refresh indexes/package, and decide publication; this review makes no claim those steps occurred.
