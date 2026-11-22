# Candidate G49: explicit-polarity assertion conflict ledger

## Decision

Pursue a bounded knowledge-graph evidence procedure that classifies each queried directed triple in one declared context as positive-only, negative-only, both/conflicted, or neither/unresolved. Keep record IDs for each polarity and make no closed-world or truth claim. This is a candidate scope, not a registered or accepted skill.

## Distinctness and nearest procedures

- GRF-018 defines relation vocabulary and licensed inverse/transitive rules. Its actual procedure and reference were inspected. It says a disabled rule is not a negative assertion and excludes contradiction solving. G49 handles *explicit* approved positive and negative source assertions under one already defined predicate; it does not define new inference rules or propagate either polarity.
- GRF-019 extracts passage-backed relationship candidates and classifies their polarity, modality, attribution and conditions. It does not reconcile multiple approved graph assertion records by exact triple, context and polarity into a conflict ledger. G49 takes reviewed records as input; raw passage interpretation remains G19's job.
- GRF-020 checks minimum and maximum distinct object counts under completeness policy. Its reference expressly does not evaluate explicit negation. G49 checks polarity collision for the same `(subject,predicate,object)` and does not evaluate min/max constraints.
- GRF-048 (draft under review) tracks alternate transitive support after one source record retraction. G49 classifies simultaneous positive and negative evidence in a frozen assertion snapshot, with no retraction or derived-fact maintenance.

Before authoring, compare the actual final versions of those neighbors and search the whole catalog for a more precise polarity-conflict skill. Reject a draft that merely relabels GRF-020's value-count violation or GRF-019's passage annotations.

## Contract and method

Input a finite node inventory, one predicate whose direction is fixed, one frozen context/snapshot ID, a complete list of reviewed assertion records `(record_ID, context_ID, subject, predicate, object, polarity)` where polarity is explicitly `positive` or `negative`, and a declared set of queried triples. Keep record IDs unique and retain excluded other-context rows in a separate ledger. Do not coerce absent, uncertain, conditional or unreviewed statements into negative assertions; request their disposition upstream. Reject unknown nodes/predicates, malformed records, reused IDs and ambiguous context identity.

For each queried triple in the selected context, collect **all** positive and negative source IDs. Classify positive-only, negative-only, both/conflicted, or neither/unresolved. A both result is an evidence conflict requiring owner review, not proof that any source is false. Neither is missing evidence, not an explicit negative. Reconcile the output against a second grouping or set-based implementation and check that every displayed source ID maps to the exact triple, context and polarity. Do not infer transitive or inverse triples, resolve source authority, delete records or claim semantic truth. If the assertion inventory is incomplete, report observed support but withhold a complete neither claim.

## Executable acceptance fixture

Fictional context `C1`, nodes A/B/C and directed predicate `linked`. Approved records: `p1` and `p2` each assert positive `(A,linked,B)`; `n1` asserts negative `(A,linked,B)`; `p3` asserts positive `(B,linked,C)`; `n2` asserts negative `(C,linked,A)`. A separate `C2` record `q1` asserts negative `(B,linked,C)` and must be excluded from C1 classification while staying visible in the exclusion ledger.

- `(A,linked,B)` is **both** with positive IDs `p1,p2` and negative ID `n1`.
- `(B,linked,C)` is **positive-only** with `p3`; C2's `q1` must not create a C1 conflict.
- `(C,linked,A)` is **negative-only** with `n2`.
- `(A,linked,C)` is **neither** despite positive A→B and B→C; no transitive rule is licensed by this task.
- A malformed string-shaped record, reused record ID, unknown endpoint, unsupported polarity and missing context contract must be rejected or held unresolved. A forged source ID or swapped polarity in the output must fail independent replay.
- With incomplete C1 coverage, the observed positive/negative IDs may be listed, but `(A,linked,C)` must be labeled unresolved coverage rather than conclusively neither.

The example is fictional and has no current platform or external-law claim. A future skill needs full SPEC structure, runnable Python 3 reference, independent review and actual `sf.py` validation before acceptance.
