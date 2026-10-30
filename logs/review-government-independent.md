# Independent government and learning review

Reviewers: initial review_g_final agent; coordinating agent continued the source-example review independently of the author completing the G collection.

## Status

Source/example review and the final rendered sample are complete for this batch. This record does not claim successful behavioral execution of all skills or audited registry status. Registry integration remains the coordinator's separate step.

## Method and initial scope

Read AGENTS.md, SPEC.md, and the shared renderer in tools/build_government_learning.py. The author is completing the remaining domains while this reviewer inspects source records read-only. Complete rendered skills will be sampled after final generation. Findings are sent to the author; this reviewer does not mutate the registry or authoring files.

## Initial findings to verify after repair

- The current shared example template returns a diagnostic table even for drafting tasks. Such tasks need actual draft text or another concrete artifact, with matching output-template fields.
- The current example next action and unresolved question are generic. Task-specific actions and verification questions should replace them where the case supports them.
- GIS-007 refers to a supplied period although its fictional input does not supply one. Keep the period unresolved or add it explicitly as fictional input.
- Existing generic not_for exclusions do not provide adjacent-task routing. Replace them with meaningful known skill IDs.

## Limits

Pending: complete source review, review of repairs, and rendered sample checks. No current-law verification or live administrative submission is performed.

## Continued source-example review

The coordinator inspected the fictional input and both example rows for all 110 existing source records: GIS, GUS, GAD, GPP, GED, GAS, GEX, GRQ, GRV, GCA, and GPR. This was an evidence-consistency pass, not a full behavioral test of every procedure. Findings were sent to the author for repair before final generation.

Recurring issue: rows sometimes introduced material not supplied in the fictional input. Examples included a prepared copy pack, official appointment confirmation, an address statement, regional records, dense worksheet instructions, a second feedback comment, flashcards, observed pilot failures, a second abstract, a later checklist, and a known appointment. The repair must either explicitly supply the fictional premise or leave it conditional/unknown. A plausible inference must not be relabeled as an observation.

Additional routing concerns: distinguish repeat-wave qualitative interviewing from customer interview guide design; distinguish cognitive questionnaire pretesting from wording repair and from whole-protocol feasibility piloting; distinguish personal calendar allocation from business portfolio capacity and recurring service-stage workload. These are separate decisions only when their procedures and artifacts preserve those boundaries.

The shared renderer was inspected for source handling, output completeness, risk boundaries, and its generated example structure. Concrete artifacts, task-specific next actions, and adjacent-task exclusions are required repairs. Final rendered checks remain pending until the author completes regeneration.

## Targeted cross-domain semantic review — forward_tests agent

This is a read-only review of selected potential collisions, not a claim of exhaustive semantic uniqueness. I inspected the source procedures for GEX, GRQ, GRV, GPR (ten records per domain) and the ten saved GRE records. I used `sf.py search` for assumption/evidence, research/interview/survey, and capacity/allocation candidates; then read the actual Procedure sections for BST-005, BPL-003, MRE-001, MRE-003, MRE-004, MRE-005, MRE-007, and MRE-009. The government author was still editing, so these findings refer to the source snapshot inspected and require post-repair confirmation.

Actionable findings sent to the author and parent:

- GRQ-005 and MRE-001 both build neutral experience-based interview guides with probes. A research/customer label alone does not distinguish them. The planned repeat-wave protocol change should preserve core prompts, within-participant comparison, wave-specific probes, and missing-wave handling.
- GRQ-006 and MRE-004 both repair ambiguous/double questions and response options. The planned cognitive-pretest change should instead collect evidence on comprehension, recall, judgment, and answer mapping before revision.
- GRQ-003 and MRE-005 both classify the question and select a method by evidence needs and constraints. Suggested replacement scope: diagnose inferential threats in an already chosen observational design and derive design repairs, with an explicit allowable-claim boundary.
- GRV-005 and MRE-009 both inspect source relevance, provenance, method, and supported use. Suggested replacement scope: verify publication identity/version and correction or retraction status, recording official source checks and their consequences for the cited claim. Do not claim a status check happened without source access.
- GEX-002 and GPR-002 both allocate tasks to limited blocks and defer overload. Suggested distinction: make exam planning a prerequisite/mastery-dependent study sequence, changing allocations from diagnostic performance; retain personal planning as calendar and energy placement.
- GRE-008 and BST-005 both prioritize decision-relevant unknowns and evidence collection. Suggested boundary: GRE-008 should route factual questions to sources capable of answering them, expose answer dependencies and stopping conditions; BST-005 should retain strategic assumptions, disconfirming tests, and commitment gates.

Pairs whose task distinctions appear meaningful in the inspected procedures:

