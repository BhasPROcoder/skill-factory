---
id: EXP-004
name: exhibit-kiosk-visitor-session-reset-review
domain: Exhibition Interpretation Operations
subdomain: Kiosk interaction continuity
version: 1.0
description: Specify and inspect visible reset behavior for shared exhibit kiosks when abandoned or completed interactions could leave confusing state for the next visitor.
triggers: ["review a museum kiosk reset", "check the next visitor experience", "design an exhibit idle return", "test abandoned interactive sessions", "check kiosk restart prompts"]
not_for: ["implementing kiosk software", "security testing or proving deletion of stored information", "legal privacy compliance", "motion-alternative design [IXA-001]"]
requires: []
risk_level: medium
---

# Exhibit kiosk visitor session reset review

## Purpose
Describe what a shared exhibit interaction should display when visitors finish, walk away or resume before a reset. The result is a visible behavior specification and observation record, not a claim that hidden storage is cleared or that the kiosk meets a security or legal standard.

## Inputs to collect
1. **Visitor journey:** Obtain the start screen, choices, generated results and finish action for the actual exhibit. Required; identify what belongs to one visitor's interaction.
2. **Session state inventory:** List visible selections, entered text, results, language, audio and any open panels. Default: inventory only supplied or observed elements; hidden state remains outside the finding.
3. **Reset intent:** Obtain which states should clear, which preferences may persist and which exhibit-wide settings must remain. Required for a pass/fail judgment; otherwise propose a contract for owner review.
4. **Idle policy:** Obtain the configured inactivity duration, warning behavior and what counts as activity. Default: no invented timeout; ask the design owner to supply or approve a testable policy.
5. **Access and test environment:** Identify whether an interactive prototype, controlled exhibit station or only static screens are available. Default: desk review with unexecuted interaction tests explicitly labeled.
6. **Observation constraints:** Use fictional test entries and an authorized session. Default: no collection of real visitor content and no changes to a public kiosk configuration.

If a required input lacks a safe default, ask in one message with at most three questions.

## Procedure
1. Draw the visible journey as named states: entry, active selection, result and any interruption prompt. Use the actual product states; a kiosk without a result screen needs no invented one.
2. Assign every inventoried state element a reset disposition: clear, restore an owner-defined default, retain by explicit design or unknown. Distinguish a visitor's selected language from a venue-wide setting even if both appear in the same menu.
3. Identify the reset triggers separately: explicit finish, return-to-start, inactivity and any supported restart. Do not assume these actions share the same behavior merely because they all display a welcome screen.
4. ⚠️ Specify what the inactivity warning permits before reset. If the design provides a continue action, state how the visitor resumes the same work and which event cancels the pending reset; do not invent a universal warning duration.
5. Describe the expected next-visitor entry view after each trigger. Include lingering sound, selected tabs, reopened overlays and visible typed content, not only the main screen title.
6. Prepare fictional marker entries that make carryover observable. Choose a distinctive harmless phrase or selection so a reviewer can distinguish retained state from default exhibit content without recording personal information.
7. Execute each permitted path in the available test environment, or record it as an unexecuted scenario. Observe the entry view and the next ordinary interaction; stale selections may be visible only after entering a later screen.
8. ⚠️ Test a continued session separately from a completed reset. A visitor who selects continue should not lose their active work merely because the warning was shown; compare against the approved contract rather than assuming either retention or clearing.
9. Record mismatches with the trigger, prior state, expected visible result and observed result. Keep unknown hidden persistence outside the pass verdict; return to a clean screen is not proof of data erasure.
10. Deliver a behavior table and repeatable observation sequence. Assign unresolved timing or retention decisions to the exhibit owner and describe what evidence would allow a narrower visible-behavior finding.

## Decision rules
- IF the welcome screen appears but prior selections return on reentry THEN record incomplete visible reset BECAUSE the next visitor still inherits the prior interaction.
- IF no inactivity policy is supplied THEN propose scenarios without declaring a timing failure BECAUSE an unapproved duration is not a test criterion.
- IF the visitor chooses continue before the approved reset point THEN expect the specified active state to remain BECAUSE continuation and new-session entry are different paths.
- IF only screenshots are available THEN leave transition behavior untested BECAUSE static endpoints do not demonstrate a reset.
- IF a test reveals real visitor content THEN stop recording that content and notify the designated exhibit owner BECAUSE the observation task needs state evidence rather than personal details.

