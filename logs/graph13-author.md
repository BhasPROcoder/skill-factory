# GRF-013 author evidence

Authored 2026-11-13 by matching_review. Draft is held for independent review; no registry changes or acceptance claim.

## Candidate decision and actual neighbor comparison

Queried sf.py for cluster, partition, stability, robustness, sensitivity and evaluation, and showed relevant GRF/TML entries. No lexical cluster result is not itself uniqueness proof. Read the actual procedures of GRF-007, GRF-008, TAN-008 and TML-002; relevant portions were inspected despite a combined output truncation.

- GRF-007 computes a full weak-component partition of a projection and explains excluded links. GRF-008 computes strong components and condensation. Neither compares arbitrary supplied community runs using label-invariant co-membership, common assigned cohorts and pair-change witnesses.
- TAN-008 varies uncertain scalar inputs around a decision boundary. It does not reconcile differing node universes, arbitrary labels or explicit unassigned states in partition outputs.
- TML-002 evaluates baseline/candidate predictions on common held-out labels. It requires supervised score semantics; GRF-013 deliberately lacks truth labels and distinguishes output stability from domain validity.

Accepted scope for authoring: supplied hard partitions only, run manifests and projection evidence, explicit coverage/assignment-state reconciliation, overlap counts and four co-membership pair classes. Changed-pair witnesses expose why agreement changed. No new clustering/community algorithm, social grouping inference, threshold recommendation or overlapping-membership method is claimed. This is an original queue-driven procedure; no external skill or code was copied.

## Specific-claim audit before saving

Reviewed every numerical or algorithmic claim: pairs are unordered distinct nodes; the denominator is n*(n-1)/2; exactly one of four co-membership categories holds per pair. Together/separate labels depend only on equality within each run, so bijective renaming preserves counts. Explicit unassigned markers are excluded rather than interpreted as a common group. Zero pairs makes agreement undefined, not perfect. Shared-ID intersection and assigned status define the limited comparison cohort; unknown identities and omitted records remain unresolved.

Fictional Birch cohort A/B/C/D has six pairs. Old grouping AB/CD and new grouping AC/BD yield split AB/CD, joined AC/BD and separated AD/BC: both0, apart2, split2, joined2, agreement2/6. E changes from unassigned to assigned and is outside those counts. Renaming old labels alone preserves two together pairs and four apart pairs, agreement6/6. These counts were executed below. Stability is not accuracy or evidence of a real-world community. No platform defaults, current version requirement, statistical significance or universal threshold is asserted. Python3.14.6 below is only the observed execution environment.

## Actual author checks

Ran tools.sf.validate_text: errors=[], warnings=[]; body whitespace count1668. Extracted and executed the exact Python fence under Python3.14.6. Observed:

```text
relabeling, pair changes, assignment coverage and empty denominator passed
published, missing, empty, identity drift, invalid and 729 bounded label-pair cases passed
```

Additional checks:

- Published P/Q/R case: P/Q together in both, denominator1, R assigned-to-unassigned separately.
- All-unassigned and empty maps: zero pair denominator, undefined agreement.
- Different inventories: reference-only a, candidate-only c, shared b alone gives undefined pair agreement.
- Blank node ID, integer label, blank label and list-valued membership rejected with ValueError.
- Enumerated each assignment of None or two labels to three nodes for each run: 27*27=729 run pairs. Independent tuple-flag classification matched every returned count; bijective renaming of candidate labels left every count unchanged.

No community algorithm, remote service, real graph perturbation, production-scale pair count or domain-validity experiment was executed. The code verifies supplied partition arithmetic, not source run correctness. Independent ordinary/missing/edge review remains required.
