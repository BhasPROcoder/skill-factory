# GRF-047 independent review

Reviewer `g32_reviewer`. Read SPEC, full draft and author evidence; inspected actual Procedure sections of GRF-003, GRF-014, GRF-015, GRF-024 and GRF-026. Those cover initial import, relational persistence, query-plan equivalence, restore reconciliation and partition ownership. GRF-047 specifically reconciles every outgoing and incoming materialized adjacency bucket with frozen primary edge IDs and a build epoch, reporting per-node directional discrepancies. This is scoped comparison, not whole-library uniqueness proof. Registry untouched.

## Executed evidence

Executed the full Python 3 reference under Python 3.14.6; its assertions printed `adjacency epoch, direction and edge-ID witnesses checked`. Direct fixtures passed for exact source/index parity, missing outgoing p2, duplicate outgoing p1, misrouted p2, absent-source `ghost`, missing incoming p2, epoch mismatch, a loop appearing once in each direction, and explicit empty isolate buckets. A separate 400-fixture multiset oracle randomized outgoing and incoming lists for nodes A/B/I and checked that every source-derived edge-ID deficit or excess had the correct directional node witness and count. Unknown/malformed index bucket contents, missing or extra node buckets, duplicate source edge ID, malformed source edge and unknown endpoint were rejected.

Initial draft accepted blank source and index markers (`''`, `''`) as a clean pass, contrary to its missing-marker rule. Author repaired the reference to reject blank or whitespace-only string markers. After repair I reran blank, whitespace and `None` marker tests: all rejected. Numeric zero markers with complete matching buckets passed, preserving a valid value without imposing an invented positive-threshold rule. Final `sf.validate_text` returned zero errors and warnings. The reference audits one frozen extract; it does not establish live concurrency correctness, rebuild completion or crash durability.

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

## Edge/Test scenario

```text
Boundary: Fictional one-node A graph; source and index epoch 0; complete source and bucket extracts.
View contract: Directed outgoing/incoming lists; loop:A→A appears once in each A bucket.
Coverage: A outgoing and incoming buckets present.
Findings: None.
Checks: Source-derived A outgoing=[loop] and incoming=[loop] matched observed buckets.
Verdict: Fresh for this boundary.
Limits: A second loop ID in either one bucket would be a duplicate there; no live state inferred.
Next action: Repeat full comparison after a new source or index build boundary.
```

## Verdict

All five Test case assertions pass. The worked example retains both parallel identities, separates incoming from outgoing, and reports exact missing/duplicate/misrouted findings plus epoch mismatch. Its graph and epoch labels are fictional. No changing platform promise, invented citation, performance claim or live rebuild claim appears. Recommend acceptance within the frozen complete-extract contract; no required repair remains.
