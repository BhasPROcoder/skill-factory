# Skill relationship graph and chunks

Built per `prompts/07-skill-graph-engineering.md`, originally against the 544 validated skills
in `skills/` at the time this pass started. Mid-pass, a peer session merged 37 commits from
`origin/main` into this branch (new graph-theory, event/rental-ops, and other skills from another
contributor), taking the registry to 639 validated skills across 81 domains. The node export was
regenerated against the full 639 and one clearly-sequential new domain (GRF, see chunk 28) was
added to this pass; the other 23 new domains (72 skills — see **Newly merged, not yet covered**
below) were not, to keep this pass's scope bounded rather than silently expanding it.

Graph data: [`registry/skill-graph-nodes.jsonl`](../registry/skill-graph-nodes.jsonl) (639 nodes,
current registry) and [`registry/skill-graph-edges.jsonl`](../registry/skill-graph-edges.jsonl)
(222 edges: 194 `feeds_into`, 16 `complements`, 6 `alternative_to`, 4 `generalizes`,
2 `specializes`).

## Method, stated honestly

No skill declared a `requires` dependency (0 found), and `sf.py overlap` found exactly one
cross-domain lexical candidate (BMD-005 <> TML-008), which turned out unrelated on inspection
(business-model experimenting vs. ML ablation experimenting share words, not a task) and was
discarded. Every edge below therefore comes from reading the 544 one-line descriptions (exported
via the new `sf.py graph-export` command, grouped by macro/domain/subdomain) and judging real
task relationships — not from pre-existing structure.

This produced 26 named chunks covering 234 of the 544 skills (43%). The remaining 310 are listed
in **Unchunked**, grouped by domain rather than one line each: most of them are parallel,
independently-selectable tasks within one domain's existing subdomain structure (already visible
in `registry/domains.jsonl`) rather than skills with no relationship to anything — a handful of
their domain-mates anchor one of the 26 chunks below as the cross-domain bridge point, and the
rest of that domain is noted as "see chunk X" rather than repeated. Two domains (GCO, GPP) had no
bridge identified at all in this pass.

Several large chunks (ML lifecycle spine, the go-to-market pipeline) span 6-9 domains; listing
every member skill of every spanned domain would blow past the 3-10 target, so those chunks list
only the bridge skills that carry the cross-domain relationship, with the domain's remaining
skills noted as siblings rather than enumerated again.

---

## 1. Hackathon delivery pipeline
**Skills (in order):** THK-001 hackathon-problem-selection -> THK-002 hackathon-minimum-demo-scope -> THK-003 hackathon-team-interface-contract -> THK-004 hackathon-risk-first-build-order -> THK-005 hackathon-demo-script -> THK-006 hackathon-fallback-demo-plan -> THK-007 hackathon-judging-evidence-map -> THK-008 hackathon-submission-package-check -> THK-009 hackathon-last-hour-triage -> THK-010 hackathon-post-event-handoff
**Why they're linked:** One domain (THK), whose own subdomain order (Scoping -> Team execution -> Demonstration -> Submission) is already the real end-to-end delivery sequence from problem pick to post-event handoff.

## 2. Kaggle competition pipeline
**Skills (in order):** TKG-001 kaggle-competition-rules-brief -> TKG-002 kaggle-evaluation-metric-translation -> TKG-003 kaggle-submission-schema-check -> TKG-004 kaggle-experiment-ledger -> TKG-005 kaggle-leaderboard-feedback-review -> TKG-006 kaggle-out-of-fold-prediction-assembly -> TKG-007 kaggle-ensemble-eligibility-review -> TKG-008 kaggle-notebook-rerun-readiness -> TKG-009 kaggle-final-submission-selection -> TKG-010 kaggle-post-competition-solution-handoff
**Why they're linked:** Declared subdomain order (Competition setup -> Submissions -> Experiments -> Finalization) is the actual competition lifecycle.
**Internal choices:** TKG-002 and TKG-007 specialize general ML-eval tasks (see chunk 17) for a leaderboard context — use TKG when you're in a Kaggle-style competition, the general TDS/TML skills otherwise.

