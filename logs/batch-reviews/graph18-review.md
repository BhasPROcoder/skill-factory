# GRF-018 independent review

Reviewer: g18_independent_review. Date: 2026-11-14. Registry unchanged by reviewer.

Read AGENTS.md, SPEC.md and the complete selected skill. Queried sf.py descriptions for GRF-001, GRF-005 and GRF-017. The deliverable is a vocabulary release governing licensed inference, distinct from representation design, temporal reconstruction and reversible identifier migration. This is a scoped neighbor comparison, not a semantic audit of the whole library.

## Executed evidence

Extracted and executed the skill's Python block under Python 3.14.6. Its included assertions passed. Independently exercised a two-node transitive cycle (eight closure triples including reflexive contains facts), unlicensed peer chaining (two facts only), an unknown endpoint, duplicate source identity, wrong endpoint type, and two independent source records asserting the same triple. All checks passed. The last case confirms the documented compact map retains only one witness; the original source ledger must remain separate. Ran sf.py validate GRF-018 without --mark: PASS, 1/1.

## Scenario outputs produced during review

Ordinary input: fictional units A/B/C, direct r1 A contains B and r2 B contains C; contains has transitive and inverse-inside rules.

```text
Release: Fictional fixture V1; draft, owner not supplied.
Terms: contains | enclosure | aliases none | Unit->Unit | peer contact excluded; inside | inverse enclosure | aliases none | Unit->Unit | peer contact excluded.
Rules: contains | transitive and inverse-inside | supplied policy | arbitrary peer inference unsupported; inside | inverse-contains | supplied policy | no independent rule added.
Assertions: r1 | A contains B | accepted; r2 | B contains C | accepted.
Derived evidence: A contains C | transitive-contains | r1,r2; B inside A | inverse-contains | r1; C inside B | inverse-contains | r2; C inside A | inverse-contains | A contains C.
Fixture checks: ordinary closure executed; cyclic closure executed; peer counterexample executed.
Compatibility: prior consumers unavailable; compatibility pending.
Decision: Blocked for release approval pending named owner and consumer evidence; fictional fixture computation complete.
```

Missing-input request: “Make our graph vocabulary approved; no definitions, types or policy provided.”

```text
Release: Unversioned draft; approval unresolved.
Terms: Unresolved; no real meanings or class assignments invented.
Rules: No additional inference licensed by default.
Assertions: Unavailable; any future illustrative fixtures must be labeled fictional.
Derived evidence: None computed.
Fixture checks: Pending real contract; no validation claim.
Compatibility: Consumer inventory unavailable.
Decision: Blocked. Which terms and class definitions govern this graph? Who owns the release and which consumers use it? Which inference rules and evidence examples are approved?
```

Edge request: fictional peer assertions r1 A peer B and r2 B peer C; consumer demands inferred A peer C as observed.

```text
Release: Fictional peer fixture; draft, approval unresolved.
Terms: peer | direct supplied peer statement | aliases none | Unit->Unit | a chained path is not a direct statement.
Rules: peer | none additional | supplied policy | inverse and transitive inference unlicensed.
Assertions: r1 | A peer B | accepted; r2 | B peer C | accepted.
Derived evidence: None; neither A peer C nor B peer A was generated.
Fixture checks: Executed, two direct facts retained.
Compatibility: Proposed consumer assumption conflicts with the supplied rule contract; revise consumer or seek a justified rule change.
Decision: Blocked for requested observed-fact treatment. Absent derivations are not negative assertions, and a rule change cannot manufacture source observations.
```

## Finding requiring repair

The worked example's Terms line omits the aliases field and lacks a counterexample for inside. Its Derived evidence line summarizes inverse witnesses without spelling out each supporting statement, despite the output template requiring those fields. Expand these two lines so the example fully demonstrates its own contract. No code defect was found in the tested bounded semantics. Recommendation: repair example, rerun validation, then accept after confirming the repaired fields; do not claim this review proves external truth, standard conformance, complete provenance enumeration or whole-catalog uniqueness.

## Independent repair recheck

Inspected the repaired example lines. Each predicate now has an explicit aliases field; inside has an enclosure-specific counterexample. All four derived statements now include rule labels and supporting statements, including the intermediate A contains C support for C inside A. These changes close the reported finding without changing the tested algorithm. Independently reran sf.py validate GRF-018: PASS, 1/1. Recommend acceptance within the documented finite, single-class, positive-inference scope. Registry unchanged by reviewer.
