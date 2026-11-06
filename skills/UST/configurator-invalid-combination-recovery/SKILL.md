---
id: UST-002
name: configurator-invalid-combination-recovery
domain: Interface State Contracts
subdomain: Configuration recovery
version: 1.0
description: Design transparent recovery from incompatible product selections when a configurator must preserve user intent while enforcing supplied compatibility rules.
triggers: ["handle invalid product combinations", "design configurator recovery", "explain incompatible options", "preserve choices after configuration errors", "prevent silent option replacement", "recover a saved invalid configuration"]
not_for: ["generic responsive component design [CTG-011]", "general empty-state copy [MPU-002]", "backend compatibility rule implementation", "pricing strategy or product safety certification"]
requires: []
risk_level: medium
---

# Configurator Invalid-Combination Recovery

## Purpose
Specify how a product configurator explains incompatible selections and offers deliberate repairs without silently changing the user's choices. The output separates compatibility, availability, and price evidence so a plausible-looking configuration is not mistaken for an orderable product.

## Inputs to collect
1. **Option model:** Collect selectable dimensions, allowed values, and which dimensions are required. This defines a complete configuration. Default: none; required for concrete recovery paths.
2. **Compatibility evidence:** Obtain explicit constraints, their authoritative owner, and their revision or effective context. This identifies prohibited combinations. Default: unknown rules remain unresolved rather than inferred from a visual preview.
3. **User intent:** Identify the most recently chosen option, deliberately pinned choices, and any user-stated priorities. This determines what should be preserved. Default: no inferred priority; offer repairs without claiming a preference.
4. **Commercial evidence:** Collect availability, quote validity, and dependencies between selection and price. This determines whether a valid combination is also purchasable. Default: price and availability remain unverified.
5. **Interaction context:** Identify whether the configuration is new, restored, shared, or already attached to a draft order. This shapes recovery without losing work. Default: a new unsaved configuration with no purchase committed.
6. **Change authority:** Identify which edits can be suggested, previewed, or applied automatically under the product's agreed behavior. This prevents silent substitution. Default: propose changes and require a deliberate user choice before applying them.

If a required input is missing and has no safe default, ask in one message with at most 3 questions.

## Procedure
1. Represent the current selection as a dimension-to-value list, retaining incomplete dimensions rather than filling them with invented defaults.
2. Identify the specific supplied rule violated by the combination. Distinguish an incompatible combination from an unavailable item, incomplete choice, or unknown rule result.
3. ⚠️ Preserve the original selection while constructing repairs. Do not mutate the only copy of user intent during validation; retain a reversible comparison between original and proposed choices.
4. Determine which dimensions are pinned or explicitly preferred. When no preference is known, describe the tradeoff among repairs instead of choosing a supposedly optimal replacement.
5. Generate repair candidates using only known allowed values. Each candidate must resolve the conflict under all supplied rules, not merely remove the first visible error.
6. Compare each repair with the original selection. Show changed dimensions, preserved dimensions, and any price or availability information that still needs rechecking.
7. Write a concise explanation naming the conflict and actionable choices. Keep incompatible options discoverable where useful so the user can understand what changing a prerequisite would enable.
8. ⚠️ Specify confirmation and undo behavior before accepting a repair. If the repair affects dependent selections, disclose all affected dimensions together rather than cascading silent replacements.
9. Define revalidation at the point of commitment. A restored or previously valid configuration must be checked against the applicable current rule evidence and commercial state before a quote or order is represented as ready.
10. Produce a recovery walkthrough from invalid state through chosen repair to rechecked state. Record remaining uncertainty; the design artifact is not proof that a live product can be ordered.

## Decision rules
- IF two repairs satisfy the rules but preserve different user choices THEN present both with explicit changes BECAUSE compatibility alone does not reveal the user's preferred tradeoff.
- IF a repair would change a pinned option THEN request a deliberate unpin or a different repair BECAUSE an inferred preference must not override an explicit constraint.
- IF compatibility is established but availability is unknown THEN label the configuration compatible with availability unverified BECAUSE rule validity and fulfillment evidence are different questions.
- IF a saved configuration violates newly supplied rules THEN retain its original values for comparison BECAUSE silent migration destroys the explanation of what changed.
- IF no supported repair exists THEN show the blocking rule and a return path BECAUSE an invented option would only conceal the unresolved conflict.

