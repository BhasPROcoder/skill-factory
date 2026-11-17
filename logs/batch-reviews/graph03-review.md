# GRF-003 independent review

Reviewer: review_graph03. Scope: existing unregistered draft, no registry changes or live graph mutation. Review performed after resumption on 2026-11-12.

## Decision

Substantively distinct and executable within its declared fixture contract. Before acceptance, expand the worked example's Node output and Edge output to include the source locators and properties/incident status requested by its own template. The abbreviated example currently promises traceability but leaves these concrete fields implicit. No algorithmic blocker found in the declared input scope.

## Neighbor comparison

Queried sf.py show for TDQ-001, TDQ-008, TDE-004, TDE-006 and TBX-001. Read the first three relevant complete procedures (TDQ-001/008 and TBX-001), plus TDE-004/006 inputs/procedures/rules. TDQ-001 diagnoses a candidate table key; TDQ-008 diagnoses joined row multiplicities; TBX-001 preserves rectangular cell coordinates. TDE-004 plans producer/consumer schema evolution and TDE-006 drafts observation/freshness contracts. GRF-003 instead emits separate node/edge inventories and a row quarantine while preserving direction, edge identity, parallel edges, loops and declared isolated nodes. These outcomes and graph-specific loss decisions are not supplied by the compared skills. This is a bounded neighbor review, not exhaustive semantic proof across the catalog.

## Executed code checks

Extracted the Python fenced block from the current draft and executed it in Python 3.14.6. Observed stdout: `3 3 1`. Its embedded assertions passed.

Additional actual executions using the extracted `prepare` function:

- Ordinary test: P/Q/R with x P-to-Q, y P-to-Q, z Q-to-Q and two t rows P-to-R/Q-to-R. Accepted positions 0/1/2 with IDs x/y/z. Quarantined positions 3/4, each reason `repeated edge ID`. All nodes remain, including R isolated after quarantine. Five input rows equal three accepted plus two quarantined.
- Exact identifiers and direction: nodes `01`, `1`, Z; edges `01`-to-`1`, `1`-to-`01`, Z-to-Z. All three accepted with original endpoints; no quarantine.
- Duplicate node fixture raised `ValueError: duplicate node ID`. Node fixtures containing None or empty string each raised `ValueError: invalid node ID`.
- Missing-field raw-function probe raised `KeyError: dst`. This is within the explicitly documented limitation: missing fields and unhashable values must be quarantined by prevalidation before calling this illustrative function. Do not advertise the snippet as a complete malformed-record parser.
- Repeated t group where first row also has unknown endpoint Z: first row retained both reasons `repeated edge ID`, `unknown endpoint`; second retained `repeated edge ID`. Neither row accepted.
- Empty node and edge lists returned three empty lists.

No target loader, exported format or database round-trip was tested. Arithmetic was recomputed by the executing assertions.

## Independent procedural scenarios

These are reviewer applications of the written procedure, not tests against a separate model service.

### Ordinary input and produced response

Input: complete P/Q/R inventory, directed graph, parallel edges/self-loops permitted, the five-row test fixture above, no destination supplied.

```text
Scope: Fictional five-row fixture; directed graph; neutral tables; snapshot-local zero-based positions.
Node output: (P,node:0,{},accepted incident edges); (Q,node:1,{},accepted incident edges); (R,node:2,{},isolated after incident rows quarantined).
Edge output: (x,P,Q,{},edge:0); (y,P,Q,{},edge:1); (z,Q,Q,{},edge:2).
Exceptions: edge:3 (t,P,R), repeated edge ID; edge:4 (t,Q,R), repeated edge ID. Owner unassigned; resolve the whole t group.
Reconciliation: 5 input rows = 3 accepted + 2 quarantined; P/Q/R all retained.
Semantic checks: Directed endpoint order preserved; x/y parallel events retained; z loop retained; R remains despite no accepted incident edge.
Destination evidence: Offline Python reference executed; no target round-trip performed.
Disposition: Blocked for full import pending t-group resolution or explicitly approved exclusion; no live import performed.
```

All five skill test assertions hold in this response.

### Missing required input and produced response

Input: only edge `e A-to-B`; no graph contract or node inventory.

Response: "Please supply (1) directed or undirected semantics and the edge identity/parallel-edge/self-loop rules, and (2) the node inventory or an explicit endpoint-creation policy. I will retain the supplied row unchanged while those are unresolved. Endpoint-derived nodes alone cannot establish isolated-node completeness; destination verification is pending."

This asks two grouped questions, preserves the source and makes no invented direction or completeness claim. No transformation is accepted before the required contract arrives.

### Edge input and produced response

Input: complete A/B inventory; undirected graph; reciprocal rows u A-to-B and v B-to-A; distinct event IDs; parallel edges allowed; target capability unknown.

Response: retain both u and v as distinct events. Obtain/declare a canonical endpoint ordering for representation only and retain each original orientation in provenance. A two-row output must retain both relationship identities; do not deduplicate reciprocal encodings based solely on endpoints. Mark destination round-trip pending and block a preservation claim for a target that cannot preserve both edges. This follows the undirected representation and parallel-edge branches without treating directionless semantics as permission to delete an event.

## Specific-claim review

The mathematical claims about identifier preservation, edge multiplicity and row partition were checked against the fixtures. Python 3 is an explicit reference-language scope; 3.14.6 above records observed execution, not a required current version. No external prices, rules, standards, legal claims or invented sources appear. Target importer behavior is deliberately a current-documentation verification step. Structural validation is separate from this review and does not justify marking the whole catalog audited.

## Repair recheck

Re-read the coordinator's changed worked example. Node output now gives each of A/B/C its `node:0`/`node:1`/`node:2` locator, empty properties and incident status. Edge output gives e1/e2/e3 the exact directed endpoints, empty properties and `edge:0`/`edge:1`/`edge:2` locators. These match the supplied fixture; e4 remains separately quarantined at position 3. The worked example now meets its concrete table template, resolving the only requested repair. Direct `tools.sf.validate_text` recheck returned errors=[], warnings=[]. No snippet change required another execution; previously executed checks remain applicable. Reviewer disposition: accept within the documented offline scope; destination loading remains untested.
