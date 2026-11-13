---
id: GRF-018
name: knowledge-relation-inference-contract
domain: Graph Engineering Foundations
subdomain: Knowledge vocabulary governance
version: 1.0
description: Define a versioned relation vocabulary with typed assertion boundaries and explicitly permitted inference rules when shared graph terms must support consistent downstream reasoning.
triggers: ["define knowledge graph relation meanings", "govern a shared graph vocabulary", "decide which graph inferences are allowed", "test inverse and transitive relation rules", "separate asserted from derived graph facts"]
not_for: ["choosing entity versus event representations [GRF-001]", "adjudicating same-entity merges [GRF-002]", "translation terminology choices [GLA-004]", "general ontology standard implementation", "extracting claims from raw documents"]
requires: []
risk_level: medium
---

# Knowledge Relation Inference Contract

## Purpose
Create a reusable vocabulary release whose terms have explicit meanings, assertion requirements and licensed inference behavior. Keep source assertions separate from rule-derived statements and preserve why each derived statement exists. This governs a shared reasoning interface; it does not establish that supplied assertions are true.

## Inputs to collect
1. **Vocabulary users and questions** — obtain producers, consumers and required reasoning questions. Why: a shared term must support the same interpretation across integrations. Default: supplied consumers only; unknown consumers remain untested.
2. **Term evidence** — collect stable term IDs, definitions, aliases, examples and counterexamples with owners. Why: matching labels need not denote the same concept. Default: provisional definitions, no synonym or identity equivalence inferred from spelling.
3. **Entity classes and identity scope** — obtain class definitions, namespace boundaries and source-key meaning. Why: a predicate's accepted endpoints need explicit types and scoped identities. Default: preserve source-scoped IDs; no entity merge.
4. **Inference policy** — obtain approved inverse, transitive and other rule choices plus their justification. Why: a traversable path is not automatically an entailed fact. Default: no additional inference licensed until specified; a disabled rule is not a negative assertion.
5. **Assertion and evidence fixtures** — obtain typed nodes and source-backed examples, including rejected and ambiguous cases. Why: a definition without counterexamples can hide incompatible interpretations. Default: clearly fictional test fixtures only.
6. **Release governance** — obtain vocabulary revision, approver, deprecation/replacement policy and consumer migration evidence. Why: changing a term's meaning changes inferred results. Default: draft release with unresolved approval; no silent replacement of published semantics.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the vocabulary revision and identify the consumers whose questions must keep their intended meaning.
2. Give each class and predicate a stable scoped ID, definition, owner and disambiguating counterexample; keep display aliases separate from identity equivalence.
3. Define each predicate's accepted subject and object classes, source-evidence requirement and explicit unknown handling. Treat these as validation constraints unless another semantics is deliberately chosen.
4. Record exactly which inference rules are licensed, including direction and applicability boundaries. Distinguish an inverse predicate from a symmetric predicate and a transitive rule from ordinary multi-hop reachability.
5. Check vocabulary references and rule compatibility before evaluating facts. An inverse must reverse endpoint roles; unresolved definitions block the dependent rule.
6. Validate supplied assertions without modifying their original evidence. ⚠️ A wrong endpoint type is a validation failure here, not permission to assign a new class to make the statement fit.
7. Derive only licensed consequences, retaining a rule identifier and supporting statements for each result. Keep direct assertions identifiable even when another path derives the same triple.
8. Test ordinary, counterexample and cyclic fixtures. Confirm that unrelated predicates do not acquire inverse, symmetric, transitive or identity consequences merely because their names resemble approved terms.
9. Compare proposed vocabulary changes against prior fixtures and consumer questions. Recompute derived views when a rule changes; do not leave obsolete consequences masquerading as source assertions.
10. Deliver the vocabulary and rule ledger with approval state, compatibility findings and unresolved meanings. Do not claim conformance to an external standard without verifying its current authoritative specification and implementation behavior.