## Output template
```text
Configuration: <current dimension=value list, up to eight entries>
Conflict: <supplied rule and affected choices, up to three sentences>
Repair options:
<option | changed values | preserved values | unresolved consequences>
<one to four rows, or no supported repair>
Interaction contract: <explanation, selection, confirmation, and undo; up to six lines>
Walkthrough: <three to six event/result pairs>
Commit gate: <compatibility, availability, and price checks still required>
Delivery status: <design only; identify unperformed checks>
```

## Quality checklist
- [ ] The conflict cites supplied constraint evidence rather than visual assumptions.
- [ ] Original choices remain available for comparison or undo.
- [ ] Every proposed repair is checked against all supplied constraints.
- [ ] Pinned choices are preserved unless the user explicitly changes them.
- [ ] Every modified dimension is disclosed before repair confirmation.
- [ ] Compatibility, availability, and pricing have distinct statuses.
- [ ] The explanation gives a usable next action rather than only an error label.
- [ ] Saved configurations have a revalidation path.
- [ ] The result is labeled as design work rather than a completed transaction.

## Anti-patterns
- **Silent substitution:** Replacing a chosen component with a default after another choice changes. Fix: show the dependent change and request a deliberate repair choice.
- **First-error repair:** Resolving one conflict while introducing another. Fix: evaluate each candidate against the complete supplied constraint set.
- **Visual compatibility:** Treating a successful render as proof of manufacturability. Fix: use explicit product rules and qualified verification where needed.
- **Unavailable equals incompatible:** Hiding a valid option because stock evidence is missing. Fix: separate the cause and state what evidence is unresolved.
- **Price carryover:** Reusing an old quote after selection changes. Fix: recheck commercial consequences before displaying a commit-ready total.

## Worked example
**Input:**
Fictional furniture studio Alder provides these rules for a decorative display table: a glass top requires the wide base; a narrow base accepts only the wood top. Both top choices and both base choices exist in the fictional catalog. User Mira currently selected narrow base and glass top. Neither is pinned, and no preference between them was supplied. Inventory and prices have not been provided. This exercise concerns selection behavior, not structural safety approval.

**Output:**
```text
Configuration: base=narrow; top=glass
Conflict: Alder's supplied rule requires a wide base for the glass top. The narrow base accepts only the wood top.
Repair options:
A | base becomes wide | glass top | availability and price unverified
B | top becomes wood | narrow base | availability and price unverified
Interaction contract: Explain that the glass top requires the wide base.
Offer A and B with a visible comparison to the current selection.
Keep original selections until Mira chooses a repair.
Confirm the changed dimension before applying it.
Provide undo to restore the original draft, including its conflict notice.
Walkthrough: Select narrow plus glass -> conflict shown without replacement.
Choose A -> preview wide plus glass, preserving the original draft.
Confirm A -> compatible under supplied rules; commercial checks remain open.
Undo -> original narrow plus glass restored with conflict notice.
Commit gate: Revalidate applicable rules and obtain availability and current price before order readiness.
Delivery status: Design only; no live configurator, inventory query, quote, order, or structural verification performed.
```

**Bad output:**
“We switched Mira to the wide base and kept the original price; the table is ready to buy.”
This applies an unchosen repair, assumes missing commercial evidence, and mistakes a design proposal for an executed transaction.

## Edge cases
- Every relevant choice is pinned: present the conflict and ask which pin may change; do not override a pin automatically.
- A rule is ambiguous or contradictory: identify the contradictory evidence and defer affected repairs until the rule owner resolves it.
- A shared link references a removed option: retain its label as historical context, mark it unavailable, and offer only supported replacements.
- Several repairs change different numbers of dimensions: display their change sets; fewer changes alone does not establish the user's preferred outcome.
- The catalog updates during confirmation: rerun applicable checks, disclose changed results, and preserve the user's draft for comparison.

## Test case
**Input:**
> Fictional studio Birch supplies a configurator rule: finish=matte requires material=wood. The current draft has finish=matte pinned and material=metal unpinned. Wood is an allowed material, but its inventory and price are unknown. Draft a recovery specification.

**Assertions:**
1. The proposed repair changes material to wood while preserving the pinned matte finish.
2. The original draft is retained for comparison or undo.
3. Availability and price remain explicitly unverified.
4. No actual product update, purchase, or live validation is claimed.
