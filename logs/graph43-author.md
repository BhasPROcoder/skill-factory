# GRF-043 author evidence

## Distinctness
sf.py catalog search for “feedback edge” found no corresponding graph entry. Actual SEQ-001 returns one prerequisite cycle witness or an order; it does not optimize a globally cycle-breaking edge-ID set. Actual GRF-035 starts with an acyclic graph and removes redundant edges while preserving all pair reachability. GRF-043 instead starts with possibly cyclic directed data and performs bounded exact minimum-cardinality cycle breaking. This is scoped comparison, not proof against every library skill.

## Execution
Direct sf.validate_text(text,path) returned empty error and warning lists. Embedded Python ran under observed Python 3.14.6; body whitespace count was 1663:
```text
minimum feedback set, cutoff and independent DAG checks passed
3.14.6
words 1663
```
Additional extracted-code fixtures:
```text
minimum feedback set, cutoff and independent DAG checks passed
{'parallel': True, 'selfloop': True, 'acyclic': True, 'cutoff': True, 'disconnected': True, 'bad_limit': True, 'string_edge': True, 'unknown_endpoint': True, 'dup_id': True}
```
Registry untouched.

## Ordinary scenario
```text
Scope: Rowan exercise R1; nodes A/B/C/I and directed records ab,ba,loop; supplied inventory complete for this exercise.
Search: Budget 20 subsets; 6 examined; edge IDs sorted ab,ba,loop.
Status: Complete minimum.
Proposed removed IDs: ab, loop; count 2.
Residual evidence: ba remains, I isolated; independent DAG check executed and passed; original records retained.
Minimum proof: Empty set and all three one-edge subsets were tested and remained cyclic.
Limits: One of multiple possible two-edge choices; count-only structural result, no owner approval to delete.
Next action: Relationship owners review edge meanings and constraints before considering a separate correction.
```

## Missing-input scenario
```text
Scope: Node inventory, direction and edge IDs unavailable.
Search: Candidate budget unresolved; zero examined.
Status: Unknown.
Proposed removed IDs: Unresolved.
Residual evidence: No graph checked.
Minimum proof: Not established.
Limits: The edge-ID universe and removal unit are undefined.
Next action: Owner supplies directed inventory, edge identities and candidate budget.
```

## Edge scenario
Fictional graph has parallel p1,p2:A→B and ba:B→A. Exact one-edge set {ba} breaks both cycles; removing only p1 or p2 does not. The executed parallel fixture checked the returned set. A separate self-loop fixture required its one edge; a candidate limit of one stopped after testing the empty set and returned unknown, not minimum.

## Claim audit
Specific claims: a complete test of all smaller edge-ID subsets plus an acyclic chosen residual proves minimum cardinality; adding one self-loop creates a directed cycle requiring removal for a DAG; parallel source records are distinct removal units; an early cutoff does not establish optimality. These are stable finite graph properties verified by subset enumeration, Kahn's method, independent DFS and extra fixtures. Example group is fictional and counts (empty set, three one-edge subsets, two two-edge tests = six) were recomputed by execution. No current legal, price, API, version promise, invented citation or statistic appears in the skill. Interpreter version here is observed execution evidence only. No business authorization or production-scale claim.
