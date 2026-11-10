---
id: MSE-011
name: search-structured-data-page-parity-audit
domain: Search Content Decisions
subdomain: Structured data validation
version: 1.0
description: Audit whether a page’s generated structured data is technically valid, supported by visible page facts, and aligned with current search-platform guidance; use before or after publishing structured markup.
triggers: ["audit page structured data", "check JSON-LD against the page", "review schema markup facts", "validate structured data output", "check whether markup matches visible content"]
not_for: ["reviewing editorial copy claims alone [MSE-010]", "choosing query intent or page purpose [MSE-001]", "legal or regulated financial conclusions"]
requires: []
risk_level: medium
---

# Search Structured Data Page Parity Audit

## Purpose
Audit structured data by tracing its properties to visible page evidence and source records. Separate technical validity, factual parity, and current platform guidance; one does not prove the others.

## Inputs to collect
1. **Page and decision scope** — page artifact, purpose, platform if relevant, and pre-release or incident context. Why: assertions depend on the decision. Default: supplied materials only; do not imply live inspection.
2. **Visible page evidence** — rendered text, relevant images/captions, and page state. Why: parity concerns what users can see. Default: if unavailable, mark comparison unverified.
3. **Generated structured data** — exact source or rendered output from the target build and page association. Why: templates can render different values. Default: a template alone does not prove generated output.
4. **Field sources and owners** — supplied authoritative records for each asserted value. Why: page text can also be wrong or stale. Default: mark unsupported fields unresolved.
5. **Current official platform and vocabulary documentation** — relevant rules can change. Default: look up current primary sources or mark guidance unchecked; do not rely on remembered eligibility rules.
6. **Validation and release evidence** — tool output, build identity, and release stage. Why: separates proposed from executed checks. Default: do not mark checks passed without evidence.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Define the page set, state, build or observation time, platform, and requested decision.
2. Label each page, markup, source, documentation, and test artifact for traceability.
3. Identify the structured-data vocabulary and every emitted object, property, and value from the generated output. If only a template is supplied, label the output as template-level evidence.
4. For each value that asserts a fact, map it to both its visible page evidence and its source record. Record exact disagreement, absent evidence, stale dates, and scope differences rather than choosing a convenient value.
5. Check technical parse and vocabulary constraints against current authoritative documentation or a suitable supplied validator result. Record the tool, version or retrieval context when available; do not invent required fields or acceptance thresholds.
6. Check page association: confirm that the markup belongs to the reviewed page and is not inherited from another product, locale, variant, or state.
7. Compare the declared page purpose and markup type with the actual page content. Flag markup that describes content not represented for users or claims an unsupported relationship.
8. Record four separate evidence states: **technical validity** (pass/fail/unchecked), **visible-page parity** (matches/conflict/not evidenced), **source support** (supported/conflict/missing/unchecked), and **platform guidance** (aligned/conflict/unchecked). A pass in one layer cannot substitute for another.
9. ⚠️ Check time-sensitive platform guidance in current official documentation. If the applicable documentation, platform, or page condition cannot be verified, use `[VERIFY: exact requirement and current official source to check]` and keep dependent guidance unchecked.
10. Compare validator findings with the generated artifact and applicable documentation; a generic warning alone does not prove a user-visible defect.
11. Recommend a specific repair, source correction, owner review, or no change. Separate preparation from live publishing.
12. Report scope, evidence states, unresolved items, owners, and completion checks. Do not promise display, ranking, traffic, or eligibility.

## Decision rules
- IF a property is technically valid but has no matching visible-page evidence THEN mark visible-page parity not evidenced and propose removal or owner review BECAUSE syntax does not establish that the asserted fact is represented to users.
- IF the markup and visible page disagree with each other or their source record THEN preserve all values and identify which owner must resolve the source before release BECAUSE a three-way mismatch cannot be repaired by choosing one representation silently.
- IF only a markup template is available THEN limit conclusions to template structure and leave generated values unchecked BECAUSE per-page rendering can introduce different content.
- IF official guidance conflicts with a validator result THEN preserve both findings and check the validator’s scope and current official rule BECAUSE tool output is not automatically the controlling platform policy.
- IF current platform eligibility is not verified THEN say eligibility is unknown and provide the exact current documentation lookup BECAUSE valid markup does not guarantee platform treatment.
- IF the user asks for deployment or publication after the audit THEN confirm the target page, approved content, and requested change scope before acting BECAUSE an audit alone does not imply permission to change live content.

