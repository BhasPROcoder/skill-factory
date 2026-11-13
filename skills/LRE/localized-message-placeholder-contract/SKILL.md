---
id: LRE-001
name: localized-message-placeholder-contract
domain: Localization Resource Engineering
subdomain: Message parameters
version: 1.0
description: Check localized message parameters against their runtime roles when translated strings can lose, rename or misuse interpolation values.
triggers: ["check translated placeholders", "validate message parameters", "find missing interpolation values", "review translated variable roles", "test localization placeholder contracts"]
not_for: ["reviewing ordinary translated names and quantities [GLA-006]", "assessing translation fluency", "design-token rename migration [DST-003]"]
requires: []
risk_level: medium
---

# Localized message placeholder contract

## Purpose
Build and test a message-specific contract connecting runtime parameter names to the meanings they carry in each localized pattern. Separate syntactic completeness from semantic placement so a string with all the right tokens can still be flagged when it exchanges the actor and recipient.

## Inputs to collect
1. **Message boundary:** Obtain stable message keys, source and target revisions, and target locales. This prevents comparing unrelated strings. Default: none; a bounded key set is required.
2. **Pattern grammar:** Obtain the installed formatter's syntax and escaping rules, including any branches or rich-text elements. This determines the parser. Default: no production parsing; request the project's current official formatter documentation.
3. **Parameter contract:** Collect each parameter's name, meaning, type and permitted omission or repetition by branch. This defines correctness. Default: unknown, not inferred from token spelling alone.
4. **Localized patterns:** Obtain actual target strings and translator context. This makes the comparison reproducible. Default: absent targets remain missing rather than copied from source.
5. **Runtime examples:** Obtain harmless representative values and the permitted execution environment. This allows rendering without exposing user data. Default: fictional fixtures and no production modification.
6. **Language review:** Identify a competent reviewer for role placement and surrounding text. This distinguishes token checks from meaning review. Default: semantic conclusions pending where competence is unavailable.

If a required input has no safe default, ask in one message with at most three questions. Group the key/revision request, grammar/contract request and review-evidence request rather than asking separately for every string.

## Procedure
1. Freeze the scoped resource revisions and list the parameter meanings for each message. Record context such as sender, recipient or remaining quantity; names alone may be ambiguous.
2. Parse the patterns using their real grammar. ⚠️ Do not use a simple token expression on a grammar with nested branches, escaping or embedded markup; choose its supported parser or stop at a declared fixture-only check.
3. Compare parameter identities with the supplied contract for each reachable branch. Report missing, unexpected and invalidly repeated parameters separately; repetition can be intentional when the contract permits it.
4. Inspect whether target placement preserves each parameter's role. Reordering words is not itself an error; a translation may need another order while still expressing the same relationship.
5. Render representative cases with distinctive fictional values. Make actor and recipient visibly different so swapped roles are observable, and include blank or long values only when the application allows them.
6. Review rendered results for unresolved tokens, truncated dynamic content and misplaced punctuation. Record the tested environment and distinguish formatter output from a real interface rendering.
7. Route each failure to its responsible layer: supplied data, parameter contract, localized pattern, formatter configuration or display layout. Avoid correcting a data mapping problem by replacing a translator's words.
8. Recheck affected branches after a repair and preserve evidence for unaffected ones. ⚠️ A default-branch pass does not prove a plural or optional branch uses the same parameters correctly.
9. Produce the contract ledger and bounded verification statement. Keep language review pending when only mechanical token correspondence was checked.

The runnable Python 3 example below uses a deliberately restricted fictional grammar: tokens are `[[identifier]]`, identifiers contain ASCII letters, digits or underscores and start with a letter or underscore, every required token appears exactly once, and escaping or nested branches are unsupported. This is not a parser for a production localization library. Save as a Python file and run it in the available Python 3 environment; record the actual interpreter version with the result.

```python
import re
from collections import Counter

TOKEN = re.compile(r"\[\[([A-Za-z_][A-Za-z0-9_]*)\]\]")

def check(pattern, required):
    residual = TOKEN.sub("", pattern)
    if "[[" in residual or "]]" in residual:
        return {"syntax": "unsupported or malformed token"}
    actual = Counter(TOKEN.findall(pattern))
    expected = Counter(required)
    return {
        "missing": sorted((expected - actual).elements()),
        "unexpected": sorted((actual - expected).elements())
    }

assert check("[[to]] received from [[from]]", ["from", "to"]) == {
    "missing": [], "unexpected": []}
assert check("[[from]] sent", ["from", "to"])["missing"] == ["to"]
assert check("[[to]] [[to]]", ["from", "to"]) == {
    "missing": ["from"], "unexpected": ["to"]}
assert "syntax" in check("[[bad-name]]", [])
print("fixture checks passed; language roles remain unverified")
```

