# GRF-040 author evidence

## Scope comparison

The catalog search for `clique` returned zero lexical matches. Actual procedures of GRF-027, GRF-031 and GRF-037 were inspected. GRF-027 searches structural bijections between two directed graphs; GRF-031 decides whether one graph has a two-color partition or odd-cycle obstruction; GRF-037 peels vertices below a degree threshold. GRF-040 instead finds a complete mutual-adjacency subset and distinguishes an observed witness from a proven greatest-size clique. A k-core may contain vertices that are not all adjacent to each other, so the certificate is distinct. This is a scoped comparison, not proof of whole-catalog semantic uniqueness.

## Executed tests

The embedded Python 3 snippet executed and printed:

```text
bounded clique witness and completed maximum checked
```

An independent exhaustive four-node test enumerated all 64 undirected simple graphs, compared the completed solver's clique size with a separate brute subset oracle, and checked limits 1, 3 and 7 for each graph. It printed:

```text
bounded clique witness and completed maximum checked
exhaustive_four_node_graphs 64 budget_and_shape_checks_pass
```

Extra malformed edge-record string, mapping and short tuple; duplicate node, unknown endpoint and duplicate edge-ID cases all raised ValueError. `sf.validate_text(text,path)` returned empty errors and warnings with the saved path supplied. Registry untouched. The reference's returned `unknown` verifier checks the witnessed clique and incomplete count, but not exact prefix fidelity; the skill says to retain the execution trace if that matters. No runtime benchmark or general-scale claim is made.

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

## Claim audit

The mathematical claims are stable: every distinct pair must be adjacent in a clique; a valid clique that cannot add one node is inclusion-maximal but need not be maximum; complete subset enumeration with a separately checked no-larger-set condition supports maximum size for the supplied projection. The worked graph is explicitly fictional. It has five vertices and therefore 32 subsets; its A/B/C triangle has three pair links, while D only links C and I only has a loop. The completed reference returns A/B/C as size three. No current price, law, software API/version promise, source quote, citation or externally attributed statistic appears in the skill. Interpreter version was not hardcoded. No registry change or push was performed by this author.
