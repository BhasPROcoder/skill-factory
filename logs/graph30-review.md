# GRF-030 independent recovery review
Coordinator independently read complete saved draft and actual GRF-006/015 Procedure and reference boundaries. G06 records each node once for relation-filtered reachability; G15 verifies query result multiplicity while tuning storage access. G30 instead tracks node/rule-state pairs for order-sensitive walk acceptance with state-pair boundary evidence. A distinct procedure and output, not plain reachability relabeling. No prior author test results assumed.

Executed embedded code plus depth-two boundary (A/s2,e3,C/done omitted), one-node cyclic rule/graph with accepting start (one pair, empty witness, exhausted), negative/Boolean/fractional depth rejection and duplicate transition rejection. All passed. Embedded fixture verifies post-back revisit and initial direct-finish rejection. Reference computes one minimum-edge endpoint witness; no exact-length or simple-path claim.

Ordinary/Test scenario:
```text
Scope: Fictional F1; A seed; complete exercise graph.
Rule contract: s0-out-s1-back-s2-finish-done; start s0, accept done; repeated-node outgoing walks; depth 3.
Accepted: C | done | e1,e2,e3.
State evidence: A/s0=0; B/s1=1; A/s2=2; C/done=3.
Boundary: None; bounded computation completed and product-state region exhausted.
Verification: Embedded search and witness continuity/rule sequence checked.
Limits: Direct finish at s0 rejected; no all-walk enumeration or domain-fact inference.
```
Missing-input scenario:
```text
Scope: Supplied graph; seed unresolved.
Rule contract: Transition contract and depth absent.
Accepted: None searched.
State evidence: None computed.
Boundary: Execution not started.
Verification: Pending seed and approved rules.
Limits: Which exact seed applies? Which finite transitions/start/accept states apply? What depth and repeated-walk policy are approved? No absence conclusion.
```
Edge scenario:
```text
Scope: Fictional F1 seed A, complete exercise graph.
Rule contract: Same three-step rule; depth 2.
Accepted: None within depth 2.
State evidence: A/s0=0; B/s1=1; A/s2=2.
Boundary: A/s2 via e3 reaches unseen C/done; bounded search complete, unrestricted state reachability not exhausted.
Verification: Independent depth-two assertion executed.
Limits: Omitted state has supplied acceptance here, but no endpoint witness within the approved depth. No general absence or all-walk claim.
```
All four Test case assertions satisfied; example fields align, stable finite-state claims supported, no current external facts. Shape validation, complete adjacency and approved semantics remain caller duties. Accept within declared deterministic transition/walk scope; no required repairs.
