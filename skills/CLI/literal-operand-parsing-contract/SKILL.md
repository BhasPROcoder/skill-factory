---
id: CLI-002
name: literal-operand-parsing-contract
domain: Command-Line Interaction Contracts
subdomain: Argument grammar
version: 1.0
description: Specify how a command distinguishes options from literal operands when filenames, spaces, delimiters, and standard-input markers could otherwise change their meaning.
triggers: ["handle filenames starting with a dash", "design command operand parsing", "test CLI argument boundaries", "accept paths containing spaces", "define end of options behavior", "avoid ambiguous stdin operands"]
not_for: ["machine output stream design [CLI-001]", "effective configuration capture [TRP-006]", "shell-specific quoting reference", "executing untrusted shell text"]
requires: []
risk_level: medium
---

# Literal Operand Parsing Contract

## Purpose
Make the boundary between command syntax and user-supplied operands explicit so a filename cannot silently become an option or multiple inputs. The output is an argument grammar, ambiguity policy, and test vector set; shell-specific invocation still requires verification in the actual environment.

## Inputs to collect
1. **Command operations** — identify supported actions and whether they read or modify operands. This bounds the consequence of misparsing. Default: specification only; no file operations.
2. **Option grammar** — list known options, required values, repetition rules, and abbreviations if any. This defines syntax before operands. Default: no invented options or implicit abbreviations.
3. **Operand grammar** — identify positional roles, allowed counts, input markers, and literal-path rules. This determines what a token means. Default: unknown roles require clarification.
4. **Invocation boundary** — establish whether the command receives an argument vector from another program or text parsed by a shell. This separates command parsing from earlier tokenization. Default: reason about an argument vector and leave shell examples unverified.
5. **Parser evidence** — collect actual parser behavior, existing compatibility requirements, and available tests. This distinguishes proposed rules from implemented behavior. Default: proposed contract, not a claim about installed software.
6. **Special input policy** — define how standard input, missing operands, directories, and nonexisting paths are handled. This prevents overloaded meanings. Default: do not assume a special marker unless explicitly chosen by the contract.

If a required input is missing and has no safe default, ask in one message with at most 3 questions.

## Procedure
1. Represent example invocations as ordered token arrays before writing shell command strings. Each array element is one token received by the command; a space inside an element does not create another element.
2. Separate tokenization responsibilities from option parsing responsibilities. A shell may transform text before the command sees it; record which layer must preserve each intended operand.
3. Declare option syntax, value attachment rules, repeated-option handling, and rejection of unknown options. Do not guess how a parser handles an omitted option value.
4. ⚠️ Define an explicit transition from option parsing to literal operands when the command needs it. A double-hyphen delimiter is a possible chosen contract, not a universal claim that every command supports it.
5. Define how option-looking paths are represented and tested after that transition. Treat an unknown option before the boundary as an error if that is the agreed grammar, rather than silently opening a similarly named file.
6. Specify standard-input marker handling separately from option termination. If a standalone marker selects standard input, provide an unambiguous way to refer to a literal file with that name and document how multiple markers behave.
7. Define operand counts and roles before accessing files. An extra token should not silently change source, destination, or operation meaning.
8. ⚠️ Preserve literal values when passing tokens to a child process. Use the available process API's argument-vector capability where suitable; verify the actual runtime behavior rather than concatenating values into an unexamined shell string.
9. Build token-level tests for an ordinary path, a path containing spaces, an option-looking path, a literal marker name, missing option value, and unknown option. Include expected parsed roles or explicit rejection.
10. Test representative invocations in the intended shell and runtime only after token-level behavior is clear. Use `[VERIFY: quoting, argument passing, and parser behavior in the installed shell, runtime, and command documentation]` for environment-specific examples.
11. Deliver the grammar and evidence, identifying which tests were token-only and which crossed a real process boundary. Keep file modifications outside the parsing test unless separately authorized and isolated.

This Python 3 fixture implements a deliberately small fictional grammar: only the flag `--verbose` is accepted before `--`, and operands are accepted after it. It is not a production parser or a claim about another command's behavior. Save and run it with an available Python 3 interpreter, recording its version.

```python
def parse_tokens(tokens):
    literal = False
    verbose = False
    paths = []
    for token in tokens:
        if literal:
            paths.append(token)
        elif token == "--":
            literal = True
        elif token == "--verbose":
            verbose = True
        else:
            raise ValueError("unexpected token before operand boundary")
    if not literal or not paths:
        raise ValueError("expected delimiter followed by a path")
    return verbose, paths

assert parse_tokens(["--verbose", "--", "a b.txt", "-draft.txt"]) == (
    True, ["a b.txt", "-draft.txt"])
for invalid in (["--unknown"], ["--"], ["--verbose"]):
    try:
        parse_tokens(invalid)
    except ValueError:
        pass
    else:
        raise AssertionError("invalid invocation accepted")
print("Token boundary checks passed")
```

