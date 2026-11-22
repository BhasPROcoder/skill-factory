# GRF-047 author evidence

## Distinctness
sf.py search for “adjacency index” found no corresponding graph skill. Actual GRF-003 reconciles an initial import artifact against source edge rows, not an already materialized bidirectional index. GRF-014 implements relational storage and verifies its persistence. GRF-015 compares query results and plans across a tuning proposal, not all index buckets against primary records. GRF-026 reconciles partition owners and replicas. GRF-024 does compare an outgoing query view in a restore workflow; G47 is narrower and operationally distinct: an index-specific full outgoing/incoming per-bucket multiset and epoch audit outside restoration, with exact missing/duplicate/misrouted/stale witnesses. This is scoped comparison, not whole-library proof.

## Execution
Reviewer found that equal blank string epochs could be mistaken for evidence. The input check now rejects empty and whitespace-only string markers while preserving valid numeric epoch markers; the embedded negative fixture tests both blank forms.

Direct sf.validate_text(text,path) returned empty errors and warnings. Embedded Python ran under observed interpreter 3.14.6; body whitespace count was 1770:
```text
adjacency epoch, direction and edge-ID witnesses checked
3.14.6
words 1770
```
Additional extracted-code tests:
```text
adjacency epoch, direction and edge-ID witnesses checked
{'stale': True, 'incoming_missing': True, 'loop_ok': True, 'epoch_only': True, 'missing_bucket': True, 'string_edge': True, 'dup_id': True}
```
Registry untouched.

## Ordinary scenario
```text
Boundary: Finch exercise F1; source epoch 7, index epoch 6; supplied A/B/I graph and complete buckets.
View contract: Directed outgoing/incoming lists; each edge ID once at its endpoint; parallel p1/p2 separate; loop in B's two direction-specific lists.
Coverage: A/B/I outgoing and incoming buckets present, including explicit empty I buckets.
Findings: out | A | p1 | duplicate | 1; out | A | p2 | missing | 1; out | B | p2 | misrouted | 1; epoch | 7 versus 6.
Checks: Source-derived lists compared with all supplied buckets; incoming view matched, outgoing did not.
Verdict: Mismatch.
Limits: Exercise extract only; no live index rebuild or performance observation.
Next action: Index owner checks build boundary and proposes an isolated rebuild, then repeats the full audit.
```

## Missing-input scenario
```text
Boundary: Source epoch and index build epoch unavailable; extraction scope unresolved.
View contract: Directed edge-ID buckets require owner confirmation.
Coverage: Incoming extract and isolated-node buckets unavailable.
Findings: No complete comparison executed.
Checks: Source-derived expectations and observed lookups pending.
Verdict: Unresolved.
Limits: Missing epochs and buckets prevent a whole-index freshness conclusion.
Next action: Index owner supplies frozen primary graph and complete outgoing/incoming buckets with epochs.
```

## Edge scenario
Fictional one-node graph has loop:A→A. One loop edge ID appears once in A outgoing and once in A incoming; both lists pass at a matching epoch. A duplicate second loop ID in either one list would be reported within that direction. Executed `loop_ok` and duplicate fixtures cover the policy.

## Claim audit
Specific claims: each directed source edge should appear once at its source outgoing bucket and once at its target incoming bucket under the declared view contract; multiset comparison detects duplicate list entries that sets hide; differing epochs preclude a same-boundary freshness pass. These are stable contract-based statements, checked by independent source-derived expectations and adversarial fixtures. Example service is fictional. Epoch numbers are fictional identifiers, not current platform facts or thresholds. No invented citations, prices, laws, current versions or statistics in the skill. Interpreter version is observed execution evidence here only. No production rebuild, concurrency, performance or crash-durability claim.

