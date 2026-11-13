Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: TAP-011
name: browser-feature-compatibility-audit
domain: API Contract Engineering
subdomain: Cross-browser capability parity
version: 1.0
description: Audit whether a browser extension feature behaves consistently across declared browser targets; use when APIs, permissions, manifest declarations, or packaging differ by target.
triggers: ["check extension support across browsers", "compare browser extension APIs", "audit browser add-on compatibility", "find target-specific extension gaps", "review extension manifest differences"]
not_for: ["general API schema design [TAP-001]", "permission minimization alone [TSC-002]", "component state combinations [DST-002]", "general software test planning"]
requires: []
risk_level: medium
---

# Browser Feature Compatibility Audit

## Purpose
This skill produces an evidence-linked capability matrix for a browser extension feature across the user’s declared browser targets. It catches cases where a feature appears implemented but is unavailable, differently permissioned, packaged incorrectly, or untested on a target. It does not certify security, store policy compliance, or publish an extension.

## Inputs to collect
1. **Feature and intended user outcome** — why: defines observable parity; default: none, required.
2. **Target browsers and supported release range** — why: capabilities change by browser and release; default: none, required.
3. **Implementation and packaging evidence** — source locations, build configuration, manifest variants, and dependency notes; why: names alone cannot prove behavior; default: none.
4. **Current authoritative vendor documentation** — why: APIs, manifest keys, permission behavior, and distribution rules change; default: look up the applicable official documentation for each target or mark the item unverified.
5. **Existing automated and manual test evidence** — why: separates code presence from observed behavior; default: no tests demonstrated.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Write the user-visible outcome as a short, testable statement.
2. List each target browser and the exact release range the project claims to support.
3. Break the outcome into user-observable actions and required platform capabilities.
4. For each capability, trace the implementation from entry point through browser API calls, permission declarations, build variant, and user-visible result.
5. ⚠️ Check each target against its current official documentation; record document title, version or retrieval date when available, and the exact relevant section. If the applicable source or release range cannot be confirmed, mark documentation stale or unchecked. Do not invent citations or infer support from a similar API name.
6. Record separate evidence rows for documentation, generated package, and runtime test; do not compress these layers into a single support status. For documentation use **documented**, **stale**, **conflict**, **not found**, or **unchecked**; for package inspection use **present**, **missing**, or **uninspected**; for runtime use **passed**, **failed**, **unrun**, or **unavailable**. Link each judgment to its evidence.
7. Compare permission and host-access requirements with the feature’s actual code path. Flag unexplained excess for the maintainer; do not silently change access declarations.
8. Inspect target-specific build and packaging outputs to confirm the intended implementation and declarations actually ship together.
9. Define a test for every support claim and meaningful difference. Execute only in the authorized local or test environment; record target, build identity, setup, result, and limitations.
10. Group gaps by user impact and release dependency, then propose the smallest concrete fix or an explicit unsupported-target decision.
11. Return unresolved questions to the maintainer before claiming parity. Do not publish, submit, or change distribution settings.

## Decision rules
- IF support is inferred only from source code or a shared API name THEN mark the documentation and runtime evidence layers unchecked until official target documentation or an executed target test supports the claim BECAUSE similar names can hide different availability or behavior.
- IF documentation is stale, undated, or for a different release range THEN mark its documentation row stale and request current vendor documentation BECAUSE compatibility is time-sensitive.
- IF a target needs a different permission or host-access declaration THEN record the minimum evidenced requirement and its user impact for maintainer review BECAUSE parity does not justify silently widening access.
- IF a test passes on one browser only THEN report only that target as tested BECAUSE another target’s build or runtime may differ.
- IF a build omits the target-specific manifest or entry point THEN classify the feature as a packaging gap even if its source exists BECAUSE source presence does not prove deliverability.
- IF there is no reasonable implementation for a declared target THEN present an explicit limitation or target removal decision for the owner BECAUSE false parity claims mislead users.

## Output template
```text
## Scope
- Feature and outcome:
- Target browsers and release ranges:
- Evidence examined:

## Capability matrix
| Capability | Target | Evidence layer | Status (see layer-specific values in Procedure) | Evidence | User impact | Follow-up |
|---|---|---|---|---|---|---|

## Test record
- Target/build/setup/result/limitations:

## Gaps and owner decisions
1. [impact] [evidence] [proposed smallest action] [decision owner]

## Unverified items
- [claim] — [VERIFY: current official documentation or target test needed]

## Conclusion
- Parity status: demonstrated / partial / unknown. Use demonstrated only when the intended user behavior passed on each declared target and each target package was inspected; documentation alone is not an end-to-end result.
- Boundary: this is a compatibility review, not a security or distribution approval.
```

