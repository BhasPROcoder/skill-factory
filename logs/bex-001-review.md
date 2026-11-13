# Independent behavioral review: TAP-011

Reviewer: independent agent pass
Artifact: `skills/TAP/browser-feature-compatibility-audit/SKILL.md`
Scope: semantic neighbor comparison and text execution of the specified test plus ordinary, missing-input, and edge prompts. No real browser implementation or external documentation was supplied, so this review tests decision behavior, not technical platform facts.

## Catalog comparison

- `TAP-006 api-version-compatibility-review` compares old and proposed API contracts and consumer behavior. It does not build a browser-target matrix joining documented platform capability, extension permission, target-specific package, and runtime evidence.
- `TAP-010 api-contract-test-fixture-design` produces producer/consumer fixtures and tests them on both sides. It does not reconcile browser target release ranges or packaging configurations.
- `TSC-002 security-permission-review-matrix` compares effective grants with business actions and owner authorization. The draft checks permissions only as one row in a cross-target feature compatibility workflow and does not replace access recertification.
- Finding: the draft has a distinct task boundary and deliverable. Its multi-layer chain—capability, permission declaration, generated package, and target-specific behavior—is materially different from these neighbors. Keep permission review bounded to compatibility evidence as written.

## Executed text evaluations

### 1. Draft's specified test case

Prompt: “Audit a page-save extension for Browser North and Browser South. I supplied code and a passing Browser North test, but no release ranges, generated Browser South package, or current Browser South documentation.”

Response produced:

```text
## Scope
- Feature and outcome: save the current page on user request.
- Target browsers and release ranges: Browser North and Browser South; supported ranges unresolved.
- Evidence examined: supplied code and one passing Browser North test; no generated Browser South package or current Browser South documentation.

## Capability matrix
| Capability | Target | Status | Evidence | User impact | Follow-up |
|---|---|---|---|---|---|
| Save action implementation | Browser North | unknown beyond supplied test | One test passes; build identity and release range were not supplied | The one tested setup may work; broader support is unproven | Identify build and range |
| Save action capability and package | Browser South | unknown | No current documentation or generated package | Support cannot be promised | Check official docs for declared range and inspect/test generated package |

## Test record
- Browser North / build identity unavailable / supplied setup / pass as reported / range and reproducibility unknown.

## Gaps and owner decisions
1. Browser South support is unverified; maintainer to supply release range, current vendor documentation, and generated package for review.

## Unverified items
- Both declared release ranges — obtain them from the maintainer.
- Browser South capability and package — [VERIFY: current official documentation for the declared release range; inspect generated package and run a target test].

## Conclusion
- Parity status: unknown
- Boundary: this is a compatibility review, not a security or distribution approval.
```

Assertion results: 1 pass (ranges explicitly unresolved); 2 pass (North result scoped to reported test); 3 pass (South remains unknown); 4 pass (documentation and generated-package checks named); 5 pass (no change/publication/broad claim). The response omitted a request for the user to provide the release ranges, but assertion 1 allows recording them as unresolved. A direct question would improve actionability.

### 2. Ordinary request

Prompt: “Compare the save-page feature in Browser North and Browser South. We have shared source code, separate package configurations, and a test passing on North. Please tell me whether the feature is ready for both.”

Response produced: North-only result remains limited to the supplied test; South is unknown because no release ranges, current official documentation, generated package, or test was supplied. The output should list each missing evidence item, identify package inspection and a South test as follow-up, and conclude parity is unknown rather than ready for both.

Evaluation: correct evidence boundary, no support inferred from shared code, and a concrete path to close the gap. It should ask for the supported release ranges because they are required input.

### 3. Missing-input request

Prompt: “Audit my extension for compatibility.”

Response produced: “Which feature and user-visible outcome should I audit? Which browser targets and supported release ranges should I compare? Can you provide the implementation/package evidence (source location, build configuration, and target packages)?”

Evaluation: asks exactly three concise questions and seeks all required inputs needed to scope a real audit. Pass.

### 4. Edge request: conflicting evidence

Prompt: “For the fictional Browser North target, current documentation supplied by our team says the capability is supported, but our test on the named build fails. The release range is known. Can I mark it supported?”

Response produced: “No. Preserve both records and mark the target-feature cell unknown pending investigation. Record the documentation title/revision or retrieval date and relevant section, plus test build identity, setup, and failure. Verify that the source and test use the same declared release range and generated package. Do not mark supported or claim parity until the conflict is resolved; if access or reproduction is unavailable, state that runtime behavior remains unobserved.”

Evaluation: correct use of the conflict edge case and avoids privileging documentation or test without reconciliation. Pass.

## Findings and recommendation

1. **Distinctness: pass.** The task is distinguishable from API schema/compatibility review, API fixture design, and general permission review.
2. **Core behavior: pass with one clarity issue.** The draft prevents source-only support claims, keeps unsupported or untested targets unknown, checks generated packages, and prevents silent permission broadening.
3. **Status vocabulary ambiguity:** “verified supported” is not defined as a platform capability (documentation-backed), a shipped implementation (package-backed), or end-to-end behavior (test-backed). The procedure separately asks to verify each support claim and inspect packaging, but the decision rule allows documentation **or** a test to support a claim. Split status by evidence layer, or define the status as applying to the specific matrix row so documentation alone cannot imply shipped/runtime support.
4. **Impact severity ambiguity:** worked example labels the gap “Medium user impact,” although no impact scale or supplied severity rubric exists. Replace this with a plain impact description or explicitly say severity is relative to a user-supplied scale.
5. **Actionability:** when release ranges are missing, ask for them in the output rather than only recording them unresolved where practical.

No external browser facts were asserted or verified during this evaluation. The review does not mark the skill as technically verified for any actual browser.

## Addendum — 2026-11-10

Rechecked the amended BEX-001 draft. Its matrix now records documentation, generated-package, and runtime evidence as separate layers with layer-specific statuses: documentation `documented/stale/conflict/not found/unchecked`; package `present/missing/uninspected`; runtime `passed/failed/unrun/unavailable`. Conflicting documentation and test evidence should remain visible in their respective rows; do not collapse the conflict into one universal support status. The ordinary, missing-input, and edge-case assertions from the prior review remain consistent: Browser North stays scoped to its supplied test/build, missing Browser South release range/docs/package remain unresolved, and inaccessible runtime testing is reported separately from documentation/package findings. No blocker found.
