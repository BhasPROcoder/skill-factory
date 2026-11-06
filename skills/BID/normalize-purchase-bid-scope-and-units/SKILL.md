---
id: BID-001
name: normalize-purchase-bid-scope-and-units
domain: Procurement Evidence Decisions
subdomain: Bid normalization
version: 1.0
description: Normalize competing purchase offers against a common demand and scope when quoted pack sizes, exclusions or charge bases differ.
triggers: ["compare quoted pack prices","normalize these purchase bids","compare delivered offer totals","reconcile bid exclusions","evaluate whole-pack overbuy"]
not_for: ["general vendor capability selection [MOP-004]","proposed part substitutions [BID-002]"]
requires: []
risk_level: medium
---

# Normalize purchase bid scope and units

## Purpose
Construct an apples-to-apples cost bridge from the original offers to the buyer's actual demand. Show which totals permit a comparison and which gaps still prevent a decision; do not turn a numerical lead into an award.

## Inputs to collect
1. Demand: obtain the required item, quantity, unit, delivery point and coverage period. These set the common basis. Without a quantity or unit, provide a symbolic bridge only.
2. Offers: collect the original offer identifiers, revisions, quantities, packaging, price basis and included services. Preserve the wording where a phrase could change the interpretation. Default to unknown for missing terms.
3. Ordering rules: establish whether partial packs are sold, minimum order quantities apply, or price tiers depend on the quantity actually purchased. Default to no assumption about fractional orders.
4. Adjustment evidence: obtain any buyer-supplied price for excluded work, freight, setup or return handling. This permits an evaluated scenario; it is not a new supplier quote. Default to unresolved rather than zero.
5. Evaluation boundary: ask for currency, required delivery conditions, treatment of surplus and any mandatory scope gates. Default to no credit for surplus unless the buyer establishes a use or recovery value; disclose that convention.

If a required input is missing and has no safe default, ask in one message with at most three questions.

## Procedure
1. Freeze a common demand line before reading prices. Describe the deliverable, timing and unit in enough detail that another reviewer can decide whether each line item satisfies it.
2. Transcribe each offer into a separate source row. Record the revision and whether a number is per piece, per pack, per order or per period. Leave the original quantities and prices intact.
3. Calculate the purchasable quantity for each offer. When only whole packs can be bought, select the smallest count that meets demand and supplied minimums. Check the applicable price tier at that count. Keep the surplus quantity visible.
4. Map scope by marking each required component included, excluded, separately priced, optional or unknown. ⚠️ Silence about delivery or setup does not make it free. Do not add an adjustment when the original total already contains the charge.
5. Rebuild the offered subtotal from quantity times its matching price basis. Resolve discrepancies against the supplier's quoted subtotal; flag any rounding or bundled item that prevents reconciliation.
6. Construct the evaluated bridge from purchasable subtotal to required delivered scope. Show evidenced adjustments separately from assumptions. If a missing charge remains, present a partial total plus a named unknown. A hypothetical break-even value can help target clarification but is never an offer.
7. Evaluate comparability before ordering the results. Align currencies, scope, time, delivery feasibility and required quality. A known cost advantage on a line is not a comparable whole-order total if another mandatory line is missing.
8. Deliver the bridge and a clarification queue ordered by which answer could change the decision. Identify the next review owner only if supplied; otherwise propose a role. Preserve all original offers for independent recalculation.

## Decision rules
- IF the buying unit differs from the consumption unit THEN show both purchasable quantity and demand BECAUSE dividing the pack price by its contents may hide a compulsory surplus purchase.
- IF an excluded service has only a buyer estimate THEN label the evaluated total conditional BECAUSE the estimate is not a commitment from either supplier.
- IF a mandatory scope or delivery condition is unmet THEN mark the offer ineligible on the supplied basis BECAUSE a cheaper incomplete deliverable cannot simply be ranked as equivalent.
- IF an adjustment lacks evidence THEN retain a symbolic term or request clarification BECAUSE treating missing cost as zero creates false precision.

## Output template
```text
Basis: <demand, required scope, comparison period and currency; up to three lines>
Offer bridge: <repeat one row per offer>
Offer | Demand / order / surplus | Quoted component | Adjustments and source | Evaluated result
Comparability: <one conclusion per offer, including open scope gates>
Clarifications: <up to three questions most likely to change the result>
Disposition: <bounded comparison, next reviewer action and any unconfirmed costs>
```

## Quality checklist
- [ ] Each figure points to an offer, buyer input or clearly labeled scenario.
- [ ] Price basis matches the quantity multiplied.
- [ ] Purchasable quantity accounts for supplied pack and minimum rules.
- [ ] Required extras are neither omitted nor counted twice.
- [ ] Unpriced exclusions are visible beside the relevant total.
- [ ] Surplus has not been silently credited or assigned a disposal cost.
- [ ] Eligibility and evaluated cost have separate conclusions.
- [ ] A reviewer can recompute the comparison without inferring a missing unit.

## Anti-patterns
- **Cheapest sticker**: the smallest printed price wins despite differing pack sizes. Fix: reconstruct the order required for the same demand.
- **Bundled duplication**: included delivery is added again for symmetry. Fix: trace the scope inclusion before adding any charge.
- **Estimate laundering**: a buyer's allowance appears as a supplier price. Fix: mark the allowance, its owner and its unknown final value.
- **Premature award**: cost normalization is presented as supplier selection. Fix: hand the result to the designated decision maker with outstanding gates.

## Worked example
**Input:** Fictional studio Echo needs 17 identical display folders delivered in one order. Both offers meet its supplied specification and timing. Fern quotes whole packs of 6 at 24 tokens each, delivery included. Vale quotes individual folders at 4 tokens each, delivery excluded. The buyer estimates Vale delivery at 6 tokens but has no binding price. All quoted figures use the same fictional currency, with no other required charges in this exercise.

**Output:**
```text
Basis: 17 folders, same specification and delivery point; single order, tokens.
Offer bridge:
Offer | Demand / order / surplus | Quoted component | Adjustments and source | Evaluated result
Fern | 17 / 18 / 1 | 3 packs × 24 = 72 | delivery included | 72
Vale | 17 / 17 / 0 | 17 pieces × 4 = 68 | delivery unknown; buyer estimate 6 | 68 + delivery; estimated 74
Comparability: Scope and timing match by premise. Fern delivered total known; Vale delivered total conditional. No value assigned to Fern's extra folder.
Clarifications: What delivery charge will Vale commit to for this order?
Disposition: Under the buyer estimate Fern is 2 tokens lower. Vale ties Fern at a delivery charge of 4 tokens. Recompare after the charge is confirmed; no award issued.
```

**Bad output:** “The per-folder prices are both 4, so either order costs 68.”
This ignores Fern's required third pack and Vale's delivery exclusion.

## Edge cases
- A discount applies only above a threshold: test the actual order against the stated conditions; keep optional larger orders in a separate scenario.
- Several lines share one freight charge: compare order totals first; assign line allocations only under an explicit buyer convention.
- Different currencies or tax treatments are unresolved: preserve native totals and request the applicable dated comparison basis; never invent a conversion rate.
- A bid revision supersedes only selected lines: tie each retained line to its governing revision and request clarification if the combination is not confirmed.

## Test case
**Input:**
> A fictional team requests a delivered comparison. One supplier quotes a sealed case exceeding demand; the other includes exactly the requested pieces but excludes an unpriced installation visit required by the buyer.

**Assertions:**
1. The sealed case remains an order unit and its surplus is shown.
2. The installation exclusion remains a named unknown for the second supplier.
3. No unconditional lowest delivered total is declared without resolving comparability.
