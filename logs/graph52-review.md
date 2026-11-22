# GRF-052 independent review

Reviewer `g32_reviewer`. Read the G52 scope card, SPEC, full draft and author evidence; inspected actual Procedure sections of GRF-006, GRF-021 and TSC-002. Those address ordinary bounded traversal, evidence-path packets and role/action permission matrices. GRF-052 checks per-principal node and edge grants before graph traversal and tests visible-result parity when only denied records change. This is a scoped distinction, not whole-library uniqueness proof. Registry untouched.

## Executed evidence

Executed the complete Python 3 reference under Python 3.14.6; its assertions printed `granted paths, denied edge and hidden-record comparison checked`. In the base fixture, grants A/B/C plus edge ab returned only A and B; C remained absent despite being a visible endpoint because both the hidden-H route and bc edge were denied. Adding denied B→H preserved the entire visible mapping. Granting bc as well produced permitted path ab,bc to C. Granting every node and edge produced a C route for a privileged principal. Invisible H seed, unknown edge grant, unknown node grant, malformed string edge, unknown endpoint and duplicate edge ID were rejected.

Independently generated 400 directed graph/grant fixtures. A separate authorized-edge reachability calculation matched every returned node key, while a path replay checked that every returned edge ID was granted, endpoints were granted and each hop followed the directed source record. A separate submitted-result replay rejected a hidden-intermediary path, a denied-edge path, a discontinuous path and an incomplete result map. The reference verifies its own generated paths and complete authorized reached set; it is not a callable verifier for externally supplied paths. `sf.validate_text` returned zero errors and warnings.

## Ordinary scenario

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

## Missing-input scenario

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

## Edge/Test scenario

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

## Verdict

All five Test case assertions pass. The skill requires owner-approved current grants and jurisdiction/policy context, with a verification placeholder for the target engine. It claims only fixture-level equality for returned node/path fields; it explicitly excludes broader side channels and production enforcement. All example entities are fictional and no changing security rule or invented source is hardcoded. Recommend acceptance within the isolated, authorized fixture scope. No required repair found.
