# 100+ High-Leverage AI Skills Across Every Domain

> Source material supplied by the repo owner on 2026-10-31 for ingestion into the Skill Factory.
> Unprocessed reference list — do not treat as registry or SKILL.md content. See
> `prompts/06-ingest-high-leverage-skills.md` for the task that turns this into registry rows and
> validated `skills/<CODE>/<name>/SKILL.md` files, deduplicated against the existing library the
> same way `logs/claude-migration.md` deduplicated the former Claude skills collection.

A reference library of reusable AI skills — prompt templates, custom instructions, and structured
workflows — that work in both Claude and ChatGPT. Each skill names what it does and when to reach
for it. Treat these as starting templates to adapt to your own data and voice, not copy-paste
magic words.

## 1. Coding & Development

- **Code Reviewer Persona** — paste a diff and have the model review it as a staff engineer: correctness, edge cases, security, naming, test coverage gaps.
- **Rubber Duck Debugger** — walk through a bug step by step with the model asking clarifying questions before suggesting fixes, instead of jumping straight to an answer.
- **Architecture Decision Record (ADR) Writer** — turn a technical decision discussion into a structured ADR: context, options considered, decision, consequences.
- **Legacy Code Explainer** — paste unfamiliar code and get a plain-language walkthrough plus a dependency map before you touch it.
- **Test Generator** — given a function or spec, generate unit tests covering happy path, edge cases, and failure modes, matching your existing test style.
- **Refactor Planner** — propose a refactor as a sequence of small, independently-shippable steps rather than one giant rewrite.
- **API Design Critic** — review a proposed REST/GraphQL schema for consistency, versioning risk, and naming conventions before you build it.
- **Commit Message / PR Description Generator** — turn a diff into a clear commit message and PR description with a summary, rationale, and testing notes.
- **Incident Postmortem Writer** — turn raw incident notes/timeline into a blameless postmortem: timeline, root cause, contributing factors, action items.
- **Regex / SQL Query Builder** — describe the matching or filtering logic in plain English and get the regex or SQL plus a line-by-line explanation.

## 2. Research & Analysis

- **Steelman / Devil's Advocate** — ask the model to argue the strongest possible case against your own conclusion before you finalize it.
- **Source Triangulation Brief** — have the model pull claims from multiple sources, flag where they disagree, and rate confidence per claim.
- **Literature Synthesis Matrix** — feed several papers/articles and get a comparison table of methodology, findings, and limitations instead of separate summaries.
- **Assumption Surfacer** — before acting on an analysis, have the model list every hidden assumption baked into it and how sensitive the conclusion is to each.
- **Pre-Mortem** — imagine the plan failed in 12 months; have the model generate the most plausible reasons why, ranked by likelihood.
- **Second-Opinion Reviewer** — paste your own analysis/memo and ask for an independent critique as if the model had never seen your reasoning.
- **Fermi Estimator** — break a hard-to-estimate number (market size, cost, time) into component estimates with explicit ranges and a sanity check.
- **Competing Hypotheses Table** — lay out 3-4 explanations for an observation side by side with the evidence that would confirm or rule out each.
- **Interview/Survey Question Designer** — turn a research goal into a non-leading question set, flagging bias risk in each question.

## 3. Writing & Content

- **Voice Cloning from Samples** — paste 3-5 pieces of your own past writing and have the model extract a style guide (sentence length, vocabulary, tics) to apply to new drafts.
- **Outline-First Drafting** — force a detailed outline with argument flow before any prose, so structural problems get caught before you've written 1,000 words.
- **The Brutal Editor** — paste a draft and get it cut by a target percentage, with every cut justified in one line.
- **Headline/Subject Line Generator** — produce 15-20 variants across different angles (curiosity, benefit, urgency, contrarian) for A/B testing.
- **Explain It to a 12-Year-Old** — simplify dense/technical writing without losing accuracy, useful for catching jargon you didn't notice.
- **Tone Shifter** — rewrite the same piece in 3-4 tones (formal, casual, executive, friendly) so you can pick the right register fast.
- **Show-Don't-Tell Rewriter** — flag abstract/generic sentences in a draft and rewrite them as concrete scenes or specifics.
- **Counter-Argument Inserter** — strengthen persuasive writing by having the model insert and then rebut the strongest objection a skeptical reader would raise.
- **Repurposing Engine** — turn one long-form piece (article, video transcript) into a thread, LinkedIn post, email, and short-form script, matched to each platform's norms.

