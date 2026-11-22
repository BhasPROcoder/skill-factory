# GRF-040 independent review

Reviewer `g32_reviewer`. Read SPEC, full draft and author evidence; inspected actual Procedure sections of GRF-027, GRF-031 and GRF-037. Those handle two-graph structural correspondence, two-color feasibility, and degree-threshold core peeling. GRF-040 finds a complete mutual-adjacency group and distinguishes a valid observed clique from a greatest-size proof. A k-core need not be a clique. This is scoped comparison evidence, not whole-library uniqueness proof. Registry untouched.

## Executed evidence

Executed the full embedded Python 3 reference under Python 3.14.6; its assertions printed `bounded clique witness and completed maximum checked`. Independently enumerated all 1,024 simple undirected graphs on five nodes. A separate subset oracle computed the largest clique size. For each graph, the 32-subset run returned `maximum` with that size and passed the verifier. Limits 1, 3, 7 and 31 each returned `unknown` with the exact tested count, a valid witnessed lower bound and no maximum claim. The graph fixture with a parallel A/B edge and isolated-node loop returned A,B,C as a size-three maximum; edgeless two-node graph returned singleton A; empty graph returned the empty set in one test.

The verifier rejected a group with a missing pair edge, a valid but nonmaximum singleton falsely labeled maximum, and a false completed-count claim. Duplicate node IDs, unknown endpoint, malformed string and short-tuple edge records, repeated edge IDs and zero budget were rejected. `sf.validate_text` returned zero errors and warnings. The supplied verifier explicitly does not prove exact prefix fidelity for an arbitrary `unknown` result; the skill states that limit and requires an execution trace if prefix fidelity matters.

## Ordinary scenario

```text
Scope: Fictional Cedar C1; five inventoried nodes; complete undirected exercise projection.
Adjacency policy: Parallel ab/ab2 yield one A/B adjacency; I loop contributes no distinct-pair adjacency.
Search: 32 candidate subsets tested of budget 32; complete.
Verdict: Maximum proven.
Clique witness: A,B,C; size 3.
Verification: Each of AB, AC and BC has an edge; independent larger-set check found no clique of size 4 or 5.
Limits: I is isolated for clique purposes; no real-world group or importance inference.
Next action: Graph owner checks source completeness before using this structural result elsewhere.
```

## Missing-input scenario

```text
Scope: Node inventory, arrow projection and search budget unavailable.
Adjacency policy: Unresolved; no direction or loop rule silently chosen.
Search: Not executed.
Verdict: Unresolved.
Clique witness: Pending.
Verification: No pair replay or maximum check performed.
Limits: Edge count alone cannot establish node coverage or adjacency.
Next action: Owner supplies snapshot inventory, approved undirected projection and positive budget together.
```

## Edge/Test scenario

```text
Scope: Fictional Cedar T1; A/B/C triangle, C/D tail, isolated I, parallel A/B ID and I loop.
Adjacency policy: Parallel A/B records give one adjacency; I loop gives no distinct-pair link.
Search: First run 1 of 32 candidate subsets; second run all 32 of budget 32.
Verdict: First maximum unknown; second maximum proven.
Clique witness: First empty valid lower bound; second A,B,C, size 3.
Verification: Executed pair replay and completed larger-set check on second run; no four- or five-node clique.
Limits: Exercise inventory only; no social-group inference.
Next action: Graph owner checks snapshot completeness before operational use.
```

## Verdict

All five Test case assertions passed. The worked example's five vertices imply 32 subsets, and the reference returned the stated size-three clique. The complete search plus an independent larger-set check supports `maximum` for the frozen supplied graph. A one-node extension check would establish only inclusion-maximality; the skill correctly separates these claims. The example is fictional; no changing external fact, invented citation or scale guarantee appears. Recommend acceptance within the small finite undirected graph scope. No required repair found.
