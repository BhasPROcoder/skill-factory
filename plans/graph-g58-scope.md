# Candidate GRF-058: knowledge-rule negation stratification audit

Status: discovery card only. No skill, staging manifest or registry entry. ID provisional.

## Rejected adjacent idea

An access-controlled traversal candidate was rejected: sf.py search found GRF-052 `authorized-graph-traversal-exposure-check`, which already tests principal node/edge grants. Do not create a renamed version.

## Distinct problem and artifact

Before evaluating a small set of explicitly supplied knowledge-graph derivation rules, determine whether each rule's negative conditions are safely bound and whether rule dependencies admit a stratum order. Return a rule-dependency ledger, unsafe-variable witnesses, any cycle containing a negative dependency, and one valid stratum assignment when possible. This is a **rule-program admission check**, not a derived-fact engine or a choice of relation meaning.

Actual nearest procedures inspected: GRF-018 `knowledge-relation-inference-contract` defines relation vocabulary, types and approved inverse/transitive rules, then derives consequences under that policy. It does not analyze recursive negation dependencies or variable binding in rule bodies. GRF-048 `knowledge-inference-retraction-support` recomputes approved transitive facts after one assertion removal, with alternate support. GRF-020 diagnoses value-constraint violations in a graph snapshot. GRF-055 finds effective-time overlap for functional relationships. None tests rule-program stratification. sf.py searches for “stratification” and “negation” found no corresponding graph rule skill.

## Rule contract

For a portable bounded reference, use a neutral finite rule notation: each rule has a head predicate with variables and a list of positive or negative body atoms. No function symbols, arithmetic predicates, aggregates, existential head variables or arbitrary text parsing. Predicate names and variable tokens are explicit strings. A variable in the head or a negative body atom must also occur in at least one **positive** body atom of that rule. A positive dependency permits equal or higher head stratum; a negative dependency requires a strictly higher head stratum. A dependency cycle containing a negative edge prevents such an assignment. Do not infer that a stratifiable program is semantically correct, authorized or safe for a particular database engine. If the user's rule language has different semantics, check its current authoritative documentation before adapting.

## Executable fictional fixture

Fictional predicates: `edge`, `blocked`, `reach`, `allowed`. Rules:

1. `reach(X,Y) <- edge(X,Y)`.
2. `reach(X,Z) <- reach(X,Y), edge(Y,Z)`.
3. `allowed(X,Y) <- reach(X,Y), not blocked(X,Y)`.

Dependencies are reach→edge positive, reach→reach positive, allowed→reach positive and allowed→blocked negative (arrow from head to body). One valid stratum assignment is edge=0, blocked=0, reach=0, allowed=1. The recursive positive reach rule is allowed. Add `blocked(X,Y) <- allowed(X,Y)`: blocked→allowed positive closes a cycle with allowed→blocked negative, so reject stratification with those two rule IDs as a witness. Replace rule 3 with `allowed(X,Y) <- not blocked(X,Y)`: X and Y lack positive binding, so reject safety even if dependency strata appear possible. An unrelated `note` predicate and empty rule set should be handled without inventing facts.

Executable check: build predicate dependency edges with polarity and rule ID; compute strongly connected regions and flag any negative edge internal to one region; independently enumerate small integer stratum assignments to verify the pass/reject fixture. Check each rule's variable sets before dependency analysis. Preserve multiple rules and duplicate-looking predicate dependencies as separate rule evidence; do not collapse rule IDs.

## Acceptance gate

Before full authoring, compare actual G18/G20/G48 and any newly accepted rule skill. Use a bounded Python 3 reference and independent verifier for the fictional fixture, plus missing-rule-contract, unsafe variable, positive recursion, negative cycle, unrelated predicate, duplicate rule ID and malformed atom tests. The skill must distinguish syntactic admission from actual derivation and current engine semantics. Independent review precedes registry acceptance.
