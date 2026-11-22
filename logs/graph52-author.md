# GRF-052 author evidence

Scope card: `plans/graph-g52-scope.md`. Read AGENTS.md and SPEC. Compared actual GRF-006, GRF-021 and TSC-002 procedures. GRF-006 traverses bounded filtered graphs but does not apply principal-specific node and edge grants or test hidden-record response stability; GRF-021 builds evidence packets; TSC-002 reviews action grants rather than graph path exposure. This is a scoped distinction, not whole-catalog uniqueness proof. No registry mutation or push.

Draft: `skills/GRF/authorized-graph-traversal-exposure-check/SKILL.md`; manifest: `staging/graph_g52.json`. Final `sf.validate_text(text, path)` returned zero errors and warnings. Complete embedded Python 3 snippet executed and printed `granted paths, denied edge and hidden-record comparison checked`. Additional direct calls:

```text
P1 grants nodes A,B,C and edge ab only: {A:(), B:(ab,)}; C absent
grant bc as well: {A:(), B:(ab,), C:(ab,bc)}
privileged principal: A,B,H,C reachable with permitted paths
invisible H seed: REJECT invisible seed
unknown edge grant: REJECT unknown grant ID
string edge record: REJECT invalid edge record
unknown endpoint: REJECT unknown endpoint
duplicate edge ID: REJECT duplicate edge ID
```

Ordinary scenario:
```text
Scope: Fictional Harbor; principal P; graph S1/S2 and policy P1; isolated authorized fixture.
Query: Seed A; outgoing; no depth cutoff; node IDs and edge-ID paths.
Projection: Granted nodes A,B,C; granted edge ab.
Visible result: A -> empty path; B -> ab. C absent.
Verification: Both paths replay against grants; authorized reached set is {A,B}.
Hidden-change comparison: S1 and S2 visible maps equal, {A:(), B:(ab)}.
Decision: Fixture passed.
Limits: No timing, error, cache or production enforcement tested; verify current owner policy.
Next action: Ask the security owner to review this fixture before target-engine adaptation.
```

Missing-input scenario:
```text
Scope: Principal and graph supplied, but no owner-approved node/edge grants or applicable jurisdiction/policy revision.
Query: Seed A; outgoing; result fields pending.
Projection: Unresolved; no inferred grants.
Visible result: None computed.
Verification: Not run without approved grant sets.
Hidden-change comparison: Not run.
Decision: Unresolved.
Limits: Topology cannot establish authorization.
Next action: Ask the owner for current policy, jurisdiction and exact grants before running an isolated fixture.
```

Edge scenario:
```text
Scope: Fictional Harbor P1; nodes A,B,C,H; edges ab,ah,hc,bc; A,B,C granted, H denied; ab granted, bc denied.
Query: Seed A; outgoing; no depth cutoff; node IDs and edge-ID paths.
Projection: Granted nodes A,B,C and edge ab; denied bc connects visible endpoints.
Visible result: A -> empty path; B -> ab. C absent.
Verification: ab replays; bc excluded by edge grant; hidden H path excluded.
Hidden-change comparison: Adding denied B→H leaves the visible map equal in this fixture.
Decision: Fixture passed.
Limits: Result-map parity does not test timing, errors, caches or actual target enforcement.
Next action: Review the same contract with the owner-approved target-engine fixture.
```

Claim audit: all facts about the fixture are from executed Python. Graph and principal names are fictional. Current security policy, jurisdiction-specific requirements and target-engine behavior are inputs or explicit verify steps, not hardcoded. No production-wide noninterference claim is made. Independent review required before acceptance.
