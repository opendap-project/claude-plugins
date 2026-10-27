#!/usr/bin/env python3
"""Block git commits that would skip OpenDAP's local checks.

Denies a `git commit` when it passes --no-verify / -n, or when the target
repository has no pre-commit hook installed. Everything else passes through.
"""
import json, os, re, shlex, subprocess, sys

def deny(reason):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
        "permissionDecision": "deny", "permissionDecisionReason": reason}}))
    sys.exit(0)

data = json.load(sys.stdin)
cmd = (data.get("tool_input") or {}).get("command", "")
cwd = data.get("cwd") or os.getcwd()
for segment in re.split(r"&&|\|\||;|\n", cmd):
    try:
        words = shlex.split(segment)
    except ValueError:
        continue
    if "git" not in words:
        continue
    words = words[words.index("git"):]
    repo, i = cwd, 1
    while i < len(words) and words[i].startswith("-"):
        if words[i] == "-C" and i + 1 < len(words):
            repo = os.path.join(repo, words[i + 1]); i += 2
        elif words[i] in ("-c",):
            i += 2
        else:
            i += 1
    if i >= len(words) or words[i] != "commit":
        continue
    flags = words[i + 1:]
    if "--no-verify" in flags or any(re.fullmatch(r"-[a-zA-Z]*n[a-zA-Z]*", f) for f in flags):
        deny("OpenDAP: commits must run the local checks; do not use --no-verify.")
    try:
        hook = subprocess.run(["git", "-C", repo, "rev-parse", "--git-path", "hooks/pre-commit"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        continue
    if not os.path.isabs(hook):
        hook = os.path.join(repo, hook)
    if os.path.exists(os.path.join(repo, ".pre-commit-config.yaml")) and not os.path.exists(hook):
        deny(f"OpenDAP: pre-commit is not installed in {repo}. Run `pre-commit install` there first.")
sys.exit(0)
