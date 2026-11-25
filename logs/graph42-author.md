# GRF-042 author evidence

Read AGENTS.md and SPEC and inspected actual GRF-032 and GRF-009 procedures. `sf.py search 'Steiner'` found no lexical match. GRF-032 connects every node in each original component via a spanning forest; GRF-009 verifies one source-to-target route. GRF-042 connects only a selected terminal set, may use nonterminal connectors, and proves a small-instance optimum by bounded complete subset enumeration. This is a scoped comparison, not whole-library uniqueness proof. No registry change or push.

Draft: `skills/GRF/bounded-steiner-connector-certificate/SKILL.md`; manifest: `staging/graph_g42.json`. Final `sf.validate_text(text, path)` returned zero errors and warnings. Complete embedded Python 3 snippet executed and printed `terminal tree, irrelevant node, loop, singleton and cutoff checked`. The main fictional fixture returned `optimal`, 128 visited subsets, retained ab/bc/bd with connector B and total 6, loop excluded. Independent BFS replay checks terminal reachability, selected vertex/edge tree count, and original-weight sum after the subset search.

Additional executed cases:
```text
disconnected A/C terminals: infeasible, 2/2 subsets visited
triangle with unit-cost edges: optimal cost 2, 8/8 subsets visited, three tied trees
parallel A-B edges each cost 2: optimal cost 2, 4/4 subsets visited, two tied identities
cap 2 before feasible completion: unknown, 2 subsets visited, no incumbent
negative weight: REJECT invalid edge or weight
unknown endpoint: REJECT unknown endpoint
string edge record: REJECT invalid edge or weight
unknown terminal: REJECT nonempty known terminal set required
singleton terminal, no edges: optimal empty tree, cost 0, 1/1 subset visited
```

Ordinary output:
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

Missing-input output:
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

Edge output:
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

Claim audit: all numeric totals and subset counts above were checked against executed code. Nonnegative exact integer costs, finite graph and complete enumeration scope are explicit; no external current value, API version, study or source claim is included. Fictional examples only. Independent review required before acceptance.

Review repair: the worked example's Optimality line now states the observed complete-search result, `one cost-6 tree observed`, matching the executed run and ordinary scenario above. Re-ran `sf.validate_text(text, path)` after the edit; zero errors and warnings.
