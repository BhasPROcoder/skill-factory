---
id: MEM-007
name: email-send-readiness-check
domain: Lifecycle Email Planning
subdomain: Design
version: 1.0
description: Email send readiness review using supplied evidence and explicit acceptance checks; use when preparing a email send readiness review deliverable.
triggers: ["help me with email send readiness review", "prepare a email send readiness review deliverable", "review our email send readiness review evidence", "create a email send readiness review action plan", "check this email send readiness review decision"]
not_for: ["Email journey collision review [MEM-008]", "Email feedback theme review [MEM-009]", "Legal or regulated financial conclusions"]
requires: []
risk_level: medium
---

# Email send readiness review

## Purpose
Produce a usable email send readiness review deliverable from evidence supplied for a specific decision. Preserve the distinction between an observed problem, a proposed response, and a result that still needs to be measured.

## Inputs to collect
1. **Decision and audience** — identify who will use this output and what they must decide; default: an internal review draft, with no authority to publish or change live systems.
2. **Task evidence** — collect approved copy, audience rules, exclusions, links, and sender details; this establishes what can actually be assessed. Default: none; request the relevant material if absent instead of substituting industry averages.
3. **Business context** — collect recipient relationship, lifecycle state, contact permissions, sender identity, and fulfillment capability; this prevents recommendations for the wrong operating conditions. Default: preserve the context explicitly present in the evidence and label everything else unknown.
4. **Constraints** — collect deadline, responsible owner, available effort, exclusions, and approval route; these determine which recommendations are actionable. Default: no assumed budget or delivery commitment.
5. **Acceptance standard** — ask how the user will recognize an adequate result; use the task-specific acceptance check below as a proposed standard if none is supplied, not as an external benchmark.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only with independent portions for which the available evidence is sufficient.

## Procedure
1. State the requested decision and delimit the evidence set by product, audience, channel, and period wherever those distinctions matter.
2. Assign a short source label to each supplied item so another reviewer can trace the recommendation without searching an entire conversation.
3. Rehearse the message for representative eligible and excluded recipient states
4. Check destination links, personalization fallbacks, and sender identity
5. Record approval, audience, and operational blockers before any send action
6. Apply the domain checks: Separate message drafting from sending; preserve unsubscribe and suppression requirements supplied by the responsible owner; avoid assuming permission from possession of an address.
7. ⚠️ Check whether the proposed response assumes a current platform rule, eligibility condition, or externally defined limit. Check the current value in the email provider official documentation and the applicable approved consent and messaging policy; if unavailable, write `[VERIFY: exact requirement and authoritative source to check]` and keep the dependent conclusion provisional.
8. Turn each supported finding into an action with an owner role, a dependency, and an observable completion check. Order work by whether it blocks the decision, not by how easy it is to describe.
9. Rehearse the proposed action against the supplied counterexample or a clearly labeled hypothetical failure. Record what would change the decision rather than asserting that the plan guarantees a result.
10. Produce the concrete artifact appropriate to this task, not merely a recommendation to create it. Use the worked example's artifact as a structural illustration; replace its content with the user's evidence. Where the output is copy, write the copy; where it is a mapping, include the actual mapped entries; where it is a rule, specify the conditions and resulting behavior.
11. Fill the output template, then run every quality checklist item. Recompute any totals, proportions, or differences using the supplied units and denominator; omit calculations that the available evidence cannot support.

## Decision rules
- IF a personalization field has no safe fallback THEN fix the fallback before marking the message ready BECAUSE the proposed deliverable must respect the decisive evidence rather than hide it in a caveat.
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
> Fictional company Juniper Works asks for email send readiness review. Its supplied record A says: The greeting inserts a blank name when the customer record lacks a name. Prepare an internal review only; the review owner is the person responsible for the affected workstream.

**Output:**
```text
## Decision
The message needs a verified fallback greeting.

## Scope
Internal review for fictional Juniper Works using supplied record A. No live change or external message is included.

## Findings
- Evidence: A — The greeting inserts a blank name when the customer record lacks a name.
  Assessment: The message needs a verified fallback greeting.
  Action: Use a neutral fallback and test both present-name and missing-name cases. Owner: affected workstream lead.

## Artifact
Name present: Hello [VERIFIED NAME],
Name missing: Hello,
Verification cases: render both states and confirm no blank or broken personalization appears.
Send status: pending the remaining audience, link, and approval checks.

## Acceptance check
Representative messages render coherently and excluded recipients remain excluded.

## Unresolved
Confirm the assigned owner and any live implementation constraints before execution.
```

**Bad output:**
> Everything looks good. Apply standard best practices and expect better performance.

This fails because it does not address the specific evidence in A, identify a concrete response, or explain how the user could verify completion.

## Edge cases
- **Decisive condition appears late**: when a personalization field has no safe fallback, revise the recommendation using the first decision rule and preserve a note explaining which new evidence changed it.
- **Only partial evidence is available**: return findings for the supplied subset, name that subset in Scope, and do not generalize to excluded channels, customers, or periods.
- **No accountable owner exists**: retain the recommended action as unassigned and request a role assignment; do not invent a person's authority or promise a completion date.
- **Task turns into a legal determination**: preserve factual questions and route the legal conclusion to a qualified professional with the relevant jurisdiction and source documents.

## Test case
**Input:**
> Fictional Juniper Works supplies record A: The greeting inserts a blank name when the customer record lacks a name. Produce email send readiness review and explain what would establish completion without assuming a performance improvement.

**Assertions:**
1. Output uses Decision, Scope, Findings, Artifact, Acceptance check, and Unresolved in that order.
2. The recommendation is consistent with this case-specific conclusion: The message needs a verified fallback greeting.
3. The action includes this concrete response: Use a neutral fallback and test both present-name and missing-name cases.
4. The acceptance check addresses this observable outcome: Representative messages render coherently and excluded recipients remain excluded.
5. No unsupported performance guarantee, current platform limit, or invented source is introduced.
