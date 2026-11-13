# Directory pilot review — 2026-10-31

Scope: first six skills from the user-supplied directory, within the existing 5,000-addition expansion. The source contains 185 numbered topics; the full planning inventory is in [directory integration](../plans/directory-integration.md). Topic inclusion is not completed domain coverage.

Observed factory results: six pilot skills passed validation and mechanical quality; registry check reported 550 skills across 60 domains. Combined quality passed 550 skills. Registry statuses remain validated, not audited. The overlap command returned the pre-existing BMD-005/TML-008 lexical candidate and no new lexical candidate; that result alone is not a semantic uniqueness proof.

| Skill | New procedure | Nearest scope and distinction |
| --- | --- | --- |
| SPD-001 | Spatial coordinate and unit handoff | TRP-010 reproduction handoff lacks the specific unit, axis, asymmetric orientation, pivot, and conversion-owner contract |
| SPD-002 | Procedural material parameter isolation | TRP-006 configuration capture records settings; this procedure traces active material dependencies and isolates scene/material confounders |
| UST-001 | Telemetry freshness interface specification | TST-003 is a general transition test matrix; CTG-011 is component composition; this procedure defines observation age, transport, validity, and late-arrival interpretation |
| UST-002 | Configurator invalid-combination recovery | MPU-002 covers empty-state copy; this procedure computes disclosed repair alternatives from supplied compatibility constraints while preserving selected intent |
| VEV-001 | Reconstruction evidence visual labeling | MVA-007/MVA-009 cover visual relationships and handoff; this procedure splits feature-level documented, inferred, illustrative, disputed, and unknown claims across views and exports |
| VEV-002 | Simulation and observation display separation | UST-001 concerns recency of observations; this procedure distinguishes observed, derived, and scenario origins and establishes comparison eligibility |

The coordinator read all six complete skills and inspected relevant existing procedures for boundary review. Authors searched existing neighbors. Different authoring agents reviewed each other's skills and executed the coordinator's ordinary, missing-input, and edge-case requests. Actual text outputs and assertion decisions are recorded in:

- [Spatial handoff/material cases](directory-pilot-spd-tests.md)
- [Telemetry/configurator cases](directory-pilot-ust-tests.md)
- [Reconstruction/simulation cases](directory-pilot-vev-tests.md)

These are 18 assertion-guided text-artifact executions, not blind trials. They do not demonstrate actual mesh import, rendering, live interface execution, historical verification, simulation validity, or portability across different models. The coordinator reviewed the recorded outputs against the requests. No blocking issue remains in this bounded pilot review.

Review correction: SPD-002 now explicitly checks active material assignment and the candidate input's path to the visible output before interpreting unchanged renders. Its disconnected-input decision rule requires a new connected baseline before a controlled trial. The original finding remains in the independent report for traceability; it is closed by this correction.

The two small Python examples in SPD were executed by the authoring agent: unit conversion assertions and the single-parameter difference assertion passed. Those checks establish the examples' arithmetic/invariant only, not spatial or material-system correctness. Fictional example quantities and times were reviewed for consistency; unknown operating thresholds remain required inputs.

The six pilot skills are narrow preparation and design capabilities. Later batches must cover implementation and artifact creation where the directory requests them; this pilot does not stand in for all 185 topics or the remaining expansion.
