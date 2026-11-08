# Independent TBX review

Reviewer: coordinator, separate from table authors. Fictional fixtures; in-memory Python only.

Python 3.14.6

reversible-wide-long-cell-mapping SHA256 18da7e0192fb3bf9c283058a5c54c4fb02abf4d4c17c1b5547e786db77d5c98b

Embedded: reshape coordinate checks passed

## TBX001 ordinary

```text

Boundary: Fictional Fir snapshot, scalar rectangle.
Identity manifests: B,A; y,x.
Long records: [('B', 'y', ''), ('B', 'x', None), ('A', 'y', 7), ('A', 'x', 0)]
Reconstruction: [('B', {'y': '', 'x': None}), ('A', {'y': 7, 'x': 0})]
Checks: Four unique coordinates; null, empty text, zero and order retained after record reversal.
Limits: In-memory only; no serialization tested.

```

Fresh assertions PASS.

## TBX001 missing input

```text

Boundary: Fictional Fir incomplete rectangle.
Identity manifests: A; x,y.
Long records: Not emitted.
Reconstruction: nonrectangular source
Checks: Absent y rejected; not converted to null.
Limits: Request actual y cell or corrected selection; no source mutation.

```

Fresh assertions PASS.

## TBX001 duplicate masks missing

```text

Boundary: Fictional Fir corrupt four-record export preserved.
Identity manifests: A,B; p,q.
Long records: [('A', 'p', 1), ('A', 'p', 1), ('A', 'q', 2), ('B', 'p', 3)]
Reconstruction: Rejected duplicate A/p and missing B/q; request corrected export.
Checks: Separate coordinate tally finds both defects; total four is insufficient. Zero-column sidecars reconstruct two empty rows.
Limits: Constructor fails fast; complete defect inventory comes from separate tally. No aggregation.

```

Fresh assertions PASS.

paired-list-positional-expansion SHA256 a2940a627e4bde2c4a231e08b40c96c5bbb2cf8acfe482726df45539b50edcb6

Embedded: paired expansion checks passed

## TBX002 ordinary

```text

Pairing contract: Fictional Larch declares shared positions.
Children: [('P', 0, 'same', 0), ('P', 1, 'same', None), ('P', 2, None, 8)]
Empty parents: E.
Rejected parents: None.
Reconciliation: Expected 3+0=3; actual 3; both lists reconstruct, duplicates and null retain position.
Limits: No exported table; parent context remains separate.

```

Fresh assertions PASS.

## TBX002 missing input

```text

Pairing contract: Fictional Larch, S missing values field.
Children: No accepted batch.
Empty parents: Not established for S.
Rejected parents: S missing 'values'; request actual list and positional contract.
Reconciliation: Missing is not empty; no invented child or list.
Limits: KeyError is caught at caller boundary; no source mutation.

```

Fresh assertions PASS.

## TBX002 unequal and invalid batch

```text

Pairing contract: Fictional Larch Q claims positional alignment.
Children: No complete accepted batch returned.
Empty parents: E observed in input; preserved separately.
Rejected parents: Q unequal paired lengths; retain original three names and two values for correction.
Reconciliation: No truncation; explicit null list and duplicate identity also rejected in fresh checks.
Limits: Fail-fast function is not a complete defect collector. No external writes.

```

Fresh assertions PASS.

## Scope and claim review

TBX001 preserves cell-coordinate bijection and identity sidecars, distinct from TDQ008 join cardinality. TBX002 preserves paired nested positions, distinct from Cartesian joins and semantic matching. Arithmetic and concrete assertions executed above. Source snippets have explicit scalar/string-identity preconditions; no general serializer guarantee. Third skill requires separate review.
