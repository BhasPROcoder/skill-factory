# GRF-053 independent review

Reviewer `g32_reviewer`. Read SPEC, full draft, author log and G53 scope card; inspected actual Procedure sections of GRF-018, GRF-001, GRF-020 and SEQ-001. GRF-018 governs vocabulary and exact endpoint constraints, GRF-001 designs representation, GRF-020 checks value cardinality, and SEQ-001 finds prerequisite cycles. GRF-053 takes an already approved strict hierarchy and computes completeness-aware inherited endpoint eligibility with replayable class-link IDs. This is scoped comparison evidence, not whole-library uniqueness proof. Registry untouched.

## Executed evidence

Executed the complete embedded Python 3 reference under Python 3.14.6; its assertions printed `subtype paths, invalid and unresolved endpoints checked`. Independently enumerated all acyclic subsets of the six nonself directed links among three classes. Across all direct-type subsets for two nodes and both completeness flags, a separate reflexive-transitive closure oracle checked 6,400 endpoint cases. Every endpoint state and assertion status agreed. A strict Person→Engineer addition and a self-link were rejected as cycles. The verifier rejected a forged Ada subtype witness using h4, which starts at Organization rather than Engineer. String-shaped class link and assertion rows, repeated link ID, unknown type, unknown assertion endpoint, unknown class, duplicate class and missing completeness flag were rejected. A direct type equal to the required class produces an empty identity path; the reference's zero-link case is covered by the exhaustive oracle. `sf.validate_text` returned zero errors and warnings.

## Ordinary scenario

```text
Scope: Fictional C1; approved strict subclass links h1–h4; fixed vocabulary revision for this exercise.
Hierarchy: Valid DAG; no cycle in supplied links.
Predicate contract: mentors | Person | Person.
Assertions: e1 | valid | Ada eligible Engineer h1,h2 | Bo eligible Employee h2; e2 | invalid | Co invalid Organization no Person path | Bo eligible Employee h2; e3 | unresolved | Ada eligible Engineer h1,h2 | Lee unresolved no supplied type.
Independent checks: Closure parity and subtype path replay passed.
Coverage: Lee incomplete; Ada, Bo, Co complete.
Limits: Fictional supplied types only; no source truth or external ontology claim.
Next action: Owner reviews e2 and requests Lee's type evidence before deciding e3.
```

## Missing-input scenario

```text
Scope: Strict-specialization meaning and vocabulary revision not approved.
Hierarchy: Unresolved; no cycle or subtype computation run.
Predicate contract: mentors endpoint classes not established.
Assertions: No eligibility verdict.
Independent checks: Pending declared classes, links, typing and predicate roles.
Coverage: Unknown for all nodes.
Limits: Class labels alone do not license inheritance.
Next action: Request strict-hierarchy declaration, predicate roles and frozen records together.
```

## Edge/Test scenario

```text
Scope: Fictional C1 plus new h5 Person→Engineer strict link.
Hierarchy: Rejected cycle Engineer --h1--> Employee --h2--> Person --h5--> Engineer.
Predicate contract: mentors | Person | Person; not evaluated on cyclic hierarchy.
Assertions: e1/e2/e3 held pending hierarchy correction.
Independent checks: Cycle path uses h1,h2,h5; no endpoint eligibility issued.
Coverage: Existing node flags retained but not applied.
Limits: Rejection follows the owner's strict-specialization contract; no external ontology claim.
Next action: Class-link owners review h5 before a separate corrected preview.
```

## Verdict

All four Test case assertions pass. Ada's two-link Engineer→Employee→Person path and Bo's one-link path match source IDs; Co's Organization→Entity branch does not reach Person, and Lee remains unresolved under incomplete typing. Fictional examples are internally consistent. No external ontology standard, changing factual claim or invented citation is asserted. Recommend acceptance within the owner-declared strict-class DAG and supplied typing-completeness scope. No required repair found.
