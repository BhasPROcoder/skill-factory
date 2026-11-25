# GRF-058 independent review

## Verdict

**Accept for the declared finite neutral rule notation.** The reference checks positive binding of head and negated variables, records every signed rule dependency, produces an actual negative-edge cycle when one exists, and assigns ranks satisfying all signed inequalities otherwise. This does not certify a particular rule engine or evaluate source facts. Registry and remote were not changed by this review.

## Scope and distinctness

I read the scope, specification, full draft, author evidence, and actual nearest procedures. GRF-018 chooses relation meanings and licensed inverse/transitive inference; GRF-020 checks graph assertion values against constraints; GRF-048 recomputes transitive support after assertion removal. GRF-058 instead admits or rejects a *rule program* based on variable safety and recursive negation dependencies. That is a distinct decision and artifact, within the limited notation stated in the skill.

## Executed evidence

- Embedded Python 3 snippet, after the repair: `safe recursion, signed cycle and independent strata checks passed`.
- Embedded snippet under optimized Python (`python -O`): the same line, followed by `optimized explicit stratum checks passed`. The final inequality check now uses an explicit `if ...: raise ValueError`; the earlier `assert` was optimization-sensitive and was repaired before this verdict.
- Independent exhaustive oracle: all 81 signed dependency patterns over two predicates (each possible edge absent, positive, or negative) agreed with small-integer rank enumeration: 24 feasible and 57 infeasible. Each returned cycle was replayed against the dependency ledger for membership, continuity, closure, and a negative edge. Every accepted assignment was checked against every inequality.
- A separate seeded randomized oracle run covered 1,000 two- and three-predicate programs and agreed on feasibility, witness validity, and rank constraints. This was before the explicit-`if` repair; the exhaustive 81-pattern rerun above was after it.
- Empty input, positive recursion, negative self-cycle, unsafe head/negative variables, duplicate IDs, malformed signs/atoms/variable tuples/tokens, and forged certificate replay were exercised. The script rejects malformed/duplicate rules and returns unsafe witnesses under the declared binding policy. Forged cycle edges, nonclosed paths, positive-only paths, and forged zero-rank assignments fail independent replay.
- `sf.validate_text` on the final draft returned `([], [], metadata)`: no validation errors or warnings.

The embedded reference does not expose a callable verifier for a separately submitted cycle or rank certificate. Its procedure explicitly requires independent checking; my replay was an external review test, not a claimed public API in the skill. This is acceptable for the bounded reference scope.

## Full observed ordinary output

```text
Scope: Fictional Cedar exercise C1, complete r1-r3 rule set under the neutral syntax.
Safety: None.
Dependencies: reach | + | edge | r1; reach | + | reach | r2; reach | + | edge | r2; allowed | + | reach | r3; allowed | - | blocked | r3.
Stratification: Accepted; edge=0, blocked=0, reach=0, allowed=1.
Witness: None.
Verification: Embedded checks and independent bounded rank enumeration passed.
Limits: No fact derivation, source-truth check, or external engine conformance claim.
Next action: Rule owner reviews intended meanings before a separate execution test.
```

Actual function tuple: `([], None, {'allowed': 1, 'edge': 0, 'blocked': 0, 'reach': 0}, [five signed dependencies listed above])`.

## Full missing-input output

```text
Scope: Incomplete rule inventory; atom polarity or variable syntax is missing.
Safety: Pending complete atoms.
Dependencies: Pending.
Stratification: Unresolved.
Witness: None established.
Verification: No complete-program audit executed.
Limits: Missing rules may introduce unbound variables or close a negative cycle.
Next action: Rule owner supplies complete rule records and syntax contract.
```

This is a procedure output, not an invented execution result; the Python reference takes complete tuple records and rejects malformed records rather than accepting a partial program.

## Full observed edge output

```text
Scope: Fictional Cedar exercise C2, complete r1-r4 rule set under the neutral syntax.
Safety: None.
Dependencies: reach | + | edge | r1; reach | + | reach | r2; reach | + | edge | r2; allowed | + | reach | r3; allowed | - | blocked | r3; blocked | + | allowed | r4.
Stratification: Rejected; no valid nonnegative integer ranks satisfy the signed constraints.
Witness: allowed | - | blocked | r3; blocked | + | allowed | r4.
Verification: Witness edges and closure replayed; bounded rank enumeration found no assignment.
Limits: No fact derivation or external engine conformance claim.
Next action: Rule owner changes the dependency design and reruns the audit.
```

The separate unsafe example `allowed(X,Y) <- not blocked(X,Y)` returned `[(u, X), (u, Y)]` as safety witnesses. It still returned dependency diagnostics, but that stratum map cannot turn the unsafe rule into an admitted program.

## Claim audit

The rank conclusion follows from the stated inequalities: head rank is at least body rank for a positive dependency and strictly greater for a negative dependency. A closed path with a negative edge implies a strict rank increase back to the same predicate, which is impossible; positive recursion alone can share a rank. Variable safety is defined by this skill's neutral contract, not asserted for other rule languages. All predicates, people, teams, and rule IDs in the examples are fictional. No changing platform fact, source, version requirement, statistic, or external rule semantics is hardcoded.
