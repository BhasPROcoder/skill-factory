# GRF-051 author evidence

## Distinctness
Scope card plans/graph-g51-scope.md compares actual GRF-006, GRF-015, GRF-039 and GRF-047. Final check confirms G51's unique artifact is a per-key, versioned cache disposition ledger across one graph mutation. GRF-006 computes a fresh bounded traversal; GRF-039 reports unbounded all-pair gains after insertion; GRF-047 audits adjacency index buckets; GRF-015 compares query plans against a fixed graph. This is scoped comparison, not a whole-library uniqueness proof.

## Execution
Direct sf.validate_text(text,path) returned empty error and warning lists; body has 1800 whitespace-counted words. The embedded reference ran on observed Python 3.14.6:
```text
bounded cache contents, versions and layer checks passed
3.14.6
```
Additional extracted-code checks:
```text
bounded cache contents, versions and layer checks passed
{'deletion': True, 'shorter_hop': True, 'filtered': True, 'parallel': True, 'baseline_invalid': True, 'missing_bound': True, 'missing_filter': True, 'bad_revision': True}
```
Registry untouched.

## Ordinary scenario
```text
Boundary: Maple exercise; r1 to hypothetical r2; add ad:A→D with label link; A/B/C/D/I in scope.
Cache contract: Q1 A/out/link/depth2; Q2 D/out/link/depth2; Q3 C/in/link/depth1; minimum-hop maps include seed at zero.
Ledger: Q1 | valid | changed, adds D1 | stale | r2 A0,B1,C2,D1. Q2 | valid | equal | stale | r2 D0. Q3 | valid | equal | stale | r2 C0,B1.
Verification: Complete before/after query recomputation and independent layer checks executed for all three keys.
Refresh plan: Q1/Q2/Q3 have verified r2 answer candidates; no live invalidation executed.
Limits: Exercise extracts only; no backend atomicity, concurrent change or wider graph claim.
Next action: Cache owner reviews the r2 candidates and executes a separately controlled refresh.
```

## Missing-input scenario
```text
Boundary: Old and new revisions unresolved; proposed edge ID unavailable.
Cache contract: Query filter and hop bound absent for an inspected key.
Ledger: Entry unresolved; no content or revision freshness conclusion.
Verification: No complete before/after query recomputation executed.
Refresh plan: Pending exact graph and query contracts.
Limits: Missing fields prevent a safe cache decision.
Next action: Cache owner supplies revisions, edge record and full query tuple.
```

## Edge scenario
Fictional baseline A→B→C has cached A/out/link/depth2 answer A0,B1,C2. Adding A→C changes C from distance two to one although its membership is unchanged. The executed shorter_hop case classifies content changed. Deleting B→C removes C from that answer; adding an edge labeled note to isolated I leaves the link-filtered answer equal but its r1 key stale for r2.

## Claim audit
Specific claims: breadth-first traversal returns minimum hop count for finite unweighted directed edges; a shorter path can change distance without changing reached membership; a cache key bound to r1 is not an r2 key even when contents match. These are stable algorithm/contract claims, checked by independent layer expansion and adversarial cases. All example teams and revisions are fictional; no current price, law, API, version promise, invented source or statistic appears in the skill. Runtime version here is observed evidence only. No live cache mutation, atomic replacement or concurrency claim.
