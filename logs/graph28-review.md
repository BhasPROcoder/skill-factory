# GRF-028 independent review
Reviewer g27_resume, independent of author. Complete candidate, author evidence and actual G01/G03 procedures inspected; G17 procedure inspected earlier in this reviewer session. G01 decides representation; G03 preserves imported edge identity and quarantines failures; G17 applies reversible identity transformation. G28 deliberately combines occurrences into derived analysis edges while retaining contribution/exclusion ledgers. Selected-neighbor comparison supports distinctness, not a whole-library semantic guarantee.

Executed entire embedded Python with Python3.14.6 and independent checks: missing/negative/Boolean/fractional included weights reject; unauthorized direction loss rejects; duplicate edge IDs reject; unknown endpoint rejects even on filtered relation; all-filtered input retains A/B/I with all four exclusions; zero contribution remains recorded; excluded loop with missing weight remains loop-excluded rather than silently included. Directed output5/7 and approved undirected12 recomputed. Included IDs and exclusions disjointly cover source IDs exactly. Tampered sum6 disagrees with independent contribution recomputation5. sf.validate_text errors=[] warnings=[].

Conservation claim is only source accounting and approved integer sums: excluded9 does not enter output12, so no preservation of total source21 is claimed. Aggregate mapping cannot reconstruct full source properties and edge identity by itself; original graph and contribution ledger remain separate. Isolation classification and consumer suitability are procedural checks, not implemented by the snippet; procedure makes them explicit. No code defect or blocking wording defect found.

Ordinary scenario output:
```text
Contract: Fictional F1/P1; visit-count consumer; independent occurrence counts summed; directed; loops excluded; all nodes A/B/I approved.
Projection: A,B,I; A->B=5; B->A=7.
Contributions: A->B | e1=2,e2=3; B->A | e3=7.
Exclusions: e4 | relation filter.
Isolation: Originally isolated I | projection-isolated I; no newly isolated nodes.
Checks: Executed source accounting and contribution recomputation; consumer run pending.
Decision: Ready within supplied projection contract; source occurrence detail collapsed in aggregates and retained externally; no consumer-result claim.
```

Missing-contract scenario output:
```text
Contract: Source supplied; output/consumer and quantity/unit/rule unresolved; direction preserved provisionally; cohort and loop policy unapproved.
Projection: None materialized.
Contributions: Pending approved grouping and weight semantics.
Exclusions: No final exclusion decisions made.
Isolation: Pending approved cohort and filters.
Checks: No aggregate or consumer execution performed.
Decision: Blocked. What quantity/unit and aggregation are approved? Which cohort, relation filters and loop policy apply? Do reverse/parallel records represent independent occurrences for this consumer?
```

Adverse Test case output:
```text
Contract: Fictional supplied A/B/I; visit counts2/3; reverse-event equivalence unresolved; direction loss unapproved; all-node cohort subject to confirmation.
Projection: No final aggregate; preserve directed source preview only.
Contributions: e1=2,e2=3 remain named candidates; reverse record requires occurrence adjudication before final contribution grouping.
Exclusions: Every omitted record needs an explicit reason; no silent reverse-row deletion.
Isolation: I retained under confirmed all-node cohort, otherwise request cohort approval.
Checks: Accounting/recomputation required after identity adjudication; no new execution claimed for these incomplete inputs.
Decision: Blocked on occurrence identity and cohort confirmation; no undirected collapse and no false claim that missing relationship means zero.
```

All four Test case assertions satisfied. Exact output fields appear in order. Stable arithmetic, declared Python operations, fictional labels and bounded semantics only; no fabricated references, version-dependent API claims or unsupported external facts. Recommend acceptance within stated approved projection scope; no required repairs.
