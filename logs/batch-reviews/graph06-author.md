# GRF-006 author evidence

2026-11-12. Candidate remains unregistered and requires independent review. No registry, indexes or shared progress files changed.

## Candidate comparison

Read AGENTS.md, SPEC.md, GOLD-SKILL format excerpt and controlling creation queue. Verified no prior graph_g06 manifest existed. Queried sf.py metadata for SEQ-001, TDS-002, TDS-012 and GRF-004; the latter remains an unregistered draft. Inspected actual relevant procedures, recovering truncated SEQ/TDS procedure output separately.

- TDS-002 constructs lineage evidence; it does not specify bounded hop execution or stopping certificates.
- TDS-012 lists descendants to support already authorized withdrawal actions. GRF-006 does not repeat its action planning, legal context or impact claims; it distinguishes bounded completion from exhaustion and interruption with direction/filter semantics.
- SEQ-001 discovers an active-path cycle or prerequisite order. GRF-006 returns a minimum-hop reached-node table and one predecessor witness, not a cycle/order artifact.
- GRF-004 checks explicit-root forest invariants using unrestricted reachability; it does not expose hop-bound exits, direction switching, minimum-hop distances or stateful traversal limitations.

Distinct artifact: reproducible bounded reached-node table plus concrete unseen-node boundary exits and execution/completeness states. This is a targeted comparison, not exhaustive semantic proof across the catalog.

## Public-source boundary

Parent supplied discovery URL https://github.com/ruvnet/ruflo/blob/main/plugins/ruflo-knowledge-graph/skills/kg-traverse/SKILL.md. Its pinned commit and license are not verified here; mark external adaptation pending rather than invent provenance. This draft was authored independently from the approved traversal queue and catalog gaps; no external text, code, plugin commands, ranking thresholds or product behavior was copied. Do not claim it is a licensed adaptation of that external skill. The public-source candidate remains available for a later provenance-complete comparison.

## Specific claims checked before saving

Breadth-first discovery yields minimum edge-count distances for this unweighted fixed filtered graph. Node-only visited state is insufficient when eligibility depends on path history; the skill explicitly excludes that implementation. A reached node at the depth bound does not itself prove omissions; exits must lead outside the final reached set. If bounded exploration completed with full adjacency and no such exit, the filtered reachable region is exhausted. Direction reversal changes permitted traversal, not original fact direction. All worked entities and tick-free graph fixtures are fictional. No changing platform behavior or external thresholds appear. Python 3 is the reference language; installed version below records actual execution, not a current release recommendation.

## Observed execution

Using Python 3.14.6, extracted the exact Python fence and executed its assertions. `tools.sf.validate_text` returned errors=[] and warnings=[]. Output:

```text
bounded, exhausted and zero-depth checks passed
test-case, reverse/both direction, empty-filter, returning-boundary, loop and parallel fixtures passed
negative, Boolean and noninteger bounds rejected
```

Additional tests covered the published P/Q/R test, incoming and either-direction queries, empty relation filters, a boundary with only return edges, a zero-depth self-loop, deterministic witness selection for parallel edges, and invalid depth inputs. No remote service, resource-cap implementation or all-path enumeration was tested.

Independently calculated all-pairs minimum hop distances with a Floyd-style relaxation oracle for every edge subset on three nodes including self-loops. Compared three traversal directions, three seeds and four depths against helper distances and its exit-based exhaustion signal. There were 512 * 3 * 3 * 4 = 18,432 comparisons. Observed output:

```text
Floyd distance/exhaustion comparisons passed: 18432
```

This bounded exhaustive fixture supports the helper contract; it does not prove arbitrary malformed inputs, external data completeness, stateful traversal or production scale. Independent reviewer ordinary/missing-input/edge application remains required before ingestion.