- BPL-003 handles portfolio combinations and skill-specific business bottlenecks; GPR-002 can handle a person's actual blocks, interruptions, energy, and carryover. The final examples must demonstrate those distinctions.
- GRE-003 distinguishes competing explanations using observations that discriminate between them; BST-005 selects strategic assumptions to test before commitment.
- GRE-009 updates a prior judgment using newly arriving evidence and independence of sources; MRE-007 reviews the current support and limitations behind research findings.
- GRV-009 synthesizes study-level evidence across populations, designs, and outcome definitions; MRE-003 synthesizes participant-level interview observations and negative cases.

No author file or registry was changed by this review. No automated status was promoted to audited. Repaired scopes and rendered examples still need confirmation before these findings can be closed.

## Repair and concrete-artifact review — forward_tests agent

Read-only follow-up inspected all of tools/government_review_repairs.py, the 17 core draft artifacts in tools/government_artifacts_core.py, and the 30 education/exam artifacts in tools/government_artifacts_education.py. Compared relevant original source records for drafting, research, career, and education cases. This review concerns authored source modules, not rendered-file validation.

The repaired GRQ-005 repeated-wave protocol and GRQ-006 cognitive-pretest procedure now change the actual task, with concrete prompts and missing-observation handling. GRQ-003 now diagnoses inferential threats in a selected observational design; GRV-005 now checks publication version/correction status. GEX-002 now uses prerequisite/mastery progression, and GPR-002 uses personal calendar/energy placement. These address the earlier method-level overlap concerns. GRE-008 had not received the proposed factual-source-routing narrowing at this snapshot.

Remaining findings sent to the parent for repair:

- The GEX-002 education artifact still excludes an evening lost to family duty, but the repaired fictional input no longer supplies that duty. It should instead demonstrate the repaired claim-identification diagnostic and transfer gate.
- The official-instruction-conflict-log draft offers both documents and their dates, while its source says dates are not supplied. Offer the documents and request or locate dates without inventing availability.
- GRQ-003 still uses old design-option rows despite its narrowed procedure. Replace them with threat/evidence/repair/claim-boundary rows. The source's before-and-after totals do not establish that a comparable group is unavailable; keep availability unknown.
- The research-protocol-decision-log rows say the original categories were defined before collection, but the fictional input only establishes that a category changed after unexpected responses. Mark original timing unverified or explicitly supply that fictional premise.

Other inspected artifacts provide usable draft language, teaching stimuli, prompts, checks, and decision rules rather than merely telling the user to create them. Proposed observations are generally separated from actual supplied results. This is a bounded substantive review, not legal verification, empirical effectiveness testing, or certification of every rendered skill. Findings require confirmation after the parent applies fixes; no registry status was changed.

## Final integration review — government_final_review agent

Applied the outstanding source repairs and regenerated the full government collection. GEX-002 now demonstrates claim-identification repair and a transfer gate without the old unsupported family-duty constraint. GAD-008's draft leaves source dates unresolved. GRQ-003 uses threat/evidence/repair/claim-boundary columns and does not assume a comparator is unavailable. GRQ-008 leaves the original protocol timing unverified. GRE-008 now routes factual questions to capable sources, checks answer dependencies, and stops on established facts or exhausted access; it is distinct from strategic assumption testing. Also aligned GPO-010's notation table with its capital-letter performance markup, and explicitly supplied the participant reports underlying GCO-004's draft.

Read rendered worked examples for GIS-007, GUS-006, GAD-008, GPP-008, GED-008, GAS-007, GEX-002, GRQ-003, GRV-005, GCA-002, GPR-002, GRE-008, GLA-003, GPO-002, and GCO-003. Separately read all thirty new language/poetry/workplace fictional inputs, example rows, and concrete artifacts. Reviewed the repaired renderer and source repair module. Together with the earlier scoped passes above, this covers every source record's examples and targeted procedure-level overlap concerns; it is not a fresh execution of every skill against unseen inputs.

Drafting tasks now include actual proposed letters, questions, teaching activities, poem alternatives, or messages. Diagnostic tasks retain concrete findings tables. Personal information, current rules, actual language translations into unspecified languages, and externally confirmed results are not invented. Language fixtures use supplied English glosses or explicitly identified practice English. Poem details are labeled invented proposals rather than observations.

The final `sf.py validate --file` run emitted PASS for all 150 paths and exited successfully. The staging manifest contains planned rows for coordinator-controlled ingestion. No registry status, index, or Git state was changed by this reviewer. Combined registry consistency and quality gates must run after ingestion. Current-law research, professional review, real submissions, and cross-model reliability remain outside the evidence established here.
