# G04 candidate and author evidence

2026-11-12; author review_graph02. Candidate GRF-004 is held for independent review, not ingested or counted.

## Scope decision and selected-neighbor comparison

Narrowed the broad G04 structural-invariants card to rooted-forest contract validation. The deliverable is a verdict under explicitly supplied roots, complete local parent-count witnesses, full unreachable-node evidence, and evidence-dependent repair/recheck handoff. This avoids an omnibus graph-validator skill.

Read creation-order.md, SPEC.md, GRF-001 and GRF-003, and used sf.py searches for tree, forest, hierarchy and parent. Read SEQ-001 and ARC-002 after sf.py discovery. Relevant distinctions:

- GRF-001 designs model semantics and tests local loan-role counts. GRF-004 evaluates an existing parent graph against independently declared roots and catches disconnected components that satisfy local counts.
- GRF-003 preserves import rows/identity and reports input exceptions. GRF-004 assumes/requires a reconciled snapshot and determines a graph-wide property; its identity guards do not replace import reconciliation.
- SEQ-001 returns a dependency cycle witness or prerequisite order. GRF-004 does not duplicate its cycle-discovery procedure or order artifact; a disconnected-cycle fixture demonstrates the local-versus-global gap, and unreachable IDs plus parent evidence are its output.
- ARC-002 designs provenance-respecting archival placement, distinguishing containers from descriptive parents. GRF-004 makes no domain placement decisions and supplies an executable structural validation/repair-preview procedure.

No external code or skill content was copied. This candidate derives from the approved queue and catalog gap review. No claim of exhaustive semantic comparison across the entire library is made.

## Specific-claim self-review

Reviewed the rooted-forest condition (zero parent edges for declared roots, one for each other node, all nodes root-reachable), disconnected-cycle counterexample, singleton roots, self-loops, parallel edges, partial-extract limits and historical-parent warning. These are stable mathematical/procedural claims. The illustrative nonempty Python helper explicitly does not decide empty-graph policy or enforce a requested single-tree root count; the numbered procedure handles those contract choices separately. No current platform behavior, external threshold, source attribution or release currency is asserted.

Worked example W1 has four nodes and three edges; r reaches only r/a, and x/y form the disconnected region despite each non-root having one parent. No repair is chosen without evidence. The separate snippet's fictional authorized preview replaces y->x with r->x, retaining three edges, connecting all nodes, and passing the checks. Adding a->x creates two incoming edges at x; no edge is deleted automatically.

## Actual executed checks

Extracted the Python fence from the draft and executed it under Python 3.14.6. `tools.sf.validate_text` returned errors=[] and warnings=[]; body word count was 1530. This direct draft check is not registry validation status.

Observed output:

```text
disconnected-cycle, repaired-preview and multiple-parent checks passed
test-case, singleton, self-loop and 5 input-rejection cases passed
exhaustive 3-node directed graph/root-set cases passed: 3584
```

Extra assertions covered the published test case (R/S roots, A has p/t parents, all nodes reachable), singleton root, isolated non-root self-loop, and rejection of empty inventory, absent roots, unknown roots, unknown endpoint and repeated edge IDs.

Exhaustive bounded check enumerated the 512 possible directed edge subsets including self-loops on three nodes and each of seven nonempty root sets: 512 * 7 = 3584 cases. An independent oracle repeatedly removed zero-indegree nodes to detect cycles, then required maximum indegree one and exact equality between declared roots and zero-indegree nodes. Helper pass/fail matched that oracle in every enumerated case. This supports the finite fixture logic, not untested production scale, arbitrary malformed inputs or domain correctness.

Independent ordinary/missing/edge scenario review remains required before acceptance. No registry, index or shared status files were changed by this author.
