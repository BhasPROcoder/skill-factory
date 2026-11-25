# GRF-041 independent review

Reviewer g33_reviewer. Read SPEC, complete draft and author evidence, and actual procedures of GRF-009, GRF-010 and GRF-035. G09's reference admits nonnegative costs and routes signed edges elsewhere; G10 certifies flows and cuts; G35 removes reachability-redundant edges from a DAG. G41 addresses directed minimum-cost walks with signed integer weights and a relevant negative-cycle certificate. This is a scoped comparison, not whole-library uniqueness proof. Registry untouched.

## Execution evidence

Executed embedded Python under Python 3.14.6; it printed `finite route, irrelevant cycle and relevant cycle checked`. Independent fixtures and verifier results:

```text
S→T finite with irrelevant reachable X/Y negative cycle: cost 3, route sa,ab,bt; corridor A,B,S,T
S→T with added B→A cost 1: no finite minimum; approach sa, cycle ab,ba, exit ab,bt
source=target S with no edges: finite cost 0, empty route
source=target S with negative self-loop: no finite minimum, empty approach/exit, loop witness
unreachable T despite negative cycle elsewhere: unreachable
parallel zero-cost tied S→T edges: finite cost 0, deterministic e1 witness
short edge, string edge, Boolean weight, duplicate edge ID: REJECT invalid record/fields
tampered finite cost, route and label map: verifier rejects each
```

I independently implemented a guarded Floyd–Warshall oracle and compared 400 seeded three-node directed multigraph cases with signed integer weights and randomly selected terminals. State classification (unreachable, finite, or no finite minimum), finite optimum cost, and every returned certificate agreed with the oracle. The oracle guards unreachable operands, preventing false negative-cycle relevance from infinity arithmetic. The candidate's finite certificate has a route attaining the claimed cost plus labels satisfying all corridor edge inequalities. A closed negative cycle with a source approach and target exit proves unbounded improvement for walks. Cycles lacking a target exit are omitted from the corridor and do not change this target's verdict.

## Ordinary scenario

```text
Scope: Fictional Cedar C1; complete exercise directed inventory and one exact integer cost unit.
Terminals and walk policy: S to T; revisits allowed.
Corridor: S,A,B,T.
Verdict: Finite minimum.
Certificate: Cost 3; route sa,ab,bt.
Verification: Directed replay 4+(-3)+2=3; executed label inequalities across all corridor edges.
Limits: X/Y negative cycle is reachable from S but cannot reach T; I isolated. No outside-snapshot claim.
Next action: Owner checks any omitted X/Y exit before applying this result to another snapshot.
```

## Missing-input scenario

```text
Scope: Node/edge inventory and common cost unit unavailable.
Terminals and walk policy: S to T supplied; revisitation unresolved.
Corridor: Pending validated directed records.
Verdict: Unresolved.
Certificate: None computed.
Verification: No reachability, relaxation or replay executed.
Limits: Unlabeled costs and unknown walk policy cannot establish a minimum or cycle relevance.
Next action: Owner supplies complete inventory, exact cost unit and walk policy together.
```

## Edge/Test scenario

```text
Scope: Fictional Cedar C1 plus ba:B→A cost 1; all other records unchanged.
Terminals and walk policy: S to T; revisits allowed.
Corridor: S,A,B,T.
Verdict: No finite minimum.
Certificate: Approach sa; closed cycle ab,ba costs -3+1=-2; exit ab,bt.
Verification: Executed replay confirms source reaches A, A→B→A is negative, and A→B→T reaches target.
Limits: X/Y remains irrelevant to T; no real-world route or policy inference.
Next action: Owner reviews the ba record and walk policy before modeling a real task.
```

## Verdict

Recommend acceptance for finite directed signed-integer additive walk models with complete scoped inventory. Example arithmetic and Test case assertions match execution. No invented source, unstable value or unsupported operational conclusion found. Simple-path optimization and production scale are explicitly outside scope.
