# Candidate GRF-056: bounded graph walk cardinality preflight

Status: discovery card only. No skill, staging manifest or registry entry. ID provisional.

## Overlap decision

Initial idea of authorized graph traversal was rejected: sf.py search and actual GRF-052 `authorized-graph-traversal-exposure-check` already cover explicit principal node/edge grants. Do not draft that variant.

The surviving candidate addresses a different operational problem: before executing an edge-sequence graph query, count how many **distinct edge-ID walks** exist at each exact hop length under a declared source, direction and relation filter, without enumerating all walks. Return a per-length/per-endpoint count ledger, total within bound, first budget-exceeding layer and a safe query-scope decision. Counts concern walk multiplicity, not unique endpoints, simple paths, query runtime or semantic importance.

Actual nearest procedures inspected: GRF-006 computes minimum-hop reached nodes and one witness per node, which intentionally suppresses repeated walks. GRF-030 finds one accepted relation-state witness per endpoint, explicitly not every accepted walk. GRF-015 tests a two-hop SQL result multiset and query plan for equivalence, but does not propagate exact walk counts by hop to preflight result explosion across an arbitrary supplied bound. GRF-012 compares restart-walk rankings rather than counting finite edge-identity walks. The distinct mechanism is dynamic count propagation over each edge identity with a declared cap; an endpoint-only reachability card would duplicate G06.

## Required contract

Inputs: frozen node and edge inventory with unique IDs; directed source/target and relation label; exact source node; allowed relation labels; nonnegative integer maximum hop count; whether zero-hop walk is included in the requested total; integer output budget chosen by the owner. Preserve parallel edge IDs as separate transitions. Allow repeated nodes/edges because these are walks, including loops and cycles. If simple paths, endpoint DISTINCT, permissions, or relation-order automata are requested, route to another contract rather than silently adapting counts.

Algorithm: initialize one zero-hop walk at the seed, then for each length propagate integer counts across every eligible edge ID from source count to target count. Keep exact counts per endpoint and layer; sum only the layers included by contract. Compare the cumulative total with the supplied result-row budget and report the first crossing layer. Use exact integer arithmetic; stop with an explicit incomplete/capped marker if operational computation is interrupted. Verify small fixtures by independently enumerating edge-ID sequences up to the bound. A count below budget does not prove query speed or memory fitness.

## Executable fictional fixture

Fictional directed graph has nodes A,B,C,I; link edges p1:A→B, p2:A→B, q1:B→C, q2:B→C, and loop l:B→B. I is isolated. Starting at A with link filter:

- Exact length 0: A has 1 empty walk, if included.
- Exact length 1: B has 2 walks (p1,p2).
- Exact length 2: B has 2 walks (p1,l and p2,l); C has 4 walks (p1/p2 followed by q1/q2); total 6.
- Exact length 3: B has 2 walks via the loop twice; C has 4 walks via one loop and one q edge; total 6.

With zero-hop excluded and result-row budget 5, cumulative total is 2 after length 1 and 8 after length 2, so layer 2 is the first over-budget layer. I has no positive-length walks. A relation-filtered note edge must not affect counts; an incoming-direction query should give a different table. Parallel edges cannot be collapsed to one neighbor. For a cycle, finite bound gives finite count even though unrestricted walk count may be unbounded.

## Acceptance gate

Before authoring, recheck actual G06/G15/G30 and catalog for any newly accepted count skill. Build a Python 3 reference with independent small-graph edge-ID sequence enumeration, empty graph/bound 0/parallel/loop/cycle/invalid-identity/budget-boundary tests, plus ordinary/missing/adversarial outputs. Distinguish a proved count within a finite bound from an unexecuted performance prediction. Independent review is required before registry acceptance.
