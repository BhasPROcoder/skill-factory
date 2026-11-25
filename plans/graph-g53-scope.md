# Candidate G53: strict class-hierarchy endpoint eligibility

## Decision

Pursue a bounded knowledge-graph procedure that checks whether each identified relationship assertion satisfies declared predicate endpoint classes through an **owner-approved strict subclass hierarchy**. It must return a subtype-edge witness for each eligible endpoint, an invalidity finding only when that node's type inventory is complete, and unresolved when no compatible type is observed but typing is incomplete. Do not treat this proposal as a registered or accepted skill.

## Distinctness and nearby procedures

- `sf.py` searches for `subclass` found no lexical skill; `class hierarchy` and `endpoint type` surfaced general hierarchy/typing entries but no matching graph class-inheritance validator. This is discovery evidence, not proof of whole-library uniqueness.
- GRF-018's actual procedure defines predicate endpoint classes and checks supplied assertion types. Its reference assigns one explicit class per node and compares that class **exactly** with the predicate's domain/range. It does not compute an owner-declared subtype closure, produce inheritance witnesses or distinguish incomplete type assignments from proven incompatibility. G53 takes the vocabulary as already approved and evaluates concrete inherited eligibility. It must not redefine term meanings or claim any external ontology standard.
- GRF-001 designs graph node/edge types and direction from questions but does not execute subclass-path eligibility checks on an assertion ledger.
- GRF-020 checks minimum/maximum distinct values for subject/predicate pairs, explicitly leaving other constraint kinds outside its reference. G53 checks type inheritance, not cardinality.
- SEQ-001 finds a cycle or ordering in a task-prerequisite graph. G53 may reject a cycle because this **particular declared strict-specialization contract** requires a DAG; cycle diagnosis is only a precondition, not its deliverable. The deliverable is endpoint eligibility with subtype paths and completeness-aware invalidity.

Before authoring, inspect the actual final nearest skills and reject a draft that is merely topological sorting or GRF-018 exact-type validation with new labels.

## Contract and procedure

Inputs: finite class IDs; identified directed `subclass-of` records `(record_ID, child_class, parent_class)` under a declared **strict** relation; node IDs with one or more asserted class IDs; per-node type-inventory completeness; one approved predicate with required subject/object class IDs; and identified relationship assertions `(edge_ID, subject_node, predicate, object_node)`. Freeze the snapshot and vocabulary revision. Require known IDs and endpoints, unique record IDs, and no strict hierarchy cycle. Parallel evidence for the same class link may remain separate IDs. Do not infer node identity, property values, class equivalence, disjointness or subtype semantics for a relation the owner has not declared strict.

For each node and required class, search upward from each asserted node type, counting the zero-length identity case and retaining one exact class-link ID path. A compatible path proves observed eligibility. If no compatible path exists and this node's type inventory is complete, classify that endpoint invalid for the declared constraint; if incomplete, classify it unresolved. Classify the assertion valid only when both endpoints have witnessed eligibility; invalid when at least one endpoint is proven invalid; otherwise unresolved. Preserve each assertion ID and its endpoint findings. Independently verify witness continuity and recompute subtype reachability by a separate closure method. No missing type or absent subtype link should be invented to make an assertion pass.

## Executable fictional fixture

Classes: Entity, Person, Employee, Engineer, Organization. Strict subclass records: `h1 Engineer→Employee`, `h2 Employee→Person`, `h3 Person→Entity`, `h4 Organization→Entity`. Nodes: Ada asserted Engineer (complete); Bo asserted Employee (complete); Co asserted Organization (complete); Lee has no supplied class (incomplete). Predicate `mentors` requires Person for both endpoints. Relationship records: `e1 Ada→Bo`, `e2 Co→Bo`, `e3 Ada→Lee`.

- `e1` is valid. Ada's subject witness is `Engineer --h1--> Employee --h2--> Person`; Bo's object witness is `Employee --h2--> Person`.
- `e2` is invalid because Co's complete asserted type Organization reaches Entity but has no path to Person. Bo remains eligible; report which endpoint failed rather than discarding its witness.
- `e3` is unresolved because Lee has incomplete type inventory and no observed compatible class. Do not label Lee invalid or assign Person by convenience.
- A Person→Engineer strict edge would create a directed cycle with h1 and h2; reject the strict hierarchy before assertion evaluation and return the cycle's class and record-ID witness.
- Add a second direct type `Person` for Ada and confirm identity-length subtype eligibility still passes. Inject unknown class, unknown assertion node, duplicate hierarchy record ID, malformed string-shaped record and forged h1/h2 witness; each must reject. A disconnected irrelevant class branch must not create eligibility.

The result is structural compliance with the **supplied** strict-class contract, not proof of source truth, legal compliance or conformity with an external ontology language. A full skill needs SPEC structure, runnable Python 3 reference, independent review and `sf.py` acceptance checks before counting.
