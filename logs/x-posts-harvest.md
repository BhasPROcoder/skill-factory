# X-post skill leads: harvest results

Source: [`staging/sources/x-posts-github-skill-leads-2026-11.md`](../staging/sources/x-posts-github-skill-leads-2026-11.md).
Resolved via three parallel research passes (posts 1+2, posts 3+6, posts 4+5), each required to
WebFetch the real repo before reporting, or explicitly flag "WebSearch-only, not independently
confirmed." Several corrections surfaced during verification — these are called out below, not
silently fixed, because a wrong owner/repo is worse than "not found."

## Corrections found during verification

| Lead's stated owner/URL | Actual | Evidence |
|---|---|---|
| `nextlevelbuild…` (UI UX Pro Max) | `nextlevelbuilder` | WebFetch |
| `github.com/ccusage/ccusage` | `github.com/ryoppippi/ccusage` | WebFetch |
| `herdrdev/herdr` | all evidence points to `ogulcancelik/herdr` — could not find `herdrdev/herdr` | WebSearch only |
| "Umair" (stalemap) | confirmed correct — `github.com/Umair/stalemap` is real | WebFetch |
| `devanshranjan1…` (landmines) | `devanshranjan10` (full handle) | WebSearch |
| `disinfeqt` (Rulebook) | **unresolved** — only a landing page (rulebook.duxi.ao / duxi.ao) found, no confirmed GitHub org | WebSearch, partial |
| Astryx owner "Meta" | confirmed `github.com/meta/astryx` (not `facebook/astryx` as the historical-branding assumption would suggest) | WebFetch x2 |
| agent-browser "checks the design itself" | the CLI itself only does browser automation; the design-check behavior is a separate skill (likely `vercel-labs/vercel-skills`'s `next-best-practices`) layered on top — the lead conflates the two | WebSearch |

## Already installed or already verified (no action needed)

Confirmed already present as the `anthropic-skills` plugin or confirmed matching an earlier
research pass this session: **Academy Guide / Frontend Design / canvas-design / pptx /
theme-factory** (all `anthropics/skills` — `frontend-design` and `pptx` confirmed already
available in this environment's skill list), **Serena, Context7, Spec Kit, Playwright MCP,
GitHub MCP Server, Claude Task Master, Aider, Graphiti, obra/superpowers, Figma Context MCP**
(all independently verified in this session's earlier GitHub-discovery report — URLs matched,
no re-research needed).

## Added to `~/.claude/skills` this pass

Per post 2's own advice ("install 2 or 3, not all 10"), five genuinely non-redundant, well-
verified skills were fetched in full (SKILL.md + any required companion scripts) and installed:

| Skill | Source | Why this one |
|---|---|---|
| `emil-design-eng` | github.com/emilkowalski/skills | Self-contained, no companion files needed. Distinct angle from `frontend-design`: animation/motion judgment specifically (easing, spring config, interruptibility), not general aesthetics. |
| `android-reverse-engineering` | github.com/gmh5225/android-reverse-engineering-skill | Self-contained. Extends the locally-authored `rea-teardown` skill into the Android/APK domain (jadx/Fernflower decompilation, Retrofit/OkHttp API extraction) — `rea-teardown` only covered Electron/npm-bundle teardown. Low-activity source repo (1 star) — a useful workflow template, not a battle-tested tool. |
| `baoyu-electron-extract` | github.com/JimLiu/baoyu-skills | Installed with its required `scripts/main.ts` (928 lines, MIT). Gives `rea-teardown`'s asar-extraction step a maintained, tested implementation (source-map restoration, Prettier fallback) instead of ad hoc commands. |
| `mattpocock-code-review` | github.com/mattpocock/skills | Renamed from `code-review` to avoid colliding with the already-installed `code-review` skill. Distinct two-axis review (Standards vs. Spec faithfulness, parallel sub-agents) directly useful for this repo's multi-session/multi-contributor PR review. |
| `hallmark` | — **not installed**, see below | |

`hallmark` (github.com/Nutlope/hallmark) was verified real and well-regarded but **not**
installed as a partial mirror: its SKILL.md calls `node <skill-dir>/scripts/theme.mjs` and
`sloplint.mjs`, and loads ~15 files under `references/` — without that whole asset tree it would
look installed but silently fail. Recommend installing it properly later via its own installer
(`npx impeccable install`-style — check the repo's own README for the exact command) rather than
a hand-copied partial.

## Full disposition table

| # | Lead | Resolved URL | Category | Disposition | Note |
|---|---|---|---|---|---|
| 1 | Reverse Engineer Anything (REA) | github.com/morluto/rea (npm `rea-agents`) | Tool (MCP+CLI) | tool-not-a-skill | Complements, doesn't replace, the locally-authored `rea-teardown` skill — this is the underlying decompilation tool; `rea-teardown` is the methodology/write-up skill. |
| 2 | Impeccable | github.com/pbakaus/impeccable (impeccable.style) | Skill | not-installed | Verified real; needs its own installer like Hallmark — not mirrored. |
| 3 | Agent Harness Construction (ECC) | github.com/affaan-m/ECC | Skill within a larger tool suite | not-installed, low confidence | Specific skill name only corroborated by a third-party index, not the README directly. |
| 4 | Hallmark | github.com/Nutlope/hallmark | Skill | not-installed | See above — needs full asset tree. |
| 5 | Code Review (Matt Pocock) | github.com/mattpocock/skills | Skill | **added** (`mattpocock-code-review`) | |
| 6 | Analytics (Marketingskills) | github.com/coreyhaines31/marketingskills | Skill collection (~40 files) | not-installed | Verified real (MIT); not installed this pass — marketing isn't this repo owner's stated workflow focus, logged for later. |
| 7 | Academy Guide (Anthropic) | github.com/anthropics/skills | Skill | already-known | Part of the installed `anthropic-skills` plugin. |
| 8 | Humanizer (blader) | github.com/blader/humanizer | Skill | not-installed | Verified real (MIT); logged for later — not core to this repo owner's current workflow. |
| 9 | SEO Agentic | github.com/AgriciDaniel/claude-seo | Skill collection | not-installed | Verified real; repo's own README is internally inconsistent on sub-skill counts (26 vs 29). |
| 10 | Create Video (OpenMontage) | github.com/OpenMontageInc/OpenMontage | Tool (agentic system) | tool-not-a-skill | AGPL-3.0; not a SKILL.md package. |
| 11 | Anti UI Slop | uizze.com | Tool/site + uncertain skill repo | not-installed, low confidence | The "anti-ui-slop" skill's exact GitHub location could not be confirmed. |
| 12 | Taste Skill | github.com/Leonxlnx/taste-skill | Skill | not-installed | Verified real; v2 rewrite now default. Logged for later. |
| 13 | Emil Design Engineering | github.com/emilkowalski/skills | Skill | **added** (`emil-design-eng`) | |
| 14 | Vercel Web Design Guidelines | github.com/vercel-labs/agent-skills (`web-design-guidelines`) | Skill | not-installed | Verified real; dynamically fetches Vercel's 100+-rule canonical ruleset — logged for later. |
| 15 | Frontend Design (Anthropic) | github.com/anthropics/skills | Skill | already-known | |
| 16 | Make Interfaces Feel Better | github.com/jakubkrehel/make-interfaces-feel-better | Skill | not-installed | Verified real; overlaps significantly with `emil-design-eng`'s polish checklist — one is enough for now. |
| 17 | UI UX Pro Max | github.com/nextlevelbuilder/ui-ux-pro-max-skill | Skill + companion CLI | not-installed | Verified real; has a paid "Premium" tier — logged for later. |
| 18 | Stageshow (Benji Taylor) | github.com/benjitaylor/skills (`stageshow`) | Skill | not-installed | Narrow use case (faux product UI for marketing pages) — logged for later. |
| 19 | claude code action | github.com/anthropics/claude-code-action | Tool (GitHub Action) | tool-not-a-skill | Official; relevant if this repo's CI ever runs Claude Code in Actions. |
| 20 | anthropic sdk python | github.com/anthropics/anthropic-sdk-python | Tool (SDK) | tool-not-a-skill | |
| 21 | herdr | github.com/ogulcancelik/herdr (owner corrected) | Tool | tool-not-a-skill | |
| 22 | buzz (Block) | github.com/block/buzz | Tool | tool-not-a-skill | |
| 23 | deer flow (ByteDance) | github.com/bytedance/deer-flow | Tool (agent harness) | tool-not-a-skill | |
| 24 | cline | github.com/cline/cline | Tool | tool-not-a-skill | |
| 25 | openviking (Volcengine) | github.com/volcengine/OpenViking | Tool | tool-not-a-skill | License/date conflict across sources — unverified specifics. |
| 26 | Awesome Claude Code | github.com/hesreallyhim/awesome-claude-code | Curated list | tool-not-a-skill | Useful as a discovery index, not itself a skill. |
| 27 | Ruflo (ruvnet) | github.com/ruvnet/ruflo | Tool | tool-not-a-skill | Confirmed real rename of claude-flow/ruv-swarm-adjacent tooling, not a mis-transcription. |
| 28 | Agents (wshobson) | github.com/wshobson/agents | Skill/agent marketplace | not-installed | Large bundle (~162 skills per one snapshot) — worth browsing later rather than bulk-importing. |
| 29 | Claude Code Router | github.com/musistudio/claude-code-router | Tool | tool-not-a-skill | |
| 30 | Claude Code Templates | github.com/davila7/claude-code-templates | Tool (CLI) | tool-not-a-skill | |
| 31 | Vibe Kanban | github.com/BloopAI/vibe-kanban | Tool | tool-not-a-skill | Conflicting signal on whether the kanban board itself is still active — verify before relying on it. |
| 32 | SuperClaude | github.com/SuperClaude-Org/SuperClaude_Framework | Tool (framework) | tool-not-a-skill | |
| 33 | opcode | github.com/winfunc/opcode | Tool (desktop GUI) | tool-not-a-skill | Maintenance activity contested across sources. |
| 34 | ccusage | github.com/ryoppippi/ccusage (owner corrected) | Tool | tool-not-a-skill | |
| 35 | Claude Code UI | github.com/siteboon/claudecodeui | Tool | tool-not-a-skill | |
| 36 | Claude Squad | github.com/smtg-ai/claude-squad | Tool | tool-not-a-skill | |
| 37 | CCPM | github.com/automazeio/ccpm | Tool (PM system) | tool-not-a-skill | Maintenance activity contested. |
| 38 | Hooks Mastery | github.com/disler/claude-code-hooks-mastery | Educational repo | tool-not-a-skill | Community project, not official Anthropic docs — don't conflate. |
| 39 | ui-ux-pro-max (post 4) | github.com/nextlevelbuilder/ui-ux-pro-max-skill | Skill | duplicate of #17 | |
| 40 | /canvas-design | github.com/anthropics/skills | Skill | already-known | |
| 41 | /pptx | github.com/anthropics/skills | Skill | already-known | |
| 42 | /theme-factory | github.com/anthropics/skills | Skill | already-known | |
| 43 | stitch-skills | github.com/google-labs-code/stitch-skills | Skill collection | not-installed | Verified real (Apache-2.0); Google Stitch MCP-dependent, not core workflow. |
| 44 | /frontend-design | github.com/anthropics/skills | Skill | already-known | |
| 45 | DESIGN.md | github.com/google-labs-code/design.md | Format spec (not a skill/MCP) | tool-not-a-skill | Alpha; npx CLI for lint/diff/Tailwind export. |
| 46 | Astryx (Meta) | github.com/meta/astryx | Tool (component library) | tool-not-a-skill | Owner corrected/confirmed as "meta", not "facebook". |
| 47 | shadcn/ui | github.com/shadcn-ui/ui | Tool | tool-not-a-skill | |
| 48 | Tailwind CSS | github.com/tailwindlabs/tailwindcss | Tool | tool-not-a-skill | |
| 49 | Magic UI | github.com/magicuidesign/magicui | Tool | tool-not-a-skill | |
| 50 | Magic MCP (21st.dev) | github.com/21st-dev/magic-mcp | MCP server (rebranded "21st MCP") | tool-not-a-skill | Old `@21st-dev/magic` package/keys deprecated. |
| 51 | Penpot | github.com/penpot/penpot | Tool + bundled MCP | tool-not-a-skill | Standalone `penpot-mcp` repo archived; MCP now lives in-repo under `mcp/`. |
| 52 | Excalidraw | github.com/excalidraw/excalidraw | Tool | tool-not-a-skill | |
| 53 | tldraw | github.com/tldraw/tldraw | Tool | tool-not-a-skill | Watermark license caveat for commercial use. |
| 54 | Lucide | github.com/lucide-icons/lucide | Tool | tool-not-a-skill | |
| 55 | Leonardo (Adobe) | github.com/adobe/leonardo | Tool | tool-not-a-skill | |
| 56 | rembg | github.com/danielgatis/rembg | Tool | tool-not-a-skill | |
| 57 | agent-browser (Vercel) | github.com/vercel-labs/agent-browser | Tool (browser automation CLI) | tool-not-a-skill | See correction above re: design-checking claim. |
| 58 | TokenEconomizer (Microsoft) | github.com/microsoft/TokenEconomizer | Tool (plugin) | tool-not-a-skill | 18.4-30.9% cost-reduction claim traced to a real arXiv paper (2610.22732) — authors' own numbers, not independently reproduced. |
| 59 | loom (ClickHouse) | github.com/ClickHouse/loom | MCP server | tool-not-a-skill | Verified via direct WebFetch. |
| 60 | nomore (globalmpc) | github.com/globalmpc/nomore | CLI tool | tool-not-a-skill | Local-only, no data sent out. |
| 61 | stalemap | github.com/Umair/stalemap | Tool (MCP+CLI+plugin+Action) | tool-not-a-skill | Owner "Umair" confirmed correct (not a wrong handle as initially suspected). |
| 62 | landmines | github.com/devanshranjan10/landmines | Tool (MCP+CLI+hook) | tool-not-a-skill | Handle corrected to the full `devanshranjan10`. |
| 63 | Rulebook | **unresolved** | Tool (menu-bar app) | dead-or-unverifiable | Only a landing page found; GitHub org/owner unconfirmed. |
| 64 | lean-subagent (mdalexandre) | github.com/mdalexandre/claude-code-lean-agents | Tool (subagent configs) | tool-not-a-skill | Author's own benchmark, not independently reproduced. |

No item in this list is a genuine gap in the `skills/` registry's own taxonomy — everything
worth adopting belongs in the personal `~/.claude/skills` library (where it was added) rather
than the SPEC.md-governed portable factory, same disposition reasoning as
`prompts/06-ingest-high-leverage-skills.md` used for the earlier high-leverage-skills list.