## Decision rules
- IF a path begins with option-like syntax THEN use the contract's literal-operand mechanism BECAUSE its spelling alone cannot determine whether it is data or syntax.
- IF an invocation is supplied as shell text THEN verify how it becomes tokens before diagnosing the command parser BECAUSE incorrect tokenization can occur before the command runs.
- IF a standalone token selects standard input THEN document a separate literal-path representation BECAUSE the same spelling must not ambiguously select both sources.
- IF an unknown option is received before the literal boundary THEN apply the explicit error policy BECAUSE silently treating mistakes as operands hides invocation errors.
- IF only token-level tests ran THEN label shell and subprocess behavior untested BECAUSE a correct token parser does not prove correct invocation through another layer.

## Output template
```text
Scope: <operation and invocation boundary; one sentence>
Grammar: <options, values, operand boundary, and positional roles; up to six lines>
Special inputs: <stdin, literal markers, empty input; up to four lines>
Token cases: <token array | expected roles or rejection; up to seven rows>
Invocation handling: <who preserves tokens and what needs verification; up to four lines>
Evidence: <performed checks and their limits, or pending>
Open questions: <up to three unresolved decisions>
```

## Quality checklist
- [ ] Token arrays distinguish spaces within an operand from token separators.
- [ ] Option syntax and option-value requirements are explicit.
- [ ] Literal-operand handling is a documented command contract.
- [ ] Unknown options have a deliberate outcome.
- [ ] Standard-input markers cannot silently collide with literal filenames.
- [ ] Operand counts and source/destination roles are checked before access.
- [ ] Shell and parser responsibilities are separated.
- [ ] Test evidence does not imply file execution or modification.

## Anti-patterns
- **Universal delimiter assumption**: Every command is presumed to support the same boundary. Fix: verify the target command or label the delimiter as a proposed grammar.
- **String assembly**: Paths are joined into shell text without preserving token boundaries. Fix: use and verify an argument-vector interface when appropriate.
- **Helpful typo acceptance**: An unknown option becomes a filename. Fix: define and test the error policy.
- **Marker collision**: A literal dash-named file accidentally selects standard input. Fix: specify and test a distinct literal path form.
- **Token-only overclaim**: A unit fixture is called cross-shell compatibility. Fix: report the tested boundary precisely.

## Worked example
**Input:**
Fictional utility Reed is designing a read-only file checker. Its proposed grammar accepts optional --verbose followed by a required -- delimiter and one or more path operands. It assigns no special meaning to a dash operand. An application supplies an argument vector containing a b.txt and -draft.txt. No real shell or filesystem test is available.

**Output:**
```text
Scope: Specify Reed's read-only checker using an application-supplied argument vector.
Grammar: Optional --verbose before required --; all following tokens are literal paths. At least one path is required. Unknown pre-boundary tokens are rejected. No abbreviations or option values are defined.
Special inputs: No stdin marker is defined; a dash after the boundary is a literal path. Missing path operands are rejected before file access.
Token cases: ["--", "a b.txt"] | one path named a b.txt
["--verbose", "--", "-draft.txt"] | verbose=true; one literal path -draft.txt
["--", "-"] | one literal dash-named path
["--unknown", "--", "x"] | reject unknown option
["--"] | reject missing path
Invocation handling: Calling application preserves each path as one argument. Shell-text quoting remains outside this token-level specification and needs environment-specific verification if later introduced.
Evidence: Proposed grammar only; no real parser, process invocation, file access, or shell compatibility test performed.
Open questions: Which runtime will implement the parser? What file-access failure policy should follow successful parsing?
```

**Bad output:**
“Join the arguments with spaces and run the string; every command treats -- as the end of options.”
This loses operand boundaries and asserts unsupported behavior across commands.

## Edge cases
- **Literal delimiter filename** — define how to represent the delimiter itself after the grammar has entered literal mode, then test that exact token sequence.
- **Repeated stdin marker** — reject or define sharing behavior explicitly; do not promise that separate consumers receive independent copies of one stream.
- **Option value looks like an option** — define attached-value or explicit-value syntax and test it rather than guessing parser intent.
- **Wrapper forwards arguments** — verify each forwarding boundary; a correctly parsed outer command does not prove the child receives identical tokens.

## Test case
**Input:**
> Fictional checker Hazel receives a list containing paths "two words.txt" and "--report". Its parser contract is not supplied. A teammate proposes joining the list with spaces and assuming that -- always protects filenames. Prepare a parsing contract review.

**Assertions:**
1. Preserves the two intended operands as distinct argument-vector elements.
2. Does not assume the target parser supports a delimiter without evidence.
3. Separates shell tokenization from option parsing.
4. Requests the missing grammar and avoids claiming file access was tested.