## 3. Exam preparation pipeline
**Skills (in order):** GEX-001 exam-syllabus-coverage-map -> GEX-002 exam-study-capacity-plan -> GEX-003 exam-practice-error-log -> GEX-004 exam-mock-review -> GEX-005 exam-retrieval-practice-design -> GEX-006 exam-interleaved-practice-selection -> GEX-007 exam-answer-structure-practice -> GEX-008 exam-time-allocation-rehearsal -> GEX-009 exam-final-review-triage -> GEX-010 exam-day-logistics-checklist
**Why they're linked:** Syllabus mapping through exam-day logistics; a real study plan's spine.
**Internal choices:** GEX-003/005/006 (error log, retrieval practice, interleaving) are a repeating loop during the study period, not one-shot steps — run them cyclically between GEX-002 and GEX-008, not strictly once each.

## 4. Career transition pipeline
**Skills (in order):** GCA-001 career-role-requirement-map -> GCA-006 career-skill-gap-priority-plan -> GCA-002 resume-bullet-evidence-rewrite -> GCA-003 career-cover-letter-evidence-draft -> GCA-004 interview-story-evidence-bank -> GCA-005 interview-question-practice-plan -> GCA-007 career-portfolio-case-study -> GCA-008 career-informational-interview-agenda -> GCA-009 career-opportunity-comparison -> GCA-010 career-transition-evidence-plan
**Why they're linked:** Research the target role, close the gap, build application materials, prep for interviews, then compare and commit to an opportunity.

## 5. Lesson design pipeline
**Skills (in order):** GED-001 learning-objective-rewrite -> GED-002 prerequisite-knowledge-check -> GED-003 worked-example-lesson-sequence -> GED-004 misconception-contrast-activity -> GED-007 lesson-question-sequence -> GED-006 scaffold-fading-plan -> GED-005 lesson-practice-alignment-review -> GED-008 accessible-learning-material-review -> GED-009 project-learning-milestone-design -> GED-010 learning-reflection-prompt-design
**Why they're linked:** Objective through reflection prompt; a complete lesson-build sequence.
**Internal choices:** GED-005 (practice alignment) feeds chunk 6's GAS-002 (assessment task validity) — lesson design and assessment design should be checked against each other, not built in isolation.

## 6. Learning assessment pipeline
**Skills (in order):** GAS-001 analytic-rubric-design -> GAS-002 assessment-task-validity-review -> GAS-003 multiple-choice-item-review -> GAS-004 short-answer-scoring-guide -> GAS-005 formative-exit-ticket-design -> GAS-006 learner-error-pattern-analysis -> GAS-007 feedback-comment-rewrite -> GAS-008 assessment-moderation-session -> GAS-009 portfolio-evidence-selection -> GAS-010 assessment-results-communication
**Why they're linked:** Design the assessment, administer it, analyze results, moderate, and communicate — a full assessment cycle. See chunk 5 for the lesson-design cross-link.

## 7. Personal weekly productivity system
**Skills (in order):** GPR-001 personal-task-inbox-triage -> GPR-003 project-next-action-decomposition -> GPR-004 personal-priority-tradeoff -> GPR-002 weekly-capacity-planning -> GPR-005 focus-session-design -> GPR-006 personal-waiting-for-tracker -> GPR-010 overdue-commitment-recovery-plan -> GPR-007 personal-weekly-review -> GPR-008 routine-experiment-plan -> GPR-009 personal-information-retrieval-design
**Why they're linked:** A GTD-style weekly loop: triage inbox, decompose into actions, prioritize against capacity, protect focus time, track what's delegated/overdue, review, and iterate.

## 8. Poem revision pipeline
**Skills (in order):** GPO-001 poem-image-bank-development -> GPO-002 poem-line-break-experiment -> GPO-005 poem-stanza-turn-design -> GPO-006 poem-speaker-address-control -> GPO-003 poem-sound-pattern-revision -> GPO-007 poem-repetition-variation-plan -> GPO-004 poem-metaphor-coherence-review -> GPO-008 poem-concrete-language-compression -> GPO-009 poem-ending-alternatives -> GPO-010 poem-reading-performance-markup
**Why they're linked:** Generate raw material, fix structure, then line-level and sound revision, then finalize for the page or a reading.

