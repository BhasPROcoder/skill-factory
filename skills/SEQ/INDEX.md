# Dependency Schedule Computation (SEQ)

Diagnose prerequisite graph cycles, select ready work and compute dependency-only duration baselines with explicit models.

Macro-area: Operations & Supply Chain

Pick the skill whose triggers best match the request. If none match, use the closest description; if still none, answer without a skill.

| ID | Skill | Use when | Example triggers | Status |
|---|---|---|---|---|
| SEQ-003 | [dependency-critical-path-slack](dependency-critical-path-slack/SKILL.md) | Compute earliest and latest task times and total slack from supplied durations when a dependency-only completion baseline is needed. | calculate dependency critical paths; compute task total slack; show earliest and latest task times | validated |
| SEQ-001 | [prerequisite-cycle-witness](prerequisite-cycle-witness/SKILL.md) | Produce an explicit closed dependency path when a prerequisite graph cannot support a completion order. | find the exact dependency cycle; show why these tasks cannot be ordered; validate a prerequisite graph | validated |
| SEQ-002 | [ready-task-priority-frontier](ready-task-priority-frontier/SKILL.md) | Compute a deterministic next-task shortlist from completion evidence and explicit priority when blocked or already-running work must not consume available dispatch slots. | choose ready tasks by priority; build a deterministic dispatch shortlist; exclude blocked tasks from selection | validated |
