# GRF-049 author evidence

## Distinctness

Read AGENTS.md, SPEC.md and the scope in plans/graph-g49-scope.md. Queried sf.py for contradiction and explicit negation. Inspected actual Procedure sections of GRF-018, GRF-019 and GRF-020. G18 governs licensed inference and warns that disabled inference is not logical negation; G19 annotates polarity from source passages but does not group reviewed graph assertions; G20 checks value-count constraints and expressly excludes explicit negation. G49 classifies approved positive/negative source records by exact triple and context, with four evidence states and an incomplete-coverage variant. It neither extracts raw text, infers new facts nor judges source truth. G48 tracks a different problem: survival of transitive facts after retraction. This is scoped comparison evidence, not a whole-catalog uniqueness proof.

## Execution

Final direct `sf.validate_text(text,path)` reported `errors [] warnings []`; body word count by whitespace split was 1,787. Embedded Python 3 executed and printed:

```text
polarity, context isolation and incomplete coverage checked
```

Additional executed negative fixtures rejected a string-shaped assertion record, repeated source ID, unknown endpoint, unsupported polarity, missing context, duplicate query, forged cross-context support ID, swapped polarity and a forged exclusion ledger. Exhaustive two-node fixture enumeration assigned one of four context/polarity states to each of four queried directed pairs and ran both complete/incomplete coverage modes: 512 cases. Each result passed the separate per-query source-record replay. Output:

```text
extra fixtures PASS; context-polarity cases 512
```

The embedded verifier scans original records afresh for every query instead of trusting the grouping dictionary. It checks exact source-ID sets, state labels and excluded other-context IDs. It does not verify that the supplied coverage assertion is true or that source polarity was semantically reviewed; those remain declared input responsibilities.

## Ordinary scenario

```text
Scope: Fictional C1 snapshot S1; directed linked; queries A/B, B/C, C/A, A/C.
Coverage: Complete for the four queries under the supplied exercise inventory.
Classification: A,linked,B | both | p1,p2 | n1; B,linked,C | positive-only | p3 | none; C,linked,A | negative-only | none | n2; A,linked,C | neither | none | none.
Other-context IDs: q1 from C2 excluded.
Replay: Exact ID/context/triple/polarity check passed.
Conflicts: A,linked,B requires source-owner review.
Limits: Fictional reviewed assertions only; no source-truth or inferred-path claim.
Next action: Ask the C1 owner to review p1,p2 and n1 together.
```

## Missing-input scenario

```text
Scope: Context identity and reviewed assertion ledger unavailable; target triple A,linked,C supplied.
Coverage: Incomplete or unknown.
Classification: A,linked,C | unresolved | no approved IDs supplied | no approved IDs supplied.
Other-context IDs: Unknown; source ledger missing.
Replay: Not run.
Conflicts: Cannot determine.
Limits: No graph evidence state can be finalized without scoped records.
Next action: Request context, frozen reviewed records and coverage statement together.
```

## Edge scenario

```text
Scope: Fictional C1 records p3 positive B,linked,C; C2 record q1 negative B,linked,C.
Coverage: Complete for the supplied C1 exercise.
Classification: B,linked,C | positive-only | p3 | none.
Other-context IDs: q1 from C2 excluded.
Replay: Exact ID/context/triple/polarity check passed.
Conflicts: None for B,linked,C in C1.
Limits: A different C1 negative record could change the status in a later snapshot.
Next action: Preserve context labels and review any later contradictory C1 record separately.
```

## Claim audit

Specific claims are finite exact record grouping, context isolation, non-inference of absent negative assertions, and source-ID replay; each was checked by code and extra fixtures. The example has two positive IDs and one negative ID for A,linked,B; a C2 negative for B,linked,C does not affect C1. With incomplete coverage, no absent triple receives a final neither label. No current rate, law, platform API, invented source or external standard claim appears. Registry untouched; independent review required before acceptance.
