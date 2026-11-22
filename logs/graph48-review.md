# GRF-048 independent review

Reviewer g33_reviewer. Read the scoped plan, SPEC, full draft and author evidence, plus actual procedures of GRF-018, GRF-005, GRF-016 and GRF-039. G18 licenses relation meaning and inference; G05 reconstructs a two-clock source view; G16 replays atomic graph patches; G39 computes directed reachability gain after adding an edge. G48 assumes an already approved transitive rule and previews retraction of one identified assertion, distinguishing genuinely lost facts from surviving facts whose selected witness became stale. This is a scoped distinction, not whole-catalog uniqueness proof. Registry untouched.

## Execution evidence

Executed the embedded Python under Python 3.14.6; it printed `retraction, alternate support, duplicate source and cycle checks passed`. Independent checks returned:

```text
G1: 9 before facts, 7 after facts; lost (B,D),(B,E); replacement witnesses for (A,D),(A,E)
G1 after paths: (A,D)=(r3,r4), (A,E)=(r3,r4,r5)
retract r1 only: (A,B) remains via r6
omit alternate r3, then retract r2: (A,D),(A,E) also lost
A↔B cycle before: (A,A),(A,B),(B,A),(B,B); retract y loses (A,A),(B,A),(B,B); (A,B) remains
forged after witness using a nonexistent ID: REJECT invalid after witness
unknown retraction ID, unapproved rule, duplicate source ID, unknown endpoint, string-shaped record: REJECT
```

I implemented a separate nonempty-walk reachability oracle and applied it to every nonempty subset of the nine possible directed arcs among three nodes and each selected source ID, totaling 2,304 retraction cases. The draft's before and after fact sets exactly matched the oracle, and lost facts equaled before minus after in every case. The independent oracle includes a self-pair only when a nonempty path closes a cycle. This confirms the loss decision depends on the complete after relation, not merely loss of an old selected path.

The fictional worked example arithmetic is consistent: the nine before facts are A,B; A,C; A,D; A,E; B,D; B,E; C,D; C,E; D,E. After r2 is removed, seven remain; the two lost facts are B,D and B,E, and the five other retained facts plus two replaced-witness facts account for all seven. The procedure's preview boundary, approved-rule requirement and source-ID identity are explicit.

## Ordinary scenario

```text
Scope: Fictional G1; five nodes, six source records, approved contains transitivity for this exercise.
Retraction: r2; preview only.
Before facts: A,B; A,C; A,D; A,E; B,D; B,E; C,D; C,E; D,E (nine).
Lost: B,D | r2; B,E | r2,r5.
Retained with replacement: A,D | r1,r2 | r3,r4; A,E | r1,r2,r5 | r3,r4,r5.
Other retained: A,B; A,C; C,D; C,E; D,E.
Verification: Independent complete closure and source-ID path replay passed.
Limits: G1 is fictional and scoped; source truth and omitted support unexamined.
Next action: Owner reviews the proposed retraction before any source change.
```

## Missing-input scenario

```text
Scope: Node inventory and rule revision unavailable.
Retraction: r2 named, but its identified source ledger absent.
Before facts: Not computed.
Lost: Unresolved.
Retained with replacement: Unresolved.
Other retained: Unresolved.
Verification: No closure or path replay executed.
Limits: Counts cannot establish complete support or transitivity approval.
Next action: Request complete identified assertions and approved rule revision.
```

## Edge/Test scenario

```text
Scope: Fictional A/B with x:A→B and y:B→A, approved transitivity and nonempty-path convention.
Retraction: y; preview only.
Before facts: A,B; B,A; A,A; B,B (four).
Lost: B,A | y; A,A | x,y; B,B | y,x.
Retained with replacement: None.
Other retained: A,B.
Verification: Independent closure and source-ID path replay passed; empty path did not prove self-facts.
Limits: Fictional two-node scope; no live deletion or wider rule-language claim.
Next action: Owner reviews y and cycle policy before a separate correction.
```

## Verdict

Recommend acceptance for complete finite identified assertion sets under an explicitly approved transitive predicate. Embedded and independent oracle results support the claims; the worked ledger is internally consistent. No invented external source, changing current value or unsupported source-truth claim found. Scale and completeness limits remain explicit.
