# GRF-051 independent review

Reviewer `g32_reviewer`. Read the G51 scope card, SPEC, full draft and author evidence; inspected actual Procedure sections of GRF-006, GRF-015, GRF-039 and GRF-047. Those compute one fresh bounded traversal, tune a fixed query plan, compare unbounded all-pair reachability after insertion, and audit adjacency index buckets. GRF-051 adds the distinct artifact of a per-key cache disposition ledger across one identified graph edge change, preserving each query's direction, filter, hop bound and revision. This is scoped comparison, not whole-library uniqueness proof. Registry untouched.

## Executed evidence

Executed full embedded Python 3 under Python 3.14.6; its assertions printed `bounded cache contents, versions and layer checks passed`. Independent fixtures covered insertion ad changing Q1 while Q2/Q3 stay content-equal and all old keys stale, deletion bc removing C, shortcut ac reducing C's hop distance without changing membership, note-label insertion leaving link-filtered content equal, and a parallel A/B insertion leaving minimum-hop content equal. A corrupted old cached answer was classified `baseline invalid` with `refresh_ready=False`. Missing/empty filter, missing bound, bad direction and unknown seed were rejected.

Independently generated 300 finite directed graph fixtures with one add/delete change and three cached queries each. A separate layer traversal oracle compared every after answer, changed/equal disposition and stale revision flag; all passed. The snippet's second-layer verifier also checks complete before and after answers. Initial draft accepted missing or blank before revisions and could offer a refresh candidate. Author repaired it to require nonblank before, after and cached revision markers; after repair, `None`, empty and whitespace-only markers were rejected, while numeric zero/one revisions remained valid. Procedure step 2 now states the nonblank revision condition. Final `sf.validate_text` returned zero errors and warnings after a small wording trim.

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

## Edge/Test scenario

```text
Boundary: Fictional A→B→C link graph; r1 to hypothetical r2; add ac:A→C link.
Cache contract: A/out/link/depth2, minimum-hop map includes A at zero.
Ledger: Q | valid | changed, C distance 2→1 with same reached IDs | stale | r2 A0,B1,C1.
Verification: Before A0,B1,C2 and after A0,B1,C1 recomputed by queue and independent layers.
Refresh plan: Q has a verified r2 candidate; no live invalidation executed.
Limits: Structural exercise only; no backend atomicity or concurrent-change proof.
Next action: Cache owner reviews the changed distance and controls the refresh.
```

## Verdict

All four Test case assertions pass. Exact content replay and revision handling are consistent: equal content does not make an old key current. The fictional examples contain no changing factual claim or invented source. No live cache mutation or concurrency guarantee is asserted. Recommend acceptance within the frozen finite graph and complete-query-contract scope. No required repair remains.
