# Independent behavioral review: MSE-011

Reviewer: independent agent pass
Artifact: `skills/MSE/search-structured-data-page-parity-audit/SKILL.md`
Scope: compare actual neighboring procedures and text-evaluate the embedded test plus ordinary, missing-input, and edge requests. No external search-platform rules were checked; the draft's `[VERIFY]` behavior is evaluated, not actual eligibility.

## Catalog comparison

- **MSE-010 search-editorial-claim-audit** extracts claims from draft editorial text, matches them to supplied support, then chooses retain/narrow/verify/remove. MSE-011 shares evidence discipline but handles a different artifact and validation chain: generated machine-readable properties mapped to rendered-page facts and source records, alongside separate parser, current-guidance, and page-association states.
- **MSE-005 search-article-refresh-triage** inventories dated or changed claims in articles and selects retain/update/merge/retire. It does not inspect generated markup properties, rendered output, vocabulary constraints, or validator scope.
- **MSE-003 search-content-brief-design** and related MSE instructions warn against unsupported factual claims and require current-source checks. They create editorial briefs, not a field-by-field parity ledger across page, source record, generated structured data, and technical/platform checks.
- **MAR-004 search-page-template-purpose-review** checks whether template sections serve the page's reader task; it does not validate emitted structured-data values or generated per-page association.
- **Finding:** The layered structured-data traceability matrix is a materially distinct deliverable. Keep MSE-011 bounded to structured-data/page parity and do not duplicate general editorial claim review or promise search presentation outcomes.

## Executed text evaluations

### 1. Embedded test case

Prompt: supplied page and source record say blue; generated structured data says green; a generic parser accepts the output; no current platform guidance is supplied. User asks whether it is ready.

Response produced:

```text
## Scope
- Pages and observed state: supplied product-page snapshot.
- Markup artifact/build: supplied generated excerpt; build identity missing.
- Platform and decision: platform not identified; release readiness requested.

## Field parity matrix
| Page/property/value | Visible page evidence | Source record | Technical validity | Page parity | Source support | Platform guidance | Follow-up |
|---|---|---|---|---|---|---|---|
| supplied product/color/green | page says blue | record says blue | generic parser accepted excerpt | conflict | conflict | unchecked | source owner confirms correct color; update page/markup and compare generated output |

## Checks performed
- Supplied generic parser result: accepted excerpt; no build or validator details supplied.
- Platform guidance: unchecked.

## Owner actions
1. Color disagreement — confirm the authoritative product value and align page/markup — catalog owner — rendered page and generated property match the approved value.

## Unverified
- Platform requirements — [VERIFY: current official documentation for the identified platform and markup type].

## Conclusion
- Status: inconsistent
- No display, ranking, traffic, or eligibility outcome is promised by this audit.
```

Assertions: 1 pass, inconsistent state follows from generated green versus page/source blue. 2 pass, parser acceptance is technical-only. 3 pass, platform guidance remains unchecked. 4 pass, owner action has observable generated/page comparison. 5 pass, no display/ranking/traffic promise. No arithmetic or external fact is asserted.

### 2. Ordinary request

Prompt: “Our fictional shop's product page says 250 ml and the approved catalog record also says 250 ml. The generated structured data says 200 ml. A validator accepts it. Can we release the page today?”

Response produced: identify the supplied page, generated output, and catalog record; mark technical validity as parser-accepted, page parity as conflict, source support as conflict, and platform guidance unchecked unless current documentation is supplied. Route correction to the catalog/page owner and require the generated property and rendered page to match the approved record before release review. Do not promise eligibility or perform publication.

Evaluation: correct separation of artifact validity and factual parity; the answer does not infer that parser acceptance or a requested release date authorizes publishing. Pass.

### 3. Missing-input request

Prompt: “Check the structured data on my site.”

Response produced: “Which page(s), locale/variant and review decision should I assess, and on which platform if guidance matters? Can you provide the rendered page evidence and the exact generated structured-data output/build? What source record supports the asserted fields, and do you have current platform documentation or validator results to include?”

Evaluation: exactly three concise questions covering scope, generated artifacts, and source/validation evidence. It does not claim it inspected a live site. Pass.

### 4. Edge request: localized variant

Prompt: “A fictional English product page describes the standard model. Its French variant is a smaller model with a different supplied catalog record, but the generated French page inherits the English structured-data values. The validator accepts both outputs. We have no current platform documentation.”

Response produced: review the English and French rendered pages and generated data as separate page/variant rows; do not borrow English facts for French. Mark technical state parser-accepted per output, but compare each field to its own visible page and source. Mark any inherited mismatches as conflicts; platform guidance stays unchecked with a targeted `[VERIFY: current official platform/vocabulary documentation for each applicable page type and locale]`. Ask the content/catalog owner to resolve and align each variant, then rerun checks on generated outputs. No eligibility or publication promise.

Evaluation: correct handling under localized/variant edge case; parser acceptance does not erase variant mismatch. Pass.

## Findings

1. **Distinctness: pass.** MSE-011's field-level generated-data parity matrix is not performed by the inspected editorial claim, article refresh, content brief, or page-template purpose workflows.
2. **Layer separation: pass.** The draft keeps technical validation, visible-page parity, source support, and platform guidance separate and gives each a distinct state vocabulary.
3. **Accuracy: pass.** The worked example is explicitly fictional and uses no questionable arithmetic or hardcoded platform rule. Current platform requirements are assigned a verification step.
4. **Authorization boundary: pass.** Auditing is not publication permission; live changes require confirmation of target and approved scope.
5. **No blockers.** This is instruction-level behavioral evidence only; no actual page, parser, search platform, or live eligibility state was inspected.
