---
id: GRF-001
name: graph-model-contract-design
domain: Graph Engineering Foundations
subdomain: Representation contracts
version: 1.0
description: Turn workflow evidence and required questions into an explicit graph representation contract before choosing storage or importing relationship data.
triggers: ["model this workflow as a graph", "decide graph nodes and edges", "design a graph representation contract", "should this relationship be an event node", "define edge direction and cardinality", "check whether this graph loses repeated events"]
not_for: ["finding a prerequisite cycle [SEQ-001]", "mapping dataset ancestry alone [TDS-002]", "migrating an existing pipeline schema [TDE-004]", "selecting a graph database product"]
requires: []
risk_level: medium
---

# Graph Model Contract Design

## Purpose
Translate a bounded workflow into a graph contract that preserves the facts needed for its stated questions. Specify entity and event identity, edge meaning, direction, multiplicity, properties and missing-information handling before storage choices obscure those decisions.

## Inputs to collect
1. **Questions and decisions** — name the queries users must answer and the decisions they support. Why: these determine necessary distinctions. Default: none; ask rather than modeling every available noun.
2. **Workflow examples** — obtain ordinary records plus repetitions, exceptions and corrections. Why: a single successful interaction can hide multiplicity. Default: supplied records only, with unobserved cases marked open.
3. **Identity evidence** — collect stable source keys, entity boundaries and event identifiers. Why: labels can repeat and the same participants can interact repeatedly. Default: retain source-scoped provisional identities; do not merge by name.
4. **Business constraints** — collect allowed roles, cardinalities, self-relations, direction conventions and completeness claims. Why: observed counts do not establish universal rules. Default: proposed constraints require owner confirmation.
5. **Time and change meaning** — distinguish a current state from an occurrence and an edited observation. Why: overwriting one with another can remove needed history. Default: preserve supplied observations and mark temporal semantics unresolved.
6. **Implementation context** — obtain language/runtime and target storage if selected. Why: physical support for edge properties or parallel edges must be verified. Default: conceptual contract plus the portable reference fixture; [VERIFY: current target storage documentation before implementation].

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Write a question ledger with required inputs, expected answer shape and one supplied example answer per question.
2. Identify persistent entities separately from occurrences, observations, and relationship roles in those examples.
3. Assign identity rules using source keys and scope; record what evidence would justify merging two identifiers.
4. Compare candidate representations for each relationship: a direct edge, a property, or an event node with role edges. Select using the questions and information that would be lost, not a blanket rule that every noun becomes a node.
5. Specify each node type's meaning, identity, required properties and explicit unknown values.
6. Specify each edge type's sentence meaning, permitted source and target types, and direction. Document reverse traversal separately; it does not automatically mean a reciprocal fact exists.
7. State cardinality per role and lifecycle stage. Identify whether missing edges mean a violation in a complete record or an unresolved observation in a partial record.
8. ⚠️ Define repetition semantics before deduplicating: distinguish duplicate observations of one occurrence from distinct occurrences with the same endpoints. Preserve event identity or explicitly supported parallel-edge identity when repetition matters.
9. Define property units, temporal interpretation, provenance and correction behavior for the questions that require them. Avoid creating inferred facts from a convenient representation.
10. Instantiate ordinary, repeated-event and missing-role fixtures; execute the question ledger against each representation and compare with the supplied expected answers.
11. Run contract checks against the fixtures and preserve failed examples as evidence for revision. Record implementation-dependent checks as pending until the actual target is tested.
12. Deliver the contract with rejected alternatives, evidence limitations and owner decisions; do not claim an import or migration occurred.

For a small fictional lending model, run this Python 3 reference in the available interpreter and record its version. It checks role counts and endpoint types for complete loan occurrences; it is not a general graph validator or a storage compatibility test.

```python
def violations(nodes, edges):
    roles = {"BORROWER": "Person", "ITEM": "Item"}
    errors = []
    for source, role, target in edges:
        if (source not in nodes or target not in nodes
                or nodes.get(source) != "Loan"
                or role not in roles
                or nodes.get(target) != roles.get(role)):
            errors.append(("invalid-edge", source, role, target))
    for node, kind in nodes.items():
        if kind == "Loan":
            for role in roles:
                count = sum(s == node and r == role for s, r, t in edges)
                if count != 1:
                    errors.append(("role-count", node, role, count))
    return errors

nodes = {"p": "Person", "i": "Item", "l1": "Loan", "l2": "Loan"}
edges = [("l1", "BORROWER", "p"), ("l1", "ITEM", "i"),
         ("l2", "BORROWER", "p"), ("l2", "ITEM", "i")]
assert violations(nodes, edges) == []
assert ("role-count", "l2", "ITEM", 0) in violations(nodes, edges[:-1])
assert ("role-count", "l1", "ITEM", 2) in violations(nodes, edges + [edges[1]])
assert any(e[0] == "invalid-edge"
           for e in violations(nodes, edges + [("p", "ITEM", "i")]))
print("complete, missing-role, duplicate-role and wrong-source cases passed")
```