## 9. Audio/music production pipeline
**Skills (in order):** TAM-001 audio-recording-session-plan -> TAM-002 audio-reference-listening-brief -> TAM-003 audio-vocal-comp-selection-plan -> TAM-004 audio-dialogue-edit-plan -> TAM-005 audio-noise-reduction-test-plan -> TAM-006 music-arrangement-density-map -> TAM-007 music-transition-arrangement-plan -> TAM-008 audio-mix-feedback-translation -> TAM-009 audio-stem-handoff-checklist -> TAM-010 audio-delivery-requirement-review
**Why they're linked:** Plan the session, edit/clean the takes, arrange, translate mix feedback, and prepare delivery.

## 10. Startup service operations pipeline
**Skills (in order):** MOP-001 startup-service-intake-form -> MOP-002 startup-support-triage-rules -> MOP-003 startup-service-delivery-checklist -> MOP-004 startup-vendor-comparison-brief -> MOP-005 startup-vendor-onboarding-checklist -> MOP-006 startup-customer-handoff-map -> MOP-007 startup-process-exception-log -> MOP-008 startup-service-capacity-plan -> MOP-009 startup-operating-procedure-draft -> MOP-010 startup-workflow-retrospective
**Why they're linked:** Design intake and delivery, bring on vendors, map handoffs, track exceptions and capacity, document the procedure, then retrospect.

## 11. Startup customer validation pipeline
**Skills (in order):** MSV-001 startup-problem-hypothesis-card -> MSV-002 startup-assumption-risk-order -> MSV-003 startup-customer-commitment-ladder -> MSV-004 startup-concierge-test-plan -> MSV-005 startup-landing-page-test-brief -> MSV-006 startup-pilot-scope-design -> MSV-007 startup-validation-result-review -> MSV-008 startup-founder-sales-learning-log -> MSV-009 startup-early-adopter-screen -> MSV-010 startup-pivot-evidence-brief
**Why they're linked:** Declared subdomain order is the real validation loop: hypothesis, risk ordering, tests of increasing commitment, review, and pivot-or-persevere. Feeds chunk 21.

## 12. Administrative casework pipeline
**Skills (in order):** GAD-003 bureaucratic-office-routing-map -> GAD-001 administrative-form-field-evidence-map -> GAD-002 administrative-attachment-index -> GAD-009 administrative-cover-note-draft -> GAD-006 administrative-case-timeline -> GAD-007 administrative-status-tracker-design -> GAD-004 official-notice-action-extraction -> GAD-005 application-rejection-error-triage -> GAD-008 official-instruction-conflict-log -> GAD-010 administrative-handoff-packet
**Why they're linked:** Route the case, prepare and submit the package, track it, then handle whatever notices/rejections/conflicts come back, ending in a handoff.
**Internal choices:** Country-specific specializations of this general pattern: see chunk 24 for GIS (India) and GUS (US) jurisdiction pairs that specialize GAD-003's routing logic.

## 13. Deployment & incident readiness toolkit
**Skills (loosely ordered):** TDV-009 deployment-environment-parity-review -> TDV-003 deployment-configuration-diff-review -> TDV-002 deployment-canary-evidence-plan -> TDV-001 deployment-rollback-readiness -> TDV-006 operations-capacity-test-plan -> TDV-005 operations-alert-actionability-review -> TDV-007 operations-incident-timeline-build -> TDV-008 operations-runbook-gap-review -> TDV-010 operations-postincident-action-review -> TDV-004 operations-backup-restore-rehearsal
**Why they're linked:** One domain; re-ordered along a release-to-incident arc for readability, but most pairs are independently-selectable checklists a team runs as needed, not a strict pipeline — **confidence: low** on the ordering, not on domain membership.

## 14. Defensive security review toolkit
**Skills (loosely ordered):** TSC-006 security-trust-boundary-map -> TSC-001 security-review-scope-charter -> TSC-002 security-permission-review-matrix -> TSC-007 security-access-recertification-plan -> TSC-003 security-secret-exposure-triage -> TSC-004 security-dependency-advisory-triage -> TSC-005 security-logging-sensitive-data-review -> TSC-009 security-backup-access-separation-review -> TSC-008 security-incident-evidence-preservation-plan -> TSC-010 security-finding-evidence-writeup
**Why they're linked:** One domain; re-ordered scope -> access -> exposure -> incident-prep -> writeup for readability. **Confidence: low** on ordering — these are largely independent review checklists.

