# GRF-005 author evidence

Candidate: graph-two-clock-snapshot-reconstruction. Author scope: skill folder and staging/graph_g05.json only; no registry ingestion or status marking. Requires independent review before acceptance.

## Distinctness comparison performed before authoring

Used sf.py show for TDS-002/TDS-012 and lexical searches for temporal, graph, history, snapshot and interval. Read TDS-002 and TDS-012 in full (recovered the latter's final sections after a combined output truncation), GRF-001 and GRF-002, and the existing GRF-003 import draft from earlier review. Read TBX-003 fully and TRP-008 through its procedure/rules.

- TDS-002 supplies parent-to-derivative provenance and unresolved ancestry, not a historical edge view selected by two clocks.
- TDS-012 traverses authorized withdrawal impacts and records action states; it does not reconstruct assertions known at past cutoffs.
- GRF-001 asks the owner to define temporal meaning as part of a graph contract. Its runnable procedure is occurrence/role modeling, without temporal interval selection or retraction evidence.
- GRF-002 assesses identity merging and preserves historical identity context; GRF-003 reconciles a supplied edge snapshot. Neither reconstructs that snapshot from correction history.
- TBX-003 assigns scalar observations to ranges and preserves multiple memberships. GRF-005 instead requires the intersection of two independently meaningful intervals per revision, stable relationship identity, explicit retractions, and exclusion of later corrections from earlier knowledge states.
- TRP-008 captures versioned data for reproducibility; it does not interpret effective time separately from record availability.

The proposed artifact is an active edge table plus revision/retraction/conflict evidence at an explicit pair of clock coordinates. Novelty is scoped to these reviewed neighbors, not an unsupported exhaustive claim about every catalog skill. The node inventory is deliberately fixed in the reference; dynamic endpoint lifetime validation remains explicit additional work.

## Specific claims reviewed before saving

All mathematical selection claims follow the stated fixture contract: starts included, ends excluded; None explicitly means unbounded upper end; an edge must match both query coordinates. These conventions are inputs, not universal defaults. Later-recorded corrections cannot appear in earlier recorded cutoffs under this contract. Retractions are retained evidence rather than proof of universal absence. Multiple matching revisions are conflicts without invented precedence. Clock conversion, history completeness, source precedence and storage behavior are not asserted as verified facts. Fictional tick values are internally consistent; actual executions below check the boundaries.

Consulted the official [MariaDB bitemporal tables documentation](https://mariadb.com/docs/server/reference/sql-structure/temporal-tables/bitemporal-tables) to verify the broad two-time-dimension distinction. The skill uses no database syntax or product/version support claim and copies no examples. All operational code is an original plain-Python fixture. Version 3.14.6 below is an observed interpreter, not a universal requirement or current-version recommendation.

## Actual checks

Ran tools.sf.validate_text against the draft: errors=[], warnings=[]. A simple whitespace count reported 1,751 body words; the structural checker passed its own limits.

Extracted and executed the Python code fence using Python 3.14.6. Stdout: `two-clock, correction-boundary, retraction and conflict checks passed`.

Additional executed results:

| Effective, recorded | Result |
|---|---|
| 7,4 | e active, r1 |
| 7,6 | e retracted, r3; no active edges |
| 3,6 | e active, r2 |
| 9,6 | e no-match |
| 5,6 | e retracted, r3 |
| 1,2 | e active, r1 |
| 1,1 | e no-match |

The independently instantiated Test case fixture returned k/a active at (6,7), and k/c retracted at (6,8), matching assertions. Duplicate revision, zero-length effective interval and unknown endpoint fixtures each raised the expected ValueError. Empty history returned no edges/evidence; the instructions forbid interpreting this as proven completeness or absence.

No timestamp library, target database, external import, dynamic node lifetimes or live mutation was tested. No author check substitutes for independent scenario review.
