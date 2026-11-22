# GRF-053 author evidence

## Distinctness

Read AGENTS.md, SPEC.md, GOLD example and plans/graph-g53-scope.md. Used `sf.py` search for subclass, class hierarchy, type inheritance and endpoint type. Inspected actual Procedure sections of GRF-018, GRF-001, GRF-020 and SEQ-001. GRF-018 checks one exact node class against required endpoint classes and governs relation semantics; G53 takes an already approved strict hierarchy and computes inherited endpoint eligibility with class-link witnesses and completeness-aware invalidity. GRF-001 designs representations; GRF-020 checks value counts; SEQ-001 diagnoses task prerequisite cycles, while G53's cycle rejection is only a strict-hierarchy precondition. This is a scoped comparison, not a whole-catalog uniqueness proof.

## Execution

Direct `sf.validate_text(text,path)` returned `errors [] warnings []` after final author edits; body word count by whitespace split was 1,784. The full embedded Python 3 snippet executed and printed:

```text
subtype paths, invalid and unresolved endpoints checked
```

Additional executed tests reported:

```text
extra fixtures PASS; DAGs 25 endpoint cases 6400
```

The tests rejected a strict Person→Engineer cycle, string-shaped link and assertion records, repeated class-link ID, unknown endpoint and a forged Ada subtype path using h4. A direct Person type returned the empty identity witness. For every acyclic subset of the six possible non-self class links on three classes (25 DAGs), 64 pairs of direct-type subsets and four endpoint-completeness combinations, `inspect` ran with independent closure and path replay: 6,400 endpoint cases. These small finite cases are algorithm checks, not a production benchmark.

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

## Claim audit

Specific claims are finite upward path existence, strict directed-cycle rejection, reflexive subtype eligibility and closure-based endpoint parity. The reference and 6,400 extra cases checked them. Example path arithmetic is Ada Engineer→Employee→Person (two links), Bo Employee→Person (one), and Co Organization→Entity with no Person path. Lee's incomplete typing remains unresolved. No changing external fact, invented source, standard claim, real-world truth or storage-write guarantee appears. Registry untouched; independent review required before acceptance.
