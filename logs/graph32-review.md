# GRF-032 independent review

Reviewer `g32_reviewer`. Read SPEC, the complete saved candidate, and the actual Procedure sections of GRF-004, GRF-009 and GRF-010. This skill minimizes the total selected edge weight for every component of an undirected graph and certifies the choice through non-tree-edge exchanges. GRF-004 validates parent/root structure, GRF-009 verifies a minimum route, and GRF-010 certifies flow and cuts. The candidate has a distinct output and decision. This is a scoped comparison, not a whole-library uniqueness proof. Registry untouched.

## Executed verification

Executed the complete embedded Python 3 snippet under Python 3.14.6; its own assertions passed and printed `spanning forest and exchange certificate checked`. Independently executed these cases against `construct` and `certify`:

| Case | Selection | Total | Exchange evidence |
|---|---|---:|---|
| Disconnected A-B=3, C-D=-4, I isolated | cd, ab | -1 | no unselected non-loop edge |
| Equal parallel A-B edges at 2 | e1 | 2 | e2 versus e1 at 2, tie |
| Negative loop -99 with A-B=3 | ab | 3 | loop excluded |
| Empty graph | empty | 0 | none |
| Two isolated nodes | empty | 0 | none |
| A-B=1, B-C=2, A-C=8; proposed ab,ac | ab, ac | 9 | bc=2 versus ac=8, fail |

Verifier rejected a nonspanning selection, duplicate selected ID, unknown selected ID, selected loop and selected cycle. Structural `sf.validate_text` returned zero errors and zero warnings with the file path supplied. The snippet's public contract requires prior tuple-shape and string-field validation; no claim is made that `validate` itself handles malformed tuples or mixed ID types. The finite in-memory reference is not a production runtime benchmark.

## Ordinary scenario

Fictional complete undirected snapshot: A-B cost 3, C-D cost -4, I isolated, one exact cost unit.

```text
Contract: Fictional F1; undirected; all supplied edges eligible; integer cost units.
Components: {A,B}; {C,D}; {I}.
Selection: ab,cd; total -1 from 3+(-4).
Feasibility: Unique selected IDs, no cycle, and all original components spanned; executed.
Exchange ledger: No unselected non-loop edges; pass vacuously.
Decision: Minimum certified for the supplied snapshot.
Limits: Separate components remain disconnected; no physical suitability claim.
```

## Missing-input scenario

The request gives a directed relationship list with no explicit projection or common weight unit.

```text
Contract: Direction interpretation and additive weight unit unresolved.
Components: Pending complete undirected eligible inventory.
Selection: None computed; total pending.
Feasibility: Not executed.
Exchange ledger: Not executed.
Decision: Unresolved.
Limits: Directed links cannot silently become undirected and incomparable values cannot be summed.
```

## Edge/Test scenario

Fictional Test input: A-B=1, B-C=2, A-C=8, and I isolated; proposed ab plus ac.

```text
Contract: Fictional F2; undirected; all supplied edges eligible; integer cost units.
Components: {A,B,C}; {I}.
Selection: Proposed ab,ac; recomputed total 9 from 1+8.
Feasibility: Unique selected IDs, acyclic, and original components spanned; executed.
Exchange ledger: bc | 2 | ac/8 | fail; replace ac with bc for total 3.
Decision: Improvable; proposed selection is not minimum.
Limits: I remains isolated; the result does not establish source-route optimality.
```

## Verdict

All four Test case assertions passed. Arithmetic and template fields agree. Stable finite-graph claims are supported by the executed checks and exchange reasoning; no changing external fact or source claim is embedded. Recommend acceptance under the declared unconstrained, undirected, exact-integer scope. No required repair found.
