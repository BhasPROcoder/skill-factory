# GRF-055 author evidence

## Distinctness

Read AGENTS.md, SPEC.md, GOLD example and plans/graph-g55-scope.md. Used `sf.py` searches for temporal exclusivity, interval overlap and effective interval. Inspected actual Procedure sections of GRF-005, GRF-020, SVC-001 and TBX-003. GRF-005 reconstructs a selected edge view at one effective-time point and recorded-time cutoff; GRF-020 counts distinct objects in one selected assertion view and explicitly excludes time overlap. SVC-001 reconciles resource bookings and remedies. G55 instead sweeps a directed graph predicate for each subject, counts distinct active objects rather than parallel edge IDs, returns maximal violation windows and retains changing source-ID subsegments. This is a scoped comparison, not a whole-catalog uniqueness proof.

## Execution

Final `sf.validate_text(text,path)` reported `errors [] warnings []`; body word count by whitespace split was 1,787. The full embedded Python 3 snippet executed:

```text
distinct objects, changing witnesses and maximal windows checked
```

Additional tests reported:

```text
extra fixtures PASS; interval-object cases 3456
```

The extra fixtures confirmed complete versus incomplete status, same-object parallel evidence, touching e2/e3 intervals, and the e5 extension to `[5,9)`. They rejected string-shaped records, duplicate edge IDs, unknown endpoints, empty intervals, Boolean tick fields, unapproved functional rule, forged edge-ID evidence, a merged segment that concealed an evidence boundary, and a nonmaximal/incorrect conflict window. Exhaustively assigned three identified A edges to all valid integer subinterval/object choices within `[0,3)` and evaluated both coverage flags: 3,456 interval-object cases. Each case ran the separate rational-point source replay and exact boundary/window verifier. This small exercise is not a scale benchmark.

## Ordinary scenario

```text
Scope: Fictional C1; managedBy; A and B; integer ticks [1,12), end-exclusive.
Rule: Owner-approved at most one distinct object per subject.
Coverage: Complete for supplied C1 exercise.
Conflict windows: A | [5,8) | M1,M2; B | none.
Evidence segments: A | [1,3) | one | M1:e1; A | [3,5) | one | M1:e1,e1b; A | [5,6) | conflict | M1:e1,e1b M2:e2; A | [6,8) | conflict | M1:e1 M2:e2; A | [8,10) | one | M2:e2; A | [10,12) | one | M1:e3. B has [1,6) none, [6,9) one M2:e4, [9,12) none.
Independent check: Rational-point source replay and full [1,12) boundary coverage passed.
Limits: Fictional selected view; no date conversion, source truth or edit approval.
Next action: Owner reviews e1,e1b and e2 together before any correction.
```

## Missing-input scenario

```text
Scope: A's edge count supplied, but interval convention and at-most-one rule approval missing.
Rule: Unresolved; no assumed functional predicate.
Coverage: Unknown.
Conflict windows: Not computed.
Evidence segments: Not computed.
Independent check: Not run.
Limits: Counts alone cannot establish simultaneous distinct objects.
Next action: Request approved predicate rule, frozen edge records, comparison unit and interval convention together.
```

## Edge/Test scenario

```text
Scope: Fictional C1 A plus e5:A→M3 [7,9); same window [1,12).
Rule: Approved at most one distinct managedBy object per subject.
Coverage: Complete for supplied exercise.
Conflict windows: A | [5,9) | changing M1/M2/M3 support.
Evidence segments: [5,6) M1:e1,e1b M2:e2; [6,7) M1:e1 M2:e2; [7,8) M1:e1 M2:e2 M3:e5; [8,9) M2:e2 M3:e5.
Independent check: Rational-point replay and maximal-window check executed.
Limits: e3 starts at e2's exclusive end 10; no conflict from touching bounds.
Next action: Owner reviews all competing edge IDs before a separate source decision.
```

## Claim audit

Specific claims are finite half-open interval membership, distinct-object counting, contiguous conflict-window grouping, and source-ID evidence replay. Embedded and extra fixtures checked them. Example arithmetic: A has one active distinct object before tick 5, two on `[5,8)`, one on `[8,12)` with a value change at tick 10; the new M3 interval extends conflict to tick 9. The selected-view completeness flag is an input claim, not independently proven. No current rate, law, API, real date, invented source, universal functional rule or live-edit guarantee appears. Registry untouched; independent review required before acceptance.
