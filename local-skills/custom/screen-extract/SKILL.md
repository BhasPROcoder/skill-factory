---
name: screen-extract
description: Screening and data extraction for a ResearchOS project. Use when the user wants to set or approve inclusion/exclusion criteria, screen papers at title/abstract or full-text stage with two independent screener agents, resolve screening conflicts, compute Cohen's kappa on a human calibration sample, produce a PRISMA 2020 flow diagram, extract structured data from included papers with page/section locators, verify extractions, or deep-read a single paper (explain, critique, extract). Do NOT use for finding papers (lit-search), comparing across papers to build a taxonomy or gap map (synthesis), or checking whether a draft's citations are real or supported (verifier).
---

# screen-extract

## Purpose
Run a Kitchenham / PRISMA 2020 screening with criteria the user approved first, two isolated screener agents, a human calibration sample, and a structured extraction sheet in which every reported value carries the page or section that supports it.

## Runtime check
`python -c "import researchos_core"`. If unavailable (claude.ai), say so and run the same steps in conversation: criteria table, two independent passes you keep separate, a calibration sample the user screens, kappa computed by hand in a code block. State that the procedure is not scripted.

## Inputs
- Sources with status `candidate` (title/abstract) or `passed_title_abstract` (full text) in `registry/sources.jsonl`.
- `screening/protocol.md` with its machine-readable JSON block.
- Full texts as `lit/text/<source_id>.txt` with `=== page N ===` markers (made by `fulltext` from PDFs).

## Workflow

### 1. Protocol (gate G-PROTOCOL)
1. `python -m researchos_core.screen protocol-init --years 2015–2026`
2. Edit the JSON block in `screening/protocol.md` with the user: inclusion (IC…), exclusion (EC…), calibration sizes, kappa threshold (default 0.6), quality instrument, and `custom_fields` for project-specific extraction fields.
3. Weakest-point check before approval: criteria that need full text to judge (move them to the full-text stage), criteria that overlap (two codes for one reason), criteria not tied to an RQ.
4. Show the protocol as an **Approve** checkpoint. On approval: `python -m researchos_core.screen protocol-approve --rationale "<user's words>"`. Any later edit to the JSON block invalidates the approval; re-approve.

### 2. Title/abstract screening (fan-out F3)
1. `python -m researchos_core.screen prepare --stage title_abstract`
   Writes two shuffled item files, a human calibration CSV (20 %, min 50), and two briefs (framing A inclusion-first, framing B exclusion-first).
2. Spawn both screener agents **in one message** (parallel) with the prompt: "Read the brief at <brief path> and follow it exactly. You may not open any other file in that fanout folder." Never give a screener the other's brief, output, or any summary of it.
3. `python -m researchos_core.screen merge --stage title_abstract` → AI–AI kappa, `conflicts.csv`. If merge reports missing decisions, re-run only the screener that missed items; never accept single-rater decisions.
4. **Escalate checkpoint**: show the conflicts table (title, both decisions, both reasons). The user fills `your_decision` (include/exclude) and `exclusion_code` in `screening/title_abstract/conflicts.csv`, or tells you row by row and you write the file. Then `python -m researchos_core.screen resolve --stage title_abstract`.
5. **Calibration checkpoint (mandatory)**: the user fills `screening/title_abstract/human_calibration.csv` without looking at agent decisions. Then `python -m researchos_core.screen calibrate --stage title_abstract`.
   - κ ≥ threshold → G-KAPPA pass.
   - κ < threshold → show `agreement.json` disagreements, revise criteria with the user, re-approve, re-screen. Waiving is possible only on the user's explicit instruction: `screen waive --stage title_abstract --rationale "..."` (logged as a high risk).
6. `python -m researchos_core.screen advance --stage title_abstract` applies statuses.

### 3. Full text
1. `python -m researchos_core.lit pdfs --status passed_title_abstract`, collect missing PDFs from the user, `python -m researchos_core.lit attach`.
2. `python -m researchos_core.screen fulltext` → `lit/text/S-xxxx.txt`. Scanned PDFs fail with "little or no extractable text"; ask the user for a text-layer version or exclude as "not retrievable" (it counts in PRISMA).
3. Repeat step 2's sequence with `--stage full_text` (calibration default 20 %, min 15). Full-text exclusions need a locator.

### 4. PRISMA
`python -m researchos_core.screen prisma` → `screening/prisma.json`, `screening/prisma_flow.svg`. Check the arithmetic against the dashboard before showing it.

### 5. Extraction (fan-out F4, gate G-EXTRACT)
1. `python -m researchos_core.screen extract-prepare --batch-size 5`
2. Spawn one agent per brief in parallel. Each writes rows that must validate against `extraction_sheet.schema.json`: every `reported` value has a paraphrased `value` and a `locator`; silence is `not_reported`; ambiguity is `unclear`; the agent's own conclusions go to `agent_inferences`, never into `core`.
3. `python -m researchos_core.screen extract-merge --fanout <id>`. Invalid rows are listed per agent; re-run those agents with the validation error appended.
4. Blind check: `python -m researchos_core.screen extract-verify-prepare` (20 % sample, new agents that never see the first extraction), spawn them, then `python -m researchos_core.screen extract-compare --fanout <verification fanout id>`. **Do not run extract-merge on the verification fan-out.**
5. **Review checkpoint**: walk the user through `extraction/verification_review.json` mismatches; the user picks the right value; fix the row and re-append it.

### 6. Single-paper deep read (on demand, no project needed)
`python -m researchos_core.screen fulltext --ids S-xxxx` (or read the user's PDF directly). Produce: one-paragraph summary in your own words; contribution and method; the 3 strongest and 3 weakest points with page locators; what would change your mind; extraction row if a project is active. Separate "the paper says (p. N)" from "I infer".

## Parallel agents
- F3: 2 screeners, same items, different order and framing, strict isolation. Merge: agree → final; disagree → user.
- F4: extraction batches of 5, cooperative; blind 20 % re-extraction, strict isolation from the first pass.
- Failures: a missing or invalid line → rerun that agent once with the error; still failing → mark the item and tell the user.

## Checkpoints
Protocol (Approve, mandatory) · conflicts (Escalate) · calibration (mandatory) · PRISMA (Review) · extraction mismatches (Review).

## Outputs
`screening/protocol.md`, `screening/<stage>/{items_A,items_B}.jsonl`, `decisions.jsonl`, `conflicts.csv`, `human_calibration.csv`, `agreement.json`, `screening/prisma.json`, `screening/prisma_flow.svg`, `extraction/sheet.jsonl`, `extraction/sheet.csv`, `extraction/verification_review.json`.

## Quality gates
- G-PROTOCOL: approved hash matches the current JSON block.
- G-KAPPA-<stage>: human–AI κ ≥ threshold (or explicit logged waiver).
- G-EXTRACT: schema-valid rows, every reported field located, blind-check mismatches resolved.

## Reporting kappa honestly
Report human–AI κ as the headline. AI–AI κ is secondary and must be described as two prompts of the same model family, whose errors correlate. Good: "Two LLM screeners (Claude, differing in prompt framing and item order) agreed with κ = 0.71; against the first author's independent screening of a random 20 % sample (n = 82), κ = 0.68." Bad: "Two independent reviewers achieved κ = 0.71."

## Failure modes
- No abstract for many records → those can't be screened at TA; mark `uncertain` (passes to full text).
- Calibration CSV filled after looking at agent decisions → the statistic is contaminated; ask the user and re-sample if so.
- Protocol edited mid-stage → prepare/merge refuse; re-approve and re-screen.
