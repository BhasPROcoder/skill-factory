# GRF-041 author evidence

## Scope comparison

The actual GRF-009 Procedure states that its executable reference permits only nonnegative costs and routes negative edges to a separately verified method with cycle handling. GRF-010 certifies a supplied flow using residual paths/cuts, not a signed-cost minimum walk. GRF-035 reduces an acyclic reachability view, not costs. GRF-041 closes the signed-weight walk gap with source-to-target corridor filtering, a finite label/route certificate or a relevant negative-cycle approach/cycle/exit certificate. This is a scoped comparison, not a whole-catalog uniqueness proof. The registry search for `shortest route` found GRF-009; the `negative cycle` lexical search did not reveal another route solver.

## Executed checks

The final embedded Python 3 snippet printed:

```text
finite route, irrelevant cycle and relevant cycle checked
```

An independently coded guarded Floyd–Warshall oracle checked 1,200 seeded three-node directed multigraph samples with signed integer weights and randomly selected terminals. Every solver state matched unreachable, finite or target-relevant negative-cycle classification; finite costs equaled the oracle; every returned certificate passed `verify`. Malformed short tuple, string, mapping, Boolean weight and duplicate edge-ID inputs raised ValueError. Its output was:

```text
finite route, irrelevant cycle and relevant cycle checked
random_three_node_cases 1200 oracle_and_shape_checks_pass
```

The first test-oracle run used a finite sentinel without guarding `infinity + negative weight`; it falsely labeled one unreachable cycle as relevant. The oracle was corrected to skip infinite operands, then all 1,200 cases passed. This was a test harness error, not a change to the skill's algorithm. `sf.validate_text(text,path)` on the final saved skill returned empty errors and warnings. No registry edit or push occurred.

## Ordinary scenario

```text
Scope: Fictional Cedar C1; complete exercise inventory; directed edges and one integer cost unit.
Terminals and walk policy: S to T; revisits allowed.
Corridor: S,A,B,T.
Verdict: Finite minimum.
Certificate: Cost 3; route sa,ab,bt.
Verification: 4+(-3)+2=3; directed replay and corridor label inequalities executed.
Limits: X/Y form a reachable negative cycle but cannot reach T; I is isolated. Ties, if any, may yield another route.
Next action: Graph owner checks omitted exits from X/Y before using the result outside C1.
```

## Missing-input scenario

```text
Scope: Node/edge inventory and common cost unit unavailable.
Terminals and walk policy: S to T supplied; revisit permission unresolved.
Corridor: Pending validated directed records.
Verdict: Unresolved.
Certificate: None computed.
Verification: No reachability, relaxation or replay executed.
Limits: Counts and unlabeled costs cannot establish a minimum or cycle relevance.
Next action: Owner supplies inventory, exact unit and walk policy together.
```

## Edge/Test scenario

```text
Scope: Fictional Cedar C1 plus ba:B→A cost 1; all other records unchanged.
Terminals and walk policy: S to T; revisits allowed.
Corridor: S,A,B,T.
Verdict: No finite minimum.
Certificate: Approach sa; cycle ab,ba costing -3+1=-2; exit ab,bt.
Verification: Source reaches A; A→B→A closes at cost -2; A→B→T reaches target; executed replay passed.
Limits: X/Y remains irrelevant to T; no operational route recommendation.
Next action: Graph owner reviews the new ba record and revisitation policy before deciding how to model the task.
```

Additional executed fixtures returned unreachable for S→I, finite zero for S→S without a returning negative cycle, no finite minimum for a reachable negative self-loop returning to S, and deterministic `e1` among tied parallel S→T edges. Their returned dictionaries passed `verify`.

## Claim audit

The specific mathematical claims are stable finite-graph properties: if a negative cycle is reachable from the source and can reach the target, repeated walks lower cost without bound; a finite label satisfying all corridor edge inequalities bounds every source-to-target walk below, and a matching route attains that bound. The fictional arithmetic is checked: 4-3+2=3 and -3+1=-2. All named edges and nodes in examples are fictional. No current law, rate, API version, source citation or external statistic is hardcoded. The reference's bounded in-memory execution is not a production runtime claim. The skill addresses walks, not the separate simple-path optimization problem.
