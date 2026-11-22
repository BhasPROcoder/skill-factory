# GRF-058 author evidence

## Distinctness
Discovery card plans/graph-g58-scope.md rejected an authorization traversal idea overlapping GRF-052. Final actual comparison: GRF-018 governs relation meanings and licensed inverse/transitive inference, not recursive negation program admission. GRF-048 recomputes transitive facts after source retraction. GRF-020 diagnoses value constraints against assertions, and GRF-055 temporal functional conflicts. G58 checks neutral rule-variable safety and signed predicate dependency stratification before fact evaluation. sf.py searches for stratification/negation found no matching graph skill. This is scoped comparison, not whole-library proof.

## Execution
Direct sf.validate_text(text,path) returned empty errors and warnings; repaired body whitespace count 1761. Embedded Python executed under observed 3.14.6:
```text
safe recursion, signed cycle and independent strata checks passed
3.14.6
```
Additional extracted-code cases:
```text
safe recursion, signed cycle and independent strata checks passed
{'empty': True, 'positive_recursion': True, 'negative_self_cycle': True, 'unsafe_head': True, 'unsafe_negative': True, 'duplicate_id': True, 'malformed_atom': True, 'bad_var': True}
```
Reviewer hardening: the builder's final signed-inequality check now raises an explicit `ValueError` rather than relying on an assertion that disappears under optimized execution. Extracted reference was also executed with `python -O`; explicit external checks verified both the safe assignment and negative-cycle rejection:
```text
safe recursion, signed cycle and independent strata checks passed
optimized explicit stratum checks passed
```
Registry untouched.

## Ordinary scenario
```text
Scope: Cedar exercise C1; complete r1–r3 neutral rule set; no external rule engine assumed.
Safety: None; X/Y/Z in heads and negative atoms have positive body binding.
Dependencies: reach | + | edge | r1; reach | + | reach | r2; reach | + | edge | r2; allowed | + | reach | r3; allowed | - | blocked | r3.
Stratification: Accepted; edge=0, blocked=0, reach=0, allowed=1.
Witness: None.
Verification: Signed inequalities and bounded independent rank enumeration executed for C1.
Limits: Rule syntax only; no source facts evaluated or engine compatibility established.
Next action: Rule owner reviews intended relation meanings before a separate execution test.
```

## Missing-input scenario
```text
Scope: Rule inventory incomplete; negative atom polarity and variable syntax unavailable.
Safety: Pending complete atoms.
Dependencies: Pending.
Stratification: Unresolved.
Witness: None established.
Verification: No program audit executed.
Limits: Missing rule records may add binding defects or close a negative cycle.
Next action: Rule owner supplies complete neutral rules and syntax contract.
```

## Edge scenario
Fictional rule r4 defines blocked(X,Y) from allowed(X,Y), closing a dependency path allowed -→ blocked +→ allowed. The embedded code returns a negative-edge cycle witness with r3/r4 and independent rank enumeration finds no feasible assignment. A separate unsafe rule has allowed(X,Y) from only not blocked(X,Y); X/Y lack positive binding and are listed as unsafe.

## Claim audit
Specific claims: a negative dependency on a predicate cycle makes nonnegative strata satisfying strict-negative and nonstrict-positive inequalities impossible; positive recursion alone permits equal strata; head/negative variables need positive binding under the explicitly declared neutral contract. The implementation checks actual dependency edges and bounded independent rank enumeration. Examples and rule IDs are fictional. No external language semantics, current platform version, invented source, law, price or statistic is claimed. Interpreter version here is observed execution evidence only. The skill does not derive facts or certify a production rule engine.
