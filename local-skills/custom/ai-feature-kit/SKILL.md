---
name: ai-feature-kit
description: Use when adding an LLM-powered feature to a hackathon build that must look impressive and never fail on stage: structured outputs, streaming, caching, fallbacks.
---

# ai-feature-kit

## Top rules
1. Judges have seen a thousand chatbots. A chat box is not a feature. Show AI doing something: deciding, extracting, acting, interrupting, generating an artifact.
2. Structured output, always. Parse JSON into UI components. Raw model text on screen looks like a wrapper.
3. Stream anything that takes over 2 seconds. Perceived speed is demo speed.
4. Cache every response for the demo inputs. Live first, cache on failure or timeout.
5. Show the reasoning trail (sources, steps, tool calls) in a collapsible panel. It's technical points for free.
6. Never claim the model does something it doesn't. Judges will test it live.

## When to use
- The scope card has an AI item in REAL.
- An AI feature works but is slow, flaky, or looks like a plain chatbot.

## Inputs needed
- The exact user action and the exact UI result the demo needs.
- Model access (Claude API key, any sponsor model).
- Latency budget for the demo moment (usually < 3 s to first visible output).

## Pattern menu

| Pattern | Use when | Demo payoff |
|---|---|---|
| Extract → cards | messy input (PDF, photo, voice) to structured data | before/after contrast |
| Judge → score + reasons | evaluating answers, code, resumes, essays | visible rubric with highlights |
| Agent with visible steps | multi-step task (search, compute, write) | live step list ticking off |
| Generate artifact | output is a file: plan, PDF, slide, code, email | judge gets something tangible |
| Proactive interrupt | AI speaks up without being asked | strongest wow moment |
| Compare / diff | two versions, two sources, two options | side-by-side highlights |

## Steps

### 1. Define the output schema first (10 min)
```ts
import { z } from "zod";

export const GapReport = z.object({
  score: z.number().min(0).max(10),
  gaps: z.array(z.object({
    concept: z.string(),
    why_missing: z.string(),
    source: z.object({ doc: z.string(), page: z.number() }),
    follow_up_question: z.string(),
  })).max(3),
  praise: z.string(),
});
```

### 2. Get structured output reliably
- Use tool use / JSON mode with the schema, or ask for JSON only and validate with zod.
- On parse failure: one retry with the validation error appended. Then fallback.
```ts
async function structured<T>(schema: z.ZodType<T>, call: (fix?: string) => Promise<string>): Promise<T> {
  const first = await call();
  const a = schema.safeParse(safeJson(first));
  if (a.success) return a.data;
  const second = await call(`Your last output failed validation: ${a.error.message}. Return valid JSON only.`);
  return schema.parse(safeJson(second));
}

function safeJson(s: string) {
  const m = s.match(/\{[\s\S]*\}/);
  return m ? JSON.parse(m[0]) : {};
}
```

### 3. Stream to the UI
- Stream tokens for prose. For structured output, stream a status line ("Reading your notes… Found 3 gaps…") then render cards when parsed.
- Skeleton loaders on cards, never a spinner alone.

### 4. Demo cache
```ts
import { createHash } from "crypto";

const cache = new Map<string, unknown>();
const key = (x: unknown) => createHash("sha1").update(JSON.stringify(x)).digest("hex");

export async function cached<T>(input: unknown, live: () => Promise<T>, ms = 8000): Promise<T> {
  const k = key(input);
  try {
    const out = await Promise.race([
      live(),
      new Promise<T>((_, r) => setTimeout(() => r(new Error("timeout")), ms)),
    ]);
    cache.set(k, out);
    return out;
  } catch (e) {
    if (cache.has(k)) return cache.get(k) as T;
    throw e;
  }
}
```
Persist the cache to the DB or a JSON file for the demo inputs so a server restart doesn't wipe it. Warm it by running the demo path 3× before judging.

### 5. Prompt hygiene
- System prompt: role, output schema, hard rules ("cite only from sources", "max 3 gaps").
- Include 1 example of ideal output for the demo case.
- Temperature low for structured outputs.
- Log every prompt and response during the hack to a table. You'll need examples for the pitch and for debugging.

### 6. Make it feel intelligent
- Use the user's own data in the answer (their name, their file, their numbers).
- Cite the exact source line.
- Give a confidence or a "here's what I'm unsure about" line.
- Do one thing proactively.

## Outputs
- Schema, prompt, route, cache, and the UI rendering components for each AI feature.
- A prompt log table for later use in submission and Q&A.

## Worked example
VoiceViva gap detection: transcript + top 6 retrieved chunks → `GapReport`. Status stream: "Listening… Checking against your notes… 2 gaps found". Cards show concept, a quote from the notes with page number, and the follow-up question spoken back via TTS. Demo inputs pre-run 3×; cache persisted in Supabase table `demo_cache`.

## Failure modes
- Chatbot UI with a text box and nothing else.
- Model output rendered as markdown blobs.
- 12-second silent wait during the live demo.
- No cache, and the API rate-limits during judging.
- Fancy agent with 8 tool calls that fails 1 in 4 runs. Fewer, reliable steps win.

## Hand-off
Back to `build-sprint`. At freeze, `demo-architect` verifies the cache is warm.
