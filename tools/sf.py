import sys, os, re, json, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "registry", "skills.jsonl")
DOM = os.path.join(ROOT, "registry", "domains.jsonl")
MAC = os.path.join(ROOT, "registry", "macros.json")
SK = os.path.join(ROOT, "skills")
TESTS = os.path.join(ROOT, "tests")
STATUSES = ["planned", "written", "validated", "audited", "failed"]
FM_KEYS = ["id", "name", "domain", "subdomain", "version", "description", "triggers", "not_for", "requires", "risk_level"]
LIST_KEYS = {"triggers", "not_for", "requires"}
SECTIONS = ["Purpose", "Inputs to collect", "Procedure", "Decision rules", "Output template", "Quality checklist", "Anti-patterns", "Worked example", "Edge cases", "Test case"]
VENDORS = re.compile(r"\b(GPT[-\s]?\d*|ChatGPT|OpenAI|Claude|Anthropic|DeepSeek|Gemini|Llama|Qwen|Mistral|Copilot)\b")
ID_RE = re.compile(r"^[A-Z]{2,4}-\d{3}$")
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def load(p):
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def save(p, rows):
    with open(p, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def macros():
    if not os.path.exists(MAC):
        return []
    with open(MAC, encoding="utf-8") as f:
        return json.load(f)


def spath(r):
    return os.path.join(SK, r["domain_code"], r["name"], "SKILL.md")


def short(r):
    return json.dumps({k: r.get(k) for k in ["id", "name", "domain_code", "subdomain", "risk_level", "requires", "description", "status"]}, ensure_ascii=False)


def parse(text):
    if not text.startswith("---\n"):
        return None, text, ["missing frontmatter start"]
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, text, ["missing frontmatter end"]
    fm, errs, order = {}, [], []
    for ln in text[4:end].split("\n"):
        if not ln.strip():
            continue
        if ":" not in ln:
            errs.append(f"bad frontmatter line: {ln[:60]}")
            continue
        k, v = ln.split(":", 1)
        k, v = k.strip(), v.strip()
        order.append(k)
        if k in LIST_KEYS:
            try:
                v = json.loads(v)
                if not isinstance(v, list):
                    raise ValueError
            except Exception:
                errs.append(f"{k} must be a JSON array of double-quoted strings")
                v = []
        else:
            v = v.strip('"').strip("'")
        fm[k] = v
    if order[: len(FM_KEYS)] != FM_KEYS and set(FM_KEYS) <= set(order):
        errs.append("frontmatter keys out of order")
    return fm, text[end + 5 :], errs


def sections(body):
    out, cur, fence = {}, None, False
    for ln in body.split("\n"):
        if re.match(r"^\s*(```|~~~)", ln):
            fence = not fence
        m = None if fence else re.match(r"^## (.+?)\s*$", ln)
        if m:
            cur = m.group(1).strip()
            out.setdefault(cur, [])
            continue
        if cur:
            out[cur].append(ln)
    return {k: "\n".join(v) for k, v in out.items()}


def heads(body):
    return list(sections(body).keys())


def validate_text(text, path, reg=None):
    E, W = [], []
    fm, body, pe = parse(text)
    E += pe
    if fm is None:
        return E, W, None
    for k in FM_KEYS:
        if k not in fm or fm[k] in ("", None):
            E.append(f"frontmatter missing: {k}")
    sid, name = fm.get("id", ""), fm.get("name", "")
    if sid and not ID_RE.match(sid):
        E.append(f"bad id format: {sid}")
    if name and (not NAME_RE.match(name) or len(name) > 64):
        E.append(f"bad name: {name}")
    if path and name and os.path.basename(os.path.dirname(path)) != name and os.path.basename(path) == "SKILL.md":
        E.append("folder name != frontmatter name")
    d = fm.get("description", "")
    if len(d) > 350:
        W.append("description over 350 chars")
    if len(re.findall(r"[.!?](\s|$)", d)) > 1:
        W.append("description looks like more than one sentence")
    t, n, r = fm.get("triggers", []), fm.get("not_for", []), fm.get("requires", [])
    if not 5 <= len(t) <= 10:
        E.append(f"triggers count {len(t)} (need 5-10)")
    if not 2 <= len(n) <= 5:
        E.append(f"not_for count {len(n)} (need 2-5)")
    rl = fm.get("risk_level", "")
    if rl not in ("low", "medium", "high"):
        E.append(f"bad risk_level: {rl}")
    if reg is not None and sid:
        row = reg.get(sid)
        if not row:
            E.append(f"id {sid} not in registry")
        else:
            if row["name"] != name:
                E.append(f"name differs from registry ({row['name']})")
            for q in r:
                if q not in reg:
                    W.append(f"requires unknown id {q}")
    if not re.search(r"^# \S", body, re.M):
        E.append("missing H1 title")
    h = heads(body)
    missing = [s for s in SECTIONS if s not in h]
    if missing:
        E.append("missing sections: " + ", ".join(missing))
    elif [x for x in h if x in SECTIONS] != SECTIONS:
        E.append("sections out of order")
    S = sections(body)
    if "```" not in S.get("Output template", ""):
        E.append("Output template has no code block")
    nif = len(re.findall(r"^- IF ", S.get("Decision rules", ""), re.M))
    if nif < 3:
        E.append(f"decision rules: {nif} IF lines (need >=3)")
    nq = len(re.findall(r"^- \[ \]", S.get("Quality checklist", ""), re.M))
    if not 6 <= nq <= 10:
        E.append(f"quality checklist items {nq} (need 6-10)")
    na = len(re.findall(r"^- \*\*", S.get("Anti-patterns", ""), re.M))
    if not 4 <= na <= 8:
        E.append(f"anti-patterns {na} (need 4-8)")
    we = S.get("Worked example", "")
    for tag in ("**Input:**", "**Output:**", "**Bad output:**"):
        if tag not in we:
            E.append(f"worked example missing {tag}")
    ne = len(re.findall(r"^- ", S.get("Edge cases", ""), re.M))
    if not 3 <= ne <= 6:
        E.append(f"edge cases {ne} (need 3-6)")
    tc = S.get("Test case", "")
    if "**Input:**" not in tc or "**Assertions:**" not in tc:
        E.append("test case needs **Input:** and **Assertions:**")
    else:
        nas = len(re.findall(r"^\d+\. ", tc.split("**Assertions:**", 1)[1], re.M))
        if not 3 <= nas <= 5:
            E.append(f"assertions {nas} (need 3-5)")
    if "⚠️" not in S.get("Procedure", ""):
        W.append("procedure has no ⚠️ step")
    wc = len(re.findall(r"\S+", body))
    if wc > 2200:
        E.append(f"body {wc} words (max 2200, target <=1800)")
    elif wc > 1800:
        W.append(f"body {wc} words (target <=1800)")
    elif wc < 500:
        W.append(f"body only {wc} words (thin)")
    vm = set(m.group(0) for m in VENDORS.finditer(body))
    if vm:
        W.append("vendor/model names: " + ", ".join(sorted(vm)))
    if rl == "high":
        lb = body.lower()
        if not ("licensed" in lb or "professional" in lb):
            E.append("high risk: no professional-referral boundary")
        if not ("verify" in lb or "cutoff" in lb):
            E.append("high risk: no verify/cutoff instruction")
        if not ("jurisdiction" in lb or "country" in lb or "state" in lb):
            W.append("high risk: no jurisdiction/country input")
    return E, W, fm


def cmd_status(a):
    R = load(REG)
    c = {s: 0 for s in STATUSES}
    for r in R:
        c[r.get("status", "planned")] = c.get(r.get("status", "planned"), 0) + 1
    print(f"macros: {len(macros())}  domains: {len(load(DOM))}  skills: {len(R)}")
    print("  ".join(f"{k}: {v}" for k, v in c.items()))


def cmd_macros(a):
    D = load(DOM)
    for m in macros():
        n = sum(1 for d in D if d["macro"] == m)
        print(f"{'DONE' if n else 'TODO'}  {n:>2}  {m}")


def cmd_codes(a):
    for d in load(DOM):
        print(f"{d['code']}\t{d['name']}\t[{d['macro']}]")


def cmd_next(a):
    n, st, dom = 5, "planned", None
    i = 0
    while i < len(a):
        if a[i] == "--status":
            st = a[i + 1]; i += 2
        elif a[i] == "--domain":
            dom = a[i + 1]; i += 2
        else:
            n = int(a[i]); i += 1
    rows = [r for r in load(REG) if r.get("status") == st and (dom is None or r["domain_code"] == dom)]
    if not rows:
        print("NONE"); return
    if dom is None and st == "planned":
        first = rows[0]["domain_code"]
        rows = [r for r in rows if r["domain_code"] == first]
    for r in rows[:n]:
        print(short(r))
        print("   path:", os.path.relpath(spath(r), ROOT))


def cmd_show(a):
    reg = {r["id"]: r for r in load(REG)}
    for i in a:
        print(short(reg[i]) if i in reg else f"{i}: not found")


def cmd_mark(a):
    st, ids = a[0], set(a[1:])
    if st not in STATUSES:
        sys.exit(f"status must be one of {STATUSES}")
    R = load(REG)
    k = 0
    for r in R:
        if r["id"] in ids:
            r["status"] = st; k += 1
    save(REG, R)
    print(f"marked {k} as {st}")


def cmd_remaining(a):
    kind = a[0]
    if kind == "taxonomy":
        D = load(DOM)
        print(sum(1 for m in macros() if not any(d["macro"] == m for d in D)))
    elif kind == "generate":
        print(sum(1 for r in load(REG) if r.get("status") in ("planned", "written")))
    elif kind == "audit":
        print(sum(1 for r in load(REG) if r.get("status") in ("validated", "failed")))
    else:
        sys.exit("kind: taxonomy | generate | audit")


def cmd_check_registry(a):
    D, R = load(DOM), load(REG)
    E = []
    codes = {}
    ms = set(macros())
    for d in D:
        for k in ("code", "name", "macro", "scope", "subdomains"):
            if k not in d:
                E.append(f"domain {d.get('code')} missing {k}")
        if not re.match(r"^[A-Z]{2,4}$", d.get("code", "")):
            E.append(f"bad domain code {d.get('code')}")
        if d.get("code") in codes:
            E.append(f"duplicate domain code {d['code']}")
        codes[d.get("code")] = d
        if d.get("macro") not in ms:
            E.append(f"domain {d.get('code')} macro not in macros.json: {d.get('macro')}")
    ids, names = set(), set()
    for r in R:
        for k in ("id", "name", "domain_code", "subdomain", "description", "risk_level", "requires", "status"):
            if k not in r:
                E.append(f"skill {r.get('id')} missing {k}")
        if not ID_RE.match(r.get("id", "")):
            E.append(f"bad id {r.get('id')}")
        elif r["id"].split("-")[0] != r.get("domain_code"):
            E.append(f"{r['id']} prefix != domain_code {r.get('domain_code')}")
        if r.get("domain_code") not in codes:
            E.append(f"{r.get('id')} unknown domain {r.get('domain_code')}")
        if r.get("id") in ids:
            E.append(f"duplicate id {r['id']}")
        if r.get("name") in names:
            E.append(f"duplicate name {r['name']}")
        if not NAME_RE.match(r.get("name", "")):
            E.append(f"bad name {r.get('name')}")
        if r.get("status") not in STATUSES:
            E.append(f"{r.get('id')} bad status")
        ids.add(r.get("id")); names.add(r.get("name"))
    for r in R:
        for q in r.get("requires", []):
            if q not in ids:
                E.append(f"{r['id']} requires unknown {q}")
    print("\n".join(E) if E else f"OK  domains={len(D)} skills={len(R)}")
    sys.exit(1 if E else 0)


def cmd_validate(a):
    mark = "--mark" in a
    a = [x for x in a if x != "--mark"]
    R = load(REG)
    reg = {r["id"]: r for r in R}
    targets = []
    if a and a[0] == "--file":
        failed = 0
        for p in a[1:]:
            if not os.path.isfile(p):
                print(f'FAIL {p}: file missing')
                failed += 1
                continue
            with open(p, encoding="utf-8") as f:
                E, W, _ = validate_text(f.read(), p, None)
            failed += bool(E)
            print(("PASS " if not E else "FAIL ") + p)
            for e in E: print("   E:", e)
            for w in W: print("   W:", w)
        sys.exit(1 if failed else 0)
    unknown = []
    if a and a[0] == "--all":
        targets = [r for r in R if os.path.exists(spath(r))]
    elif a and a[0] == "--domain":
        targets = [r for r in R if r["domain_code"] == a[1] and os.path.exists(spath(r))]
    else:
        targets = [reg[i] for i in a if i in reg]
        for i in a:
            if i not in reg:
                print(f"FAIL {i}: not in registry")
                unknown.append(i)
    bad, ok = 0, []
    for r in targets:
        p = spath(r)
        if not os.path.exists(p):
            print(f"FAIL {r['id']}: file missing {os.path.relpath(p, ROOT)}"); bad += 1; continue
        with open(p, encoding="utf-8") as f:
            E, W, _ = validate_text(f.read(), p, reg)
        print(("PASS " if not E else "FAIL ") + r["id"])
        for e in E: print("   E:", e)
        for w in W: print("   W:", w)
        if E: bad += 1
        else: ok.append(r["id"])
    if mark and ok:
        for r in R:
            if r["id"] in ok and r.get("status") in ("planned", "written", "failed"):
                r["status"] = "validated"
        save(REG, R)
        print(f"marked {len(ok)} validated (audited ones unchanged)")
    print(f"{len(targets) - bad}/{len(targets)} passed")
    sys.exit(1 if bad or unknown else 0)


def fm_of(r):
    p = spath(r)
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as f:
        fm, _, _ = parse(f.read())
    return fm


def esc(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def cmd_index(a):
    D = {d["code"]: d for d in load(DOM)}
    R = load(REG)
    codes = list(D) if (a and a[0] == "--all") else a
    for c in codes:
        d = D.get(c)
        if not d:
            print(f"{c}: unknown"); continue
        rows = [r for r in R if r["domain_code"] == c]
        out = [f"# {d['name']} ({c})", "", d["scope"], "", f"Macro-area: {d['macro']}", "", "Pick the skill whose triggers best match the request. If none match, use the closest description; if still none, answer without a skill.", "", "| ID | Skill | Use when | Example triggers | Status |", "|---|---|---|---|---|"]
        for r in rows:
            fm = fm_of(r) or {}
            trig = "; ".join(fm.get("triggers", [])[:3]) if fm else ""
            out.append(f"| {r['id']} | [{r['name']}]({r['name']}/SKILL.md) | {esc(fm.get('description', r['description']))} | {esc(trig)} | {r['status']} |")
        os.makedirs(os.path.join(SK, c), exist_ok=True)
        with open(os.path.join(SK, c, "INDEX.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(out) + "\n")
        print(f"wrote skills/{c}/INDEX.md ({len(rows)} skills)")


def cmd_router(a):
    D, R = load(DOM), load(REG)
    out = ["# ROUTER", "", "Load this first. Find the macro-area, then the domain, then open that domain's INDEX.md to choose one skill. Load only the chosen SKILL.md.", ""]
    for m in macros():
        ds = [d for d in D if d["macro"] == m]
        if not ds:
            continue
        out.append(f"## {m}")
        for d in ds:
            n = sum(1 for r in R if r["domain_code"] == d["code"])
            out.append(f"- **{d['code']}** {d['name']} ({n}) — {d['scope']} → `skills/{d['code']}/INDEX.md`")
        out.append("")
    with open(os.path.join(ROOT, "ROUTER.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"wrote ROUTER.md ({len(D)} domains, {len(re.findall(r'\S+', ' '.join(out)))} words)")


def cmd_testpack(a):
    reg = {r["id"]: r for r in load(REG)}
    for i in a:
        r = reg.get(i)
        if not r or not os.path.exists(spath(r)):
            print(f"{i}: missing"); continue
        with open(spath(r), encoding="utf-8") as f:
            text = f.read()
        tc = sections(parse(text)[1]).get("Test case", "")
        if "**Assertions:**" not in tc:
            print(f"{i}: no test case"); continue
        inp, asr = tc.split("**Assertions:**", 1)
        inp = "\n".join(l[2:] if l.startswith("> ") else l.lstrip(">") for l in inp.replace("**Input:**", "").strip().split("\n")).strip()
        d = os.path.join(TESTS, i)
        os.makedirs(os.path.join(d, "results"), exist_ok=True)
        with open(os.path.join(d, "PROMPT.md"), "w", encoding="utf-8") as f:
            f.write("Follow the skill below exactly to handle the user request at the end.\n\n<skill>\n" + text.strip() + "\n</skill>\n\n<user_request>\n" + inp + "\n</user_request>\n")
        with open(os.path.join(d, "ASSERTIONS.md"), "w", encoding="utf-8") as f:
            f.write(f"# {i} assertions\n\n" + asr.strip() + "\n")
        print(f"wrote tests/{i}/PROMPT.md, ASSERTIONS.md; save model outputs to tests/{i}/results/<model>.md")


def cmd_export(a):
    dest = os.path.abspath(a[0] if a else os.path.join(ROOT, "dist", "claude-skills"))
    k = 0
    for r in load(REG):
        if r.get("status") not in ("validated", "audited") or not os.path.exists(spath(r)):
            continue
        with open(spath(r), encoding="utf-8") as f:
            fm, body, _ = parse(f.read())
        meta = "\n".join(f"- {key}: {json.dumps(fm[key], ensure_ascii=False) if key in LIST_KEYS else fm[key]}" for key in FM_KEYS if key not in ("name", "description"))
        o = os.path.join(dest, r["name"])
        os.makedirs(o, exist_ok=True)
        with open(os.path.join(o, "SKILL.md"), "w", encoding="utf-8") as f:
            f.write(f"---\nname: {fm['name']}\ndescription: {json.dumps(fm['description'], ensure_ascii=False)}\n---\n" + body.rstrip() + "\n\n## Metadata\n" + meta + "\n")
        k += 1
    print(f"exported {k} skills to {dest}")


def cmd_ingest(a):
    """Append reviewed author manifests without concurrent registry writers."""
    existing_d, existing_r = load(DOM), load(REG)
    domains = {r['code']: r for r in existing_d}
    skills = {r['id']: r for r in existing_r}
    names = {r['name']: r['id'] for r in existing_r}
    additions_d, additions_r = [], []
    for path in a:
        with open(path, encoding='utf-8-sig') as stream:
            batch = json.load(stream)
        for row in batch['domains']:
            code = row['code']
            if code in domains:
                if domains[code] != row:
                    sys.exit(f'FAIL conflicting domain {code}')
                continue
            if not re.fullmatch(r'[A-Z]{2,4}', code) or row['macro'] not in macros():
                sys.exit(f'FAIL invalid domain {code}')
            if not all(k in row for k in ['name', 'scope', 'subdomains']):
                sys.exit(f'FAIL incomplete domain {code}')
            domains[code] = row
            additions_d.append(row)
        for row in batch['skills']:
            sid, name = row['id'], row['name']
            if sid in skills:
                if any(skills[sid].get(k) != row.get(k) for k in ['name', 'domain_code', 'subdomain']):
                    sys.exit(f'FAIL conflicting skill {sid}')
                continue
            if not ID_RE.fullmatch(sid) or not NAME_RE.fullmatch(name) or len(name) > 64:
                sys.exit(f'FAIL invalid skill {sid}')
            if name in names or row['domain_code'] not in domains or sid.split('-')[0] != row['domain_code']:
                sys.exit(f'FAIL duplicate name or invalid domain {sid}')
            if row.get('status') != 'planned' or row.get('risk_level') not in ['low', 'medium', 'high']:
                sys.exit(f'FAIL invalid initial state {sid}')
            if not all(k in row for k in ['description', 'subdomain', 'requires']):
                sys.exit(f'FAIL incomplete skill {sid}')
            names[name] = sid
            skills[sid] = row
            additions_r.append(row)
    for row in additions_r:
        if any(sid not in skills for sid in row['requires']):
            sys.exit(f"FAIL missing prerequisite for {row['id']}")
    for path, rows in [(DOM, additions_d), (REG, additions_r)]:
        with open(path, 'a', encoding='utf-8') as stream:
            for row in rows:
                stream.write(json.dumps(row, ensure_ascii=False) + '\n')
    print(f'ingested domains={len(additions_d)} skills={len(additions_r)}')


def cmd_quality(a):
    """Mechanical quality gates; these do not replace substantive review."""
    import hashlib
    rows = load(REG)
    reg = {r['id']: r for r in rows}
    domains = {d['code']: d for d in load(DOM)}
    failures, fingerprints, counts = [], {}, []
    selected = rows if not a or a == ['--all'] else [reg[sid] for sid in a]
    for row in selected:
        path = spath(row)
        if not os.path.isfile(path):
            failures.append(f"{row['id']}: missing skill")
            continue
        with open(path, encoding='utf-8') as stream:
            content = stream.read()
        errors, warnings, fm = validate_text(content, path, reg)
        failures.extend(f"{row['id']}: {err}" for err in errors)
        if not fm:
            continue
        _, body, _ = parse(content)
        words = len(re.findall(r'\S+', body))
        counts.append(words)
        if not 700 <= words <= 1800:
            failures.append(f"{row['id']}: {words} words, expected 700-1800")
        sec = sections(body)
        example = sec.get('Worked example', '')
        if 'fictional' not in example.lower():
            failures.append(f"{row['id']}: worked example lacks an explicit fictional label")
        template_fences = re.findall(r'```[^\n]*\n(.*?)```', sec.get('Output template', ''), re.S)
        example_output = example.split('**Output:**', 1)[-1].split('**Bad output:**', 1)[0]
        example_fences = re.findall(r'```[^\n]*\n(.*?)```', example_output, re.S)
        if template_fences and example_fences:
            labels = re.findall(r'^(?:## [^\n]+|[A-Za-z][A-Za-z -]+:)', template_fences[0], re.M)
            position = -1
            for label in labels:
                found = example_fences[0].find(label, position + 1)
                if found < 0:
                    failures.append(f"{row['id']}: worked example missing or reorders output label {label}")
                    break
                position = found
        for name in ['Procedure', 'Worked example', 'Test case']:
            signature = hashlib.sha256(re.sub(r'\s+', ' ', sec.get(name, '')).encode()).hexdigest()
            key = (name, signature)
            if key in fingerprints:
                failures.append(f"{row['id']}: identical {name} to {fingerprints[key]}")
            fingerprints[key] = row['id']
        if fm.get('risk_level') != row['risk_level']:
            failures.append(f"{row['id']}: risk differs from registry")
        if fm.get('domain') != domains.get(row['domain_code'], {}).get('name'):
            failures.append(f"{row['id']}: domain name differs from registry")
        if fm.get('subdomain') != row['subdomain']:
            failures.append(f"{row['id']}: subdomain differs from registry")
        if set(fm.get('requires', [])) != set(row.get('requires', [])):
            failures.append(f"{row['id']}: prerequisites differ from registry")
        for exclusion in fm.get('not_for', []):
            for target in re.findall(r'\[([A-Z]{2,4}-\d{3})\]', exclusion):
                if target not in reg:
                    failures.append(f"{row['id']}: unknown routing reference {target}")
    print('\n'.join(failures) if failures else f'QUALITY PASS {len(selected)} skills; structural, length, exact-duplicate gates')
    if counts:
        print(f'body words: min={min(counts)} max={max(counts)} total={sum(counts)}')
    print('Substantive accuracy and behavioral reliability require review; this command does not mark audited.')
    sys.exit(1 if failures else 0)


def cmd_coverage(a):
    """Report observed on-disk coverage without silently marking statuses."""
    rows, domains = load(REG), load(DOM)
    for d in domains:
        selected = [r for r in rows if r['domain_code'] == d['code']]
        present = sum(os.path.isfile(spath(r)) for r in selected)
        ready = sum(r['status'] in ['validated', 'audited'] and os.path.isfile(spath(r)) for r in selected)
        print(f"{d['code']}: files={present} validated_or_audited={ready} planned_total={len(selected)} {d['name']}")
    print(f"TOTAL files={sum(os.path.isfile(spath(r)) for r in rows)} registered={len(rows)} domains={len(domains)}")


def cmd_overlap(a):
    """Print lexical routing candidates for human review, not duplicate verdicts."""
    import itertools
    stop = {'review','plan','planning','design','preparation','prepare','map','mapping','evidence','draft','drafting','brief','briefing','in','us','startup','business','search','administrative'}
    records = []
    for row in load(REG):
        words = set(row['name'].split('-')) - stop
        records.append((row, words))
    found = []
    for (left, lw), (right, rw) in itertools.combinations(records, 2):
        if left['domain_code'] == right['domain_code'] or not lw or not rw:
            continue
        similarity = len(lw & rw) / len(lw | rw)
        if similarity >= 0.6:
            found.append((similarity,left,right))
    for score,left,right in sorted(found,key=lambda item:(-item[0],item[1]['id'])):
        print(f"REVIEW {score:.2f} {left['id']} {left['name']} <> {right['id']} {right['name']}")
    print(f'{len(found)} lexical cross-domain candidates; semantic review required')


def cmd_package(a):
    """Create a deterministic portable archive from validated source skills."""
    import zipfile
    import hashlib
    destination = os.path.abspath(a[0] if a else os.path.join(ROOT, 'dist', 'portable-skills.zip'))
    rows = [r for r in load(REG) if r['status'] in ['validated', 'audited']]
    reg = {r['id']: r for r in load(REG)}
    contents = []
    for row in rows:
        path = spath(row)
        if not os.path.isfile(path):
            sys.exit(f"FAIL {row['id']}: file missing")
        with open(path, encoding='utf-8') as stream:
            original = stream.read()
        errors, _, fm = validate_text(original, path, reg)
        if errors:
            sys.exit(f"FAIL {row['id']}: {'; '.join(errors)}")
        _, body, _ = parse(original)
        metadata = '\n'.join(f'- {key}: {json.dumps(fm[key], ensure_ascii=False) if key in LIST_KEYS else fm[key]}' for key in FM_KEYS if key not in ('name','description'))
        content = f"---\nname: {fm['name']}\ndescription: {json.dumps(fm['description'], ensure_ascii=False)}\n---\n" + body.rstrip() + '\n\n## Metadata\n' + metadata + '\n'
        contents.append((f"{row['name']}/SKILL.md", content.encode('utf-8')))
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    with zipfile.ZipFile(destination, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for name, content in sorted(contents):
            info = zipfile.ZipInfo(name, date_time=(1980,1,1,0,0,0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, content)
    with zipfile.ZipFile(destination) as archive:
        if archive.testzip() is not None or len(archive.namelist()) != len(rows):
            sys.exit('FAIL archive verification')
    with open(destination, 'rb') as stream:
        digest = hashlib.sha256(stream.read()).hexdigest()
    print(f'packaged {len(rows)} skills to {destination}')
    print(f'archive integrity PASS; sha256={digest}')


def cmd_sync_metadata(a):
    """Synchronize reviewed metadata from files while preserving identity and status."""
    rows = load(REG)
    known_ids = {r['id'] for r in rows}
    domains = {d['code']: d for d in load(DOM)}
    selected = set(a)
    changed = 0
    for row in rows:
        if selected and row['domain_code'] not in selected and row['id'] not in selected:
            continue
        fm = fm_of(row)
        if not fm or fm.get('id') != row['id'] or fm.get('name') != row['name']:
            sys.exit(f"FAIL metadata identity mismatch {row['id']}")
        if fm.get('domain') != domains[row['domain_code']]['name']:
            sys.exit(f"FAIL metadata domain mismatch {row['id']}")
        if fm.get('risk_level') not in ('low', 'medium', 'high'):
            sys.exit(f"FAIL metadata risk invalid {row['id']}")
        for key in ('description','subdomain','risk_level','requires'):
            if key not in fm:
                sys.exit(f"FAIL missing metadata {row['id']}: {key}")
        updated = {key: fm[key] for key in ('description','subdomain','risk_level','requires')}
        if any(sid not in known_ids for sid in updated['requires']):
            sys.exit(f"FAIL metadata unknown prerequisite {row['id']}")
        if any(row.get(key) != value for key,value in updated.items()):
            row.update(updated)
            changed += 1
    save(REG, rows)
    print(f'synchronized metadata for {changed} skills; identities and statuses unchanged')


def cmd_search(a):
    """Bounded local discovery without dumping the registry."""
    if not a:
        sys.exit('usage: sf.py search <task words>')
    query = ' '.join(a).lower()
    aliases = {'seo': 'search', 'bureaucracy': 'administrative', 'government': 'administrative', 'datasets': 'dataset', 'hackathons': 'hackathon'}
    terms = set(re.findall(r'[a-z0-9]+', query))
    terms |= {aliases[t] for t in list(terms) if t in aliases}
    domains = {d['code']: d for d in load(DOM)}
    matches = []
    for row in load(REG):
        title = row['name'].replace('-', ' ')
        context = ' '.join([row['description'], row['subdomain'], domains[row['domain_code']]['name']]).lower()
        score = sum(3 for term in terms if term in title) + sum(1 for term in terms if term in context)
        if score:
            matches.append((score, row))
    for score, row in sorted(matches, key=lambda item: (-item[0], item[1]['id']))[:10]:
        print(short(row))
        print('   path:', os.path.relpath(spath(row), ROOT))
    print(f'{min(len(matches),10)} shown of {len(matches)} lexical matches; narrow the query for a specific task')


CMDS = {"status": cmd_status, "macros": cmd_macros, "codes": cmd_codes, "next": cmd_next, "show": cmd_show, "mark": cmd_mark, "remaining": cmd_remaining, "check-registry": cmd_check_registry, "validate": cmd_validate, "index": cmd_index, "router": cmd_router, "testpack": cmd_testpack, "export": cmd_export, "ingest": cmd_ingest, "quality": cmd_quality, "coverage": cmd_coverage, "overlap": cmd_overlap, "package": cmd_package, "sync-metadata": cmd_sync_metadata, "search": cmd_search}

def cmd_migration_check(a):
    """Check source coverage and destination integrity without copying source text."""
    import hashlib
    from pathlib import Path
    removed = bool(a and a[0] == '--removed')
    if removed:
        a = a[1:]
    if len(a) < 2:
        sys.exit('usage: migration-check <source-folder> <mapping.json>... | --removed <source-folder> <receipt.json>')
    source = Path(a[0]).resolve()
    reg = {r['id']: r for r in load(REG)}
    if removed:
        with open(a[1], encoding='utf-8') as stream:
            receipt = json.load(stream)
        if str(source) != receipt['source_folder'] or source.exists():
            sys.exit('FAIL original folder still exists or receipt identifies another folder')
        for sid, digest in receipt['targets'].items():
            if sid not in reg or reg[sid]['status'] not in ('validated', 'audited'):
                sys.exit(f'FAIL unavailable target {sid}')
            path = Path(spath(reg[sid]))
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                sys.exit(f'FAIL target changed or missing {sid}')
        print(f"REMOVAL VERIFIED: original folder absent; {len(receipt['sources'])} source workflows mapped; {len(receipt['targets'])} destination skills intact")
        return
    if not source.is_dir():
        sys.exit('FAIL source folder missing')
    files = {p.parent.name: p for p in source.glob('*/SKILL.md')}
    if not files:
        sys.exit('FAIL no source skills found')
    mappings, targets = {}, {}
    for manifest in a[1:]:
        with open(manifest, encoding='utf-8') as stream:
            entries = json.load(stream)
        for entry in entries:
            name = entry['source']
            if name in mappings or name not in files:
                sys.exit(f'FAIL duplicate or unknown source {name}')
            if entry.get('disposition') not in ('new', 'covered', 'merged') or not entry.get('rationale') or not entry.get('targets'):
                sys.exit(f'FAIL incomplete mapping {name}')
            for sid in entry['targets']:
                if sid not in reg or reg[sid]['status'] not in ('validated', 'audited'):
                    sys.exit(f'FAIL target not ready {name}: {sid}')
                path = Path(spath(reg[sid]))
                if not path.is_file():
                    sys.exit(f'FAIL missing target file {sid}')
                errors, _, _ = validate_text(path.read_text(encoding='utf-8'), str(path), reg)
                if errors:
                    sys.exit(f'FAIL invalid target {sid}: {errors}')
                targets[sid] = hashlib.sha256(path.read_bytes()).hexdigest()
            mappings[name] = entry
    missing = sorted(set(files) - set(mappings))
    if missing:
        sys.exit('FAIL unmapped sources: ' + ', '.join(missing))
    receipt = dict(source_folder=str(source), sources={name: hashlib.sha256(path.read_bytes()).hexdigest() for name,path in files.items()}, targets=targets, mappings=list(mappings.values()))
    destination = Path(ROOT) / 'logs' / 'claude-migration-verification.json'
    destination.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    report = ['# Portable workflow migration', '',
              'Each source workflow was compared with the library. New procedures fill gaps; covered or merged entries reuse existing destinations. Source-specific names, business details, changing rates, unsupported thresholds, and vendor-only invocation commands were not carried into the portable skills.', '',
              'This table records the human comparison decisions and verified destination files. Structural validation is not proof of identical behavior or professional certification. Detailed reviews: [technical](claude-comparison-technical.md), [operations](claude-comparison-operations.md), [business](claude-comparison-business.md).', '',
              '| Source folder | Disposition | Portable destinations | Reason |', '|---|---|---|---|']
    for name, entry in sorted(mappings.items()):
        links = ', '.join(f"[{sid}](../skills/{reg[sid]['domain_code']}/{reg[sid]['name']}/SKILL.md)" for sid in entry['targets'])
        report.append(f"| {name} | {entry['disposition']} | {links} | {entry['rationale'].replace('|', '/')} |")
    (Path(ROOT) / 'logs' / 'claude-migration.md').write_text('\n'.join(report) + '\n', encoding='utf-8')
    print(f'MIGRATION PASS: {len(files)} source workflows mapped to {len(targets)} validated destination skills')
    print('Saved logs/claude-migration-verification.json and logs/claude-migration.md; source content not copied. Semantic equivalence is documented in the review reports.')


CMDS['migration-check'] = cmd_migration_check

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in CMDS:
        sys.exit("commands: " + " | ".join(CMDS))
    CMDS[sys.argv[1]](sys.argv[2:])
