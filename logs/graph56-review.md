# GRF-056 independent review

Reviewer `g32_reviewer`. Read G56 scope, SPEC, full draft and author evidence; inspected actual Procedure sections of GRF-006, GRF-015, GRF-030 and GRF-012. These compute minimum-hop endpoint reachability, compare a fixed query result during plan tuning, find one accepted relation-state witness, or compare restart-walk ranks. GRF-056 instead counts every bounded edge-ID walk by exact length and endpoint, then identifies the first cumulative row-budget crossing. This is scoped comparison evidence, not whole-library uniqueness proof. Registry untouched.

## Executed evidence

Executed the complete Python 3 reference under Python 3.14.6; its assertions printed `edge-ID walk layers and budget boundary checked`. The fictional base fixture has positive-length layer totals 2, 6, 6 and zero-hop-excluded cumulative totals 0, 2, 8, 14; budget five first crosses at length two. Two parallel A→B IDs and two B→C IDs contribute separately, and the B loop permits bounded revisits. Isolate I has zero positive-length walks. Incoming direction, relation-filter exclusion, a single-node loop, budget equality at two rows, first crossing at length three, and depth-zero include/exclude policies passed direct fixtures.

Independently generated 350 finite directed graph/query fixtures with up to six identified edges, parallel endpoints, cycles, two labels, outgoing/incoming direction, bounds zero through four, both zero-hop policies and owner budgets. A separate explicit edge-ID-sequence enumerator matched every per-node layer table, cumulative total and first strict budget-crossing layer. Duplicate node or edge IDs, unknown seed or endpoint, string-shaped edge, missing labels, invalid direction, negative/Boolean depth, negative/Boolean budget and missing zero-hop policy were rejected. Final `sf.validate_text` returned zero errors and warnings.

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

## Edge/Test scenario

```text
Scope: Fictional one-node A graph with identified loop l:A→A, link relation, outgoing, bound 3.
Walk policy: Edge IDs distinct, repeats allowed; zero hop excluded from total.
Layers: Length 0 A=1; length 1 A=1; length 2 A=1; length 3 A=1.
Cumulative: 0, 1, 2, 3 through lengths 0,1,2,3.
Budget: Two rows; equality at length 2 does not cross; first crossing at length 3.
Verification: Explicit l, l/l and l/l/l sequences match propagation.
Limits: Finite bound only; no unrestricted count or runtime claim.
Next action: Query owner decides whether bound two is the intended result contract.
```

## Verdict

All five Test case assertions pass. The example's counts were independently recomputed as edge-ID sequences, and crossing uses strictly greater than the supplied owner budget. The fictional exercise makes no current price, platform or performance claim and invents no source. Recommend acceptance within the finite graph, bounded-walk and declared result-row semantics. No required repair found.
