---
id: GRF-020
name: knowledge-graph-constraint-witness-review
domain: Graph Engineering Foundations
subdomain: Knowledge constraint diagnostics
version: 1.0
description: Diagnose declared knowledge graph value constraints with supporting assertion witnesses and completeness-aware absence findings when reviewing a scoped graph snapshot or proposed repair.
triggers: ["find knowledge graph constraint conflicts", "show evidence for graph violations", "check required graph relationships", "review graph constraint repairs", "distinguish missing relations from missing data"]
not_for: ["validating a parent forest [GRF-004]", "defining inference licenses [GRF-018]", "extracting relation candidates from text [GRF-019]", "deciding entity merges [GRF-002]", "implementing a general ontology reasoner"]
requires: []
risk_level: medium
---

# Knowledge Graph Constraint Witness Review

## Purpose
Evaluate a frozen assertion snapshot against explicitly supplied value constraints and return evidence for each failure. Separate violations witnessed by present records from missing-value findings that depend on completeness. Preserve source evidence while comparing proposed repairs; conformance alone does not establish real-world truth.

## Inputs to collect
1. **Snapshot and scope** — collect revision, node inventory, selected context and structured assertions. Why: records from different contexts can create artificial conflicts. Default: no verdict until the selected scope is explicit.
2. **Constraint contract** — obtain target subjects, predicates, permitted value counts and owner. Why: the validator must not invent cardinality from typical practice. Default: unresolved constraints; request the contract.
3. **Identity semantics** — establish whether distinct endpoint IDs count as distinct values. Why: maximum-value findings depend on the chosen identity model. Default: preserve supplied scoped IDs and declare counting by exact ID; unresolved intended semantics block final approval.
4. **Completeness evidence** — identify which subject/predicate pairs have a complete value inventory. Why: absence in an extract need not mean absence in the graph. Default: incomplete for every pair.
5. **Assertion provenance** — obtain unique record IDs and source or derivation references. Why: findings must point back to evidence. Default: unsupported records remain input exceptions rather than trusted facts.
6. **Repair alternatives** — collect proposed changes, supporting evidence and decision owners. Why: removing a conflicting value is a domain decision. Default: diagnostic report only, with all original records retained.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the selected context, snapshot revision, constraint revision and identity convention.
2. Check record identities, known endpoints and provenance references before evaluating constraints.
3. Materialize the exact assertion view to inspect, retaining direct records and derivation support separately.
4. Enumerate every targeted subject/predicate pair, including pairs with no records.
5. Group records by distinct endpoint ID while preserving every record supporting each value.
6. Compare present distinct values with the supplied maximum and return all supporting record IDs when it is exceeded.
7. ⚠️ Compare present values with the minimum only after checking completeness: label a shortfall unresolved when coverage is incomplete, instead of inventing a missing relationship.
8. Report passing observed bounds separately from complete conformance; additional unseen values could still break a maximum.
9. Attach proposed repair alternatives to their source evidence and owner decisions, retaining the original assertion ledger.
10. Recompute affected derived views and rerun all declared constraints on a separate repaired preview; record execution as pending when no preview was evaluated.
11. Deliver the witness ledger, unresolved coverage questions and preview results without claiming deployment or truth verification.

This Python 3 reference checks minimum and maximum distinct values for explicit subject/predicate targets in one already selected context. Record the installed interpreter version when running it. It does not evaluate disjoint classes, explicit negation, time overlap or inference validity; those require separately specified checks. Record IDs, node IDs and predicates are nonempty strings; validate those shapes before calling. Assertions are `(record_ID, subject, predicate, object)`. Constraints are `(subject, predicate, minimum, maximum)`, where maximum may be `None`.

```python
def check_values(nodes, records, constraints, complete):
    known = set(nodes)
    if len(known) != len(nodes):
        raise ValueError("duplicate node identity")
    if len({r[0] for r in records}) != len(records):
        raise ValueError("duplicate record identity")
    if any(s not in known or o not in known for _, s, p, o in records):
        raise ValueError("unknown endpoint")
    keys = [(s, p) for s, p, lo, hi in constraints]
    if len(set(keys)) != len(keys) or not set(complete) <= set(keys):
        raise ValueError("duplicate target or undeclared coverage")
    result = []
    for s, p, lo, hi in constraints:
        if s not in known or type(lo) is not int or lo < 0:
            raise ValueError("invalid minimum or subject")
        if hi is not None and (type(hi) is not int or hi < lo):
            raise ValueError("invalid maximum")
        rows = [(rid, o) for rid, a, q, o in records if (a, q) == (s, p)]
        values = sorted({o for rid, o in rows})
        covered = (s, p) in complete
        if hi is not None and len(values) > hi:
            state = "maximum violation"
        elif len(values) < lo:
            state = "minimum violation" if covered else "unresolved minimum"
        else:
            state = "conforms" if covered else "observed bounds only"
        result.append((s, p, state, values, sorted(rid for rid, o in rows)))
    return result

nodes = ["A", "B", "C"]
records = [("r1", "A", "owner", "B"), ("r2", "A", "owner", "B"),
           ("r3", "A", "owner", "C")]
constraints = [("A", "owner", 1, 1), ("B", "owner", 1, 1)]
out = check_values(nodes, records, constraints, {("A", "owner")})
assert out[0] == ("A", "owner", "maximum violation", ["B", "C"],
                  ["r1", "r2", "r3"])
assert out[1][2] == "unresolved minimum"
assert check_values(nodes, records[:2], constraints[:1],
                    {("A", "owner")})[0][2] == "conforms"
print("distinct values, retained evidence and incomplete absence checked")
```

