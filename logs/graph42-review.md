# GRF-042 independent review

Reviewer `g32_reviewer`. Read SPEC, full draft and author evidence; inspected actual GRF-032 and GRF-009 procedures. GRF-032 spans every original component; GRF-009 certifies one minimum route. GRF-042 instead selects any nonterminal connectors needed to join a specified terminal set at least total cost, with exact completion or cutoff evidence. Catalog search for Steiner found no lexical entry. This is scoped comparison evidence, not whole-library uniqueness proof. Registry untouched.

## Executed evidence

Executed the complete Python 3 reference under Python 3.14.6; its assertions printed `terminal tree, irrelevant node, loop, singleton and cutoff checked`. Independently tested 500 finite random four-node graph fixtures with nonnegative integer costs, optional parallel A/B edges and loops, and terminal sets of one to four nodes. A separate exhaustive subset oracle checked optimal cost or infeasibility for every complete run. All matched. For each fixture, subset caps 1 and half the total were checked: whenever below the total, the solver returned `unknown` with the exact visited count, never an unsupported optimum or infeasibility claim.

Direct fixtures: disconnected A/C terminals returned infeasible after 2/2 subsets; three unit-cost triangle edges returned a cost-2 tree with three tied choices after 8/8 subsets; parallel A/B edges of cost 2 returned two distinct identity ties after 4/4 subsets; a one-terminal graph returned the empty cost-0 tree after 1/1 subset. Negative cost, unknown endpoint, duplicate edge ID, malformed edge, missing/unknown terminals and zero cap were rejected. An independent selected-edge replay accepted the main `ab,bc,bd` witness and rejected forged cost 5, missing terminal coverage, added loop and wrong connector ledger. The reference itself independently replays its completed incumbent; it does not accept an external submitted certificate as a callable API.

The main example actually returned `optimal`, visited 128 subsets, selected `ab,bc,bd` at total 6 with connector B, and found exactly one cost-6 tree. Initial worked-example wording left the tie status conditional; author changed it to `one cost-6 tree observed`, matching executed evidence. `sf.validate_text` returned zero errors and warnings before this wording change; the coordinator should run the final registry validator on the final text.

## Ordinary scenario

```text
Scope: Fictional Harbor S1; undirected eligible inventory; terminals A,C,D; exact cost units.
Search: Cap 1000; visited 128/128 non-loop subsets; complete.
Selection: ab,bc,bd; connector B; total cost 6.
Verification: Three edges, no cycle, A/C/D connected through B; 2+2+2=6.
Optimality: Proved minimum for S1; one cost-6 tree observed.
Exclusions: loop; X and bx remain in inventory but are not selected.
Limits: The cost unit does not establish physical suitability.
Next action: Preserve the witness with S1 for owner review before operational use.
```

## Missing-input scenario

```text
Scope: Terminals A,C,D stated, but no complete eligible edge inventory or common cost unit.
Search: Not run.
Selection: None.
Verification: Pending source edges, endpoints and exact comparable weights.
Optimality: Unresolved.
Exclusions: Unknown.
Limits: A route suggestion cannot establish minimum terminal-connector cost.
Next action: Request the complete undirected edge table, common cost unit and snapshot ID together.
```

## Edge/Test scenario

```text
Scope: Fictional A/B/C, edges ab=1, bc=1, ac=1; terminals A,B,C.
Search: Cap 10; visited 8/8 subsets; complete.
Selection: ab,ac; no nonterminal connectors; total cost 2.
Verification: Two edges, no cycle, A/B/C connected; 1+1=2.
Optimality: Proved minimum; three tied cost-2 trees (ab/ac, ab/bc, ac/bc).
Exclusions: None.
Limits: Tie choice follows sorted edge IDs, not physical preference.
Next action: Ask owner for any external selection constraint before operational use.
```

## Verdict

All four Test case assertions passed. The code's complete-search result supports optimum only for the frozen eligible graph and nonnegative exact-cost objective. The example is fictional and its cost, subset count and tie status agree with execution. No changing external fact, invented citation or physical-construction guarantee appears. Recommend acceptance under the small finite undirected scope. No required repair remains.
