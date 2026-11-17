# Independent ARC-003 continuation

Coordinator review of the archive author's third skill. ARC-001/002 cases are in b4-arc-tests.md. These are fresh text executions, not image inspection or external factual validation.

## Case 1

Request: Fictional leaf A must have front/back. C1front, D1thumbnail of C1, C2back. No images inspected.

```text
Scope: A, both sides required; manifest only.
Expected coverage: A/front and A/back.
Correspondence:
Source-view key | Capture | Role and lineage | Selection | Evidence state
A/front | C1 | master; D1 thumbnail | C1 | mapped, visually uninspected
A/back | C2 | capture | C2 | mapped, visually uninspected
Exceptions: None in supplied mapping; thumbnail is not a third view.
Sequence checks: Proposed C1 then C2; viewer sequence untested.
Disposition: Two required views mapped from three files; no image-quality certification.
```

Result: Source-view counting, missing evidence and selection authority retained. No blocking finding.

## Case 2

Request: Fictional folder contains twenty scans with no source inventory or view policy; user asks whether complete.

```text
Scope: Supplied scan count only; no source identity inspection.
Expected coverage: Unknown.
Correspondence:
Source-view key | Capture | Role and lineage | Selection | Evidence state
unknown | twenty files | roles unknown | pending | no identity mapping
Exceptions: Unassigned sources, expected views and derivative lineage unknown.
Sequence checks: Filename order cannot establish physical order.
Disposition: Completeness unresolved; obtain item/view inventory, capture manifest and policy before counting coverage.
```

Result: Source-view counting, missing evidence and selection authority retained. No blocking finding.

## Case 3

Request: Fictional source leaf B front required; captures R and S both claim it; file S newer but no retake decision; B back absent despite both-side policy.

```text
Scope: B front/back required; manifest review.
Expected coverage: B/front; B/back.
Correspondence:
Source-view key | Capture | Role and lineage | Selection | Evidence state
B/front | R and S | competing captures | unresolved | modification time not selection evidence
B/back | none | required | none | missing
Exceptions: Front selection unresolved; back gap.
Sequence checks: Select front on supported criteria before building sequence; keep back gap visible.
Disposition: One source view represented by candidates, not complete coverage; request retake decision and missing back. No files deleted.
```

Result: Source-view counting, missing evidence and selection authority retained. No blocking finding.