## 15. E-commerce customer-journey audit toolkit
**Skills (loosely ordered):** MEC-001 ecommerce-product-page-information-audit -> MEC-002 ecommerce-variant-selection-review -> MEC-003 ecommerce-size-guide-brief -> MEC-006 ecommerce-product-comparison-table -> MEC-004 ecommerce-cart-transparency-review -> MEC-005 ecommerce-checkout-friction-review -> MEC-009 ecommerce-out-of-stock-experience -> MEC-008 ecommerce-postpurchase-message-plan -> MEC-007 ecommerce-return-policy-content-review -> MEC-010 ecommerce-catalog-attribute-cleanup
**Why they're linked:** One domain; re-ordered along the actual shopper journey (browse -> cart -> checkout -> post-purchase) for readability. **Confidence: low** on ordering — each is an independently-selectable audit.

## 16. Translation QA pipeline
**Skills (in order):** GLA-001 translation-brief-preparation -> GLA-002 translation-ambiguity-query-log -> GLA-003 translation-negation-modality-check -> GLA-004 translation-terminology-decision-log -> GLA-005 translation-register-alignment -> GLA-006 translation-proper-name-number-check -> GLA-007 translation-idiom-function-adaptation -> GLA-008 translation-review-disagreement-resolution
**Why they're linked:** Brief through reviewer-disagreement resolution; the real sequence of a translation QA pass.
**Internal choices:** GLA-009/010 (language-learner error feedback, practice-dialogue scaffolding) are a different task inside the same domain — language *teaching*, not translation QA. They complement chunk 5's GED-004/GED-003 instead (a language-learning case of general lesson design), not this pipeline.

## 17. ML project lifecycle spine
**Skills (bridge points only — each domain has 7-10 more members not listed here):** TDS-007 dataset-split-release-manifest -> TDQ-001 dataset-key-uniqueness-check -> TDQ-006 dataset-referential-integrity-review -> TFE-001 feature-availability-time-audit -> TFE-010 feature-training-serving-parity-plan -> TDE-006 pipeline-data-contract-draft -> TDE-010 pipeline-observability-signal-map -> TML-001 model-validation-split-selection
**Why they're linked:** This is the real shape of an ML project across six domains: dataset intake and release (TDS) -> quality checks (TDQ) -> feature/label pipelines (TFE) -> production data pipeline design (TDE) -> model evaluation (TML), with analytics (TAN) and reproducibility (TRP) cutting across every stage rather than sitting at one point in the chain.
**Internal choices (branches, not core members):** TKG-002/TKG-007 (chunk 2) **specialize** TDS/TML steps for a Kaggle competition context — use the TKG versions in a competition, the general ones otherwise. TRP-001/TRP-009 (reproducibility: run manifest, experiment diff) **complement** TML-010 and TAN-005 respectively, supplying the evidence those steps consume. TAN (analytics/metrics, 10 skills) and the remaining TDS/TDQ/TFE/TDE/TML skills are each independently selectable within their own domain — pick the ones your specific dataset/pipeline/model stage needs.

## 18. Skill-design meta loop
**Skills (in order):** SKR-001 repertoire-gap-selection -> SKR-002 specialized-workflow-generalization -> SKR-003 skill-forward-test-design -> CTG-006 evidence-led-skill-revision
**Why they're linked:** This is literally the loop this graph-engineering task and the skill factory itself run on: find a gap, generalize a workflow into a skill, design its forward test, then revise it from real evidence — which surfaces the next gap, re-entering SKR-001.

## 19. Fiction: structure feeds scene craft
**Skills (bridge points):** MSS-010 fiction-outline-pacing-review -> MSC-001 fiction-scene-goal-pressure; MSS-003 fiction-character-arc-map -> MSC-009 fiction-emotional-beat-grounding; MSS-005 fiction-reveal-setup-payoff -> MSC-008 fiction-scene-ending-turn; MSS-006 fiction-stakes-escalation-map -> MSC-004 fiction-action-blocking-repair
**Why they're linked:** MSS (story structure, 10 skills) and MSC (scene craft, 10 skills) are the big-picture and execution halves of the same novel-writing work — a structural decision in MSS should show up concretely in a specific scene in MSC. Both domains' remaining skills are independently selectable scene/structure tasks.

