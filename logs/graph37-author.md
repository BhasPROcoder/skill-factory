# GRF-037 author evidence

## Distinctness check
The sf.py catalog search for “core” found no graph k-core entry. Actual GRF-007 procedure partitions weak/undirected connected components and explains filter boundaries; it does not apply a degree threshold. Actual GRF-013 compares two supplied community label maps and does not compute edge-based membership. Actual GRF-029 enumerates newly separated surviving pairs after one removal, not repeated degree peeling. G37 computes the maximal degree-constrained induced subgraph with a replayable removal certificate. This is a scoped comparison, not a whole-library uniqueness proof.

## Execution and validation
Reviewer found the first input check could interpret a three-character string as an edge triple. Repaired adjacency validation now requires each edge record to be an actual tuple or list of three fields; the embedded regression test rejects `peel(["a","b"], ["xab"], 1)`. This repairs input interpretation without changing the degree or peeling policy.

Embedded Python executed under observed Python 3.14.6:
```text
k-core, cascaded peeling and ledger checks passed
3.14.6
words 1595
```
Additional extracted-code assertions executed:
```text
k-core, cascaded peeling and ledger checks passed
{'empty': True, 'pair_parallel': True, 'loop_only': True, 'k_zero': True, 'tampered_round': True, 'invented_removal': True, 'negative_k': True, 'duplicate_edge': True, 'unknown_endpoint': True}
```
Direct sf.validate_text(text,path) returned empty errors and warnings. Registry untouched.

## Ordinary scenario
```text
Scope: Willow exercise W1; supplied undirected inventory A/B/C/D/E/I complete for this exercise.
Threshold and degree policy: k=2; distinct retained neighbors; parallel A/B IDs collapse for degree; E loop contributes zero neighbors.
Survivors: A, B, C.
Peeling rounds: Round 1 | E | 1; I | 0. Round 2 | D | 1.
Source exceptions: None; ab and ab2, and loop, remain in the source ledger.
Verification: Embedded reference replay and final induced-degree assertions executed for W1.
Limits: Exercise topology only; no domain community, importance or wider graph claim.
Next action: Graph owner checks any omitted links before using the W1 result in a separate analysis.
```

## Missing-input scenario
```text
Scope: Node inventory, undirected projection and threshold not supplied.
Threshold and degree policy: Pending owner choice; no default threshold or direction conversion.
Survivors: Pending.
Peeling rounds: Pending.
Source exceptions: Inventory and interpretation missing.
Verification: No peeling executed.
Limits: No complete k-core claim possible from the available information.
Next action: Owner supplies complete scoped nodes, directed/undirected interpretation and nonnegative k.
```

## Edge scenario
Fictional two-node graph has p and q as parallel A/B records, plus A self-loop. With the declared distinct-neighbor degree and k=2, both endpoints are removed in round one with degree one, and the result is empty. The records remain separate in source evidence. Executed pair-parallel and loop-only tests verify the policy; no raw-edge-degree shortcut is used.

## Claim audit
Specific claims: iterative deletion of all vertices with induced degree below k reaches a fixed point whose survivors all have degree at least k; replay of complete low-degree rounds prevents fabricated or skipped deletions; distinct-neighbor degree collapses parallel endpoint records and excludes self-neighbor loops under the explicitly chosen policy. These are stable finite graph operations, checked by the reference and adversarial fixtures. All example people/organizations are fictional. No external citations, changing rates, law, version claims or numerical statistics appear in the skill. Runtime and observed interpreter version are evidence here only. No production scale guarantee or semantic importance conclusion is made.