## 4. Business Strategy & Planning

- **Business Model Canvas Fill-In** — generate a first-pass canvas (value prop, channels, cost structure, revenue) from a one-paragraph idea description, then stress-test each box.
- **Porter's Five Forces Analyzer** — apply the framework to your specific market with concrete, named competitors rather than generic textbook answers.
- **SWOT with Teeth** — generate a SWOT, then force-rank each item by impact so it's not just a list of platitudes.
- **Pricing Strategy Sparring Partner** — walk through cost-plus, value-based, and competitor-based pricing for a specific product and argue the trade-offs.
- **OKR Drafting Assistant** — turn a vague goal into measurable objectives and key results, flagging any KR that isn't actually measurable.
- **Scenario Planner (Best/Base/Worst)** — build three narrative scenarios for a strategic decision with the specific triggers that would move you from one to another.
- **Board Memo Writer** — turn messy internal notes into a structured board update: highlights, lowlights, asks, metrics.
- **Vendor/Partner Comparison Matrix** — compare 3+ vendors against your specific requirements (not generic features), weighted by what matters to you.

## 5. Data & Spreadsheets

- **Formula Explainer** — paste a gnarly spreadsheet formula and get a plain-English breakdown plus a simpler equivalent if one exists.
- **Messy Data Cleaner** — describe inconsistencies in a dataset (date formats, duplicate names, typos) and get a cleaning script or formula set, not just advice.
- **Pivot Table Planner** — describe the question you want answered and get the exact rows/columns/values/filters to configure, before you touch the data.
- **Data Validation Rule Writer** — generate validation rules and conditional formatting logic to catch bad entries before they corrupt an analysis.
- **Dashboard Spec Writer** — turn "I want to track X" into a specific list of metrics, chart types, and refresh cadence for a dashboard build.
- **Anomaly Explainer** — given a chart or number that moved unexpectedly, generate a ranked list of plausible causes to investigate first.
- **Cohort Analysis Framer** — set up the logic for cohort/retention analysis correctly (common source of errors) before building it in a tool.
- **SQL-to-Plain-English (and back)** — translate business questions into SQL and SQL results back into a plain-language summary for non-technical stakeholders.

## 6. Documents, Slides & Office

- **Meeting Notes to Action Items** — turn raw/messy meeting notes into a clean summary plus a task list with owners and due dates pulled from context.
- **Slide Deck Outliner** — turn a messy brain dump into a slide-by-slide outline (one idea per slide, a headline that states the takeaway) before any design work starts.
- **Executive Summary Compressor** — compress a long report into a one-page executive summary that a time-pressed reader can act on.
- **Template-to-Document Filler** — feed a company template (contract, SOP, report) plus raw facts and have the model fill it correctly, flagging any required field it can't find data for.
- **Document Comparison / Redline Explainer** — compare two versions of a document and explain what changed in plain language, not just a diff.
- **Policy/SOP Writer** — turn a description of how a process actually works into a clear, numbered standard operating procedure.
- **Email Thread Summarizer** — compress a long back-and-forth thread into "what was decided, what's still open, who owes what."

## 7. Design & Visual

