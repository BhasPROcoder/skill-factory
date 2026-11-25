# GRF-050 author evidence

Source scope: `plans/graph-g50-scope.md`. Read AGENTS.md and SPEC. Actual procedure comparisons: GRF-029 measures new connectivity loss among surviving nodes after hypothetical failure; GRF-014 tests database constraint enforcement; GRF-017 migrates identities reversibly; GRF-024 reconciles restored data. Cross-domain TDQ-006 tests parent/child key integrity, without relation-specific retirement disposition. `sf.py search` for retirement, record deletion, referential, cascade and dangling found no existing procedure producing the same incident-edge policy ledger and exact hypothetical graph inventory. This is scoped comparison, not whole-library uniqueness proof. No registry mutation or push.

Draft: `skills/GRF/graph-node-retirement-referential-preview/SKILL.md`; manifest: `staging/graph_g50.json`. `sf.validate_text(text, path)` returned zero errors and warnings. The embedded Python 3 snippet executed and printed `blocked, unresolved, parallel, loop and referential preview checked`. Additional calls:

```text
isolated I retirement: preview removes only I; all five original edges remain unchanged
duplicate edge ID: REJECT duplicate edge ID
unknown endpoint: REJECT unknown endpoint
string edge record: REJECT invalid edge record
stale snapshot: REJECT snapshot changed or missing
```

Ordinary cascade scenario:
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

Missing-policy scenario:
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

Blocked scenario:
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

Claim audit: example counts were checked against the executable inventory and results. `restrict` and `cascade` are fixture policy labels, not a claim about any installed database or legal retention rule. The skill uses fictional examples and makes no current product/API/version claim. Real storage behavior remains a verification step. Independent review is required before acceptance.
