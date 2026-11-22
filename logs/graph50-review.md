# GRF-050 independent review

Reviewer `g32_reviewer`. Read the G50 scope card, SPEC, full draft and author evidence; inspected actual Procedure sections of GRF-029, GRF-014, GRF-017, GRF-024 and TDQ-006. GRF-029 measures connectivity loss after hypothetical undirected failure, GRF-014 verifies storage constraints, GRF-017 migrates identities, GRF-024 reconciles a restore, and TDQ-006 compares parent/child references. GRF-050 instead resolves directed incident edge IDs against relation-specific retirement policies and checks the exact hypothetical surviving inventory. This is scoped comparison evidence, not whole-library uniqueness proof. Registry untouched.

## Executed evidence

Executed the full Python 3 reference under Python 3.14.6; it printed `blocked, unresolved, parallel, loop and referential preview checked`. The fictional base fixture returned blocked with e3 under `owned=restrict`, unresolved with e3 when the owned policy was absent, and a cascade preview removing B and precisely e1/e2/e3/e4 while retaining e5 C→A and isolate I. The B→B loop appeared once in the removed-ID ledger; two A→B parallel IDs stayed separate. Retiring isolated I removed only I and kept all five edges unchanged.

Independently generated 300 directed graph fixtures with link/owned/other relation types and partial restrict/cascade policy maps. A separately calculated incident-ID set and policy precedence matched every blocked, unresolved or preview outcome; every preview preserved precisely the unrelated original edge records and nodes. Stale revision, unknown target, duplicate edge ID, unknown endpoint, malformed edge row and invalid policy were rejected. An independent submitted-result replay accepted the valid preview and rejected a missing removed ID, collateral removal of e5, rewriting e5's direction/payload, and leaving original B incident edges in the survivor set. The reference does not expose a callable submitted-result verifier, but its internal assertions and the review replay cover the same invariants. `sf.validate_text` returned zero errors and warnings.

## Ordinary scenario

```text
Scope: Fictional Vale S complete exercise; target B; 4 nodes and 5 edge IDs.
Policy: link -> cascade; owned -> cascade.
Incident ledger: e1 A→B link remove; e2 A→B link remove; e3 B→C owned remove; e4 B→B link remove once.
Decision: Verified hypothetical preview.
Survivors: Nodes A,C,I; edge e5 C→A.
Verification: Removed IDs equal {e1,e2,e3,e4}; e5 unchanged; both endpoints of e5 survive.
Limits: Source records unchanged; owner approval and real transaction checks outstanding.
Next action: Send the exact ledger and preview to the relation owners for approval.
```

## Missing-input scenario

```text
Scope: Fictional Vale S complete exercise; target B; 4 nodes and 5 edge IDs.
Policy: link -> cascade; owned -> unresolved.
Incident ledger: e1/e2/e4 link cascade proposed; e3 owned unresolved.
Decision: Unresolved, with e3 as missing-policy witness.
Survivors: Pending owner policy; no definitive inventory produced.
Verification: Incident identities enumerated; post-retirement checks pending.
Limits: Source records unchanged; no default owned-edge policy.
Next action: Ask the owned-relation owner to specify its disposition for e3.
```

## Edge/Test scenario

```text
Scope: Fictional Vale S complete exercise; target B; 4 nodes and 5 edge IDs.
Policy: link -> cascade; owned -> restrict.
Incident ledger: e1/e2/e4 link cascade proposed; e3 owned restrict.
Decision: Blocked, with e3 as restricting witness.
Survivors: Pending; no definitive retirement preview produced.
Verification: All four incident IDs identified; e4 counted once; no post-retirement state claimed.
Limits: Source records unchanged.
Next action: Return the e3 policy conflict to the relation owner.
```

## Verdict

All four Test case assertions pass. The example is fictional and its incident/remaining record counts match execution. Restrict/cascade are explicit fixture policy labels, not claims about a live database or legal retention. No changing current fact or invented source appears. Recommend acceptance within the complete frozen-snapshot, hypothetical-preview scope. No required repair found.