- **Mockup-to-Spec Translator** — describe a screen or feature in words and get a structured UI spec (layout, states, components) a designer or developer can build from.
- **Design Critique Partner** — paste a screenshot/description of a design and get a critique structured around hierarchy, contrast, and usability, not vague taste opinions.
- **Brand Voice/Visual Guide Extractor** — feed existing brand assets and have the model articulate the implicit visual/voice rules so new work stays consistent.
- **Color Palette Rationale Builder** — generate a palette plus the accessibility and psychological rationale for each color choice, not just hex codes.
- **Icon/Asset Naming Convention Generator** — produce a consistent naming system for a growing asset library so files stay findable.
- **Accessibility Audit Checklist** — generate a contrast/alt-text/keyboard-nav checklist tailored to a specific interface before a compliance review.
- **Before/After Copy for Visual Ads** — pair a visual concept with 5-10 headline/body copy variants matched to the image's emotional register.

## 8. Sales & Outreach

- **Cold Email Personalizer at Scale** — turn a prospect's public info (company news, role, LinkedIn post) into a genuinely specific opening line, not a mail-merge token.
- **Objection Handler Script Builder** — generate response scripts for the 10 most common objections in your sales motion, each with a question that reopens the conversation.
- **Discovery Call Question Bank** — generate qualifying questions mapped to your specific ICP and deal stage, not generic SPIN-selling filler.
- **Deal Risk Spotter** — paste CRM notes from a deal and have the model flag stalled signals (no economic buyer identified, no next step, ghosting pattern).
- **Proposal/SOW Drafting Skill** — turn a scoping call's notes into a structured proposal with deliverables, timeline, and pricing tiers.
- **LinkedIn Outreach Sequencer** — build a 4-5 touch outreach sequence with each message escalating value, not just repeating the ask.
- **Win/Loss Analysis Synthesizer** — feed closed-deal notes across a quarter and get patterns in why deals were won or lost.
- **Negotiation Prep Brief** — given the other side's likely priorities, generate your BATNA, anchor point, and concession ladder before a negotiation.

## 9. Operations & Project Management

- **Process Documentation from a Walkthrough** — describe (or paste a transcript of) how you do a task and get a clean, numbered SOP with decision points called out.
- **Weekly Status Report Compiler** — turn scattered updates (Slack, email, notes) into a structured status report: done, in-progress, blocked, next.
- **RACI Matrix Builder** — given a project description, assign Responsible/Accountable/Consulted/Informed roles and flag any task with no owner.
- **Vendor Onboarding Checklist Generator** — produce a tailored checklist (contracts, access provisioning, compliance docs) for onboarding a new vendor or contractor.
- **Root Cause Analysis (5 Whys) Facilitator** — walk a problem through the 5 Whys method, pushing back when an answer is too shallow.
- **Capacity Planning Sanity Check** — given team size and backlog, flag unrealistic timeline commitments before they're promised externally.
- **Meeting Agenda Tightener** — turn a vague meeting invite into a tight agenda with a stated decision or outcome for each item.
- **Runbook Writer for Recurring Incidents** — turn a one-off incident fix into a reusable runbook for the next time the same symptom appears.

## 10. Finance & Accounting

- **Unit Economics Builder** — walk through CAC, LTV, contribution margin for a specific business model, flagging which inputs are guesses versus known.
- **Budget Variance Explainer** — paste actuals vs. budget and get a plain-language explanation of the biggest drivers of variance, not just the numbers restated.
- **Invoice/Expense Categorization Assistant** — classify a batch of transactions into chart-of-accounts categories consistently, flagging ambiguous ones for human review.
- **Financial Model Assumption Auditor** — review a model's assumptions tab for internal inconsistency (e.g., growth rate implies a market share that contradicts TAM).
- **Break-Even Scenario Builder** — model break-even under different pricing/cost assumptions and narrate what has to be true for each to work.
- **Investor Update Writer** — turn raw metrics into a structured monthly/quarterly investor update: headline, metrics, asks, risks.
- **Cash Flow Forecast Sanity-Checker** — stress-test a cash flow forecast against seasonality or known upcoming expenses it may have missed.

## 11. Education & Learning

