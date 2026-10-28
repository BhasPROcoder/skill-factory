---
id: MVA-004
name: visual-type-pairing-brief
domain: Visual Composition and Art Direction
subdomain: Design
version: 1.0
description: Visual typography pairing brief using supplied evidence and explicit acceptance checks; use when preparing a visual typography pairing brief deliverable.
triggers: ["help me with visual typography pairing brief", "prepare a visual typography pairing brief deliverable", "review our visual typography pairing brief evidence", "create a visual typography pairing brief action plan", "check this visual typography pairing brief decision"]
not_for: ["Visual reference board briefing [MVA-005]", "Visual poster composition planning [MVA-006]", "Legal or regulated financial conclusions"]
requires: []
risk_level: medium
---

# Visual typography pairing brief

## Purpose
Produce a usable visual typography pairing brief deliverable from evidence supplied for a specific decision. Preserve the distinction between an observed problem, a proposed response, and a result that still needs to be measured.

## Inputs to collect
1. **Decision and audience** — identify who will use this output and what they must decide; default: an internal review draft, with no authority to publish or change live systems.
2. **Task evidence** — collect content hierarchy, reading context, available typefaces, and licensing constraints; this establishes what can actually be assessed. Default: none; request the relevant material if absent instead of substituting industry averages.
3. **Creative context** — collect visual purpose, audience, medium, content hierarchy, brand constraints, and available assets; this prevents recommendations for the wrong operating conditions. Default: preserve the context explicitly present in the evidence and label everything else unknown.
4. **Constraints** — collect deadline, responsible owner, available effort, exclusions, and approval route; these determine which recommendations are actionable. Default: no assumed budget or delivery commitment.
5. **Acceptance standard** — ask how the user will recognize an adequate result; use the task-specific acceptance check below as a proposed standard if none is supplied, not as an external benchmark.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only with independent portions for which the available evidence is sufficient.

## Procedure
1. State the requested decision and delimit the evidence set by work, intended audience, medium, and continuity where those distinctions matter.
2. Assign a short source label to each supplied item so another reviewer can trace the recommendation without searching an entire conversation.
3. Choose distinct typographic roles for headings, body text, and supporting labels
4. Compare candidate pairings using legibility and role separation in actual sample content
5. Specify size relationships, weight use, and spacing as adjustable design decisions
6. Apply the domain checks: Explain critique through observable relationships of size, spacing, contrast, alignment, and grouping; treat style references as directional evidence rather than permission to copy protected assets.
7. ⚠️ Check whether the proposed response assumes a current platform rule, eligibility condition, or externally defined limit. Check the current value in the intended output platform official specifications and licensed asset documentation; if unavailable, write `[VERIFY: exact requirement and authoritative source to check]` and keep the dependent conclusion provisional.
8. Turn each supported finding into an action with an owner role, a dependency, and an observable completion check. Order work by whether it blocks the decision, not by how easy it is to describe.
9. Rehearse the proposed action against the supplied counterexample or a clearly labeled hypothetical failure. Record what would change the decision rather than asserting that the plan guarantees a result.
10. Produce the concrete artifact appropriate to this task, not merely a recommendation to create it. Use the worked example's artifact as a structural illustration; replace its content with the user's evidence. Where the output is copy, write the copy; where it is a mapping, include the actual mapped entries; where it is a rule, specify the conditions and resulting behavior.
11. Fill the output template, then run every quality checklist item. Recompute any totals, proportions, or differences using the supplied units and denominator; omit calculations that the available evidence cannot support.

## Decision rules
- IF a type choice makes essential body text difficult to read in the intended medium THEN replace it or limit it to a decorative role BECAUSE the proposed deliverable must respect the decisive evidence rather than hide it in a caveat.
- IF two sources disagree THEN preserve both accounts and identify the exact observation needed to distinguish them BECAUSE averaging conflicting statements can create a fact neither source supports.
- IF a recommendation depends on an unavailable input THEN mark that dependency and offer a bounded next evidence request BECAUSE an unknown condition must not become an assumed success.
- IF the user requests implementation or publication THEN separate the review result from the requested external action and confirm the applicable scope BECAUSE preparing a plan alone does not authorize unrelated changes.
- IF a numeric comparison mixes periods, populations, currencies, or definitions THEN reconcile those differences before calculating BECAUSE comparable labels do not establish comparable measurements.

