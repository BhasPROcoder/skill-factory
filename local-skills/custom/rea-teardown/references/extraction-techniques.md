# Extraction techniques by artifact type

## npm package
```bash
npm pack <package-name>          # exact published tarball, zero side effects
tar -xzf <package>-<version>.tgz -C extracted/
grep -o '"[a-z_]\{3,30\}"' extracted/package/dist/index.js | sort -u   # candidate command/tool names
grep -n "You are\|I want you to act\|Act as" extracted/package/dist/*.js   # leaked prompt text
```
Check `package.json` `optionalDependencies` for `<pkg>-win32-x64`, `-darwin-arm64`, `-linux-x64`
style entries — this is the "tiny JS shim + per-platform prebuilt binary" pattern (same as esbuild,
swc). The real logic may be in the platform binary, not the JS shim.

## Electron desktop app
```bash
npx @electron/asar extract "<path to app.asar>" extracted/
```
- Find the asar: usually `resources/app.asar` under the install directory
  (`%LOCALAPPDATA%\Programs\<app>` on Windows, `/Applications/<app>.app/Contents/Resources` on
  macOS).
- `extracted/out/renderer/index.html` size tells you everything: near-0 bytes → UI loads from a
  remote URL (check `Constants-*.js` or similar for the hardcoded entry URL); several MB with a
  real `index.js`/webpack bundle → UI ships locally.
- `resources/app.asar.unpacked/node_modules/` holds native `.node` addons that can't live inside
  an asar — this is your native-dependency list without needing to read any JS.
- Look for a `patches/` folder (patch-package or similar) — a patched dependency is a direct
  pointer to a real production limitation they hit.

## Any minified/bundled JS, static (no install/run needed)
```bash
npx rea-agents analyze-javascript-application <path-or-url>
```
Produces a structured report instead of hand-reading a multi-MB bundle. Use this first on
anything that looks hostile to manual reading (webpack/esbuild/Bun-minified single files with no
source map).

## Grepping any extracted bundle for leaks
```bash
grep -rn "You are\|system prompt\|I want you to act" extracted/ --include=*.js
grep -rno '"[a-z][a-z_-]\{2,24\}"' extracted/**/index.js | sort | uniq -c | sort -rn | head -50
find extracted/ -name "*.json" -iname "*schema*"
```
Minifiers rename variables and strip whitespace; they do not rewrite string literal *contents*.
Tool names, command names, and prompt text inside string literals survive intact.

## IPC / command surface enumeration (Electron)
Search the main-process bundle for `ipcMain.handle(` / `ipcMain.on(` call sites (Electron) or
equivalent RPC registration calls for other frameworks. The count and names of registered
channels is close to a literal list of "everything the UI is allowed to ask the native layer to
do" — often more precise than any public feature list.

## Security-model read for AI-agent file/device access
Look for (usually under a `policy/` directory or similarly named module):
1. A static denylist of filenames/extensions/substrings (secrets, credential files, dangerous
   executable extensions).
2. Platform-specific path protection (OS system directories, reserved device names on Windows).
3. Path canonicalization: `realpath`-then-compare, not `path.startsWith()` (the latter is the
   classic `/home/user` vs `/home/user2` false-pass bug); check whether every path *component* is
   checked for symlinks, not just the final target.

Missing layer 3, or using string-prefix containment instead of real relative-path math, is a
findable, nameable security bug — call it out explicitly if present.

---

# CO-STAR build-prompt skeleton (step 6 output)

Use this to turn a finished teardown into a prompt you hand to a coding agent to scope a new
build in the same category.

```
## C — Context
I want to build <category/product type>: <one or two sentences on what it does for the user>.
I reverse-engineered an existing product in this category (<name>) down to its architecture, and
want to build toward the category using the patterns it proved out, not clone its UI. Here is
what the teardown found, which should directly shape the technical plan:

1. <Takeaway 1, phrased as a requirement: "X is mandatory, not optional, because...">
2. <Takeaway 2>
3. <Takeaway 3>
... (4-6 takeaways total, strongest first)

## O — Objective
<What a working first version needs to do, concretely.>

## S — Style
<e.g. "production-grade, not a demo" / "optimize for solo-maintainer simplicity">

## T — Tone
<e.g. "pragmatic, call out trade-offs rather than picking one silently">

## A — Audience
<Who reviews/uses the output of this prompt — you, a team, an investor-facing demo, etc.>

## R — Response
<What you want back: an architecture doc, a task breakdown, working code, a build-vs-buy
recommendation, etc.>
```
