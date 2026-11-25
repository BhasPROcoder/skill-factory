# GRF-048 author evidence

## Distinctness

Read AGENTS.md, SPEC.md and the full GRF-018 inference-contract candidate, plus actual Procedure sections of GRF-005, GRF-016, GRF-020, GRF-021 and GRF-039. GRF-018 governs relation meaning and derives facts but stores only one witness per triple; GRF-005 reconstructs an assertion snapshot by two clocks; GRF-016 applies atomic source patches; GRF-039 adds one directed edge and reports gained reachability. G48 freezes an approved transitive rule and retracts one identified assertion, then distinguishes actual fact loss from stale selected witnesses by finding alternate source-ID support. See plans/graph-g48-scope.md. This is a scoped comparison, not proof of whole-catalog uniqueness.

## Execution

Final `sf.validate_text(text,path)` returned `errors [] warnings []`. Body word count by whitespace split was 1,761. The complete embedded Python 3 reference executed and printed:

```text
retraction, alternate support, duplicate source and cycle checks passed
before 9 after 7 lost [('B', 'D'), ('B', 'E')] replaced [('A', 'D'), ('A', 'E')]
```

Additional executed tests reported:

```text
extra fixtures PASS; exhaustive three-node retractions 2304
```

The extra tests covered r1-only retraction retaining A,B via r6; removal of r3 from the input followed by r2 retraction causing A,D and A,E to be lost; forged after witness containing r2 rejected; unknown retraction ID, unapproved rule, duplicate source ID, unknown endpoint, string-shaped assertion and string-shaped node or assertion inventories rejected. For every nonempty subset of the nine possible directed arcs on three nodes and every selected source ID in that subset, the preview independently compared fact sets by closure and replayed source-ID paths: 2,304 retraction cases completed. This is a small finite oracle, not a scale benchmark.

## Ordinary scenario

```text
Scope: Fictional G1; five nodes and six source records; approved contains transitivity for this exercise.
Retraction: r2; preview only.
Before facts: Nine distinct facts.
Lost: B,D | r2; B,E | r2,r5.
Retained with replacement: A,D | r1,r2 | r3,r4; A,E | r1,r2,r5 | r3,r4,r5.
Other retained: A,B; A,C; C,D; C,E; D,E.
Verification: Independent closure and source-ID path replay passed.
Limits: G1 is fictional and scoped; source truth and wider omitted support unexamined.
Next action: Owner reviews the proposed retraction before any source change.
```

## Missing-input scenario

```text
Scope: Node inventory and rule revision unavailable.
Retraction: Record r2 named, but source ledger not supplied.
Before facts: Not computed.
Lost: Unresolved.
Retained with replacement: Unresolved.
Other retained: Unresolved.
Verification: No closure or path replay executed.
Limits: Record counts do not prove complete support or transitivity permission.
Next action: Request complete identified assertions and approved rule revision.
```

## Edge scenario

```text
Scope: Fictional two-node A/B cycle with x:A→B, y:B→A and approved transitivity.
Retraction: y; preview only.
Before facts: A,B; B,A; A,A; B,B.
Lost: B,A | y; A,A | x,y; B,B | y,x.
Retained with replacement: None.
Other retained: A,B.
Verification: Independent closure and path replay passed; empty path did not establish self-facts.
Limits: Nonempty-path convention; fictional exercise only.
Next action: Owner checks source y and cycle policy before a separate correction.
```

## Claim audit

Specific claims are finite directed transitive closure, nonempty cycle support for self-facts, and source-ID path replay; these were checked in the reference and extra fixtures. Example arithmetic is nine before facts, seven after facts and two lost facts. The full direct source ledger is retained; the skill does not claim truth, a live deletion, arbitrary rule-language support, completeness beyond supplied input or production performance. No external source, changing rate, standard/version assertion or invented citation appears. Registry untouched; independent review still required.
