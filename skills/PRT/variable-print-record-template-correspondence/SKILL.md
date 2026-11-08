---
id: PRT-005
name: variable-print-record-template-correspondence
domain: Print Production Handoffs
subdomain: Variable content correspondence
version: 1.0
description: Reconcile supplied data records with personalized print templates and rendered samples when field mapping, conditional content or record coverage may be wrong.
triggers: ["check personalized print records", "review variable print field mapping", "verify conditional print content", "reconcile mailer records and samples", "check blank values in personalized artwork"]
not_for: ["deciding lawful mailing eligibility", "verifying postal deliverability", "operating a production merge system"]
requires: []
risk_level: medium
---

# Variable print record and template correspondence

## Purpose
Create a traceable bridge between a supplied record set, its field-to-template rules and observed personalized outputs. Catch wrong-field substitutions, invalid conditional branches and missing or duplicate record outputs without assuming that a visually plausible sample proves the entire run.

## Inputs to collect
1. **Record identity:** Obtain the bounded data revision and a stable record key. Required; if no key exists, agree on a temporary row reference that will not be reused after sorting or filtering.
2. **Template revision:** Collect the artwork template and named variable locations. Required; a sample alone cannot establish which mapping rule generated it.
3. **Mapping rules:** Obtain source fields, transformations, conditions and approved fallbacks for each variable location. Required for conformance findings; missing rules remain unresolved.
4. **Output evidence:** Request rendered samples or a manifest mapping outputs to record keys. Default: mapping review only, with no claim that generated content was inspected.
5. **Coverage policy:** Identify the intended record subset, exclusion reasons and expected outputs per record. Default: no silent filtering or duplication.
6. **Review data boundary:** Use only necessary fields and appropriately masked review data. Default: omit unrelated personal details from the report and reference stable keys instead.

If required inputs have no safe defaults, ask in one message with at most three questions.

## Procedure
1. Freeze the identities of the data, template, rules and output evidence being compared. A changed data sort or template revision requires its own correspondence check.
2. Build a mapping table from each variable location to its exact source field and approved transformation. Distinguish an intentionally combined display name from accidentally substituting a company or address field.
3. Enumerate the permitted conditional branches and their triggering evidence. Record the behavior for missing, blank, invalid and unmatched values according to supplied rules rather than treating them all as the same case.
4. Choose review records that exercise the actual branches and relevant formatting boundaries. Include long values, optional fields and repeated display names where present; selection is evidence coverage, not a statistical guarantee.
5. ⚠️ Match each observed output to a stable record identity before judging its contents. A correct-looking name on the wrong recipient's output is a correspondence failure, not a passing layout result.
6. Compare each selected record's expected visible values with the observed output. Preserve a distinction between correct content that overflows its location and content that came from the wrong field.
7. Check whether fallback text, punctuation and conditional blocks leave unintended blanks or fragments. Report only inspected cases; do not infer all missing-value combinations from one passing sample.
8. Reconcile the output manifest with intended record coverage. Track excluded keys with their supplied reasons and flag repeated or absent keys against the expected number of outputs per record.
9. Prepare corrections at the responsible layer: data, mapping, condition, layout or output enumeration. Require new evidence for affected branches when any rule changes, not just regeneration of the example that exposed the defect.
10. Deliver the correspondence ledger and unresolved questions using keys rather than unnecessary personal data. State exactly which outputs were inspected and whether whole-run coverage was checked through a manifest.

Any application-specific merge syntax or export behavior must be checked against the current application's documentation before execution. This skill supplies a review procedure, not runnable merge code or a legal basis for processing recipient data.

## Decision rules
- IF two records share a display name THEN retain separate stable keys BECAUSE name equality does not establish recipient identity.
- IF a required field lacks a supplied fallback THEN hold the affected branch for a decision BECAUSE invented text can change personalized meaning.
- IF selected samples pass THEN report sample-level findings BECAUSE uninspected outputs may exercise other values or branches.
- IF a mapping rule changes THEN recheck its affected branches BECAUSE a local correction can alter multiple outputs.
- IF an output key repeats unexpectedly THEN investigate coverage independently of appearance BECAUSE duplicate-looking or correct-looking outputs can still leave another record missing.

