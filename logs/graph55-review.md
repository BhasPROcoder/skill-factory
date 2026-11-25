# GRF-055 independent review

Reviewer `g32_reviewer`. Read G55 scope, SPEC, full draft and author evidence; inspected actual Procedure sections of GRF-005, GRF-020, SVC-001 and TBX-003. GRF-005 selects one two-clock edge view, GRF-020 checks distinct values at one selected view, SVC-001 reconciles booking resource occupancy, and TBX-003 assigns numeric observations to ranges. GRF-055 sweeps an already selected graph-predicate view over effective-time intervals, counts distinct active objects per subject and returns maximal conflict windows with changing edge-ID evidence. This is scoped comparison evidence, not whole-library uniqueness proof. Registry untouched.

## Executed evidence

Executed complete embedded Python 3 under Python 3.14.6; its assertions printed `distinct objects, changing witnesses and maximal windows checked`. The base fictional fixture returned A conflict `[5,8)` and no B conflict; adding e5 A→M3 `[7,9)` extended A to `[5,9)`. Parallel e1/e1b records for M1 were both retained as evidence but counted as one object. The e2 `[5,10)` and e3 `[10,12)` intervals only touch at 10 and do not overlap under the declared end-exclusive convention. With incomplete coverage the observed conflict remains, while one/none segments are provisional.

Independently generated 500 finite interval fixtures across two subjects, three possible objects, parallel identities, windows clipped to `[0,6)` and both coverage flags. A separate per-integer-tick oracle compared every elementary segment's exact object-to-edge-ID buckets and status; all matched. The standalone verifier rejected a forged edge ID, a nonmaximal conflict window and a merged segment concealing an evidence boundary. Malformed string-shaped record, duplicate edge ID, unknown endpoint, empty interval, Boolean tick, unknown subject and unapproved rule were rejected. Final `sf.validate_text` returned zero errors and warnings.

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

## Verdict

All four Test case assertions pass. The fictional example's interval arithmetic, same-object parallel treatment, touching bounds and changing witnesses match execution. The selected view's completeness and at-most-one rule are supplied owner claims, not presumed universal facts. No changing current value, invented source or live edit promise appears. Recommend acceptance within the declared integer-tick half-open contract. No required repair found.
