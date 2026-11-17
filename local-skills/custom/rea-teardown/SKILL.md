---
name: rea-teardown
description: Use to reverse-engineer a competitor's shipped product (desktop app, CLI, npm package) down to its actual architecture and strategic decisions, then optionally turn the findings into a build-scoping prompt for a similar product.
---

# rea-teardown

## Top rules
1. Pull the real artifact, not a description of it. `npm pack`, `@electron/asar extract`, or `npx rea-agents analyze-javascript-application` on the actual shipped bundle beats reading marketing pages every time.
2. Every claim needs a source location. "The renderer is 0 bytes, so the UI loads remotely" beats "it's probably a thin client." If you can't point at a file/line, it's a guess — label it one.
3. Read for *decisions*, not features. Every finding should end in a takeaway: what trade-off did they make, and when would you make the same one.
4. Minified/bundled code still leaks. Tool names, IPC channel lists, prompt strings, and schema files survive minification as string literals — grep for them before giving up on a bundle.
5. Compare at least two products in the same category when possible. One teardown is trivia; two is a pattern (e.g. "thin remote shell" vs "ship the UI locally" are both valid, for different reasons).

## When to use
- Scoping a new product and want to learn from how a comparable one is actually built, not how its landing page describes it.
- Technical due diligence on a competitor, acquisition target, or "should we build vs. adopt this" decision.
- You have a shipped artifact available (an installer, an npm package, a `.deb`/`.app`, a public repo with no source maps) and want to know what's really inside.

## Inputs needed
Ask for anything missing. Do not guess.
- The target product and how you can obtain its real artifact: npm package name, installer/winget/brew name, or a URL to download it from.
- Platform (Windows/macOS/Linux) if it's a desktop app — architecture can differ per platform.
- What you actually want out of it: architecture understanding, a build-it-yourself scoping prompt, a security/trust review, or a competitive comparison.
- Whether you're allowed to install/run it locally (most teardown steps need the artifact on disk; a few, like `rea-agents analyze-javascript-application`, work on static JS without running it).

## Steps

### 1. Acquire the real artifact, not a proxy for it
Pick the lowest-friction extraction path for what you're targeting (see `references/extraction-techniques.md` for exact commands):
- **npm package** → `npm pack <name>` downloads the exact published tarball. No install, no asar, nothing to unwrap first.
- **Electron desktop app** → install it, then `npx @electron/asar extract <path-to-app.asar> <out-dir>`. Electron apps almost always ship an `app.asar` you can unpack directly.
- **Any minified/bundled JS, with or without running it** → `npx rea-agents analyze-javascript-application <target>` for a structured static-analysis report instead of hand-reading a 2MB bundle.
- **Native binary with no readable source** → scope down to what you can actually get (`strings`, package manifests, shipped config/schema files) rather than attempting a full disassembly unless that's explicitly the goal.