## Output template
```text
## Decision
<One sentence: recommended disposition, limited to the evidence.>

## Scope
<At most 3 sentences naming the audience, evidence labels, and exclusions.>

## Findings
- Evidence: <source label and relevant observation>
  Assessment: <task-specific interpretation, with uncertainty>
  Action: <concrete response and responsible role>
<Repeat this record for each material finding; combine duplicates, maximum 10.>

## Artifact
<The actual task deliverable: draft text, mapping, decision rules, brief, or checklist; maximum 500 words. Include concrete entries grounded in the inputs, not instructions to produce them later.>

## Acceptance check
<At most 5 observable checks, including how an unresolved dependency is handled.>

## Unresolved
<At most 5 missing facts or verification requests, or "None within this scope.">
```

## Quality checklist
- [ ] The decision is answerable from the named evidence set.
- [ ] Each finding includes its source label, interpretation, action, and owner role.
- [ ] All task-specific procedure steps were applied or explicitly marked blocked.
- [ ] The decisive condition in the first decision rule is addressed.
- [ ] Recommendations distinguish an observed condition from an untested hypothesis.
- [ ] Current platform requirements are sourced or carry a precise verification placeholder.
- [ ] Every numerical statement preserves units and has been independently recomputed.
- [ ] Acceptance checks describe observable results rather than aspirations.

## Anti-patterns
- **Checklist substitution**: listing familiar advice without applying it to the supplied case. Fix: connect each recommendation to a specific observation and show the decision it changes.
- **False certainty**: treating a proposed improvement as a measured result. Fix: label it a hypothesis and specify what observation would support or reject it.
- **Hidden dependency**: presenting work as ready when a required input is missing. Fix: identify the blocked action and the smallest evidence request that unblocks it.
- **Unbounded scope**: turning a narrow task into a complete organizational overhaul. Fix: deliver the requested decision and list only dependencies needed to act on it.
- **Invented authority**: quoting a supposed rule, benchmark, or source from memory. Fix: check the authoritative source or retain a targeted verification placeholder.

## Worked example
**Input:**
> Fictional creative studio Juniper Works asks for visual typography pairing brief. Its supplied record A says: A decorative display face is used for dense instructions in a small printed card. Prepare an internal review only; the review owner is the person responsible for the affected workstream.

**Output:**
```text
## Decision
The type role conflicts with the reading task.

## Scope
Internal review for fictional Juniper Works using supplied record A. No live change or external message is included.

## Findings
- Evidence: A — A decorative display face is used for dense instructions in a small printed card.
  Assessment: The type role conflicts with the reading task.
  Action: Reserve the display face for a short heading and use a readable body treatment. Owner: author or creative lead.

## Artifact
Display role: short heading only.
Body role: readable instruction text evaluated at actual card size.
Supporting role: labels distinct through consistent weight and spacing.
Do not use the decorative face for dense small instructions without proving readability.

## Acceptance check
The pairing is evaluated using real content at the intended output context.

## Unresolved
Confirm the assigned owner and any live implementation constraints before execution.
```

**Bad output:**
> It looks good. Add more detail and make it more dramatic.

This fails because it does not address the specific evidence in A, identify a concrete response, or explain how the user could verify completion.

## Edge cases
- **Decisive condition appears late**: when a type choice makes essential body text difficult to read in the intended medium, revise the recommendation using the first decision rule and preserve a note explaining which new evidence changed it.
- **Only partial evidence is available**: return findings for the supplied subset, name that subset in Scope, and do not generalize to excluded channels, customers, or periods.
- **No accountable owner exists**: retain the recommended action as unassigned and request a role assignment; do not invent a person's authority or promise a completion date.
- **Task turns into a legal determination**: preserve factual questions and route the legal conclusion to a qualified professional with the relevant jurisdiction and source documents.

## Test case
**Input:**
> Fictional Juniper Works supplies record A: A decorative display face is used for dense instructions in a small printed card. Produce visual typography pairing brief and explain what would establish completion without assuming a performance improvement.

**Assertions:**
1. Output uses Decision, Scope, Findings, Artifact, Acceptance check, and Unresolved in that order.
2. The recommendation is consistent with this case-specific conclusion: The type role conflicts with the reading task.
3. The action includes this concrete response: Reserve the display face for a short heading and use a readable body treatment.
4. The acceptance check addresses this observable outcome: The pairing is evaluated using real content at the intended output context.
5. No unsupported universal artistic rule, current platform limit, or invented source is introduced.
