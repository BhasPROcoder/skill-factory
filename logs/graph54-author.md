# GRF-054 author evidence

## Distinctness
The scope card plans/graph-g54-scope.md compares actual GRF-016/024/047. Final comparison also inspected actual TDE-005. G16 applies one versioned patch with replay receipt; G24 reconciles restored graph state; G47 checks adjacency index buckets. TDE-005 reviews generic checkpoint versus target commit. G54's distinct artifact is a cross-system exact source-operation-to-feed delivery coverage ledger with graph object identities, parallel edges, payload conflicts, contiguous revision scan and endpoint-order hazards. This is scoped comparison, not whole-library uniqueness proof.

## Execution
Reviewer found that unavailable feed pages previously produced a definitive missing-operation finding. The implementation now labels such keys `unobserved; feed incomplete`, leaves contiguous coverage unresolved and omits a definitive checkpoint comparison. Embedded regression uses an empty partial feed to check that no `missing` finding escapes.

Direct sf.validate_text(text,path) returned empty errors and warnings. Embedded Python executed under observed 3.14.6. Repaired body whitespace count 1793:
```text
source-to-feed coverage, retry and checkpoint checks passed
3.14.6
words 1793
```
Additional extracted-code tests:
```text
source-to-feed coverage, retry and checkpoint checks passed
{'conflict': True, 'foreign': True, 'hazard': True, 'unavailable': True, 'parallel_missing': True, 'source_gap': True}
```
Reviewer follow-up: the first implementation treated unseen operations as definitely missing despite unavailable feed pages, and flagged endpoint order without a supplied nodes-first policy. It now accepts explicit `nodes_first`, suppresses definitive order hazards when pages are incomplete, labels unseen keys `unobserved; feed incomplete`, and leaves contiguous coverage unresolved. Executed regression:
```text
source-to-feed coverage, retry and checkpoint checks passed
{'complete_nodes_first_hazard': True, 'policy_false_no_hazard': True, 'partial_no_definitive_hazard': True}
```
Registry untouched.

## Ordinary scenario
```text
Scope: Fir exercise revisions 1–3; complete independent source and feed extracts; supplied checkpoint claims revision 3.
Coverage: Revisions 1–2 observed complete; first gap at revision 3.
Findings: (2,E2,e1) | duplicate attempt | offsets 12,13 identical hp; (3,E3,e2) | missing | q addition absent.
Checkpoint: Claim 3 exceeds observed coverage 2; consumer target graph remains unverified.
Checks: Per-revision source and feed keys compared; accepted attempts matched source digests through revision 2.
Replay proposal: Owner reviews bounded revision-3 delivery and consumer state before any replay.
Limits: Exercise records only; no live target-state, exactly-once or persistence claim.
```

## Missing-input scenario
```text
Scope: Source manifest supplied for revisions 1–3; one feed page unavailable; checkpoint semantics unresolved.
Coverage: Unresolved.
Findings: Visible rows can be listed, but absence from unavailable page cannot be finalized.
Checkpoint: Claim compared only after complete feed evidence and target-state policy are supplied.
Checks: Partial extract classification only; full identity comparison pending.
Replay proposal: Pending feed-page recovery and owner review.
Limits: No complete delivery or consumer-state conclusion.
```

## Edge scenario
Fictional feed delivers E2/e1 edge p before E1/nA and E1/nB node additions, yet later contains all records. Under a stated consumer node-before-edge policy, the executed fixture flags endpoint-order hazard; complete identity coverage alone does not guarantee apply order. A separate conflicting digest for E2/e1 is classified conflict rather than a harmless retry.

## Claim audit
Specific claims: exact logical keys distinguish parallel edge operations even when endpoints match; all smaller source revisions must be fully covered before a contiguous coverage frontier can advance; duplicate identical deliveries do not establish extra source commits; feed delivery does not prove target application. These are stable contract and set-comparison statements, checked in the embedded and adversarial fixtures. Fictional team, IDs, offsets and digests are clearly example data; no current platform API, law, price, invented source or statistic appears. Interpreter version is observed evidence here only. No production exactly-once or durability claim.