## Output template
```text
Review boundary: <station, artifact and permitted observation scope; up to three lines>
State disposition: <up to eight rows; attach larger inventories>
Element | Clear/default/retain/unknown | Owner criterion | Evidence
Transition review: <one row per supplied trigger and continuation path>
Trigger | Prior state | Expected visible result | Observed result or untested | Finding
Open decisions: <up to four policy or implementation questions>
Retest sequence: <up to six actions using fictional markers>
Conclusion: <visible behavior established and hidden behavior outside scope; up to three lines>
```

## Quality checklist
- [ ] The inventory covers supplied visible selections, entries, results and overlays.
- [ ] Each retention or clearing decision has an owner criterion or remains pending.
- [ ] Explicit finish and inactivity are separate paths.
- [ ] Warning continuation is distinguished from reset completion.
- [ ] Tests use fictional markers rather than visitor information.
- [ ] The next interaction is inspected for delayed visible carryover.
- [ ] Static review is not reported as executed interaction testing.
- [ ] The conclusion does not assert hidden deletion or compliance.

## Anti-patterns
- **Welcome-screen proof:** a home screen is treated as complete reset. Fix: reenter the interaction and check the specified state elements.
- **Invented timeout:** an arbitrary duration is declared mandatory. Fix: obtain the exhibit's approved idle policy.
- **Reset by surprise:** a warning destroys work even when continue is selected. Fix: specify and test the continuation branch.
- **Invisible-storage claim:** clean visible screens are called proof of erasure. Fix: limit the finding to observed display behavior.
- **Live visitor capture:** real entered content is used in test evidence. Fix: use fictional markers in a permitted session.

## Worked example
**Input:** Fictional exhibit Pebble lets a visitor select an animal and type a caption. The owner says Finish must clear both; language may remain. A controlled prototype review selects “fox” and enters “Copper kite.” Finish returns to welcome. Reentry shows fox selected and an empty caption. No idle policy is supplied.

**Output:**
```text
Review boundary: Pebble controlled prototype; supplied observation of Finish and reentry only.
State disposition:
Element | Clear/default/retain/unknown | Owner criterion | Evidence
animal | clear | owner Finish rule | fox persists on reentry
caption | clear | owner Finish rule | caption empty on reentry
language | retain | owner permits retention | not observed in this run
Transition review:
Trigger | Prior state | Expected visible result | Observed result or untested | Finding
Finish | fox, Copper kite | fresh selection and blank caption | fox persists; caption blank | animal reset mismatch
inactivity | active interaction | policy pending | untested | no timing verdict
Open decisions: Obtain inactivity duration, activity definition and warning continuation policy.
Retest sequence: Enter fictional markers; select Finish; reenter; inspect animal, caption and language; compare each with the owner contract.
Conclusion: Supplied observation supports an incomplete visible animal reset. No hidden-storage deletion or live exhibit behavior was tested.
```

**Bad output:** “It returns home, so all visitor data is erased and the kiosk is compliant.”
The statement ignores the observed selection carryover and makes unsupported hidden-state and compliance claims.

## Edge cases
- Audio continues after the screen resets: record the visible-and-audible session mismatch against the owner's intended audio behavior.
- A group intentionally shares one session: define the group completion boundary before treating successive interactions as separate visitors.
- The station offers no text input: use a distinctive harmless selection pattern rather than adding a fictional input field to the specification.
- A restart restores an unfinished screen: record that observed path separately from Finish; do not infer that a restart is intended to end a session.

## Test case
**Input:**
> Fictional kiosk Willow shows an idle warning. Selecting Continue keeps the choices, as required. Selecting Finish clears the main view, but opening the results tab reveals the previous fictional caption. Only those paths were observed.

**Assertions:**
1. Treats the observed Continue behavior as consistent with the supplied requirement.
2. Flags the previous caption on the results tab as visible carryover after Finish.
3. Leaves unobserved reset paths untested.
4. Makes no claim about hidden storage or legal compliance.