This Python 3 reference uses a finite fixed node inventory with one explicit class per node. Each predicate entry is `(subject_class, object_class, inverse_ID_or_None, enable_transitive_rule)`. It supports only named inverses and same-class transitive rules; disabled rules mean unlicensed computation, not logical negation. Prevalidate tuple shapes and nonempty string IDs. Run the complete snippet and record the installed interpreter version.

```python
def derive(types, classes, vocabulary, assertions):
    if any(t not in classes for t in types.values()):
        raise ValueError("unknown node class")
    for p, (domain, range_, inverse, transitive) in vocabulary.items():
        if domain not in classes or range_ not in classes or type(transitive) is not bool:
            raise ValueError("invalid predicate contract")
        if transitive and domain != range_:
            raise ValueError("reference requires same-class transitivity")
        if inverse is not None:
            if inverse not in vocabulary:
                raise ValueError("unknown inverse")
            other = vocabulary[inverse]
            if other[:2] != (range_, domain) or other[2] != p:
                raise ValueError("incompatible inverse contract")
    evidence, direct, source_ids = {}, set(), set()
    for fid, s, p, o in assertions:
        if fid in source_ids:
            raise ValueError("duplicate source identity")
        source_ids.add(fid)
        if p not in vocabulary or s not in types or o not in types:
            raise ValueError("unknown predicate or endpoint")
        if (types[s], types[o]) != vocabulary[p][:2]:
            raise ValueError("endpoint type mismatch")
        triple = (s, p, o)
        direct.add(triple)
        evidence.setdefault(triple, ("asserted", fid))
    while True:
        before = len(evidence)
        facts = list(evidence)
        for s, p, o in facts:
            inverse = vocabulary[p][2]
            if inverse is not None:
                evidence.setdefault((o, inverse, s), ("inverse", (s, p, o)))
            if vocabulary[p][3]:
                for a, q, b in facts:
                    if q == p and a == o:
                        evidence.setdefault((s, p, b),
                                            ("transitive", (s, p, o), (a, q, b)))
        if len(evidence) == before:
            return direct, evidence

types = {"A": "Unit", "B": "Unit", "C": "Unit"}
vocabulary = {"contains": ("Unit", "Unit", "inside", True),
              "inside": ("Unit", "Unit", "contains", False),
              "peer": ("Unit", "Unit", None, False)}
assertions = [("r1", "A", "contains", "B"),
              ("r2", "B", "contains", "C"),
              ("r3", "A", "peer", "B"), ("r4", "B", "peer", "C")]
direct, facts = derive(types, {"Unit"}, vocabulary, assertions)
assert ("A", "contains", "C") in facts and ("C", "inside", "A") in facts
assert ("A", "contains", "C") not in direct
assert ("A", "peer", "C") not in facts and ("B", "peer", "A") not in facts
assert len(direct) == 4 and len(facts) == 8
print("licensed closure, inverse evidence and unlicensed-rule checks passed")
```

The returned evidence stores one derivation witness per triple; retain the complete input assertion ledger separately, including multiple source records supporting the same triple. The monotone loop terminates because it adds only triples over the fixed finite nodes and predicates. This is not a general reasoning engine, contradiction solver or truth verifier.

## Decision rules
- IF a label has different meanings across contexts THEN split or qualify its term entries BECAUSE shared spelling does not establish semantic identity.
- IF a path uses an unlicensed predicate rule THEN retain the path without asserting a new fact BECAUSE traversal and entailment are different operations.
- IF a type constraint fails THEN report the original statement for review BECAUSE coercing its endpoint types conceals a disagreement.
- IF a derived statement loses its supporting rule in a new release THEN rebuild the derived view BECAUSE previously inferred content is not independent source evidence.
- IF a consumer depends on changed semantics THEN require an explicit compatibility decision BECAUSE an unchanged term ID does not make the change harmless.