## 20. Reasoning feeds research synthesis
**Skills (bridge points):** GRE-001 argument-premise-map <-> GRV-008 claim-source-traceability-audit; GRE-003 alternative-explanation-test <-> GRQ-003 study-design-question-fit; GRE-009 evidence-update-ledger -> GRV-009 narrative-evidence-synthesis; GRE-005 counterexample-generalization-check <-> GRV-006 conflicting-study-findings-map
**Why they're linked:** General reasoning moves (GRE) are the same underlying discipline as research-methods tasks (GRQ study design, GRV evidence synthesis) applied to a literature or a formal study instead of a single argument.

## 21. Startup validation feeds strategy & fundraising
**Skills (bridge points):** MSV-007 startup-validation-result-review -> BST-005 strategy-assumption-test-plan; MSV-010 startup-pivot-evidence-brief -> BMD-004 business-model-assumption-map; MSV-008 startup-founder-sales-learning-log -> COP-007 fundraising-evidence-narrative; BST-003 competitor-evidence-comparison -> COP-007 fundraising-evidence-narrative
**Why they're linked:** Evidence produced validating customers (chunk 11, MSV) is exactly the input strategy assumption-testing (BST) and business-model updates (BMD) need, and both strategy and validation evidence feed a fundraising narrative (COP-007).

## 22. Commercial legal lifecycle
**Skills:** CTR-002 service-agreement-obligation-map -> DSP-001 dispute-evidence-chronology; CTR-003 contract-negotiation-issue-list <-> CMP-001 compliance-obligation-control-map; CMP-004 in-privacy-request-handling-plan <-> CMP-005 us-privacy-request-handling-plan; CTR-004 in-service-contract-review-brief <-> CTR-005 us-service-contract-review-brief; DSP-004 in-dispute-counsel-handoff <-> DSP-005 us-dispute-counsel-handoff
**Why they're linked:** A signed contract's obligation map (CTR) is the baseline a dispute (DSP) checks against, and ongoing compliance obligations (CMP) are negotiated from the same commitments. Three jurisdiction pairs sit inside this lifecycle.
**Internal choices:** CMP-004/CMP-005, CTR-004/CTR-005, and DSP-004/DSP-005 are each **alternative_to** pairs — pick India or US by governing law/jurisdiction, not both, for the same underlying task.

## 23. API contract feeds test design
**Skills:** TAP-010 api-contract-test-fixture-design -> TST-001 test-boundary-value-design; TAP-002 api-error-response-contract <-> TST-010 test-failure-injection-plan
**Why they're linked:** A defined API contract (TAP) is the direct input to designing tests against that contract (TST); error-response contracts and failure-injection plans target the same failure surface from opposite sides.

## 24. Government citizen-services jurisdiction variants
**Skills:** GAD-003 bureaucratic-office-routing-map -> GIS-001 in-passport-evidence-preflight; GAD-003 -> GUS-003 us-passport-renewal-route-preflight; GIS-001 <-> GUS-003; GIS-003 in-birth-record-request-preparation <-> GUS-001 us-birth-certificate-copy-preflight; GIS-007 in-information-request-scope-draft <-> GUS-006 us-public-records-request-draft
**Why they're linked:** GAD's general office-routing pattern (chunk 12) is **generalized**; GIS (India) and GUS (US) each **specialize** it for a specific citizen service, and the matching same-task pairs across the two countries are **alternative_to** each other.
**Internal choices:** Pick GIS or GUS by jurisdiction. GPP (public policy analysis) sits in the same macro but is a distinct analytical task — see Unchunked.

## 25. Visual production craft toolkit
**Skills:** MPH-005 photo-shot-list-sequencing <-> MVA-006 visual-poster-composition-plan; MVA-006 <-> TVE-005 video-broll-coverage-plan; MPH-005 -> TVE-001 video-footage-logging-plan
**Why they're linked:** A shoot's shot list (MPH), a composed visual asset's layout (MVA), and a video edit's coverage/logging (TVE) are drawn from the same campaign brief and footage on a real visual-content project, even though each domain's other nine skills are independent craft checklists.

