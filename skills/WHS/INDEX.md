# Warehouse Stock Operations (WHS)

Reconcile physical stock discrepancies and resolve order-line picking exceptions using count, movement, eligibility and fulfillment evidence.

Macro-area: Operations & Supply Chain

Pick the skill whose triggers best match the request. If none match, use the closest description; if still none, answer without a skill.

| ID | Skill | Use when | Example triggers | Status |
|---|---|---|---|---|
| WHS-001 | [counted-stock-discrepancy-reconciliation](counted-stock-discrepancy-reconciliation/SKILL.md) | Reconcile an observed warehouse count with a recorded quantity when location, stock identity or movement timing could explain the difference. | resolve a warehouse count variance; reconcile this bin count; explain a physical inventory difference | validated |
| WHS-002 | [pick-short-exception-resolution](pick-short-exception-resolution/SKILL.md) | Prepare a fulfillment decision for a short pick when confirmed picked quantities, eligible alternatives and order constraints must be reconciled. | a picker cannot complete this order line; resolve a short pick; which inventory can cover this unfilled quantity | validated |
