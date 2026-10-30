---
id: MOP-008
name: startup-service-capacity-plan
domain: Startup Operating Workflows
subdomain: Design
version: 1.1
description: Guide startup service capacity planning when working from recurring service request mix, arrival observations, work-stage effort, rework frequencies, and role availability.
triggers: ["startup service capacity planning", "help with startup service capacity planning", "work on startup service capacity plan", "review my startup service capacity planning", "apply startup service capacity planning to these materials"]
not_for: ["Allocate finite specialist capacity among competing business initiatives [BPL-003]", "Diagnose observed workflow delays after delivery [MOP-010]"]
requires: []
risk_level: medium
---

# Startup service capacity planning

## Purpose
Complete this startup service capacity planning task using material supplied for a specific decision. Preserve the distinction between an observed problem, a proposed response, and a result that still needs to be measured.

## Inputs to collect
1. **Decision and audience** — identify who will use this output and what they must decide; default: an internal review draft, with no authority to publish or change live systems.
2. **Task evidence** — collect recurring service request mix, arrival observations, work-stage effort, rework frequencies, and role availability; this establishes what can actually be assessed. Default: none; request the relevant material if absent instead of substituting industry averages.
3. **Business context** — collect team roles, current workflow, demand patterns, service commitments, and available systems; this prevents recommendations for the wrong operating conditions. Default: preserve the context explicitly present in the evidence and label everything else unknown.
4. **Constraints** — collect deadline, responsible owner, available effort, exclusions, and approval route; these determine which recommendations are actionable. Default: no assumed budget or delivery commitment.
5. **Acceptance standard** — ask how the user will recognize an adequate result; use the task-specific acceptance check below as a proposed standard if none is supplied, not as an external benchmark.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only with independent portions for which the available evidence is sufficient.

## Procedure
1. State the requested decision and delimit the evidence set by product, audience, channel, and period wherever those distinctions matter.
2. Assign a short source label to each supplied item so another reviewer can trace the recommendation without searching an entire conversation.
3. Decompose one recurring service request into preparation, review, handoff, and conditional rework stages using observed or explicitly estimated effort
4. Translate the expected request mix into workload for each role in the same planning window, retaining uncertainty in arrivals and rework
5. Identify the role whose stage workload limits accepted service volume and define a review trigger when the request mix changes
6. Apply the domain checks: Separate an agreed service commitment from an aspirational target; expose single-person dependencies; design exception handling alongside the normal path rather than assuming every request is complete.
7. ⚠️ Check whether the proposed response assumes a current platform rule, eligibility condition, or externally defined limit. Check the current value in the approved operating policy and relevant vendor official service documentation; if unavailable, write `[VERIFY: exact requirement and authoritative source to check]` and keep the dependent conclusion provisional.
8. Turn each supported finding into an action with an owner role, a dependency, and an observable completion check. Order work by whether it blocks the decision, not by how easy it is to describe.
9. Rehearse the proposed action against the supplied counterexample or a clearly labeled hypothetical failure. Record what would change the decision rather than asserting that the plan guarantees a result.
10. Produce the concrete artifact appropriate to this task, not merely a recommendation to create it. Use the worked example's artifact as a structural illustration; replace its content with the user's evidence. Where the output is copy, write the copy; where it is a mapping, include the actual mapped entries; where it is a rule, specify the conditions and resulting behavior.
11. Fill the output template, then run every quality checklist item. Recompute any totals, proportions, or differences using the supplied units and denominator; omit calculations that the available evidence cannot support.

## Decision rules
- IF an estimate excludes necessary rework or handoff effort THEN include that effort or label the estimate incomplete BECAUSE the proposed deliverable must respect the decisive evidence rather than hide it in a caveat.
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
> Fictional company Juniper Works asks for startup service capacity planning. Its supplied record A says: The plan allocates preparation time but no review time even though every deliverable requires review. Prepare an internal review only; the review owner is the person responsible for the affected workstream.

**Output:**
```text
## Decision
The capacity estimate omits required work.

## Scope
Internal review for fictional Juniper Works using supplied record A. No live change or external message is included.

## Findings
- Evidence: A — The plan allocates preparation time but no review time even though every deliverable requires review.
  Assessment: The capacity estimate omits required work.
  Action: Add review demand before accepting the delivery schedule. Owner: affected workstream lead.

## Artifact
Service-unit worksheet: preparation effort + mandatory review effort + handoff effort + conditional rework effort.
Known gap: review effort is absent from the current estimate.
Role workload rule: aggregate each stage over the expected request mix in the same planning window, keeping unknown effort as an open input.
Readiness: do not accept service-volume commitments until review workload and role availability are supplied; portfolio initiative tradeoffs belong in BPL-003.

## Acceptance check
The plan includes all required work and makes the limiting resource visible.

## Unresolved
Resolve the dependencies explicitly identified in the artifact or findings; confirm the assigned owner and applicable implementation constraints before execution.
```

**Bad output:**
> Everything looks good. Apply standard best practices and expect better performance.

This fails because it does not address the specific evidence in A, identify a concrete response, or explain how the user could verify completion.

## Edge cases
- **Decisive condition appears late**: when an estimate excludes necessary rework or handoff effort, revise the recommendation using the first decision rule and preserve a note explaining which new evidence changed it.
- **Only partial evidence is available**: return findings for the supplied subset, name that subset in Scope, and do not generalize to excluded channels, customers, or periods.
- **No accountable owner exists**: retain the recommended action as unassigned and request a role assignment; do not invent a person's authority or promise a completion date.
- **Task turns into a legal determination**: preserve factual questions and route the legal conclusion to a qualified professional with the relevant jurisdiction and source documents.

## Test case
**Input:**
> Fictional Juniper Works supplies record A: The plan allocates preparation time but no review time even though every deliverable requires review. Produce startup service capacity planning and explain what would establish completion without assuming a performance improvement.

**Assertions:**
1. Output uses Decision, Scope, Findings, Artifact, Acceptance check, and Unresolved in that order.
2. The recommendation is consistent with this case-specific conclusion: The capacity estimate omits required work.
3. The action includes this concrete response: Add review demand before accepting the delivery schedule.
4. The acceptance check addresses this observable outcome: The plan includes all required work and makes the limiting resource visible.
5. No unsupported performance guarantee, current platform limit, or invented source is introduced.