## Quality checklist
- [ ] Every declared target has an identified release range or is explicitly unresolved
- [ ] Every feature claim maps to code, official documentation, or executed test evidence
- [ ] Unknown and unavailable states are not represented as supported
- [ ] Permission differences are reviewed against the actual feature path
- [ ] The packaged output was inspected for each target claimed as deliverable
- [ ] Test evidence identifies target, build, setup, result, and limitations
- [ ] User impact is stated for each material gap
- [ ] No publishing or permission change is implied by the report

## Anti-patterns
- **API-name matching**: assume similarly named APIs behave alike. Fix: verify target and release-specific documentation.
- **Manifest-only audit**: infer runtime behavior from declarations. Fix: trace implementation and test behavior.
- **Source-equals-shipping**: treat code presence as packaged support. Fix: inspect generated target output.
- **Permission creep**: add broad access to make tests pass. Fix: document the narrow requirement and ask the owner to decide.
- **False universal claim**: call a feature cross-browser after testing one target. Fix: scope each claim to its evidence.
- **Stale reference**: rely on old documentation without checking its applicability. Fix: record current source and date or mark `[VERIFY: current official browser documentation]`.

## Worked example
**Input:** Fictional team Cedar supports an extension feature that saves the current page title and URL. The team lists Browser North and Browser South as targets. Their build contains one shared implementation and two package configurations, but only a Browser North test result is supplied. Official documentation for Browser South’s declared release range has not been checked.

**Output:**
```text
## Scope
- Feature and outcome: save the active page title and URL on user request.
- Target browsers and release ranges: Browser North (range supplied); Browser South (range supplied).
- Evidence examined: shared implementation, two package configurations, one Browser North test.

## Capability matrix
| Capability | Target | Evidence layer | Status | Evidence | User impact | Follow-up |
|---|---|---|---|---|---|---|
| Read active tab details after user action | Browser North | Runtime | passed | Supplied test passes for the identified build | Save action worked in tested setup | Retain test record |
| Read active tab details after user action | Browser South | Documentation | unchecked | No current official documentation supplied | Save behavior cannot be promised | Verify current documentation |
| Read active tab details after user action | Browser South | Runtime | unrun | No target test supplied | Save behavior cannot be promised | Run target test |
| Intended declaration ships | Browser South | Package | uninspected | Configuration exists; generated package not supplied | Delivery not demonstrated | Inspect generated package |

## Test record
- Browser North / supplied build / user invokes save / pass / one setup only.

## Gaps and owner decisions
1. Browser South save behavior and package delivery are unverified; check current official documentation, inspect its generated build, and run a target test; owner: extension maintainer.

## Unverified items
- Browser South active-tab access — [VERIFY: current official documentation for the declared release range and a target test]

## Conclusion
- Parity status: partial
- Boundary: this is a compatibility review, not a security or distribution approval.
```

**Bad output:**
> Both browsers support the feature because the same API name appears in the source.

Fails because it treats shared source as proof of target support, package inclusion, and runtime behavior.

## Edge cases
- **Target release range is unspecified**: list it as an owner decision and keep affected cells unknown.
- **Official documentation conflicts with a test**: preserve both records, identify target/build versions, and investigate before concluding; do not select the convenient result.
- **Target cannot be accessed for testing**: report the documentation-based assessment separately and state that runtime behavior was not observed.
- **Build configuration generates manifests**: inspect the generated artifacts for each target, not only the generator source.
- **A feature is intentionally unsupported on one target**: record the user-visible limitation and require owner approval of the support statement.

## Test case
**Input:**
> Audit a page-save extension for Browser North and Browser South. I supplied code and a passing Browser North test, but no release ranges, generated Browser South package, or current Browser South documentation.

**Assertions:**
1. The response asks for or records the missing target release ranges.
2. Browser North’s result is scoped to its supplied test and build.
3. Browser South support remains unknown, not inferred from shared code.
4. The response identifies current official documentation and generated-package inspection as follow-up evidence.
5. No permission change, publication, or broad support claim is made.
</skill>

<user_request>
Audit a page-save extension for Browser North and Browser South. I supplied code and a passing Browser North test, but no release ranges, generated Browser South package, or current Browser South documentation.
</user_request>