## 26. Go-to-market content & campaign pipeline
**Skills (bridge points — each domain has 9 more members not listed here):** MRE-010 research-to-opportunity-handoff -> MSE-003 search-content-brief-design; MRE-010 -> MBR-005 commercial-editorial-calendar; MBR-005 -> MCA-001 campaign-objective-brief; MCA-001 -> MEM-001 email-welcome-sequence-plan; MCA-001 -> MSA-001 sales-discovery-question-plan; MEM-001 -> MME-001 marketing-metric-definition-sheet; MME-010 marketing-report-action-summary -> MRE-010 (closes the loop); MSE-001 search-intent-evidence-map <-> MAR-001 search-navigation-task-map
**Why they're linked:** This is the real shape of a GTM motion across eight domains: customer research (MRE) feeds both SEO/content (MSE) and editorial planning (MBR), which feed campaign planning (MCA), which feeds lifecycle email (MEM) and sales enablement (MSA); measurement (MME) closes the loop back to research.
**Internal choices (branches, not core members):** MAR-001 **generalizes** to MSL-001 (local-business navigation/profile) and MSE-003 **generalizes** to MSL-004 (local-business content brief) — use the MSL (Local Search Operations) versions for a local/multi-location business. Each domain's other skills are independently selectable within their own stage.

## 27. Product UX audit & handoff pipeline
**Skills (in order):** MPU-001 product-task-flow-review -> MPU-004 product-form-question-audit -> MPU-002 product-empty-state-copy -> MPU-003 product-error-message-review -> MPU-005 product-onboarding-friction-review -> MPU-006 product-prototype-test-scenario -> MPU-007 product-feedback-deduplication -> MPU-008 product-feature-request-reframing -> MPU-009 product-release-note-drafting -> MPU-010 product-design-handoff-checklist
**Why they're linked:** Audit the flow and its micro-copy, check onboarding, test the prototype, triage feedback into reframed requests, then ship release notes and a design handoff.

## 28. Graph engineering build pipeline
**Skills (in order):** GRF-001 graph-model-contract-design -> GRF-003 graph-edge-list-import-reconciliation -> GRF-002 graph-entity-merge-impact-review -> GRF-004 rooted-forest-contract-validation -> GRF-005 graph-two-clock-snapshot-reconstruction -> GRF-006 bounded-graph-traversal-contract -> GRF-007 weak-component-scope-diagnosis -> GRF-008 strong-component-condensation-analysis -> GRF-009 weighted-route-cost-verification -> GRF-010 flow-feasibility-cut-certificate -> GRF-011 bipartite-matching-certificate -> GRF-012 restart-walk-rank-sensitivity -> GRF-013 graph-community-partition-sensitivity -> GRF-014 relational-graph-storage-implementation -> GRF-015 graph-query-plan-equivalence -> GRF-016 versioned-graph-patch-replay -> GRF-017 reversible-graph-identity-migration
**Why they're linked:** One domain (GRF, 17 skills — larger than this doc's usual 3-10 target, kept whole because every step genuinely depends on the last): design the representation contract, import and clean the data (merge-impact review reordered after import, since duplicates surface once data is in), validate structural invariants, then the actual graph-analysis techniques (traversal, components, routes, flow, matching, ranking, community), then productionize (storage, query tuning, incremental updates, migration).
**Note:** this is, structurally, the same build this whole task just ran by hand on the skill library itself — GRF-001/003 is this task's own steps 1-2, GRF-007/008-style component analysis is this task's own chunking step, and GRF-014 is this task's own `registry/skill-graph-*.jsonl` output.

---

## Newly merged, not yet covered by this pass

A peer session merged 23 more new domains (72 skills) from `origin/main` after this pass's reading
was already done: ARC, ATR, BID, CLI, DST, EVT, EXP, GEO, IPR, IXA, LIR, LRE, PRT, RNT, SDR, SEQ,
SHP, SPD, SVC, TBX, UST, VEV, WHS (see `registry/domains.jsonl` for full names). A couple have an
obvious likely bridge worth flagging for a follow-up pass rather than guessing now: TBX (table
reshape/wrangling, AI/ML & Data Science) plausibly complements chunk 17's TDQ domain; CLI
(command-line interaction contracts, Software Engineering) plausibly complements chunk 23's
TAP/TST domains. Re-run `prompts/07-skill-graph-engineering.md` scoped to these 23 domains to
extend the graph properly rather than retrofitting guesses here.

---

