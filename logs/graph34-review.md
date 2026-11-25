# GRF-034 independent review — accepted recommendation

Reviewer `g32_reviewer`. Read complete candidate and author log. Embedded Python executed under Python 3.14.6. Independently compared its dominator sets with an exhaustive simple-path oracle for all 4,096 directed simple graphs on four vertices; all matched. Separate fixtures passed for a parallel-edge cycle with an isolate, a direct bypass, empty edges, unknown root, duplicate IDs, unknown endpoint and malformed edge records. Registry untouched.

## Repaired certificate gap

The initial code constructed the correct immediate parent, but its subsequent parent-certificate checks only required strict membership and a chain to the root. A corrupted sample certificate with `parent['D']='R'` passed those checks although `A` is the true immediate dominator. The author repaired the code and Procedure step 9 to require that every other verified strict dominator of a child also dominates its proposed parent. The reference now accepts a supplied parent map and rejects the forged `D→R` map, an incomplete map, a self parent and an unknown parent. I reran these independent tests after the repair: all four corrupt maps were rejected. A 4,096-graph exhaustive comparison with a separately implemented simple-path oracle passed again, including acceptance of each computed parent map as a supplied certificate. Structural `sf.validate_text` returned zero errors and warnings after repair.

## Ordinary scenario

```text
Scope: Fictional Cedar exercise C1; root R; directed source-to-target links; supplied inventory complete for the exercise.
Reachable: R, A, B, C, D.
Unreachable: I.
Dominator sets: R | R; A | R,A; B | R,A,B; C | R,A,C; D | R,A,D.
Immediate parents: A | R; B | A; C | A; D | A.
Verification: Fixed-point, independent removal and immediate-parent maximality checks executed; forged D→R rejected.
Limits: Exercise topology only; no physical availability claim.
Next action: Graph owner reviews source links and any omitted bypasses before using A as a structural gate.
```

## Missing-input scenario

```text
Scope: Root, arrow semantics and complete node inventory unavailable.
Reachable: Pending.
Unreachable: Pending.
Dominator sets: Pending.
Immediate parents: Pending.
Verification: No graph computation executed.
Limits: Without a root and directed inventory, no path population is defined.
Next action: Owner supplies root ID, directed edge records and scoped node inventory together.
```

## Edge/Test scenario

```text
Scope: Fictional F2; root R; directed p1/p2: R→A, ab: A→B, ba: B→A, isolated I.
Reachable: R, A, B.
Unreachable: I.
Dominator sets: R | R; A | R,A; B | R,A,B.
Immediate parents: A | R; B | A.
Verification: Parallel and cycle fixture executed; parent maximality check executed.
Limits: Parallel edges remain distinct source records; the cycle does not bypass A.
Next action: Owner checks source inventory before any operational use.
```

## Verdict

The repaired candidate passes the five Test case assertions. The review covers the declared root, directed snapshot and small finite-graph contract. GRF-006 addresses bounded traversal, GRF-008 strongly connected regions, GRF-029 undirected removal sensitivity and GRF-004 validation of a declared rooted forest; the dominator sets and independently checked immediate-parent certificate are a distinct output. This is scoped overlap evidence, not proof of whole-library uniqueness. The example is fictional; its sets and parent assignments match the executed reference. No changing external fact or invented source is present. Recommend acceptance; registry remains untouched by this reviewer.