## Decision rules
- IF the grammar includes unsupported escaping or branches THEN obtain an appropriate parser BECAUSE fixture token recognition cannot establish production syntax validity.
- IF token identities match but their surrounding roles are uncertain THEN keep semantic review open BECAUSE a set comparison cannot distinguish sender from recipient.
- IF a target intentionally repeats a parameter THEN compare against its explicit branch contract BECAUSE source occurrence counts are not a universal translation rule.
- IF a required runtime value is absent THEN fix or clarify the data contract BECAUSE deleting its placeholder can hide a caller defect.

## Output template
```text
Boundary: <keys, revisions, locales and grammar; up to three lines>
Contract ledger:
Key/branch | Parameter and role | Target occurrence | Mechanical finding | Meaning review
<up to twelve rows; each cell at most thirty words>
Executed cases: <up to six cases; inputs, environment and observed output>
Repairs: <up to five layer-specific actions and rechecks>
Pending: <up to three grouped questions, or None>
Limits: <two sentences distinguishing tokens, meaning and interface rendering>
```

## Quality checklist
- [ ] Each finding identifies a message key and resource revision.
- [ ] The real grammar or fixture restriction is stated.
- [ ] Parameter roles come from a supplied contract or remain unresolved.
- [ ] Missing and unexpected parameters are distinct findings.
- [ ] Branches and permitted repetition are checked separately.
- [ ] Test values distinguish roles without using private data.
- [ ] Semantic approval is not inferred from token equality.
- [ ] Actual execution and unexecuted production checks are clearly separated.

## Anti-patterns
- **Universal regex:** a small token matcher is used on nested message syntax. Fix: use the formatter's parser or restrict the claim to the fixture grammar.
- **Order policing:** target token order is forced to match source order. Fix: verify roles and grammar rather than word order.
- **Token-only approval:** matching parameter names are called a correct translation. Fix: retain a competent meaning review.
- **Convenient deletion:** a missing runtime value is addressed by dropping a required parameter. Fix: resolve the data or approved message contract.
- **Branch blindness:** one default rendering approves every alternative. Fix: exercise the actual reachable branches and record omissions.

## Worked example
**Input:**
> Fictional app Alder's message transfer has source revision S and target revision T for the project's locale label West. It uses sender and receiver exactly once under the fixture grammar above. Sender is the person giving a document; receiver is the person getting it. Target pattern says “[[receiver]] received from [[sender]].” A supplied competent reviewer confirms the roles. Supplied run record E identifies the interpreter and successful Python fixture assertions; no interface render exists.

**Output:**
```text
Boundary: Alder transfer, source S and target T, locale West; restricted double-bracket fixture grammar.
Contract ledger:
Key/branch | Parameter and role | Target occurrence | Mechanical finding | Meaning review
transfer/default | sender gives document | once after from | conforms to supplied contract | reviewer confirms giver role
transfer/default | receiver gets document | once before received | conforms to supplied contract | reviewer confirms recipient role
Executed cases: Supplied run record E reports successful Python fixture token assertions and identifies the interpreter. No interface case executed.
Repairs: None established for supplied pattern and contract.
Pending: None for this bounded check.
Limits: Token identity and supplied role review support this pattern. Actual display fit and production formatter behavior were not tested.
```

**Bad output:** “The tokens changed order, so replace the target with source word order.”
This rejects a role-preserving construction without evaluating its meaning and may damage the translation.

## Edge cases
- **Parameter renamed by an adapter:** require the explicit caller-to-pattern mapping and test the mapped names; do not assume aliases exist.
- **Optional branch omits a value:** apply that branch's supplied contract and show why omission is permitted.
- **Literal token-like text:** obtain the formatter's escape behavior before deciding the text is a parameter; the fixture checker cannot model escapes.
- **Same displayed values:** use distinct fictional replacements to expose role exchange; identical values can conceal it.

## Test case
**Input:**
> Fictional message invite requires inviter and invitee once each. Target contains invitee twice and no inviter. The names displayed in the supplied preview happen to match. No competent language review is available.

**Assertions:**
1. Reports missing inviter and unexpected extra invitee under the supplied contract.
2. Does not accept identical displayed names as evidence of correct mapping.
3. Requests distinct fictional render values after repair.
4. Leaves language meaning review pending.
