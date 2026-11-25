# GRF-039 independent review

Reviewer g33_reviewer. Read SPEC, complete candidate and author evidence, plus actual procedures of GRF-006, GRF-029 and GRF-035. G06 bounds one-seed traversal; G29 measures undirected loss after a removal; G35 removes redundant DAG edges while preserving reachability. G39 computes exact all-pair gain from one hypothetical directed insertion, including cycles and self-pairs. This is a scoped distinctness comparison, not proof against all library entries. Registry untouched.

## Execution evidence

Executed the sole embedded Python block under Python 3.14.6; it printed `directed addition delta, witnesses and closure checks passed`. Independently called the extracted routines on these fixtures and checked gained pairs against complete after-before sets, no lost pairs, directed witness continuity and presence of the proposed ID:

```text
new edge B→C between A→B and C→D: gains (A,C),(A,D),(B,C),(B,D)
cycle A→B plus B→A: gains (A,A),(B,A),(B,B)
parallel A→B insertion: gains none
self-loop on X: gains (X,X)
isolated I retained when A→B inserted: gain (A,B) only
unchanged old A→C pair when B→C inserted: gain (B,C) only
duplicate proposed edge ID: REJECT duplicate edge ID
unknown proposed endpoint: REJECT unknown endpoint
string-shaped baseline edge: REJECT invalid edge record
tampered A→C witness using only A→B: REJECT by endpoint and proposed-edge checks
```

The code uses independent closure recomputation for exact before and after ordered-pair sets; the extra fixture confirms an already reachable pair is excluded from gains. The witness loop confirms every claimed new path is continuous and uses the proposed edge. Its exhaustive method is explicitly scoped to small in-memory graphs, and it does not authorize a source relationship or access change.

## Ordinary scenario

```text
Scope: Fictional Maple M1; complete exercise nodes A/B/C/D/I and directed ab A→B, cd C→D.
Proposed edge: bc, B→C; hypothetical only.
Gained pairs: A,C | ab,bc; A,D | ab,bc,cd; B,C | bc; B,D | bc,cd.
Lost pairs: None.
Checks: Executed exact before/after pair-set comparison and every witness replay; all four gains contain bc.
Limits: Exercise graph only; I remains isolated. No source relationship creation or access approved.
Next action: Owner verifies the proposed edge's meaning before a separate change request.
```

## Missing-input scenario

```text
Scope: Baseline node inventory and arrow meaning unavailable.
Proposed edge: Pending distinct ID and existing endpoints.
Gained pairs: Pending.
Lost pairs: Pending.
Checks: No pair comparison or path replay executed.
Limits: No frozen universe or directed semantics means the delta is unresolved.
Next action: Owner supplies complete baseline nodes/identified edges, direction rule and proposed edge.
```

## Edge/Test scenario

```text
Scope: Fictional A/B directed ab A→B; proposed ba B→A, with unchanged node universe.
Proposed edge: ba, B→A; hypothetical only.
Gained pairs: A,A | ab,ba; B,A | ba; B,B | ba,ab.
Lost pairs: None.
Checks: Executed independent closure and witness replay; baseline (A,B) persists and is absent from the gain set.
Limits: Nonempty-path convention makes cycle self-pairs reachable; structural result grants no permission.
Next action: Owner reviews the proposed relationship before any source change.
```

## Verdict

Recommend acceptance within the declared complete directed snapshot and one-edge insertion scope. Worked example and Test case set arithmetic match executed results. No changing value, invented source or unsupported authorization claim found. Exactness depends on the supplied complete node/edge projection and the stated nonempty-path convention.
