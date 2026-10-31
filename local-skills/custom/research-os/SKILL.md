---
name: research-os
description: Orchestrator for ResearchOS research projects. Use when the user wants to start a new research paper project, continue/resume "my research project", see project status or the dashboard, decide what to do next, switch run mode (copilot/autopilot/sprint), or record a project decision, risk or research question. Do NOT use for doing a phase's actual work — finding papers (lit-search), screening or extracting (screen-extract), checking citations or numbers (verifier) — route to those skills instead. Do NOT use for one-off questions about a paper that isn't part of a project.
---

# research-os

## Purpose
Own the project's shared state, run the intake interview, decide the phase plan for the paper type, route each phase to the right skill, and show checkpoints. Every other ResearchOS skill reads `research_state.json` on start and writes it on finish through the same core package, so a project can be resumed from any session.

## Runtime check (do this first, every time)
1. Run `python -c "import researchos_core, sys; print(researchos_core.__version__)"` (on Windows try `py -3` if `python` is missing).
2. If the import fails: you are on claude.ai or the package is not installed. Say exactly: "ResearchOS scripts aren't available in this runtime, so I'll keep state in this conversation and use web search instead of the APIs. Counts won't be reproducible." Then follow the same workflow by hand, writing the state JSON as a file if file tools exist.
3. Commands below are `python -m researchos_core.ros ...`. `--project <slug-or-path>` selects a project; without it the nearest `research_state.json` above the working directory is used.

## When to use
- "Start a research project on X" → Intake.
- "Continue my research project", "where are we", "status" → Resume.
- "Switch to autopilot/sprint" → Mode change.
- "What's next?" → Next step.

## Inputs
- User answers to the intake block.
- Existing `research_state.json` (resume).
- `references/phases.md` for the per-paper-type phase plan and skill routing.

## Workflow

### A. Intake (new project)
1. Ask ONE block of questions with AskUserQuestion (max 4 per call; use two calls if needed). Each has 2–4 options, a recommended first option labelled "(Recommended)", and a one-line reason. Cover: topic (free text via Other), paper type, subfield, target venue + deadline, solo/co-author, compute (default 6 GB VRAM + Colab/Kaggle), data access, human participants/ethics, run mode. See `references/intake.md` for the exact option sets.
2. Push back before creating anything if: the deadline is under 6 weeks for an SLR or empirical study (propose sprint or a workshop venue); human participants are involved with no ethics route (propose `--irb not_started` and a risk); the paper type doesn't fit the RQ (e.g. "SLR" for a question no literature can answer).
3. Create the project:
   `python -m researchos_core.ros init --slug <kebab> --title "<title>" --topic "<topic>" --paper-type <type> --subfield <subfield> --venue "<venue>" --venue-kind <kind> --deadline YYYY-MM-DD --mode <mode> [--coauthor "<name>"] [--human-subjects --irb not_started] [--tradeoff "<rigor traded>" ...]`
   Sprint mode requires at least one `--tradeoff`.
4. Add each RQ: `python -m researchos_core.ros rq add --text "<RQ>" --type <type>`.
5. Show the phase plan the init printed, with each skip/light reason, as an **Approve** checkpoint.

### B. Resume
1. `python -m researchos_core.ros list` if the project is unclear; `python -m researchos_core.ros --project <slug> status`.
2. Summarise in ≤8 lines: phase position, counts, gate states, open questions, running fan-outs, deadline.
3. If a fan-out is still `running`, check whether its agent output files exist before anything else; merge them with the owning skill's merge command.
4. Propose the next action as a **Choose** checkpoint using `ros next`.

### C. Routing
Hand each phase to its skill (table in `references/phases.md`). Before handing off: `ros phase <phase> in_progress`. After the skill reports done and its gates pass: `ros phase <phase> done --artifact <path>`.

### D. Decisions, risks, questions
- Every user choice at a checkpoint: `ros decide --phase <p> --question "<q>" --option A --option B --recommended A --chosen <x> --rationale "<why>" --type <approve|choose|review|escalate> [--irreversible]`.
- In autopilot, assumptions you make yourself: same command with `--by autopilot_assumption`.
- `ros risk add --text ... --category ... --likelihood ... --impact ... --mitigation ...`; `ros question add --text ... --blocks <phase>`.

### E. Mode switch
`ros mode <copilot|autopilot|sprint> [--tradeoff "..."] --reason "<why>"`. In sprint, list what rigor is traded away before confirming (e.g. single-stage screening, no forward snowballing, 3 reviewer personas).

## Checkpoints
Render every checkpoint exactly like this, then wait (copilot) or continue (autopilot, unless it is in the mandatory list):

```
CHECKPOINT [Approve|Choose|Review|Escalate] · <phase> · <short id>
Done:     <what was produced, with counts and files>
Decided:  <decision ids and one-line reasons>
Next:     <what happens on approval>
Risk:     <what goes wrong if this is wrong>
Options:  A (recommended — <reason>) / B / C
```
The user can answer "skip", "go deeper", "redo with X", or "switch mode" at any checkpoint.

Mandatory stops in every mode: screening protocol approval, human calibration sample, outline approval, any paid API spend, any contact with human participants, the verifier gate, final submission, anything irreversible.

## Outputs
- `<projects_dir>/<slug>/research_state.json` (schema: `researchos_core/schemas/research_state.schema.json`)
- Folder tree created by `init` (registry/, lit/, screening/, extraction/, verify/, paper/, fanout/ …)

## Quality gates
- **G-STATE**: `python -m researchos_core.ros validate` passes before you hand off to any skill and after any manual edit. If it fails, fix the reported path; never hand-edit around the schema.

## Advisor duty
At intake and at every phase boundary, name the single weakest point of the current plan (RQ too broad, venue mismatch, method can't answer the RQ, deadline unrealistic) and propose a concrete fix. Credit what's strong in one line. Don't pad.

## Failure modes
- State invalid → stop, show the error path, fix it with `ros` commands.
- Two sessions editing at once → the file lock serialises writes; if a lock wait times out, tell the user another session is mid-write.
- User asks for a phase whose prerequisites aren't done (e.g. write before screening) → say what's missing, offer sprint-mode shortcut with the rigor cost stated.

## Example
User: "Continue my research project"
1. `ros list` → `hai-collab  slr  copilot  next: screen_extract → skill screen-extract`
2. `ros --project hai-collab status` → 412 sources, title/abstract screening merged, 37 conflicts escalated, calibration not filled.
3. Checkpoint:
```
CHECKPOINT [Choose] · screen_extract · TA-resume
Done:     412 records screened by 2 agents; κ AI–AI 0.71; 37 conflicts in screening/title_abstract/conflicts.csv
Decided:  D-004 protocol v1 approved
Next:     you resolve conflicts and fill the 82-row calibration sheet, then I compute human–AI κ
Risk:     skipping calibration leaves no defensible agreement statistic for reviewers
Options:  A (recommended — unblocks the stage) resolve conflicts now / B fill calibration first / C switch to sprint and waive calibration
```