## Unchunked

Mostly domain-mates of a chunk's bridge skill, independently selectable within that domain
(see the named chunk for the cross-domain relationship); a one-line reason per *domain*, not per
skill, given the scale (one-domain groupings follow `registry/domains.jsonl`, not a new judgment).

- **BMD** (4: 001,002,003,005) — business-model design toolkit; BMD-004 bridges to chunk 21, the rest are independent canvas-building steps.
- **BPL** (5, all) — business planning toolkit; no cross-domain bridge identified in this pass.
- **BST** (3: 001,002,004) — strategy toolkit; BST-003/005 bridge to chunks 17/21/22, the rest are independent.
- **CBG** (15, all) — a flat general-workflow domain (document/workbook/presentation/PDF handling, negotiation, market sizing, etc.); CBG-014 has one noted loose tie to GCO-003 but not a full chunk; the rest are independently selectable, unrelated to each other beyond sharing this catch-all domain.
- **CMP** (2: 002,003) — compliance toolkit; CMP-001/004/005 bridge to chunk 22, the rest are independent.
- **COP** (14, all) — venture-ops toolkit; COP-007 bridges to chunk 21, the rest are independent one-off preparation tasks (diligence, cap table, tax, IP, etc.).
- **CTG** (10: all but 006) — applied AI workflow engineering toolkit; CTG-006 bridges to chunk 18, the rest (orchestration design, cost accounting, context handoff, model-adaptation diagnosis, eval harness, local-inference envelope, requirement elicitation, responsive-component composition) are independent.
- **CTR** (1: 001) — NDA clause review; standalone, no sequence dependency on the rest of the domain's chunk-22 members.
- **DSP** (2: 002,003) — dispute toolkit; DSP-001/004/005 bridge to chunk 22, the rest are independent.
- **GCO** (10, all) — workplace message-type toolkit; **no bridge identified in this pass** — each message type is picked independently for its situation.
- **GIS** (7) / **GUS** (7) — country citizen-service toolkits; 3 skills each bridge to chunk 24, the rest are independent per-service tasks (identity correction, driving licence, grievance, appointments, benefits, etc.) with no cross-domain link found.
- **GLA** (2: 009,010) — see chunk 16's note; these two are a language-*teaching* pair, not part of the translation-QA pipeline.
- **GPP** (10, all) — public policy analysis; **no bridge identified in this pass** — a distinct analytical task from GAD/GIS/GUS citizen-service execution despite sharing a macro.
- **GRE** (6) / **GRQ** (9) / **GRV** (7) — reasoning/research toolkits; 4 bridge pairs form chunk 20, the rest are independent reasoning or research-methods tasks.
- **MAR/MBR/MCA/MEM/MME/MRE/MSA/MSE** (9 each) — the eight GTM domains; one or two bridge skills per domain form chunk 26, the rest are independently selectable within their own marketing stage.
- **MPH/MVA/TVE** (9/9/8) — visual-production domains; one bridge skill each forms chunk 25, the rest are independent craft checklists.
- **MSC** (6) / **MSS** (6) — fiction-writing domains; 4 bridge pairs form chunk 19, the rest are independent scene/structure tasks.
- **MSL** (10, all) — local search operations; MSL-001/004 are noted as specializations inside chunk 26's branch note but not listed as core members; the rest are independent local-business tasks.
- **TAN** (10, all) — analytics/metrics toolkit; TAN-005/010 are noted as branches inside chunk 17 but not core members; the rest are independent metric/diagnostic tasks.
- **TAP** (8: all but 002,010) — API contract toolkit; two skills bridge to chunk 23, the rest are independent contract-design tasks.
- **TDE/TDQ/TDS/TFE/TML** (8-9 each) — the five core ML-pipeline domains; one or two bridge skills per domain form chunk 17's spine, the rest are independent stage-specific tasks.
- **TRP** (10, all) — reproducibility toolkit; TRP-001/009 are noted as branches inside chunk 17 but not core members; the rest are independent reproducibility checklist items.
- **TST** (8: all but 001,010) — test-design toolkit; two skills bridge to chunk 23, the rest are independent test-design techniques.

**310 skills unchunked, 251 chunked (234 from the original 544 + 17 GRF), 72 newly merged and
not yet assessed, 639 total.**
