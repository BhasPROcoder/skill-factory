# GRF-035 author evidence

Scope review: read AGENTS.md, SPEC.md, GOLD example; queried sf.py for transitive reduction/reachability and inspected actual GRF-006, GRF-008, GRF-015 and SEQ-001 procedures. Those respectively perform bounded seed traversal, strong-component condensation, query-plan equivalence and task-cycle diagnosis. None constructs an edge-minimal DAG view with all-pair reachability parity and final alternate-path witnesses. This is a scoped comparison, not proof against every catalog entry. No registry change.

Candidate: `skills/GRF/dag-reachability-reduction-certificate/SKILL.md`; manifest `staging/graph_g35.json`. `sf.validate_text(text, path)` returned `([], [])` after the final edit. Full embedded Python 3 snippet executed and printed `DAG reduction, parallel identities, isolates and cycle rejection checked`. Further independent calls produced:

```text
chain_skip retained ['ab','bc','cd']; final removal paths ac=(ab,bc), ad=(ab,bc,cd), bd=(bc,cd)
chain_skip reachable pairs (A,B),(A,C),(A,D),(B,C),(B,D),(C,D)
disconnected retained ['ab','xy']; reachable pairs (A,B),(X,Y); I isolated
parallel retained ['e2']; removed e1=(e2,); reachable pair (A,B)
self-loop REJECT cycle or self-loop: DAG required
two-edge cycle REJECT cycle or self-loop: DAG required
unknown endpoint REJECT unknown endpoint
duplicate edge ID REJECT duplicate edge ID
```

All retained graphs were compared by exact reachable-pair sets with originals. The extra chain fixture caught an initially stale decision-time path for ad; the skill and code were corrected to rebuild every removed-edge witness in the final retained graph, then rerun successfully. No fabricated external source, changing current value, API claim or statistic. Mathematical statements are confined to finite directed DAGs under the given structural reachability contract. Fictional example A→B→C has three original pairs and exactly three retained pairs; I is isolated.

Ordinary scenario output:
```text
Scope: Fictional Atlas S1; nodes A,B,C,I; directed edges ab,bc,ac; all eligible.
Eligibility: DAG confirmed.
Retained: ab,bc.
Removed: ac -> ab,bc.
Verification: Original and retained pairs both {(A,B),(A,C),(B,C)}; each retained edge essential.
Decision: Certified analysis reduction.
Limits: I remains isolated; no source record deletion or semantic-equivalence claim.
Next action: Use the retained IDs in the analysis view; ask the record owner before any source change.
```

Missing-input scenario output:
```text
Scope: Snapshot lacks node inventory and direction convention.
Eligibility: Unresolved; cannot check a DAG or complete node-pair reachability.
Retained: None computed.
Removed: None computed.
Verification: Not executed.
Decision: Unresolved.
Limits: Edge counts alone cannot establish paths or isolated nodes.
Next action: Request complete node/edge inventory, direction and snapshot identifier together.
```

Edge scenario output:
```text
Scope: Fictional Beacon T1 plus directed s R→P.
Eligibility: Cycle blocker P→Q→R→P using p,q,s.
Retained: None certified.
Removed: None certified.
Verification: DAG precondition failed; no reduction parity asserted.
Decision: Rejected for this DAG procedure.
Limits: Other semantic effects of cycle unexamined.
Next action: Resolve cycle policy before attempting DAG reduction.
```

Review repair: an independent reviewer found that a three-character string could pass the old edge-record shape check. `check_input` now requires each record to be a tuple or list of three nonempty strings. Re-executed the embedded snippet; it passed. Direct malformed-record checks rejected a string, a short tuple, and a mapping with `invalid edge record`. Final `sf.validate_text(text, path)` returned no errors or warnings. The earlier parent review should be repeated against the repaired file.

Ready for independent review; not accepted or counted by author.
