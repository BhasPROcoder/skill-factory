# GRF-056 author evidence

## Distinctness
Discovery card plans/graph-g56-scope.md records an initial rejected authorization traversal idea because actual GRF-052 covers it. Final actual comparison: GRF-006 returns minimum-hop endpoints and one witness, suppressing repeated walks; GRF-030 returns one relation-state witness per endpoint, not all walks; GRF-015 checks a fixed two-hop SQL multiset during query-plan tuning, not arbitrary-bound cardinality propagation; GRF-012 compares restart-walk ranks. G56's distinct artifact is exact edge-ID walk counts per hop and endpoint with first budget-crossing layer. This is scoped comparison, not whole-library uniqueness proof.

## Execution
Direct sf.validate_text(text,path) returned empty errors and warnings; body whitespace count 1748. Embedded Python ran under observed 3.14.6:
```text
edge-ID walk layers and budget boundary checked
3.14.6
```
Additional extracted-code fixtures:
```text
edge-ID walk layers and budget boundary checked
{'incoming': True, 'filter': True, 'budget_equal': True, 'empty': True, 'cycle': True, 'string_edge': True, 'duplicate': True, 'bad_depth': True, 'bad_budget': True}
```
Registry untouched.

## Ordinary scenario
```text
Scope: Fern exercise F1; A/B/C/I and identified directed link edges; seed A, outgoing, bound 3.
Walk policy: Edge IDs distinct, repeats allowed, zero hop excluded from cumulative total.
Layers: 0 | A | 1; 1 | B | 2; 2 | B | 2, C | 4; 3 | B | 2, C | 4; all other endpoint counts zero.
Cumulative: Length 0 | 0; length 1 | 2; length 2 | 8; length 3 | 14.
Budget: Five rows; first exceeded at length 2.
Verification: Dynamic propagation matched independent edge-ID sequence enumeration for all four layers.
Limits: Exercise graph and bound only; no runtime or memory estimate.
Next action: Query owner chooses a shorter bound or changes the output contract before execution.
```

## Missing-input scenario
```text
Scope: Seed and relation filter supplied; direction and maximum hop bound absent.
Walk policy: Edge IDs distinct, repeats allowed; zero-hop inclusion unresolved.
Layers: Pending complete query contract.
Cumulative: Pending.
Budget: Owner limit absent; no crossing decision.
Verification: No walk count executed.
Limits: Direction, bound and zero-hop policy alter the count population.
Next action: Query owner supplies direction, nonnegative bound, zero-hop choice and optional row budget.
```

## Edge scenario
Fictional single-node A has loop l:A→A. With bound three and zero-hop excluded, each positive layer has one walk, giving cumulative totals one, two, three. Executed cycle fixture checked this; unrestricted count is not asserted. A separate budget-equality fixture confirmed two rows against budget two is not an exceedance.

## Claim audit
Specific claims: finite-bound edge-ID walk counts follow dynamic propagation by summing each prior-layer count across every eligible edge identity; parallel IDs and loops produce distinct walk sequences; cumulative count crosses a budget only when strictly greater. These are stable finite combinatorial properties, checked by independent edge-ID sequence enumeration and adversarial fixtures. Example team is fictional; numbers were recomputed by executed assertions. No current prices, laws, software-version promise, invented citation or statistic appears in the skill. Interpreter version is observed evidence here only. Count is not a runtime or memory guarantee.
