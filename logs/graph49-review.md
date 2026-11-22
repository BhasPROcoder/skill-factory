# GRF-049 independent review

Reviewer g33_reviewer. Read scope, SPEC, full candidate and author evidence, plus actual procedures of GRF-018, GRF-019, GRF-020 and GRF-048. G18 governs inference semantics, G19 extracts passage-backed relation candidates, G20 checks value-count constraints, and G48 tracks transitive support after retraction. G49 classifies already reviewed explicit positive and negative assertions by exact directed triple and context; it performs no extraction, path inference or retraction. This is a scoped distinction, not proof against the entire catalog. Registry untouched.

## Execution evidence

Executed the embedded Python under Python 3.14.6; it printed `polarity, context isolation and incomplete coverage checked`. Built an independent per-query oracle for four source-record possibilities (none, C1 positive, C1 negative, C2 negative) across two distinct IDs and both completeness values. All 32 combinations matched the candidate's exact status, positive-ID tuple, negative-ID tuple and excluded-context tuple. Additional fixtures returned:

```text
duplicate positives p1,p2 plus negative n1 in C1: both | p1,p2 | n1; C2 q1 excluded
forged positive source ID: REJECT classification or source replay mismatch
swapped positive/negative ID lists: REJECT classification or source replay mismatch
forged empty excluded-context ledger: REJECT classification or source replay mismatch
string-shaped assertion, duplicate record ID, unknown endpoint, unsupported polarity, empty context: REJECT
```

With complete coverage the statuses are exactly both, positive-only, negative-only and neither; with incomplete coverage the same evidence yields observed-both, observed-positive, observed-negative or unresolved. The verifier rescans original rows and checks complete ID sets and excluded IDs, not just counts. The coverage flag and upstream semantic review are declared inputs; the code cannot prove either from record syntax. Neither means no reviewed assertion in this scope, never an explicit negative or a truth verdict.

## Ordinary scenario

```text
Scope: Fictional C1 S1; directed linked predicate; queries A/B, B/C, C/A, A/C.
Coverage: Complete for these four queries under the supplied exercise inventory.
Classification: A,linked,B | both | p1,p2 | n1; B,linked,C | positive-only | p3 | none; C,linked,A | negative-only | none | n2; A,linked,C | neither | none | none.
Other-context IDs: q1 from C2 excluded.
Replay: Exact ID/context/triple/polarity scan passed.
Conflicts: A,linked,B queued for source-owner review.
Limits: Fictional reviewed assertions only; no source-truth or inferred-path claim.
Next action: Ask the C1 owner to review p1,p2 and n1 together.
```

## Missing-input scenario

```text
Scope: Target A,linked,C supplied; context and reviewed ledger unavailable.
Coverage: Incomplete or unknown.
Classification: A,linked,C | unresolved | no approved IDs supplied | no approved IDs supplied.
Other-context IDs: Unknown; ledger missing.
Replay: Not run.
Conflicts: Cannot determine.
Limits: No evidence state can be finalized without scoped records.
Next action: Request selected context, frozen reviewed records and coverage statement together.
```

## Edge/Test scenario

```text
Scope: Fictional C1 p3 positive B,linked,C and C2 q1 negative B,linked,C.
Coverage: Complete for supplied C1 exercise.
Classification: B,linked,C | positive-only | p3 | none.
Other-context IDs: q1 from C2 excluded.
Replay: Exact ID/context/triple/polarity scan passed.
Conflicts: None for B,linked,C in C1.
Limits: A later C1 negative source could change status in a new snapshot.
Next action: Preserve context labels and review any later C1 contradiction separately.
```

## Verdict

Recommend acceptance for finite reviewed assertion ledgers with explicitly declared context, predicate, query list and coverage. Worked example record arithmetic and Test case assertions match execution. No invented source, changing current value, implicit inference, closed-world truth claim or unsupported winner selection found.
