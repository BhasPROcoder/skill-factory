# GRF-034 author evidence

## Scope comparison
Rejected first proposal, dependency order plus cycle witness, because actual SEQ-001 already returns a complete prerequisite-first order or explicit closed cycle; SEQ-003 likewise computes an order. No file or ID was allocated for that proposal. For the replacement, sf.py search for “dominator” found no entry. Actual GRF-029 procedure evaluates undirected single removals and newly lost surviving pairs. GRF-006 reports bounded directional reachability, while GRF-008 groups mutually reachable vertices and condenses them. GRF-004 validates an already declared rooted forest. GRF-034 instead computes the root-relative all-path dominator relation in a directed graph and verifies its immediate-parent tree independently by removal. This is a scoped comparison, not whole-library semantic uniqueness proof.

## Author execution
Reviewer found that the first verifier checked only strict-dominator membership and root termination; a forged parent D→R would pass despite A being closer. Repaired verification now derives dominators independently by vertex removal, requires every other strict dominator of a vertex to dominate its proposed parent, and rejects the D→R forgery in the embedded negative test. This is a verification repair; the builder's chosen parent was unchanged.
Procedure step 9 now states the same maximality check explicitly for readers executing the skill without the reference code.

Python 3.14.6 executed the embedded reference. Output:
```text
root-relative dominators and removal checks passed
3.14.6
```
This output is from the repaired snippet, including the explicit expected rejection of tampered parent D→R. A direct `sf.validate_text(text,path)` rerun returned empty errors and warnings.
Additional tests executed against the extracted embedded code:
```text
root-relative dominators and removal checks passed
{'parallel': True, 'cycle': True, 'direct_bypass': True, 'empty_edges': True, 'missing_root': True, 'unknown_endpoint': True, 'duplicate_id': True}
```
Direct `sf.validate_text(text,path)` returned empty errors and warnings. Body word count 1560 by the author’s whitespace-oriented regex; final registry validator should make its own determination. Registry untouched.

## Ordinary scenario
```text
Scope: Cedar exercise C1; root R; directed source-to-target links; supplied inventory complete for this exercise.
Reachable: R, A, B, C, D.
Unreachable: I.
Dominator sets: R | R; A | R,A; B | R,A,B; C | R,A,C; D | R,A,D.
Immediate parents: A | R; B | A; C | A; D | A.
Verification: Reference fixed-point and independent vertex-removal assertions executed for C1; parent chains reach R.
Limits: Exercise topology only; B and C each have a bypass to D, while A does not. No physical availability claim.
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

## Edge scenario
Fictional directed R→A has separate p1 and p2 IDs, A→B, B→A, and isolated I. The parallel records remain distinct source evidence while the vertex relation is `R | R; A | R,A; B | R,A,B`; immediate parents `A | R; B | A`; I remains unreachable. A directed cycle does not grant a route around A. The executed parallel and cycle assertions cover these features.

## Claim audit
Specific algorithmic claims: a vertex dominates a reachable target iff deleting it makes the target unreachable from the root; the root dominates every reachable target; immediate dominators form a parent tree for reachable vertices. These are stable finite directed graph properties, also checked in the implementation. Example IDs and graph are explicitly fictional. No current rates, standards, version promises, external citations or sourced statistics occur in the skill. Interpreter version is reported only here as observed test evidence, not hardcoded in the skill. Bounds: finite small graph; no production-scale or physical outage claim.
