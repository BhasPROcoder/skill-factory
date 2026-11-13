# GRF-015 independent review

Reviewed by storage_review on 2026-11-14. Decision: accept for coordinator checks; no blocking finding. Only this review log was changed. No registry, skill or Git mutation was performed.

## Completeness and uniqueness

Read full GRF-015, AGENTS.md and SPEC.md. The draft contains all required sections, runnable code and complete example/test material despite the absent author log. Direct tools.sf.validate_text returned errors=[] and warnings=[]. This is direct draft validation, not registry acceptance.

Queried sf.py for TDQ-008 and GRF-014. Read TDQ-008's actual procedure and used the full GRF-014 procedure already inspected in this review session. TDQ-008 diagnoses per-key row multiplication and recommends meaning-aware repair. GRF-014 creates storage with endpoint/transaction integrity. GRF-015 instead tests a bounded graph-query tuning hypothesis against a precise edge-sequence multiset and observed access plans. It preserves legitimate parallel-path multiplicity and separates result equivalence from performance measurement. This supports selected-neighbor novelty, not an exhaustive global uniqueness proof.

## Actual execution

Extracted and executed the exact Python fence. Installed runtime observations were Python 3.14.6 and SQLite 3.50.4. Embedded assertions passed with eight sequence rows and three destinations. Observed plans:

```text
baseline plan [(3, 0, 216, 'SCAN a'), (22, 0, 53, 'SEARCH b USING AUTOMATIC PARTIAL COVERING INDEX (relation=? AND source=?)')]
candidate plan [(3, 0, 56, 'SEARCH a USING COVERING INDEX hop_lookup (source=? AND relation=?)'), (11, 0, 56, 'SEARCH b USING COVERING INDEX hop_lookup (source=? AND relation=?)')]
review independent 6-sequence fixture, wrong DISTINCT=3, filter/direction/ordering/parameter isolation/nonmutation PASS
direct validation ([], [])
```

The plan strings are observations from this run, not required output for another release. No latency benchmark was run.

Independent fixture: p/q each S-to-M link; r M-to-T link; loop M-to-M link; back M-to-S link; note M-to-U note. An independently written expected Counter contained p/r, q/r, p/loop, q/loop, p/back and q/back with their respective endpoints. Baseline and indexed candidate exactly matched those six records. Selecting note as the second relation returned only p/note and q/note. Starting at T returned no walks. A bound value resembling SQL syntax returned no rows instead of changing the query. Explicit ordering by both edge IDs and destination matched the sorted expected multiset. Source table equality showed that the tuning experiment changed no edge records. Endpoint DISTINCT produced three destination rows, proving a different contract.

All work used an in-memory disposable database. No production index, remote system or persistent user data was touched.

## Documentation and specific claims

Consulted [SQLite EXPLAIN QUERY PLAN documentation](https://www.sqlite.org/eqp.html), which explicitly warns that output format may change and describes it as plan/debugging evidence. Consulted [SQLite query planning documentation](https://www.sqlite.org/queryplanner.html) for multicolumn/covering-index interpretation. The draft correctly avoids plan-string assertions or a speedup inferred from the observed plan. The exact plan is evidence only for the installed environment.

Checked all numerical example claims by execution: two first-hop edges each combine with four permitted second-hop edges, yielding eight sequences; destinations C/B/A yield three unique endpoints. Row identity includes both edges, so parallel relationships survive. Two-edge walks may repeat nodes; the draft expressly excludes a simple-path guarantee. No current optimizer threshold, release recommendation, runtime improvement or deployment authorization is hardcoded.

## Ordinary procedural application

Input: fictional S/M/T fixture with only p/q S-to-M and r M-to-T; exact two-link walks with both edge IDs required; proposed rewrite returns DISTINCT T; no timing measurements.

```text
Contract: Fictional three-edge snapshot; S/link/link; two directed edges; row identity includes both edge IDs; order unspecified.
Baseline: Independently enumerated required rows p/r/T and q/r/T: two sequence records.
Candidate: DISTINCT destination would yield only T; changes the output meaning.
Equivalence: Rejected by explicit row-contract comparison; the indexed six-sequence reviewer fixture separately passed exact multiset checks.
Plan evidence: No plan supplied for this particular rewrite; plan appearance cannot repair the semantic mismatch.
Performance: Unmeasured; no speedup claimed.
Disposition: Rejected as an equivalent candidate.
Next action: Preserve both sequence rows; test a semantics-preserving candidate in a disposable copy before any deployment decision.
```

This satisfies the published test's four assertions. The small three-edge response is reviewer enumeration, not an invented separate database execution.

## Missing-input application

Input: “Make my graph query faster” without query, result semantics or workload.

Response: “Please provide the query, parameters and exact output/ordering contract. Does the result mean walks, simple paths, distinct endpoints or existence, and what repetition/filter rules apply? What frozen schema/data fixture, installed environment and representative workload can be tested in a disposable copy?”

Three grouped questions in one message. No index or performance claim is invented from an unspecified query.

## Edge application

Input: the reviewer fixture includes the M self-loop and M-to-S return, but the user now asks for simple paths excluding repeated nodes.

Response: the current walk query is not sufficient. Establish node/edge repetition rules and independently enumerate the permitted paths before comparing candidates. For this stated no-repeated-node contract, p/r/T and q/r/T remain, while the loop and return sequences do not. Treat that as a changed result contract, not an optimization preserving the old six-sequence answer. No modified production query or benchmark is claimed.

A changing snapshot similarly invalidates before/after equality evidence; no-match results from the edge-only reference cannot distinguish an isolated known seed from an absent identity without the node inventory. These limitations are explicit in the draft. No blocking repair identified.