## Output template
```text
Release: <revision, owner, draft/approved scope; maximum 60 words>
Terms: <scoped ID | definition | aliases | endpoint classes | counterexample>
Rules: <predicate | licensed inference | justification | unsupported inference>
Assertions: <source ID | typed statement | accepted/rejected/unresolved>
Derived evidence: <statement | rule | supporting statements; full ledger or attachment>
Fixture checks: <ordinary/counterexample/cycle | observed or pending>
Compatibility: <consumer | changed meaning/result | required action>
Decision: <ready for approval / blocked; unresolved meanings, maximum 80 words>
```

## Quality checklist
- [ ] Term identity is separate from labels and entity identity.
- [ ] Definitions include a distinguishing counterexample.
- [ ] Endpoint constraints state whether they validate or infer types.
- [ ] Every generated consequence has a licensed rule and witness.
- [ ] Direct assertions remain distinguishable from derived statements.
- [ ] Absence of a consequence is not presented as negation.
- [ ] Semantic changes have consumer and derived-view checks.
- [ ] Tested scope is separate from standard conformance and truth claims.

## Anti-patterns
- **Synonym merge**: equate entities because terms share a label. Fix: preserve scoped identities and review equivalence separately.
- **Path becomes fact**: infer transitivity for every relation. Fix: use explicit licensed rules.
- **Type laundering**: reclassify an endpoint to pass validation. Fix: expose the mismatched assertion.
- **Derived becomes sourced**: cite an inferred triple as a direct observation. Fix: retain its rule and input chain.
- **Silent semantic release**: change a definition without rerunning consumers. Fix: version the contract and compare fixtures.

## Worked example
**Input:** Fictional catalog Juniper approves the snippet vocabulary: contains has an inverse inside and a transitive rule; peer has neither. Its four assertions and Unit classifications are supplied for testing.

**Output:**
```text
Release: Juniper draft V1; catalog owner approval recorded for the fixture rules only.
Terms: contains | enclosing unit | Unit->Unit | peer contact is not containment; inside | inverse role | Unit->Unit; peer | direct peer statement | Unit->Unit | no chained relationship implied.
Rules: contains transitive and inverse-inside; inside inverse-contains; peer no extra rules licensed.
Assertions: r1 A contains B; r2 B contains C; r3 A peer B; r4 B peer C; all typed Unit and accepted.
Derived evidence: A contains C from r1/r2; B inside A, C inside B, C inside A with inverse witnesses. Four asserted plus four derived triples.
Fixture checks: Reference checks eight total triples when executed; A peer C and B peer A are not generated, not declared false.
Compatibility: Consumers must distinguish contains from peer and preserve direct/derived evidence; external consumers untested.
Decision: Ready for vocabulary-owner review within fixture scope; no external truth or standard-conformance claim.
```

**Bad output:** “All two-hop links are transitive, so A peer C is true and missing links are false.”
This invents both an inference license and a closed-world negation rule.

## Edge cases
- **Cyclic transitive assertions**: permit the licensed closure to expose self-relations; review whether the intended domain contract actually allows those assertions.
- **Several sources assert one triple**: retain all source records outside the compact derivation map; do not collapse their provenance.
- **Deprecated term**: retain historical meaning and explicit replacement guidance; do not substitute a new term merely because its label matches.
- **Multiple types or inheritance**: specify a separately tested semantics; the single-class reference does not implement it.
- **Incomplete evidence**: mark unknown assertions unresolved; absence from the closure proves neither truth nor falsehood outside the supplied model.

## Test case
**Input:**
> Fictional A/B/C are Unit nodes. Assertions A peer B and B peer C use a predicate with no licensed inverse or transitive rule. A proposed consumer wants A peer C and B peer A treated as observed facts. Produce a vocabulary decision.

**Assertions:**
1. Retains the two direct peer assertions with their supplied evidence.
2. Does not derive A peer C or B peer A under the stated policy.
3. Distinguishes an absent inference from a negative assertion.
4. Requires a justified rule/consumer contract change rather than inventing observations.
