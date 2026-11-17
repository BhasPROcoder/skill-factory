# Additional skill discoveries (independent of the X posts)

Per Part 4 of `prompts/08-skill-harvest-graph-and-readme.md`: an open-ended search for Claude
Skills relevant to this repo owner's actual workflow (skill-factory maintenance at scale,
multi-session/multi-agent git collaboration, skill-authoring/evaluation meta-work, competitive
product-teardown research), not already covered by the six X posts or already present in
`skills/`, `local-skills/`, or `~/.claude/skills`.

Confidence: items marked "WebFetch" had their actual repo/README/SKILL.md content read directly.
Items marked "WebSearch/listing only" were found via search or a repo's own listing page but not
independently content-verified — treat those as leads, not confirmed facts.

## Solidly verified (WebFetch)

1. **vskill** — https://github.com/anton-abyzov/vskill
   npm-based package manager for AI agent skills (Claude Code, Cursor, Copilot, Gemini CLI). `install` runs a 3-tier security scan before installing; `audit --ci` emits SARIF; `eval sweep` benchmarks a skill across models; ships a local "Skill Studio" IDE.
   *Relevance:* `sf.py`'s own `quality --all` is a mechanical gate; `vskill`'s SARIF/eval-sweep approach is worth comparing against, and it's a safer way to vet third-party skills (like this session's X-post harvest) before they land in `~/.claude/skills` — scans for prompt-injection/malicious patterns first.

2. **Skill_Seekers** — https://github.com/yusufkaraaslan/Skill_Seekers
   Python CLI (`skill-seekers create <source>`) converting docs/repos/PDFs into SKILL.md + reference-file packages, with quality scoring and cross-source conflict detection. MIT, 15.3k stars.
   *Relevance:* the closest thing to automated bulk skill-drafting for a 645-skill factory — point it at a domain's canonical source and get a first draft to then hand-edit against SPEC.md/GOLD-SKILL.md. Conflict detection matters when two agents draft overlapping domains in parallel, exactly this repo's situation.

3. **ckelsoe/claude-skill-prompt-architect** — https://github.com/ckelsoe/claude-skill-prompt-architect
   Scores a draft prompt 1-10 on clarity/specificity/context/structure, recommends from 31 prompting frameworks (CO-STAR included, with its own template file), asks clarifying questions, then applies and refines the chosen framework. MIT, 335 stars.
   *Relevance:* this repo owner explicitly writes COSTAR-format research prompts by hand — this operationalizes the same move as a reusable drafting/critique loop instead of hand-rolling the template every time.

4. **samber/cc-skills — skill-progressive-disclosure-design** — https://github.com/samber/cc-skills (`skills/skill-progressive-disclosure-design`)
   Decision framework for splitting a skill's content between SKILL.md and reference files — split patterns, anti-patterns (splitting just to hit a line count), pointer hygiene, an eval method for measuring how often each reference file actually loads.
   *Relevance:* directly addresses the factory's "match GOLD-SKILL.md's depth and structure" quality bar at scale across many authoring sessions.

5. **samber/cc-skills — conventional-git** — same repo, `skills/conventional-git`
   Branch/commit/worktree naming standard; worktrees under `.claude/worktrees/`, named after their branch; bans "worktree" in branch names and AI co-author trailers; warns against doing unrelated work in someone else's worktree.
   *Relevance:* fits this exact repo's multi-session/parallel-contributor/merge-conflict-prone pattern (see `logs/progress.md`'s own merge-conflict-resolution entries this session).

6. **alirezarezvani/claude-skills — git-worktree-manager** — https://github.com/alirezarezvani/claude-skills (`engineering/git-worktree-manager`)
   Manages multiple parallel-dev worktrees with port isolation/environment sync, automated lifecycle + cleanup scripts.
   *Relevance:* a second, independently-authored reference for juggling concurrent agent workspaces on one repo, worth comparing against. (Raw SKILL.md content wasn't fetched — a guessed path 404'd — treat feature claims as repo-page-sourced.)

7. **gmh5225/android-reverse-engineering-skill** — already added this session, see `logs/x-posts-harvest.md`.

8. **JimLiu/baoyu-skills — baoyu-electron-extract** — already added this session, see `logs/x-posts-harvest.md`.

9. **Lum1104/Understand-Anything** — https://github.com/Lum1104/Understand-Anything
   MIT Claude Code plugin running a multi-agent pipeline that turns codebases/docs/wikis into an interactive, force-directed knowledge graph with community clustering — deterministic parser extracts wikilinks/categories, then LLM agents find implicit relationships and extract entities. Browser dashboard included.
   *Relevance:* maps almost exactly onto this session's own skill-relationship-graph work (`logs/skill-graph-chunks.md`, 287 edges, 37 chunks). Worth comparing methodology against — the deterministic-parse-then-LLM-inference split could validate or simplify the existing hand-built graph pipeline over `skills/<DOMAIN-CODE>/<name>/SKILL.md`.

## Leads only — not independently content-verified

10. **gmh5225/android-reverse-engineering-skill — note on #7**: confirmed via WebFetch, listed above as solid.

11. **alirezarezvani/claude-skills — commit-craft** — expected path `engineering/commit-craft` (404'd on direct fetch). Per the repo's own listing: splits a tangled working tree into a reviewable commit series, blocks staged secrets, lints commit messages. If real, useful for cleaning up multi-agent commit history before merging — **verify before relying on it.**

12. **pionxzh/wakaru** — JavaScript decompiler/webpack-bundle unpacker with source-map recovery, falling back to deobfuscating mangled variable names. Found via a registry mirror, not independently confirmed on the origin GitHub repo. Would complement `baoyu-electron-extract` for the non-Electron case (plain webpack bundles) in the `rea-teardown` workflow — **verify the repo exists before using.**

13. **samber/cc-skills — deep-research** — same repo, `skills/deep-research`, listed under "Productivity" but not content-fetched. Worth a side-by-side comparison against the locally-authored `research-os`/`lit-search` skills to see if it covers a gap they don't.

## Method

WebSearch across targeted clusters (skill-registry/validator tooling, git-worktree/multi-agent
merge-conflict skills, APK/Electron/bundle reverse-engineering skills, knowledge-graph/markdown-
graph skills, COSTAR/prompt-framework skills), then WebFetch of the actual github.com page for
every candidate before inclusion, with the handful of 404s/unfetched items flagged above rather
than asserted as fact. No star count or feature claim is stated beyond what a fetch actually
returned; third-party SEO-aggregator sites (skills.sh, openskillindex.com, etc.) were treated as
leads only, never as confirmation without a direct github.com fetch backing them up.
