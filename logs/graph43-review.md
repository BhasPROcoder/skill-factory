# GRF-043 independent review

Reviewer g33_reviewer. Read SPEC, complete draft and author evidence; inspected actual SEQ-001 and GRF-035 procedures and queried sf.py. SEQ-001 finds one cycle or a prerequisite order; GRF-035 assumes a DAG and removes reachability-redundant edges. G43 solves minimum-cardinality removal across all directed cycles in the supplied finite graph. This is a scoped distinction, not whole-catalog uniqueness proof. Registry untouched.

## Execution evidence

Executed the sole embedded Python block under Python 3.14.6; it printed `minimum feedback set, cutoff and independent DAG checks passed`. I built an independent brute-force oracle using directed reachability closure to decide whether each residual has a self-reachable node. This does not use the candidate's Kahn or DFS DAG methods. Results:

```text
two disjoint cycles (A↔B and C loop): removed ab,loop; count 2; examined 6; oracle 2
parallel p1,p2 A→B and ba B→A: removed ba; count 1; examined 2; oracle 1
acyclic A→B with isolate I: empty removal; count 0; oracle 0
empty edge inventory: empty removal; count 0; oracle 0
disconnected A↔B and C↔D: removed ab,cd; count 2; oracle 2
one-candidate cutoff on A↔B: unknown; examined 1; next ('ab',)
bad zero budget: REJECT positive integer candidate budget required
string-shaped edge: REJECT invalid edge record
unknown endpoint: REJECT unknown endpoint
duplicate edge ID: REJECT duplicate edge ID
all 16 simple two-node directed graphs including possible loops: candidate count equals independent oracle
tampered removal of ab only in two-cycle fixture: residual DAG check false (C loop remains)
tampered removal of all three records: residual DAG true, but smaller optimum of 2 exists
```

These checks distinguish a feasible cycle break from a minimum one: residual acyclicity alone accepts the over-removal, but enumeration of every smaller subset rejects its minimum claim. The candidate verifies a chosen residual with independent DFS and explicitly tests every smaller set. Budget exhaustion returns unknown before an untested candidate, with no optimum assertion. Its guarantee applies only to cardinality, not edge costs, protected records or deletion authority.

## Ordinary scenario

```text
Scope: Fictional Rowan R1; complete exercise nodes A/B/C/I and directed ab A→B, ba B→A, loop C→C.
Search: Budget 20 subsets; 6 examined; IDs sorted ab,ba,loop.
Status: Complete minimum.
Proposed removed IDs: ab,loop; count 2.
Residual evidence: ba remains and I isolated; independent DAG check executed and passed; original records retained.
Minimum proof: Empty and all three one-edge subsets remained cyclic; first tested feasible two-edge set found.
Limits: One of multiple count-optimal choices; no source deletion or owner approval.
Next action: Relationship owners review meanings and constraints before a separate correction.
```

## Missing-input scenario

```text
Scope: Node inventory, edge IDs and arrow direction unavailable.
Search: Candidate budget unresolved; zero examined.
Status: Unknown.
Proposed removed IDs: Unresolved.
Residual evidence: No graph checked.
Minimum proof: Not established.
Limits: Edge-ID universe and removal unit undefined.
Next action: Owner supplies directed inventory, unique edge IDs and a candidate budget.
```

## Edge/Test scenario

```text
Scope: Fictional A/B with p1,p2 A→B and ba B→A, complete directed exercise inventory.
Search: Budget 10 subsets; 2 examined; IDs sorted ba,p1,p2.
Status: Complete minimum.
Proposed removed IDs: ba; count 1.
Residual evidence: p1,p2 remain as parallel forward edges; independent DAG check executed and passed.
Minimum proof: Empty set cyclic; first one-edge candidate ba makes residual acyclic.
Limits: Other source meanings and edit authority unexamined.
Next action: Owner checks whether ba may be changed before any real edit.
```

## Verdict

Recommend acceptance for bounded finite directed graphs under one-edge-ID removal and minimum-count objective. Worked example arithmetic (6 examined candidates) and Test case assertions match execution. No invented source or changing value appears. Production scale, weighted/protected choices and operational authority are explicit exclusions.
