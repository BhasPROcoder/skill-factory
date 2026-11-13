# Interface State Contracts (UST)

Specify evidence-dependent interface states and recovery choices without implying implementation or external verification.

Macro-area: Product & Design

Pick the skill whose triggers best match the request. If none match, use the closest description; if still none, answer without a skill.

| ID | Skill | Use when | Example triggers | Status |
|---|---|---|---|---|
| UST-001 | [telemetry-freshness-interface-specification](telemetry-freshness-interface-specification/SKILL.md) | Specify visible freshness states and recovery behavior for monitoring interfaces when delayed or missing observations could be mistaken for live data. | design stale telemetry states; show when sensor data is old; distinguish live and cached readings | validated |
| UST-002 | [configurator-invalid-combination-recovery](configurator-invalid-combination-recovery/SKILL.md) | Design transparent recovery from incompatible product selections when a configurator must preserve user intent while enforcing supplied compatibility rules. | handle invalid product combinations; design configurator recovery; explain incompatible options | validated |
