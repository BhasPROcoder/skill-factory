# GRF-036 author evidence

Read AGENTS.md, SPEC.md and GOLD example; queried sf.py for coloring, color assignment and scheduling conflict. Inspected actual GRF-031 procedure: it gives a linear two-color decision or odd-cycle witness, with no arbitrary finite palette, per-node allowed sets or cutoff state. GRF-011 solves one-to-one matching; SVC-001 is resource occupancy rather than abstract coloring. This is a scoped distinction, not a whole-catalog uniqueness proof. No registry mutation or push.

Draft: `skills/GRF/bounded-graph-coloring-feasibility/SKILL.md`. Manifest: `staging/graph_g36.json`. Final `sf.validate_text(text, path)` returned zero errors and warnings. The embedded Python 3 snippet executed and printed `coloring, exhaustive failure, cutoff and loop checked`. Full example returned feasible after 5 entered states with A=0, B=1, C=2, I=0. A triangle restricted to two colors completed and returned infeasible. Budget 1 returned unknown. A loop returned immediate infeasible.

Additional executed cases:
```text
parallel A/B edges: feasible, 3 states, A=0 B=1
adjacent fixed A=0 B=0: infeasible, 2 states
empty graph: feasible, 1 state, empty coloring
isolated I with empty allowed set: infeasible, 0 states
string edge record: REJECT invalid edge
missing allowed-set map: REJECT allowed sets must cover every node
zero state limit: REJECT positive integer state limit required
```

Ordinary output:
```text
Scope: Fictional Cedar S1; A,B,C,I; undirected ab,bc,ca; palette {0,1,2}; A={0}, others={0,1,2}.
Search: Nodes A,B,C,I; ascending allowed colors; limit 100; completed after 5 states.
Verdict: Feasible.
Certificate: A=0, B=1, C=2, I=0.
Verification: All four nodes covered; colors allowed; ab,bc,ca cross different colors.
Limits: I is isolated; color labels have no scheduling meaning.
Next action: Check any real assignment constraints before using these labels operationally.
```

Missing input:
```text
Scope: Node and edge inventory supplied, but no palette and no direction projection policy.
Search: Not run; no state budget used.
Verdict: Unresolved.
Certificate: None.
Verification: Cannot check colors or conflict edges without the missing contract.
Limits: A partial inventory or implicit direction choice could change the answer.
Next action: Request exact palette and undirected projection rule together.
```

Edge output:
```text
Scope: Fictional Cedar S1 triangle, palette {0,1}, all nodes allowed both, I isolated.
Search: Nodes A,B,C,I; ascending allowed colors; limit 100; all branches explored in 5 states.
Verdict: Infeasible.
Certificate: Completed exhaustive search; no allowed coloring.
Verification: Every explored partial assignment that reaches C conflicts with A or B; no complete map exists.
Limits: The verdict covers only the supplied triangle and restrictions.
Next action: Ask the owner whether a larger palette or changed conflict contract is permitted.
```

Claim audit: Specific counts above are observed from the executed reference. General claims are finite graph constraints and explicit search-state semantics. No external source, changing platform claim, law, price or statistical claim is included. The examples are fictional and arithmetic is consistent. Independent review remains required; this draft is not accepted or counted by author.
