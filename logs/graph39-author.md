# GRF-039 author evidence

## Distinctness
sf.py search for “reachability change” surfaced GRF-035 and no single-edge insertion delta. Actual GRF-006 computes bounded traversal from one seed, not complete before/after ordered-pair change. Actual GRF-029 compares undirected connectivity loss after one removal, including surviving-pair population. Actual GRF-035 removes redundant edges from an acyclic graph while preserving all existing pair reachability. G39 handles one proposed directed insertion, allows cycles, and enumerates gained ordered pairs with paths through the inserted edge. This is a scoped comparison, not a whole-library uniqueness claim.

## Execution
Direct sf.validate_text(text,path) returned empty error and warning lists. Embedded reference executed under observed Python 3.14.6; body word count 1596 by whitespace count:
```text
directed addition delta, witnesses and closure checks passed
3.14.6
words 1596
```
Additional extracted-code cases:
```text
directed addition delta, witnesses and closure checks passed
{'parallel_empty': True, 'cycle_self': True, 'empty_nonloop': True, 'isolate': True, 'duplicate': True, 'unknown': True, 'string': True}
```
Registry untouched.

## Ordinary scenario
```text
Scope: Maple exercise M1; A/B/C/D/I, directed links, supplied inventory complete for this exercise.
Proposed edge: bc, B→C; hypothetical only.
Gained pairs: A,C | ab,bc; A,D | ab,bc,cd; B,C | bc; B,D | bc,cd.
Lost pairs: None.
Checks: Embedded reference exact pair-set comparison and witness replay executed for M1.
Limits: Exercise graph only; I remains isolated. No relationship creation or access permission approved.
Next action: Graph owner verifies the proposed bc source meaning before any separate change request.
```

## Missing-input scenario
```text
Scope: Baseline node inventory and arrow meaning unavailable.
Proposed edge: Pending distinct ID and existing endpoints.
Gained pairs: Pending.
Lost pairs: Pending.
Checks: No pair comparison executed.
Limits: Without one frozen node universe and directed semantics, a before/after relation is undefined.
Next action: Owner supplies baseline nodes, edge records, direction and proposed edge together.
```

## Edge scenario
Fictional graph has A→B with edge ab; proposed ba:B→A closes a cycle. New ordered pairs are B→A, A→A and B→B under the nonempty-path convention; no old pair is lost. The executed cycle_self assertion checked this exact set. A parallel A→B proposal in a separate fixture yielded no new pair.

## Claim audit
Specific graph claims: appending an edge cannot remove a previously existing directed path in an unchanged node universe; a genuinely gained path must traverse the inserted edge; closure includes self-pairs only through a nonempty cycle or loop under the chosen convention. These are stable finite graph properties and are checked by independent pair-set recomputation and witness replay. Examples are fictional, arithmetic is simple set enumeration, and no current law, price, API, version promise, invented citation or statistic appears in the skill. Interpreter version here is observed test evidence only. No production-scale or access-authorization claim is made.