## Decision rules
- IF repeated interactions must be counted separately THEN give occurrences distinct evidenced identities BECAUSE endpoint equality alone does not establish one event.
- IF a relationship has independently queried participants, revisions or lifecycle THEN compare an event-node model with an identified edge model BECAUSE flattening can discard queryable distinctions.
- IF a required role is absent from a complete record THEN flag a violation, but for incomplete evidence mark it unresolved BECAUSE unknown and prohibited are different states.
- IF a constraint comes only from examples THEN label it proposed BECAUSE a small sample does not establish a business invariant.
- IF the target cannot preserve the chosen multiplicity THEN redesign or select an explicitly verified encoding BECAUSE a conceptual distinction must survive storage.
- IF two source labels match without identity evidence THEN retain separate scoped identifiers BECAUSE lexical equality is not entity equivalence.

## Output template
```text
Scope: <workflow, evidence and exclusions; maximum 80 words>
Questions: <up to 6 question | expected answer shape rows>
Nodes: <type | meaning | identity | required properties/unknowns>
Edges: <type | source → target | meaning | role cardinality/completeness>
Semantics: <repetition, direction, time, provenance and correction rules; up to 8 bullets>
Fixtures: <case | expected answer | observed check or pending; up to 6 rows>
Alternatives: <rejected representation | lost information; up to 3 rows>
Open decisions: <owner | unresolved requirement | closing evidence; up to 5 rows>
```

## Quality checklist
- [ ] Every modeled distinction supports a named question or supplied constraint.
- [ ] Entity identity differs explicitly from display labels and occurrence identity.
- [ ] Every edge has endpoint types and a sentence defining direction.
- [ ] Cardinalities state the completeness and lifecycle scope where they apply.
- [ ] Repeated occurrences survive the fixture without merging by endpoint pair.
- [ ] Missing evidence is distinguished from a complete-record violation.
- [ ] Fixture answers preserve source facts without adding reciprocal or transitive claims.
- [ ] Actual executed checks and target-dependent pending checks are distinguishable.

## Anti-patterns
- **Noun collection**: turn every word into a node. Fix: test its need against the question ledger.
- **Pair deduplication**: merge repeated events by participants. Fix: preserve evidenced occurrence identifiers.
- **Direction by drawing**: let arrow layout imply meaning. Fix: define an explicit relationship sentence.
- **Sample becomes law**: impose observed degree as a universal maximum. Fix: request the controlling constraint.
- **Unknown becomes zero**: conclude no relation exists from an incomplete extract. Fix: preserve the coverage gap.

## Worked example
**Input:** Fictional depot Cedar supplies two complete loan records, l1 and l2, both involving person p and item i. The owner confirms each loan occurrence has exactly one borrower and one item. The questions are how many loan occurrences exist and which item belongs to each occurrence. No dates or return records are supplied.

**Output:**
```text
Scope: Cedar's two complete loan records; conceptual modeling only. Dates, returns and current availability excluded.
Questions: How many occurrences? → integer; which item per occurrence? → loan/item pairs.
Nodes: Person | borrower entity | source person ID | no other properties required; Item | lent entity | source item ID | none; Loan | occurrence | loan ID | none.
Edges: BORROWER | Loan → Person | this loan has this borrower | exactly one per complete loan; ITEM | Loan → Item | this loan concerns this item | exactly one per complete loan.
Semantics: l1 and l2 remain distinct despite equal participants. No reciprocal edges or current possession inferred. Corrections retain source occurrence identity and evidence.
Fixtures: supplied l1/l2 | count 2, l1/i and l2/i | reference assertions pass when executed; missing l2 item | incomplete evidence or complete-record violation depends on declared coverage | owner context required.
Alternatives: One simple Person→Item edge | loses repeated-loan count. An identified parallel-edge model could preserve it but requires target support verification.
Open decisions: storage owner | physical encoding | confirm supported multiplicity and rerun fixtures; domain owner | dates/returns if later needed | supply records and query requirements.
```

**Bad output:** “p borrowed i, so store one edge; i is currently with p.”
This loses one occurrence and invents current possession without return or time evidence.

## Edge cases
- **Three or more participants**: consider an occurrence node with named roles; verify required and optional participants independently.
- **Same item display name**: retain source-scoped IDs until identity resolution is authorized and evidenced.
- **Partial extract**: downgrade absence claims; do not enforce complete-record minima as factual conclusions.
- **Conflicting corrections**: preserve versions and route the conflict to the source owner before selecting current truth.

## Test case
**Input:**
> Fictional depot has loan records x and y for the same person and item. Each occurrence must be countable. Record y lacks its item link in an explicitly partial export. Design the model; no return evidence or database is supplied.

**Assertions:**
1. Preserves x and y as distinct occurrences using IDs or an explicitly identified-edge alternative.
2. Marks y's missing role unresolved under partial evidence rather than proving a business-rule violation.
3. Defines direction, endpoint types and role cardinality with completeness scope.
4. Infers neither current possession nor an actual database implementation.
5. Includes fixtures distinguishing repeated occurrences from duplicate observations.
