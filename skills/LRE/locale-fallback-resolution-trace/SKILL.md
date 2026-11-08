---
id: LRE-002
name: locale-fallback-resolution-trace
domain: Localization Resource Engineering
subdomain: Resource fallback
version: 1.0
description: Trace which locale resource actually supplies a message when fallback order, blank values or unavailable bundles can conceal missing translations.
triggers: ["trace locale fallback", "why is this message in another language", "check missing translation fallback", "test blank localized values", "inspect message resource resolution"]
not_for: ["token-reference cycle diagnosis [DST-001]", "translation quality assessment", "choosing a user's locale without a product policy"]
requires: []
risk_level: medium
---

# Locale fallback resolution trace

## Purpose
Explain the exact resource selected for a localized message and why earlier candidates did not supply it. Produce a repeatable resolution trace that keeps fallback availability separate from native-locale translation coverage.

## Inputs to collect
1. **Requested context:** Obtain the message key, requested locale, namespace and application state. This fixes the lookup boundary. Default: none; message and request identity are required.
2. **Resolution policy:** Obtain the configured candidate order, namespace behavior and handling of missing, null and empty values. This establishes the algorithm. Default: unknown; do not infer locale parents by trimming a locale name.
3. **Resource snapshot:** Obtain relevant bundles and their revision identifiers. This provides the values being considered. Default: missing snapshot prevents a current selection claim.
4. **Loading evidence:** Identify which bundles were loaded, still pending or unavailable at the observed lookup. This distinguishes resource absence from a load race. Default: loading state unknown, not presumed complete.
5. **Runtime evidence:** Collect a reproducible request or supplied trace and the installed formatter/resource-loader details. Default: reference-fixture execution only; check current official documentation before asserting framework-specific behavior.
6. **Acceptance intent:** Ask whether fallback is permitted for this message and whether a blank string is intentional. Default: report resolution without approving release or inventing translation requirements.

If a required input has no safe default, ask in one message with at most three questions. Group requests around lookup identity, configured policy and resource/loading evidence.

## Procedure
1. Record the precise lookup request and resource snapshot. Keep a source-of-truth key separate from text that merely resembles its displayed result.
2. Expand the supplied resolution policy into an ordered list of candidate locale/namespace pairs. ⚠️ Do not derive a generic language hierarchy: the application's configured order is the contract to test.
3. Classify each candidate as available, pending load or unavailable according to the supplied observation. Keep a pending bundle visible even if the application temporarily selected a later candidate.
4. Inspect the key in each available bundle using the supplied missing-value policy. Distinguish absent key, explicit null, empty string and nonempty value; an empty value can be deliberate under one policy and missing under another.
5. Stop the trace at the first candidate that qualifies under the policy. Record its locale and namespace alongside the displayed value so a fallback does not masquerade as a translated target value.
6. Compare the predicted trace with actual runtime evidence, if available. A disagreement requires investigating the snapshot, cache, loading state or lookup policy rather than editing translations blindly.
7. Exercise a present-target case, an absent-key case and a blank-value case. Add a loading transition case when the application can resolve before all bundles arrive.
8. Determine which missing translations are masked by a successful fallback. A visible string can keep the interface usable while still leaving target-language coverage incomplete.
9. Recommend a correction at the responsible layer and define the replay needed. ⚠️ Do not change fallback order solely to hide a missing target translation; obtain the product's intended language behavior first.
10. Deliver the resolution trace and evidence limits, retaining unknowns instead of stating that a fixture reproduces an unobserved application.

This runnable Python 3 fixture models an explicitly supplied ordered locale list for one namespace. Bundle values are strings or null, all bundles are already loaded, null is always missing, and the caller explicitly chooses whether empty strings qualify. It has no locale negotiation, cache or asynchronous loading implementation. Save it as a Python file and run it with the available Python 3 interpreter; record the actual environment.

```python
def resolve(key, order, bundles, empty_is_value):
    if len(order) != len(set(order)):
        raise ValueError("duplicate locale in explicit order")
    trace = []
    for locale in order:
        if locale not in bundles:
            trace.append((locale, "bundle unavailable"))
            continue
        bundle = bundles[locale]
        if key not in bundle:
            trace.append((locale, "key absent"))
            continue
        value = bundle[key]
        if value is None or (value == "" and not empty_is_value):
            trace.append((locale, "value missing by policy"))
            continue
        if not isinstance(value, str):
            raise ValueError("fixture values must be string or null")
        trace.append((locale, "selected"))
        return {"locale": locale, "value": value, "trace": trace}
    return {"locale": None, "value": None, "trace": trace}

bundles = {"target": {"title": ""}, "base": {"title": "Archive"}}
assert resolve("title", ["target", "base"], bundles, False)["locale"] == "base"
assert resolve("title", ["target", "base"], bundles, True)["value"] == ""
assert resolve("absent", ["target", "base"], bundles, False)["locale"] is None
assert resolve("title", ["unknown", "base"], bundles, False)["trace"][0] == (
    "unknown", "bundle unavailable")
print("explicit-order fixture checks passed")
```

