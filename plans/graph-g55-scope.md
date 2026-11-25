# Candidate G55: time-window functional relationship conflict

## Decision

Pursue a bounded graph-constraint procedure that sweeps effective-time intervals for one subject/predicate and identifies maximal windows where **more than one distinct object** is simultaneously active under an owner-declared at-most-one rule. Retain every supporting edge ID, including duplicate records for the same object. This is a scope proposal, not a registered or accepted skill.

## Distinctness and nearest procedures

- GRF-005's actual procedure reconstructs an active identified-edge view at one effective-time point and recorded-time cutoff, resolving competing revisions of the **same edge ID**. G55 consumes an already selected revision view and checks a declared cross-edge relationship rule over an entire effective-time window. It must not repeat two-clock selection or treat a correction as a second logical relationship.
- GRF-020's actual procedure compares distinct object counts with min/max constraints in an already selected assertion snapshot. Its reference explicitly excludes time overlap. G55 computes the exact intervals during which the distinct-object count exceeds one; it is not a point-in-time count with timestamps added to output.
- SVC-001 reconciles overlapping bookings for shared room/operator resources and proposed appointment remedies. Its actual procedure was inspected. G55 instead groups graph edges by `(subject,predicate)`, collapses parallel records for the same object **only for the constraint count**, preserves all edge-ID evidence, and returns a segmented validity ledger for a functional relationship. It does not schedule or approve a resource reassignment. If the eventual draft is merely pairwise interval overlap without distinct-object grouping and maximal conflict windows, reject it as a renamed occupancy skill.
- TBX-003 checks numeric observation membership in supplied ranges; it neither computes active graph relationship values nor functional-rule violations.

Catalog searches for `temporal exclusivity`, `interval overlap` and `effective interval` surfaced those neighbors but no matching graph procedure. This is scoped discovery evidence, not a whole-library uniqueness guarantee.

## Contract and method

Input one frozen selected source revision, known subject/object IDs, one directed predicate, owner-approved at-most-one-distinct-object rule, and identified active assertions `(edge_ID, subject, predicate, object, effective_start, effective_end)` using one explicitly approved comparison unit and half-open `[start,end)` intervals. Require finite integer boundaries in the reference; do not silently parse dates, convert zones or infer missing endpoints. `effective_end` must be greater than `effective_start`. The selected source population and interval coverage must be declared complete before certifying absence of conflict. Keep different subjects and predicates in separate groups. Preserve parallel edge IDs to the same object in the witness ledger while counting that object once.

For each `(subject,predicate)` group, collect interval boundaries and evaluate the active distinct-object set on each consecutive elementary segment. Group adjacent violating segments into **maximal contiguous conflict windows**, while retaining each subsegment's active object and edge-ID evidence; keep an independent point-probe or pairwise interval oracle to check the sweep. At touching boundaries, the ending interval is inactive and the starting interval active. If coverage is incomplete, report observed conflicts but do not certify conflict-free windows or exclusivity over omitted source records. Do not delete edges, choose a winning object or claim that the declared constraint is a universal graph standard.

## Executable fictional fixture

Fictional context C1, subject A, predicate `managedBy`, object IDs M1/M2. Active records: `e1 A→M1 [1,8)`, `e1b A→M1 [3,6)` (parallel same-object evidence), `e2 A→M2 [5,10)`, `e3 A→M1 [10,12)` (touches e2 at 10), and `e4 B→M2 [6,9)` for a different subject. The owner declares at most one distinct `managedBy` object per subject at any effective instant, and C1 coverage is complete for `[1,12)`.

- A has one distinct object M1 on `[1,5)`, two M1/M2 on `[5,8)`, one M2 on `[8,10)`, and one M1 on `[10,12)`. The **only** A conflict window is `[5,8)`. At `[5,6)`, its witness IDs are e1/e1b/e2; at `[6,8)`, e1/e2. Preserve these evidence changes while reporting the one maximal conflict window.
- e1b must not turn `[3,5)` into a conflict because it supports the same object M1. e3 does not overlap e2 at their shared endpoint 10 under `[start,end)`.
- e4 does not affect A; B is evaluated separately. Inject a new A→M3 interval `[7,9)` and require the conflict window to extend to `[5,9)` with correctly segmented object/edge witnesses.
- Reject duplicate edge ID, unknown endpoint, reversed/equal bounds, malformed string-shaped record, unsupported interval convention and undeclared at-most-one rule. Under incomplete coverage, retain established observed `[5,8)` conflict but label any apparent conflict-free interval unresolved rather than certified.

The numbers are fictional integer exercise ticks; no live platform, law, date or source claim is embedded. A full skill needs SPEC structure, runnable Python 3 reference, independent review and `sf.py` acceptance checks before counting.
