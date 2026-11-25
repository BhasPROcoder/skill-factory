# GRF-035 independent review

Reviewer g33_reviewer. Read AGENTS, SPEC, the complete candidate and author evidence, plus actual procedure sections of GRF-006, GRF-008, GRF-015 and SEQ-001. The neighbors perform bounded traversal, component condensation, query-plan equivalence and prerequisite-cycle diagnosis. G35 instead removes redundant identities from an acyclic directed view and certifies complete reachable-pair parity and final alternate-edge paths. This comparison is scoped; no entire-catalog uniqueness claim. Registry untouched.

## Execution evidence

Executed the full embedded Python under Python 3.14.6; it printed `DAG reduction, parallel identities, isolates and cycle rejection checked`. Independently reran these fixtures after the input-shape repair, comparing exact reachable pair sets and replaying each final removal witness against retained edges:

```text
redundant: retained ab,bc; removed ac=(ab,bc); pairs (A,B),(A,C),(B,C)
cover: retained ab,bc; none removed; pairs (A,B),(A,C),(B,C)
parallel: retained e2; removed e1=(e2); pair (A,B)
disconnected with isolated I: retained ab,xy; pairs (A,B),(X,Y)
chain skips: retained ab,bc,cd; ac=(ab,bc), ad=(ab,bc,cd), bd=(bc,cd); six original and retained ordered pairs
two-edge cycle: REJECT cycle or self-loop: DAG required
self-loop: REJECT cycle or self-loop: DAG required
unknown endpoint: REJECT unknown endpoint
duplicate edge ID: REJECT duplicate edge ID
malformed three-character string record: REJECT invalid edge record
malformed mapping record: REJECT invalid edge record
short tuple record: REJECT invalid edge record
```

Initial review found the string-record defect: the earlier `len(e)==3` check silently accepted a three-character string as an edge. The author repaired `check_input` to require a tuple or list of three string fields. I inspected the changed condition and reran embedded and malformed-record fixtures; all now behave as declared.

The independent witness replay checks each path identity exists among final retained edges, follows directed endpoints in order, and ends at the removed edge's target. A deliberately incorrect witness would fail that replay; the reference returns its own witnesses and does not expose a standalone arbitrary-certificate validator. Its pair comparison uses exact sets rather than matching counts.

## Ordinary scenario

```text
Scope: Fictional Atlas S1; nodes A,B,C,I; directed edges ab,bc,ac; all eligible.
Eligibility: DAG confirmed.
Retained: ab,bc.
Removed: ac -> ab,bc.
Verification: Original and retained pairs both {(A,B),(A,C),(B,C)}; each retained edge essential.
Decision: Certified analysis reduction.
Limits: I remains isolated; no source record deletion or semantic-equivalence claim.
Next action: Use retained IDs in the analysis view; consult the record owner before a source change.
```

## Missing-input scenario

```text
Scope: Node inventory and direction convention unavailable; snapshot unconfirmed.
Eligibility: Unresolved; DAG status cannot be checked.
Retained: None computed.
Removed: None computed.
Verification: No complete pair set or witness calculation run.
Decision: Unresolved.
Limits: Counts alone cannot establish paths or isolated nodes.
Next action: Request node and identified edge inventory, direction rule and snapshot ID together.
```

## Edge/Test scenario

```text
Scope: Fictional Beacon T1: P→Q (p), Q→R (q), P→R (r), isolated I; changed scenario adds R→P (s).
Eligibility: T1 DAG confirmed; changed scenario has cycle P→Q→R→P using p,q,s.
Retained: T1 p,q; none certified for changed scenario.
Removed: T1 r -> p,q; none certified for changed scenario.
Verification: T1 original and retained pairs {(P,Q),(P,R),(Q,R)}; changed scenario rejected before reduction.
Decision: Certified analysis reduction only for T1; changed scenario rejected by DAG precondition.
Limits: I remains isolated; no source deletion or semantic-equivalence claim.
Next action: Resolve cycle policy before any analysis reduction of changed scenario.
```

## Verdict

Recommend acceptance after the recorded input-shape repair. The worked example and Test case arithmetic are consistent, the positive and negative fixtures pass, and no changing value, invented source or unsupported business deletion claim appears. The result is scoped to a complete finite DAG projection; runtime scalability and semantic interchangeability remain outside its guarantee.