- **Feynman Explainer** — explain a concept simply, then have the model find the gaps by asking you to re-explain it back, surfacing what you don't actually understand.
- **Socratic Tutor** — instead of giving the answer, the model asks guiding questions that lead you to derive it yourself.
- **Spaced-Repetition Card Generator** — turn notes or a textbook chapter into flashcards optimized for recall, not just fact restatement.
- **Study Plan Builder from a Syllabus** — turn a syllabus/exam date into a day-by-day study schedule with built-in review cycles.
- **Practice Problem Generator at Difficulty Level** — generate problems calibrated to where you're actually stuck, with full worked solutions.
- **Concept Map Builder** — given a topic, map how its sub-concepts relate to each other, useful before diving into a new technical domain.
- **Essay/Argument Structure Coach** — critique the logical structure of an argumentative essay (claim, evidence, warrant) separately from the prose quality.

## 12. Creative, Music & Media

- **Lyric Rhyme-Scheme Scaffolder** — build the syllable/rhyme/meter skeleton for a verse-chorus structure first, so you write to a form rather than fighting it afterward.
- **Song Concept-to-Structure Mapper** — turn a raw theme or emotion into a verse/pre-chorus/chorus/bridge arc with a stated narrative turn at the bridge.
- **Genre Reference Deconstructor** — describe the production/arrangement qualities of a reference track in words you can act on (without reproducing any lyrics or protected material).
- **Alt-Take Generator** — generate multiple structurally different directions for the same raw idea (different hook placement, different POV) before committing.
- **Video Script-to-Shot-List Converter** — turn a written script into a numbered shot list with framing and estimated duration per shot.
- **Podcast Outline + Question Bank** — turn an episode topic into a segment structure plus a guest-specific question bank.
- **Caption/Hook Variant Generator** — produce multiple opening-line variants for short-form video optimized for the first 2 seconds.

## 13. Meta / Prompt-Engineering Skills

- **Prompt Critique Loop** — have the model critique its own prompt before answering: what's ambiguous, what's missing, what assumption it's about to make.
- **Few-Shot Example Builder** — turn 2-3 of your best past outputs into formatted examples that lock in format/tone for future generations.
- **System Prompt Compressor** — take a bloated custom-instructions block and cut it to the minimum that still produces the desired behavior, removing redundant rules.
- **Chain-of-Thought Scaffolder** — for multi-step reasoning tasks, explicitly request the intermediate steps before the final answer, catching errors mid-chain.
- **Role + Constraints Template** — a reusable skeleton (role, context, task, constraints, output format) you fill per-task instead of writing prompts from scratch.
- **Output Format Enforcer** — specify exact structure (JSON schema, table columns, word count) up front to cut down on reformatting afterward.
- **Red-Team Your Own Prompt** — ask the model to find ways the prompt could be misread or produce an unwanted result before you deploy it at scale.
- **Skill/Template Librarian** — maintain a running personal doc of your best-performing prompts by task type, so you reuse rather than reinvent each time.

## Top 10 Cross-Domain Must-Haves

| # | Skill | Why it's cross-domain |
|---|---|---|
| 1 | Steelman / Devil's Advocate | Catches weak reasoning before it ships, in any domain |
| 2 | Outline-First Drafting | Prevents structural rework in docs, decks, code plans |
| 3 | The Brutal Editor | Forces every deliverable to earn its length |
| 4 | Role + Constraints Template | Turns every one-off prompt into a reusable asset |
| 5 | Assumption Surfacer | Exposes the hidden bets in any plan or model |
| 6 | Executive Summary Compressor | Every report eventually needs a one-page version |
| 7 | Meeting Notes to Action Items | The single highest-frequency use case across all roles |
| 8 | Pre-Mortem | Cheap insurance before any high-stakes decision |
| 9 | Voice Cloning from Samples | Makes every other writing skill sound like you, not generic AI |
| 10 | Red-Team Your Own Prompt | Meta-skill that improves every other skill on this list |

Start with whichever skill matches the task you repeat most often — it pays back fastest, and
adapting it to your own context teaches you more about prompting than any generic guide.
