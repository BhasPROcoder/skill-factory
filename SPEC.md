# SPEC — Portable Skill Format v1

A skill is portable when a different model, with zero context, reads it once and behaves the same way. Every rule below serves that.

## 1. Portability rules
1. Plain Markdown with frontmatter. No tool calls, plugins, or model-specific syntax.
2. No vendor or model names (GPT, Claude, DeepSeek, Gemini, etc.) unless the skill is literally about comparing models.
3. Operational language only. Not "be thorough" but "run all 8 checklist items before answering."
4. Judgment becomes explicit rules: `- IF <condition> THEN <action> BECAUSE <reason>`.
5. The output is pinned by an exact template inside a code block.
6. One good worked example and one bad one with the reason it fails.
7. A weaker model must be able to follow it: numbered steps, one action each, no hidden knowledge.
8. Body length 700–1,800 words. Larger → split into two skills linked by `requires`.

## 2. File location
`skills/<DOMAIN-CODE>/<name>/SKILL.md` where `<name>` equals the frontmatter `name`.

## 3. Frontmatter (exact keys, exact order)
Lists MUST be JSON arrays with double-quoted strings.

```
---
id: LAW-014
name: contract-clause-risk-review
domain: Contract Law
subdomain: Commercial contracts
version: 1.0
description: One sentence saying what it does and when to use it.
triggers: ["5 to 10 phrases a user might say"]
not_for: ["2 to 5 adjacent tasks, with the right skill ID in brackets if known"]
requires: []
risk_level: low
---
```
- `id`: `<CODE>-<3 digits>`, must exist in the registry.
- `name`: kebab-case, globally unique, max 64 chars.
- `risk_level`: `low` | `medium` | `high`. High = law, medicine, mental health, finance, tax, safety, security.

## 4. Body sections (exact headings, exact order)
```
# <Title>
## Purpose
## Inputs to collect
## Procedure
## Decision rules
## Output template
## Quality checklist
## Anti-patterns
## Worked example
## Edge cases
## Test case
```
- **Purpose**: 2–3 sentences.
- **Inputs to collect**: numbered; each has name, why, and default if not given. End with the rule: if a required input is missing and has no safe default, ask in one message, max 3 questions.
- **Procedure**: numbered single actions. Mark the error-prone steps with ⚠️ and say what to do instead.
- **Decision rules**: at least 3 lines starting `- IF `.
- **Output template**: one fenced code block holding the exact answer structure, with length limits.
- **Quality checklist**: 6–10 items, each `- [ ] ...`, each objectively checkable.
- **Anti-patterns**: 4–8 items, `- **Name**: failure. Fix: ...`
- **Worked example**: `**Input:**`, `**Output:**`, `**Bad output:**` (+ one line on why it fails).
- **Edge cases**: 3–6 items, each with the exact handling.
- **Test case**: exactly this shape:
```
**Input:**
> the test request

**Assertions:**
1. checkable statement
2. ...
```
3–5 assertions, each verifiable by reading the output.

## 5. Domain rules
- **High-risk skills** must: ask for jurisdiction/context with no silent default; tell the user to verify current law/guidelines because knowledge has a cutoff; state when to see a licensed professional; never invent citations, case names, section numbers, drug doses or statistics — write `[VERIFY: what to look up]` instead.
- **Prompting/AI**: give real prompt templates, not descriptions of them.
- **Code/technical**: state language/version, include runnable snippets, include the verification step.
- **Creative**: describe style as observable features (sentence length, POV, structure, devices).
- **Country-specific**: put the country in the name (`in-gst-invoice-check`, `us-llc-formation`). Cover India and US first where relevant.

## 6. Self-check before saving
- [ ] Frontmatter complete, lists are JSON arrays
- [ ] Description = what + when, one sentence
- [ ] Every procedure step is one concrete action
- [ ] ≥3 IF/THEN rules
- [ ] Output template in a code block
- [ ] Worked example follows the template exactly
- [ ] No invented facts, citations or numbers
- [ ] Test case has 3–5 checkable assertions
- [ ] A smaller model could follow it without guessing
