# GRF-005 independent review

Reviewer: temporal_review, 2026-11-12. Decision: accept for coordinator ingestion and checks; no blocking finding. Only this review log was changed. No registry acceptance or live database action is claimed.

## Scope and distinctness

Read AGENTS.md, SPEC.md, the entire GRF-005 draft and actual Procedure/Decision rules sections of TDS-002, TDS-012, TBX-003 and TRP-008 after sf.py metadata lookup. TDS-002 creates artifact ancestry; TDS-012 scopes authorized withdrawal actions across descendants; TBX-003 assigns scalar values to intervals; TRP-008 captures reproducible input versions. GRF-005 instead intersects independently meaningful effective and recorded intervals per edge revision and retains active/retracted/no-match/conflict states. Its historical answer changes are attributable to revision evidence rather than silently replacing earlier knowledge. These selected neighbors do not provide that artifact. This bounded comparison does not establish exhaustive uniqueness across every catalog skill.

## Executed checks

Extracted and executed the exact Python fence from the current draft on Python 3.14.6. Observed stdout: `two-clock, correction-boundary, retraction and conflict checks passed`. Direct tools.sf.validate_text returned errors=[] and warnings=[]. This is a draft check, not registered status.

Instantiated the published test case with fixed nodes P/Q and revisions a/b/c. Actual query results:

| Effective | Recorded | Active result | Evidence |
|---:|---:|---|---|
| 6 | 7 | k, P, Q, a | active, a |
| 6 | 8 | none | retracted, c |
| 4 | 8 | none | retracted, c |
| 3 | 8 | k, P, Q, b | active, b |
| 10 | 8 | none | no-match |
| 0 | 1 | k, P, Q, a | active, a |
| 0 | 0 | none | no-match |

Added competing active revision d with effective [0,10), recorded [8,open). At (6,8), actual output was `([], {'k': ('conflict', ['c', 'd'])})`; no active winner was emitted. Empty history returned `([], {})`, which does not establish relationship absence or completeness. Duplicate revision, endpoint outside fixed inventory, empty interval and unsupported state each raised the expected ValueError. Boolean, float and string query clock inputs were rejected. A deep-copy comparison confirmed input rows were unchanged.

## Ordinary reviewer application

Fictional input: fixed nodes P/Q, complete supplied history; a asserts k for effective [0,10), recorded [1,8); b corrects active interval to [0,4), recorded [8,open); c retracts [4,10), recorded [8,open). Compare effective 6 at recorded 7 and 8. Intervals are explicitly half-open integer ticks. No database request.

```text
Query: Fictional ledger K1; effective=6, recorded=8.
Comparison: effective=6, recorded=7.
Clock contract: Integer ticks, inclusive starts and exclusive ends; open upper ends are unbounded. Fixed supplied P/Q inventory.
Active edges: None at (6,8); comparison at (6,7) contains k | P | Q | a.
Evidence: k | retracted | c at (6,8): effective 4<=6<10 and recorded 8<=8 with open end. At (6,7), k | active | a: effective 0<=6<10 and recorded 1<=7<8.
Boundary checks: Executed (6,7) selects a; (6,8) selects c; (4,8) selects c; (3,8) selects b; (10,8) no-match.
Disposition: Accepted scoped view of K1; the later retraction does not erase the earlier recorded answer.
Limits: Supplied fictional history only. No database, timestamp conversion or independent historical truth verification.
```

All four published test assertions hold. Both selection predicates were included in the evidence rather than using the interval membership result as an unexplained status.

## Missing-input reviewer application

Fictional input: "Show the graph last month" with only today's current edge table and no retained revision ledger.

Response: "Which effective-time point and recorded-time cutoff do you intend? Can you supply the versioned assertion ledger, including corrections/retractions and its retained-history coverage? What interval/timezone conventions and node membership or lifetime rules apply? Historical reconstruction is incomplete from today's table alone; I will not invent earlier recorded intervals."

This is one message with three questions, no silent current-time default, and no invented historical snapshot. The missing ledger is an actual prerequisite, not a reason to produce a current graph labeled historical.

## Conflict and partial-history reviewer applications

For the executed c/d conflict above:

```text
Query: Fictional K2; effective=6, recorded=8.
Clock contract: Supplied integer half-open intervals; fixed P/Q nodes.
Active edges: None accepted for k.
Evidence: k | conflict | c,d; both match effective 6 and recorded 8, but c retracts while d asserts active.
Boundary checks: Executed (6,8) retained both selected revision IDs and emitted no active edge.
Disposition: Blocked for k; request an evidenced source-precedence or correction decision. Revision names and input order supply no authority.
Limits: Other edges were not supplied; no live mutation or complete-world claim.
```

For a partial ledger whose retained history begins after the requested recorded cutoff, return `incomplete`, not an accepted absence finding. Even if the helper reports no-match or empty evidence, the procedure's history-coverage rule blocks reconstruction of the unavailable earlier state. Request the missing historical source or explicitly restrict the answer to the retained ledger. A selected active edge with unknown changing-node eligibility must likewise remain held; the fixed-inventory reference cannot verify dynamic lifetimes.

## Claims and limits

Reviewed two-clock selection, exclusive upper boundaries, open ends, correction/retraction evidence and competing-version handling. The executed fixtures support these claims under the explicit input convention. Numbers are fictional clock coordinates, not external rates or current thresholds. No source, law, platform version or current product capability is invented in the skill. The observed interpreter version above is execution evidence only. The helper is intentionally an offline fixed-node, integer-clock illustration; history completeness, timestamp normalization, dynamic node eligibility and storage semantics were not tested. Malformed tuple shapes fail before selection rather than producing a valid view. No blocker identified within the stated scope.