## Output template
```text
Revision set: <data, template, rules and output evidence; up to four lines>
Mapping ledger: <up to ten rows; attach complete mapping when larger>
Template location | Source/rule | Missing-value behavior | Status
Observed cases: <key, branch, expected value category, observation and disposition>
Coverage: <intended keys, exclusions, missing/repeated outputs and evidence scope>
Corrections: <up to five grouped issues, responsible layer and recheck>
Questions: <up to three consolidated questions>
Verification limits: <inspected samples versus whole-run checks>
```

## Quality checklist
- [ ] Data and template revisions are identified.
- [ ] Records are matched using stable keys rather than display names alone.
- [ ] Variable locations have explicit source-field rules.
- [ ] Missing-value behavior is supplied or remains unresolved.
- [ ] Conditional branches are named in reviewed cases.
- [ ] Content correctness and layout fit have separate findings.
- [ ] Coverage claims match manifest or sample evidence actually inspected.
- [ ] Reports avoid unnecessary recipient details.

## Anti-patterns
- **Attractive sample bias:** one neat output is treated as a complete-run check. Fix: name the inspected branches and separately reconcile coverage.
- **Row-number drift:** a row reference survives a changed sort without reconciliation. Fix: use a stable key or establish a new frozen reference.
- **Helpful fallback:** missing names are replaced with invented salutations. Fix: use approved fallback rules or request a decision.
- **Field/fit confusion:** shrinking text is proposed for a wrong-field substitution. Fix: diagnose content source before layout adjustment.
- **Silent exclusion:** incomplete records disappear from the count. Fix: preserve excluded keys and supplied reasons.

## Worked example
**Input:** Fictional studio Moss supplies records K and L for template T. The rule maps the company block to company_name; a blank company_name must omit the whole block. K contains company_name Birch. L has that field blank. The observed K output shows Birch correctly. L shows a literal field label “company_name.” The manifest contains K and L once each.

**Output:**
```text
Revision set: Supplied records K/L, template T and stated company-block rule; corresponding sample views and manifest.
Mapping ledger:
Template location | Source/rule | Missing-value behavior | Status
Company block | company_name | omit whole block | rule supplied; L output fails
Observed cases: K, populated branch, company text, Birch observed, passes supplied rule. L, blank branch, omitted block expected, field label observed, fails.
Coverage: K and L both present once in supplied manifest; no missing or repeated keys identified in that scope.
Corrections: Template/condition owner to repair blank-field rendering and recheck both populated and blank branches in replacement outputs.
Questions: Please supply regenerated evidence for both branches after correction.
Verification limits: Company-block samples and supplied manifest checked; other fields and actual printed output uninspected.
```

**Bad output:** “Both recipients have files, so personalization is correct.”
Coverage does not prove field mapping or missing-value behavior, and L visibly fails its supplied rule.

## Edge cases
- A record deliberately generates several pieces: reconcile each named piece against the supplied expected multiplicity instead of treating all repeats as errors.
- A field contains punctuation meaningful to the layout: inspect its rendered result without silently rewriting source data.
- Records change after sampling: invalidate only the affected evidence where traceability supports that scope; otherwise request a new correspondence check.
- No output manifest exists: report sample findings and request coverage evidence rather than reconstructing whole-run counts from filenames alone.

## Test case
**Input:**
> Fictional records A and B share the display name Rowan. The output manifest lists A twice and omits B, while both previews look correct. Each record should generate one piece.

**Assertions:**
1. Identifies duplicate A and missing B using stable keys.
2. Does not accept matching display names as proof of coverage.
3. Requests corrected output enumeration and replacement evidence.
4. Separates observed appearance from record correspondence.
