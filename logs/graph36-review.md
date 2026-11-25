# GRF-036 independent review

Reviewer `g32_reviewer`. Read SPEC, complete draft and author evidence; inspected actual GRF-031 and SVC-001 procedures. GRF-031 decides unrestricted two-color bipartition with a possible odd-cycle witness. SVC-001 reconciles actual booking-resource occupancy. GRF-036 decides finite-palette graph coloring with per-node restrictions, complete search evidence and cutoff uncertainty. This is a scoped distinction, not a whole-library uniqueness proof. Registry untouched.

## Executed evidence

Executed the complete embedded Python 3 snippet under Python 3.14.6; its coloring, exhaustive failure, cutoff and self-loop assertions passed. Independently enumerated all eight simple undirected graphs on three nodes, every allowed-color subset for each node under palette `{0,1}`, and limits 1, 2, 3 and 100: 2,048 solver cases. A separate brute-force assignment oracle checked that every feasible return was a complete allowed edge-valid map, no infeasible return hid a valid map, and every limit-100 outcome matched feasibility. Results: 135 feasible, 1,349 infeasible and 564 unknown. Infeasible returns came from direct empty allowed sets or completed search, never a cutoff.

Additional executed fixtures: parallel A/B edges gave A=0, B=1 in three states; a loop returned infeasible in zero states; one isolate was assigned in two states; the empty graph returned an empty coloring in one state; adjacent singleton colors both fixed at zero exhausted in two states. Missing allowed-map entry, color outside palette, unknown endpoint, duplicate edge ID, zero limit and Boolean palette label were rejected with `ValueError`. For any returned coloring, the reference itself independently checks complete node coverage, allowed membership and every supplied edge inequality. A forged incomplete, disallowed or same-color map would fail those checks; the function does not expose a separate API for externally submitted certificates. `sf.validate_text` returned zero errors and zero warnings.

## Ordinary scenario

```text
Scope: Fictional Cedar S1; A,B,C,I; undirected ab,bc,ca; palette {0,1,2}; A={0}, others={0,1,2}.
Search: Nodes A,B,C,I; ascending allowed colors; limit 100; completed after 5 states.
Verdict: Feasible.
Certificate: A=0, B=1, C=2, I=0.
Verification: All four nodes covered; colors allowed; ab,bc,ca cross different colors.
Limits: I is isolated; color labels have no scheduling meaning.
Next action: Check real assignment constraints before using labels operationally.
```

## Missing-input scenario

```text
Scope: Node/edge inventory supplied; palette and undirected projection policy missing.
Search: Not run; no state budget used.
Verdict: Unresolved.
Certificate: None.
Verification: Color membership and conflict edges cannot be checked without the contract.
Limits: Direction and omitted restrictions can change feasibility.
Next action: Owner supplies exact palette and projection rule together.
```

## Edge/Test scenario

```text
Scope: Fictional Delta T1; P,Q,R triangle and isolated I; palette {0,1}, all nodes allowed both.
Search: Nodes I,P,Q,R; ascending allowed colors; limit 100; exhaustive search completed.
Verdict: Infeasible.
Certificate: Completed search; no allowed two-color assignment.
Verification: Independent assignment enumeration finds no map satisfying all three triangle edges.
Limits: Only supplied undirected constraints assessed; no scheduling policy inferred.
Next action: Ask owner whether palette or conflict contract can change.
```

The same triangle with palette `{0,1,2}`, P fixed to 0 and a sufficient limit returns a complete valid assignment including I. With limit 1 it returns `unknown`, so the Test case's cutoff assertion is met.

## Verdict

All four Test case assertions are supported. The worked example's five entered states and map match the executed reference; its fictional arithmetic and counts are consistent. No time-changing factual claim, invented source or platform promise appears. Recommend acceptance within the finite, supplied-graph scope. No required repair found.
