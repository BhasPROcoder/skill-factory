# Rental Asset Operations (RNT)

Reconcile rental unit allocation, checkout kits, return observations, usage readings, custody follow-up and turnaround handoffs from supplied records without imposing fees or technical acceptance.

Macro-area: Operations & Supply Chain

Pick the skill whose triggers best match the request. If none match, use the closest description; if still none, answer without a skill.

| ID | Skill | Use when | Example triggers | Status |
|---|---|---|---|---|
| RNT-001 | [rental-serial-allocation-reconciliation](rental-serial-allocation-reconciliation/SKILL.md) | Reconcile physical rental unit identities with class-level reservations when duplicate serial assignments or substitution constraints obscure fulfillment readiness. | resolve duplicate rental serial assignments; map rental units to reservations; check class versus serial allocation | validated |
| RNT-002 | [rental-checkout-accessory-completeness](rental-checkout-accessory-completeness/SKILL.md) | Reconcile required rental accessories with the actual checkout kit when base-unit presence does not establish complete fulfillment. | check this rental kit; is the hire package complete; reconcile checkout accessories | validated |
| RNT-003 | [rental-return-condition-evidence-comparison](rental-return-condition-evidence-comparison/SKILL.md) | Compare checkout and return condition evidence for the same rental asset while separating visible changes from unsupported cause or liability conclusions. | compare rental return photos; was this mark present at checkout; reconcile return condition notes | validated |
| RNT-004 | [rental-usage-meter-reading-reconciliation](rental-usage-meter-reading-reconciliation/SKILL.md) | Reconcile rental meter observations into supported usage intervals when units, resets, replacements or transcription conflicts make subtraction unreliable. | reconcile rental meter readings; check usage between checkout and return; the return counter is lower | validated |
| RNT-005 | [rental-overdue-custody-followup](rental-overdue-custody-followup/SKILL.md) | Prepare an evidence-based follow-up for an apparently overdue rental when due-date changes, pickup arrangements or unposted returns leave custody uncertain. | rental still shows overdue; check before chasing a return; reconcile an unposted rental return | validated |
| RNT-006 | [rental-turnaround-readiness-handoff](rental-turnaround-readiness-handoff/SKILL.md) | Reconcile rental turnaround task evidence into a release handoff when physical return, completed work and authorization to reallocate are separate states. | is this returned rental ready again; prepare the turnaround release handoff; reconcile open rental preparation tasks | validated |