The reported record set is a sufficient witness, not necessarily a smallest explanation. Several records can support the same value, so deleting one record might leave the violation intact. Before accepting supplied completeness evidence, check that its version and selection match the actual assertion view. Treat extracted candidates awaiting semantic review as separate inputs rather than silently including them in the accepted assertion view.

## Decision rules
- IF present distinct values exceed a maximum THEN report a witnessed violation BECAUSE those records already exceed the declared bound.
- IF a minimum is unmet without complete coverage THEN return unresolved absence BECAUSE unseen records may satisfy it.
- IF observed counts fit but coverage is incomplete THEN report observed bounds only BECAUSE unseen values may break a maximum.
- IF several records support one value THEN count the value once and retain every record BECAUSE value cardinality and evidence multiplicity differ.
- IF a repair changes source assertions supporting derived values THEN rebuild the derived view BECAUSE deleting a visible consequence alone leaves its support active.
- IF a requested constraint is outside the implemented subset THEN mark it unchecked BECAUSE a partial validator cannot establish whole-contract conformance.

## Output template
```text
Scope: <snapshot, context, contract, identity convention; maximum 70 words>
Coverage: <target pair | complete/incomplete | evidence revision>
Findings: <target | bound | distinct values | state | supporting record IDs>
Input exceptions: <unsupported or malformed records; complete attachment if needed>
Repair alternatives: <change | evidence | owner/state; maximum 8 rows>
Preview rerun: <preview revision | checks executed/results or pending>
Decision: <conforms in complete scope / violates / unresolved; unchecked constraints>
Limits: <truth, inference and deployment limitations; maximum 60 words>
```

## Quality checklist
- [ ] Context and revision identify one assertion view.
- [ ] Cardinality bounds come from a supplied contract.
- [ ] Distinct-value counting has explicit identity semantics.
- [ ] Duplicate supporting records survive in the evidence ledger.
- [ ] Every confirmed maximum failure has record witnesses.
- [ ] Absence findings refer to matching completeness evidence.
- [ ] Proposed repairs preserve original records and have owners.
- [ ] Preview results distinguish executed checks from pending work.

## Anti-patterns
- **Count evidence as values**: duplicate sources inflate cardinality. Fix: group by endpoint identity first.
- **Absence becomes falsehood**: an empty extract proves no relationship exists. Fix: check completeness before concluding a minimum failure.
- **Convenient deletion**: discard whichever value produces a passing result. Fix: require correction evidence and owner review.
- **Silent equality**: merge endpoint IDs to satisfy a maximum. Fix: route identity decisions separately.
- **Partial checker approval**: claim all constraints passed after checking only counts. Fix: list unsupported constraints as unchecked.

## Worked example
**Input:** Fictional catalog W supplies the snippet records and exact-ID counting. Contract K requires one owner value for A and B. Coverage is complete for A only. No correction is authorized.

**Output:**
```text
Scope: W; one supplied context; K; distinct exact endpoint IDs.
Coverage: A/owner | complete | W; B/owner | incomplete | no coverage evidence.
Findings: A/owner | 1..1 | B,C | maximum violation | r1,r2,r3; B/owner | 1..1 | none | unresolved minimum | none.
Input exceptions: None within the supplied fictional fixture.
Repair alternatives: No approved change; catalog owner must adjudicate conflicting values and supply B coverage evidence.
Preview rerun: Pending; no repaired preview supplied.
Decision: Violates A maximum; B minimum unresolved; constraints beyond counts unchecked.
Limits: No source-truth verification, inference validation or deployment established.
```

**Bad output:** “A has three owners; delete r3 and invent an owner for B.”
This confuses records with values and fabricates a correction without evidence.

## Edge cases
- **Empty target inventory**: report no targets checked; never present this as validating an intended nonempty population.
- **Unknown endpoint**: return an input exception before the reference count check; do not create an entity to force validity.
- **Derived assertion**: require a checked support chain and selected inference revision; otherwise report its status as unresolved input.
- **Conflicting contexts**: partition by supplied context before evaluation; request a context policy if none exists.
- **Repair regression**: retain newly introduced failures from the full preview rerun, even when the original violation disappeared.

## Test case
**Input:**
> Fictional A has two source records for owner B, a maximum of one distinct owner, and incomplete coverage. C has no owner records and a required minimum of one with incomplete coverage. Diagnose both.

**Assertions:**
1. Counts one observed owner value for A and retains both source records.
2. Reports observed bounds only for A rather than complete conformance.
3. Reports C's missing owner as unresolved without inventing a value.
4. Proposes no automatic deletion, merge or deployed repair.