## Output template
```text
## Scope
- Pages and observed state:
- Markup artifact/build:
- Platform and decision:

## Field parity matrix
| Page/property/value | Visible page evidence | Source record | Technical validity | Page parity | Source support | Platform guidance | Follow-up |
|---|---|---|---|---|---|---|---|

## Checks performed
- Artifact/tool or documentation source:
- Result and limitations:

## Owner actions
1. [issue] — [specific action] — [owner role] — [observable completion check]

## Unverified
- [claim] — [VERIFY: exact requirement and current official source or artifact needed]

## Conclusion
- Status: consistent / inconsistent / incomplete
- No display, ranking, traffic, or eligibility outcome is promised by this audit.
```

## Quality checklist
- [ ] Each page and generated markup artifact is identified or explicitly missing
- [ ] Every fact-bearing property has a visible-page comparison and a source-record comparison
- [ ] Technical validity, page parity, source support, and platform guidance are reported separately
- [ ] Template-only evidence is not represented as generated-page verification
- [ ] Current official guidance is checked or marked unchecked with a specific verification request
- [ ] Conflicting values remain visible until the responsible source owner resolves them
- [ ] Validation claims identify what was actually checked and any scope limits
- [ ] The report does not promise search display, ranking, eligibility, traffic, or business results

## Anti-patterns
- **Syntax-equals-truth**: treat a valid data block as proof that its values are correct. Fix: trace every fact-bearing value to visible-page and source evidence.
- **Template-equals-render**: assess only the template and claim all pages match. Fix: inspect generated output for each declared page or narrow the conclusion.
- **Visible-copy-only review**: verify page text but ignore structured-data values. Fix: compare the actual emitted properties row by row.
- **Eligibility promise**: predict a search display from markup presence. Fix: verify current platform guidance and still report actual display as outside the audit unless observed.
- **Stale-rule assertion**: hardcode a remembered property requirement. Fix: check current official guidance or write a targeted `[VERIFY: ...]` item.
- **Silent value repair**: make markup match page text when both may be wrong. Fix: preserve the mismatch and route source correction to its owner.

## Worked example
**Input:** Fictional shop Cedar Lantern supplies one product page, a generated markup excerpt, and a product record. The visible page and product record list the product as blue. The markup says green. A generic parser accepts the excerpt; no current platform-specific guidance has been checked. The shop asks whether the markup is ready.

**Output:**
```text
## Scope
- Pages and observed state: supplied Cedar Lantern product page snapshot.
- Markup artifact/build: supplied generated excerpt; build identifier not supplied.
- Platform and decision: platform-specific guidance is unchecked; assess release readiness from supplied evidence.

## Field parity matrix
| Page/property/value | Visible page evidence | Source record | Technical validity | Page parity | Source support | Platform guidance | Follow-up |
|---|---|---|---|---|---|---|---|
| Product/color/green | Page shows blue | Product record says blue | Parser accepted excerpt | Conflict | Conflict | Unchecked | Owner confirms authoritative color, then align all representations |

## Checks performed
- Supplied generic parser result: accepted the excerpt; this does not resolve the color mismatch.
- Current platform guidance: not checked.

## Owner actions
1. Color mismatch — confirm the authoritative product record and correct page or markup — catalog owner — generated output and page show the approved value.

## Unverified
- Platform guidance — [VERIFY: current official platform documentation for the declared markup type and page purpose]

## Conclusion
- Status: inconsistent
- No display, ranking, traffic, or eligibility outcome is promised by this audit.
```

**Bad output:**
> The parser accepts the markup, so it is ready and should qualify for an enhanced result.

Fails because parser acceptance does not resolve the fact mismatch or establish current platform eligibility or display.

## Edge cases
- **Localized or variant pages**: review each rendered page and its associated data separately; do not borrow values from a default locale or variant.
- **Source record and page disagree but markup matches one**: retain the three values in the matrix and route the source decision to its owner.
- **No generated output supplied**: assess only the template and list generated-output parity as unverified.
- **Validator is unavailable**: mark technical validity unchecked and provide the exact artifact and suitable validation evidence needed; do not call the markup valid by inspection alone.
- **Platform guidance is unclear or changed**: record the consulted official source and date if available, mark the disputed guidance unchecked, and avoid eligibility conclusions.

## Test case
**Input:**
> A product page visibly says “blue,” its supplied product source record also says “blue,” but generated structured data says “green.” A generic parser accepts it. No current platform guidance is supplied. Is this ready?

**Assertions:**
1. The conclusion is inconsistent because the markup conflicts with both visible-page and source evidence.
2. Parser acceptance is reported only as technical evidence and does not resolve the mismatch.
3. Platform guidance remains unchecked and is not converted into an eligibility claim.
4. The output assigns source resolution to an owner and states an observable correction check.
5. No enhanced display, ranking, or traffic outcome is promised.