### 2. Map the shape before reading any single file
- Is the UI shipped locally (a real `renderer`/`webpack` build on disk, several MB) or loaded remotely (an empty or near-empty `index.html`, a hardcoded production URL)? This one fact predicts most of the rest of the architecture.
- List native node addons / per-OS helper binaries (`better-sqlite3`, a Swift/C# helper process, prebuilt platform-specific optional dependencies). A separate native helper process almost always means "this needs OS permissions a web/JS sandbox can't get" (accessibility APIs, global hotkeys, raw filesystem/process access).
- Note the IPC surface: how many channels/commands does the main process expose to the renderer (or the cloud to the desktop app)? The size and shape of that list *is* the product's actual feature boundary — often more honest than the marketing page.

### 3. Grep bundles for what minification can't hide
⚠️ Don't stop at "it's minified, I can't read it." Search the bundle text for:
- Tool/command name lists (string arrays near the top of a CLI's entry bundle) — these reveal the real command surface.
- Prompt-shaped text: look for first-person system-prompt phrasing ("You are...", "Act as...", "When the request is..."). Minifiers don't touch string literals' content, only variable names.
- Schema/IPC contract files (`schema.json`, `*.d.ts`, generated-types comments) — these are often shipped unminified even in an otherwise-minified bundle, and they're a precise, unambiguous spec of the real data model.
- Dependency names in `package.json`/`node_modules` manifests — a patched or forked dependency (check for a `patches/` folder) tells you they hit a real limitation of the stock library and is worth reading the patch for.

### 4. For anything that does sensitive things (filesystem access, running an AI agent with tool access, handling credentials), read the security model specifically
- IF the product gives an AI/agent real device access (files, messages, shell) THEN look for a denylist (secrets/credential file names, dangerous extensions), platform-specific path protection, and path canonicalization (`realpath`, symlink-aware containment checks) — this three-layer pattern is close to best practice; a product missing layer 3 (real containment math, not `path.startsWith()`) has a path-traversal bug waiting to be found.
- IF it opens a network channel (local server, outbound relay/WebSocket) THEN note which direction it dials (inbound local server vs. outbound-only relay) — outbound-only avoids exposing any local listening port, at the cost of needing a relay service.
- IF it stores credentials/tokens THEN check whether raw tokens or only hashes (`_sha256` suffixes) appear in logs/messages — logging raw tokens is a real finding, not a style nit.

### 5. Turn every finding into a takeaway, then write the teardown doc
For each numbered finding: one paragraph of evidence (with exact file/path), then a **Takeaway:** line stating the design trade-off and when you'd make the same call. A finding with no takeaway is trivia — cut it or finish it.

### 6. (Optional) Convert the teardown into a build-scoping prompt
If the goal is "build something in this category," restructure the strongest 4-6 takeaways into a CO-STAR prompt (Context, Objective, Style, Tone, Audience, Response) addressed to a coding agent: state what you're building, say explicitly "I reverse-engineered an existing product in this category down to its architecture, and want to build toward the category using the patterns it proved out, not clone its UI," then list the takeaways as numbered technical requirements that should shape the plan. See `references/extraction-techniques.md` for the CO-STAR skeleton.

## Decision rules
- IF the renderer/UI directory is empty or near-empty THEN the real product is server-side and the local app is a thin shell — don't waste time reading client-side "logic" that doesn't exist.
- IF you find a native helper process or platform-specific optional-dependency binaries THEN assume OS-level permissions are the reason, and go look at what that helper can do before anything else.
- IF a dependency has a `patches/` folder THEN read the patch — it's a direct pointer to a real limitation they hit in production, which is worth more than any other finding in the bundle.
- IF the artifact is an npm package THEN always start with `npm pack`, never `npm install -g` — you get the exact published bytes with zero side effects.
- IF you cannot get a running instance but can get static JS THEN use `rea-agents analyze-javascript-application` before giving up on dynamic-looking code.

## Output template
```
TEARDOWN — <product name> <version>
Target & method: <artifact source, extraction command(s) used>

## <N>. <Finding title>
<Evidence with exact file path / line / string>
**Takeaway:** <the trade-off, and when you'd make the same call>

... (repeat per finding)

## Summary
<One paragraph: the single biggest strategic decision this product made, and the
category-level lesson it implies.>
```

## Worked example
**Input:** "Tear down Notion desktop on Windows, I want to know how they do offline-first sync and whether their AI agent file-access is safe to copy."

**Output excerpt:**
```
TEARDOWN — Notion Desktop v7.40.1
Target & method: winget install, @electron/asar extract on app.asar

## 1. Ships the renderer locally, not remote (opposite of Linear)
app.asar is 26MB with a real .webpack/renderer tree (dozens of mini-apps, each own
index.html+index.js). .webpack/main/index.js is 4.4MB of real main-process logic.
**Takeaway:** offline-first-by-design costs you a release pipeline (every UI fix needs a
new build); choose this only when users genuinely need full offline capability.

## 2. Three-layer sandbox for AI filesystem access (clientMcpHost/policy/)
Layer 1: static secrets/extension denylist (id_rsa, .env, .pem...). Layer 2: OS-specific
dangerous-path blocking (%SystemRoot%, .exe/.dll). Layer 3: realpath + per-component
symlink checks, real containment math (not path.startsWith()).
**Takeaway:** this is close to best practice for "give an AI real file access" — copy
layers 1+2 directly; layer 3 (symlink-aware containment) is the one most teams skip and
the one that actually prevents path-traversal escapes.

## Summary
Notion bet on "ship a real local app, own a real local SQLite+search cache" instead of
Linear's thin-remote-shell approach, and separately built a genuinely production-grade
agent-sandboxing model years before "AI agent with file access" was a common feature
request elsewhere — worth studying even outside the note-taking category.
```

**Bad output:** "Notion desktop is a well-built Electron app with good security practices." — no file paths, no mechanism, no takeaway. Not a teardown, a compliment.

## Edge cases
- Target has no public artifact (web-only SaaS, no desktop/CLI/package) → teardown is limited to what their own public API docs, browser network tab, and public GitHub (if any) reveal; say so explicitly rather than inventing internals.
- Obfuscated beyond minification (control-flow flattening, string encryption) → note that standard grep-for-strings won't work and scope down to metadata (dependency list, file sizes, network calls) instead of claiming a false negative means "nothing there."
- Legal/ToS restrictions on reverse engineering the specific target → flag this before starting, don't proceed on a product whose terms explicitly prohibit it.

## Failure modes
- Treating "I read the README" as a teardown. The README is marketing; the artifact is the product.
- Collecting findings with no takeaway — a list of trivia nobody can act on.
- Giving up at the first minified file instead of grepping it for string literals.
- Skipping the security read on anything with real file/device access, because it's "just a nice-to-have feature" — this is usually the most valuable part of the teardown.

## Hand-off
If this teardown feeds a new build: pass the CO-STAR prompt (step 6) to `stack-launcher` or `build-sprint` to scope the actual implementation.