## Decision rules
- IF a fallback supplies the displayed value THEN record its actual locale BECAUSE display success does not establish requested-locale coverage.
- IF a target bundle is pending load THEN preserve that state in the diagnosis BECAUSE temporary resolution can differ from the fully loaded snapshot.
- IF an empty string is intentional under the supplied policy THEN retain it as a value BECAUSE substituting fallback text changes the approved message behavior.
- IF runtime and fixture disagree THEN investigate the implementation contract BECAUSE the reference model does not prove the application's actual lookup sequence.
- IF a message forbids fallback under product requirements THEN report its missing target value as a release issue BECAUSE a generic fallback rule cannot override message-specific intent.

## Output template
```text
Lookup: <key, requested locale, namespace and snapshot; up to three lines>
Policy: <ordered candidates and missing-value rules; up to three lines>
Trace:
Candidate | Loading state | Key/value state | Decision
<up to twelve rows; continue explicitly if required>
Selection: <actual supplier, value or unresolved; two sentences maximum>
Coverage: <native target versus fallback availability; two sentences maximum>
Correction and replay: <up to four owned actions and test cases>
Evidence limit: <fixture, supplied trace or runtime execution; two sentences>
```

## Quality checklist
- [ ] The lookup includes namespace and requested locale.
- [ ] Candidate order comes from supplied configuration.
- [ ] Empty, null and absent states are distinguished.
- [ ] Pending load is not silently recorded as permanent absence.
- [ ] The selected value retains its actual supplier identity.
- [ ] Native-language coverage and visible availability are separate findings.
- [ ] Runtime observations are distinguished from fixture predictions.
- [ ] Replays cover the changed policy or resource state.

## Anti-patterns
- **Locale trimming:** assumed parents replace configured lookup order. Fix: collect the actual ordered policy.
- **Truthy lookup:** a blank value is skipped without checking its meaning. Fix: apply the explicit empty-value rule.
- **Visible equals translated:** any displayed text counts as target coverage. Fix: retain the selected resource locale.
- **Race erased:** a pending bundle is called a missing translation. Fix: compare loading states before and after completion.
- **Fixture certainty:** a reference algorithm is described as the live application. Fix: label the model and compare an actual trace before runtime conclusions.

## Worked example
**Input:**
> Fictional app Birch requests key title in namespace exhibits for locale target. Supplied policy tries target then base, treats empty strings as missing, and all supplied bundles are loaded. Target has title as an empty string; base has Archive. The Python reference fixture produced that trace; no live app test is available.

**Output:**
```text
Lookup: Birch title, requested target, namespace exhibits, supplied frozen bundle snapshot.
Policy: target then base; null and empty string count as missing; all fixture bundles loaded.
Trace:
Candidate | Loading state | Key/value state | Decision
target/exhibits | loaded in fixture | title empty | skip by supplied policy
base/exhibits | loaded in fixture | title Archive | select
Selection: Reference fixture selects Archive from base, not target.
Coverage: Fallback text is available. Target title translation remains missing under the supplied policy.
Correction and replay: Translation owner supplies target title if required; replay target-present and target-empty cases with the actual application before a runtime claim.
Evidence limit: Python reference fixture executed against supplied inputs. No live loader, cache or interface behavior tested.
```

**Bad output:** “Title displays successfully, so target localization is complete.”
This conceals the fallback supplier and confuses availability with target-language coverage.

## Edge cases
- **Same text in several locales:** use selected resource identity rather than the appearance of the text to determine which locale supplied it.
- **Namespace fallback:** preserve locale/namespace pairs in the configured order instead of applying two independent guessed loops.
- **Cached old value:** compare resource revision and cache evidence before blaming the new translation; do not assume cache invalidation occurred.
- **All candidates miss:** report unresolved lookup and the application's supplied missing-key behavior; do not invent a display placeholder as observed output.

## Test case
**Input:**
> Fictional app Cedar permits intentional empty labels. Target key subtitle is empty, base is Details, and both are loaded. A developer proposes a truthiness-based lookup that skips the target value.

**Assertions:**
1. Selects the empty target value under the supplied policy.
2. Flags the proposed lookup as inconsistent with intentional blank behavior.
3. Does not replace the empty label with Details without a policy change.
4. Separates fixture behavior from actual application execution.
