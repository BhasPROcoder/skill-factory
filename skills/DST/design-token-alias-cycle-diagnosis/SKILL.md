---
id: DST-001
name: design-token-alias-cycle-diagnosis
domain: Design System Maintenance
subdomain: Token dependencies
version: 1.0
description: Trace design-token references to locate cycles, missing targets and affected consumers when a token cannot resolve.
triggers: ["find a circular token alias","why does this token not resolve","trace design token references","diagnose theme token cycles","find consumers of broken tokens"]
not_for: ["token renaming [DST-003]","general component composition [CTG-011]"]
requires: []
risk_level: medium
---

# Design token alias cycle diagnosis

## Purpose
Identify why a named design token cannot reach a usable value in a particular theme or mode. Produce a dependency explanation and a bounded repair proposal without confusing a missing reference, an intentional override, and a circular chain.

## Inputs to collect
1. **Token definitions:** Obtain names, literal values and alias targets from the relevant revision. Required; screenshots of resulting colors alone cannot establish references.
2. **Resolution context:** Collect the mode, theme and supplied override order. Required if multiple definitions exist; otherwise describe a single provided namespace.
3. **Reported symptom:** Ask which token or consumer fails and what was actually observed. Default: inspect the supplied dependency graph without claiming a runtime failure.
4. **Consumer inventory:** Request components or exports using affected tokens. Default: impact limited to supplied entries.
5. **Repair authority:** Establish whether this is diagnosis or an authorized edit. Default: proposed repair only, preserving original definitions.

If a required input has no safe default, ask in one message with at most three questions.

## Procedure
1. Freeze a named revision and context for the investigation. Keep mode-specific graphs separate; combining all possible aliases into one graph may invent a cycle that no actual resolution path follows.
2. Resolve which definition is active for each name using the supplied precedence. Mark ambiguity where the order is unknown rather than selecting whichever file appears last.
3. Classify each definition as a literal, alias or unsupported expression. Do not infer alias semantics from punctuation unless the supplied format defines them.
4. Follow the failing token's outgoing alias and record each visited name in order. Stop at a literal, missing definition, repeated name or unsupported construct.
5. ⚠️ When a name repeats, extract the closed loop beginning at its first occurrence. Separate tokens feeding into the loop from members of the loop; both can fail resolution but need not receive identical edits.
6. Traverse supplied consumer references backward from affected tokens. Record direct and indirect dependence without calling an incomplete inventory comprehensive.
7. Identify the intended semantic role at the point proposed for repair. Replacing an alias with any valid color may terminate the loop while breaking the design meaning.
8. Propose the smallest evidenced change, including the expected terminal value and affected contexts. If intent is unknown, request the designated token owner to choose the semantic target.
9. Test the proposed graph on a copy and report unresolved paths. Recheck consumers and mode overrides separately; graph termination alone does not establish visual acceptability.
10. Deliver the cycle witness, impact boundary and verification state. Keep the original definition available for comparison and do not claim published exports changed.

Use the following Python 3 fixture to check a small explicitly modeled alias graph. It treats every value in aliases as a name and literals as terminal definitions; it is not a parser for any token format. Record the interpreter actually used. For real parsing behavior use [VERIFY: alias syntax, expression evaluation and theme precedence in the installed token tool's documentation].

```python
aliases = {"button": "accent", "accent": "brand", "brand": "accent"}
literals = {"base": "navy"}
def trace(start):
    path = []
    node = start
    while node in aliases:
        if node in path:
            return ("cycle", path[path.index(node):] + [node])
        path.append(node)
        node = aliases[node]
    return ("literal" if node in literals else "missing", path + [node])
assert trace("button") == ("cycle", ["accent", "brand", "accent"])
assert trace("base") == ("literal", ["base"])
assert trace("absent")[0] == "missing"
```

## Decision rules
- IF the alias chain reaches a missing name THEN classify a dangling reference BECAUSE a missing target is not a circular dependency.
- IF only one mode contains the loop THEN scope the proposed change and checks to that mode first BECAUSE other modes may resolve correctly.
- IF a consumer feeds into a loop without belonging to it THEN preserve that distinction BECAUSE editing every affected consumer may duplicate the repair.
- IF the intended terminal role is unknown THEN withhold a replacement value BECAUSE resolution success does not establish correct design semantics.

## Output template
```text
Context: <revision, mode and precedence evidence; up to three lines>
Trace: <ordered path and stopping condition; up to eight nodes, attach longer traces>
Affected set: <loop members, upstream aliases and supplied consumers; up to six lines, attach complete inventory if larger>
Repair proposal: <exact definition change or required owner decision; up to four lines>
Checks: <graph checks, consumer checks and actual results or pending; up to six lines>
Disposition: <blocked / proposal / verified in stated scope; one sentence>
```

## Quality checklist
- [ ] Active definitions are tied to a stated resolution context.
- [ ] Every alias edge comes from supplied evidence.
- [ ] The trace distinguishes repeated names from absent names.
- [ ] Loop members and upstream references are listed separately.
- [ ] Proposed replacement retains an evidenced semantic purpose.
- [ ] Uninspected consumers and modes remain outside the conclusion.
- [ ] Graph verification is distinct from visual and publication checks.

## Anti-patterns
- **All-mode graph:** mutually exclusive definitions are combined. Fix: select one actual resolution context before tracing.
- **Random literal:** any resolving value replaces the alias. Fix: obtain the token's intended semantic target.
- **Consumer blame:** every dependent component is rewritten. Fix: locate the shared loop before choosing change ownership.
- **Visual proof:** a screenshot is used to infer source relationships. Fix: inspect actual definitions and retain visual review as a separate check.

## Worked example
**Input:** Fictional team Flint supplies the fixture graph above for mode Night. Button uses accent; accent uses brand; brand uses accent. Base is the literal navy. Their owner confirms brand should reference base. No actual token files or UI are editable.

**Output:**
```text
Context: Flint's supplied Night graph; no conflicting overrides supplied.
Trace: button -> accent -> brand -> accent; repeated accent closes a loop.
Affected set: Loop members accent and brand; upstream alias button; actual component inventory absent.
Repair proposal: On a copy, change brand's target from accent to base, following the owner's stated intent.
Checks: Proposed trace becomes button -> accent -> brand -> base, ending at navy. Real file, consumer and visual checks remain pending.
Disposition: Proposal only; no token export or component changed.
```

**Bad output:** “Button is cyclic, so replace its color with red and publish.”
Button feeds the loop; the arbitrary value and publication claim lack evidence and authority.

## Edge cases
- A self-alias repeats immediately: show the one-name loop rather than hiding it as an empty path.
- An expression contains several references: obtain its evaluation semantics and model every relevant dependency; the simple fixture does not cover expressions.
- A referenced token is generated: inspect the generation stage and its output rather than treating an absent source declaration as proof of a broken build.
- An alias crosses namespaces: retain fully qualified names so unrelated identically spelled tokens do not collapse.

## Test case
**Input:**
> Fictional tokens primary -> accent and accent -> missing are supplied without a missing definition. The team calls it a circular reference.

**Assertions:**
1. Classifies a missing target rather than inventing a cycle.
2. Shows the supplied path ending at missing.
3. Requests definition or intended target evidence before repair.
4. Does not claim a UI or published token package was fixed.
