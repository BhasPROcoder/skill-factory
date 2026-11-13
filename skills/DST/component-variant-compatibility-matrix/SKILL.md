---
id: DST-002
name: component-variant-compatibility-matrix
domain: Design System Maintenance
subdomain: Component contracts
version: 1.0
description: Build a supported-state matrix for component variants when independent properties can combine into invalid or undefined behavior.
triggers: ["document component variant combinations","which component props work together","build a design-system state matrix","find unsupported component variants","test component combination coverage"]
not_for: ["product configurator repair [UST-002]","generic state-transition test design [TST-003]"]
requires: []
risk_level: medium
---

# Component variant compatibility matrix

## Purpose
Translate a component's property definitions into explicit supported, prohibited and unresolved combinations. The matrix helps designers, implementers and reviewers distinguish a complete interaction contract from a collection of attractive isolated examples.

## Inputs to collect
1. **Component boundary:** Obtain the component name, revision and responsibilities. Required; do not merge unrelated components just because they share styles.
2. **Property domains:** Collect each exposed property's allowed values and actual defaults. Required for a finite matrix; unspecified defaults remain unknown.
3. **Combination rules:** Request constraints and their source, including dependent properties and required content. Default: absence of a rule means unresolved support, not permission.
4. **Behavior evidence:** Gather implemented examples, design specifications and known failures. Default: proposed contract only; no rendered results.
5. **Coverage priority:** Identify common uses and consequential interactions. Default: enumerate the supplied small space and flag larger spaces for explicit sampling.
6. **Owner decisions:** Identify who can declare support or remove an option. Default: recommendations await the component owner.

If required inputs lack a safe default, ask one message with at most three questions.

## Procedure
1. Normalize property names and values without erasing distinctions such as absent, false, empty and explicitly selected. These may map to different behavior under the actual implementation.
2. Calculate the nominal combination space from independent property domains. State the model's assumptions; mutually derived properties should not be counted as independent choices.
3. Apply supplied constraints to each combination. Label a combination supported only when its behavior contract is established; distinguish prohibited by rule from unresolved due to missing evidence.
4. ⚠️ Separate static combinations from transitions between them. A loading button may have a valid appearance yet lack a rule for focus and activation when loading changes.
5. Write expected visible content, input handling and state communication for representative supported rows. A screenshot alone does not establish whether activation is accepted or which label is announced.
6. Identify equivalent rows only through a stated behavior invariant. Do not collapse different keyboard behavior because two rows look identical.
7. Choose tests covering each explicit constraint and each distinct supported behavior. For a large space, document omitted combinations and the rationale rather than claiming complete coverage from a small gallery.
8. Run or request render and interaction checks for selected rows in the actual target environment. Preserve failed and not-executed states; an example missing from a gallery is not itself evidence that the component rejects it.
9. Route contradictory rules to the component owner. Preserve both sources and the conflicting row so the decision can be resolved without guessing.
10. Deliver the matrix, unresolved contract items and coverage statement. Treat a design decision as proposed until the implementation and consumer documentation align.

The following Python 3 fixture enumerates a fictional static space; it does not implement a component or certify accessibility. Record the interpreter used. Check current framework prop coercion and event behavior in the installed framework's official documentation before applying a real implementation.

```python
from itertools import product
rows = list(product(["normal", "loading"], ["text", "icon"]))
forbidden = {("loading", "icon")}
supported = [r for r in rows if r not in forbidden]
assert len(rows) == 4
assert len(supported) == 3
assert ("loading", "icon") not in supported
```

## Decision rules
- IF a property default is unspecified THEN keep absent-property behavior unresolved BECAUSE an explicit value does not prove default behavior.
- IF a constraint forbids a combination THEN include a rejection or normalization requirement BECAUSE hiding the row from documentation does not prevent consumers requesting it.
- IF visual states match but interaction rules differ THEN retain separate coverage BECAUSE appearance is not a complete behavioral contract.
- IF tests cover only selected combinations THEN report the selection boundary BECAUSE an exhaustive input list and an exhaustive execution are different achievements.

## Output template
```text
Component: <identity and supplied contract scope; one sentence>
Space: <property domains, nominal count and assumptions; up to five lines>
Matrix: <up to eight representative rows; attach remaining distinct contracts rather than omit them>
Combination | Support status | Expected behavior | Evidence or question
Coverage: <selected cases, constraints exercised and omissions; up to six lines>
Owner decisions: <up to three consolidated decisions>
Verification: <actual execution or proposed checks and limits; up to four lines>
```

## Quality checklist
- [ ] Allowed property values and unknown defaults are explicit.
- [ ] Nominal count is computed from the stated domains.
- [ ] Unsupported and unresolved combinations are distinguished.
- [ ] Representative rows include interaction, not only appearance.
- [ ] Every collapsed row has a stated equivalence basis.
- [ ] Each explicit constraint has a checkable case.
- [ ] Test selection and actual execution are reported separately.
- [ ] Contradictory source rules remain visible.

## Anti-patterns
- **Gallery completeness:** a few attractive screenshots are called full coverage. Fix: map them to explicit combinations and show gaps.
- **Implicit prohibition:** unsupported combinations disappear from the table. Fix: specify what consumers receive when requesting them.
- **Defaults by habit:** familiar values are assumed to be defaults. Fix: inspect the supplied implementation or obtain a decision.
- **Pair count inflation:** redundant derived properties multiply the nominal space. Fix: identify which properties are independently settable.
- **Silent normalization:** the implementation changes a consumer's request without a contract. Fix: document rejection or normalization and test its observable outcome.

## Worked example
**Input:** Fictional team Garnet defines Button-R with phase normal or loading and content text or icon. Its supplied contract permits the three combinations except loading plus icon. Text remains visible while loading and activation is rejected; normal rows permit activation. No default or rendered UI is provided.

**Output:**
```text
Component: Garnet Button-R, supplied static property contract.
Space: phase={normal,loading}; content={text,icon}; two independent choices each produce four nominal combinations; absent defaults unknown.
Matrix:
Combination | Support status | Expected behavior | Evidence or question
normal,text | Supported by contract | Text visible, activation accepted | Supplied rule; runtime untested
normal,icon | Supported by contract | Icon visible, activation accepted | Accessible name requirement unresolved
loading,text | Supported by contract | Text retained, activation rejected | Supplied rule; loading announcement unresolved
loading,icon | Prohibited | Rejection or normalization behavior requires decision | Supplied constraint
Coverage: Propose all four static rows and normal-to-loading transition; no checks executed.
Owner decisions: Define absent defaults; accessible naming and state communication; prohibited-request handling.
Verification: Matrix prepared only; rendering, keyboard and assistive interaction remain untested.
```

**Bad output:** “Four prop combinations means four valid components; screenshots prove they work.”
The supplied constraint excludes one, and no interaction tests were performed.

## Edge cases
- A free-text property has unbounded content: use explicit representative content classes and disclose that enumeration is not exhaustive.
- Responsive layout alters behavior: add the relevant environment dimension instead of treating width as purely decorative.
- Different versions permit different combinations: keep version-specific tables and identify migration decisions.
- Consumer overrides bypass the component contract: record the override separately and do not attribute its behavior to the supported component.

## Test case
**Input:**
> Fictional component mode has values compact and expanded; dismissible has true and false. A rule prohibits compact plus dismissible, but a sample gallery shows that combination.

**Assertions:**
1. Computes four nominal combinations.
2. Records a conflict between the rule and gallery rather than selecting one silently.
3. Requests the owner's intended contract and runtime evidence.
4. Does not claim that every combination was executed.
