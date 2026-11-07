# Design System Maintenance (DST)

Trace token dependencies and coordinate component contracts, renames and consumer retirement without assuming runtime or release readiness.

Macro-area: Product & Design

Pick the skill whose triggers best match the request. If none match, use the closest description; if still none, answer without a skill.

| ID | Skill | Use when | Example triggers | Status |
|---|---|---|---|---|
| DST-004 | [component-deprecation-consumer-handoff](component-deprecation-consumer-handoff/SKILL.md) | Prepare a consumer-specific retirement handoff when a design-system component is being deprecated and its replacement may not preserve every supported behavior. | deprecate a shared component; handoff component retirement; migrate consumers from an old component | validated |
| DST-002 | [component-variant-compatibility-matrix](component-variant-compatibility-matrix/SKILL.md) | Build a supported-state matrix for component variants when independent properties can combine into invalid or undefined behavior. | document component variant combinations; which component props work together; build a design-system state matrix | validated |
| DST-001 | [design-token-alias-cycle-diagnosis](design-token-alias-cycle-diagnosis/SKILL.md) | Trace design-token references to locate cycles, missing targets and affected consumers when a token cannot resolve. | find a circular token alias; why does this token not resolve; trace design token references | validated |
| DST-003 | [design-token-rename-migration-map](design-token-rename-migration-map/SKILL.md) | Map a proposed design-token rename through aliases, generated outputs and consumer references when preserving a value alone may not preserve compatibility. | rename a design token safely; map token rename consumers; plan a semantic token migration | validated |
