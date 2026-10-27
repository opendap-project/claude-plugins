"""guard-commit.py: the PreToolUse hook that keeps commits on the local checks."""
import json
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

# Under a pre-commit hook git exports GIT_DIR and others; without them every fixture repository is its own.
ENV = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "guard-commit.py"


def run(command, cwd):
    data = json.dumps({"tool_input": {"command": command}, "cwd": str(cwd)})
    return subprocess.run([sys.executable, str(SCRIPT)], input=data, capture_output=True, text=True, env=ENV)


class GuardCommit(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = pathlib.Path(self.tmp.name)
        subprocess.run(["git", "init", "-q", str(self.repo)], check=True, env=ENV)

    def tearDown(self):
        self.tmp.cleanup()

    def test_no_verify_is_denied_with_the_reason_on_stderr(self):
        r = run("git commit --no-verify -m x", self.repo)
        self.assertEqual(r.returncode, 0)
        out = json.loads(r.stdout)["hookSpecificOutput"]
        self.assertEqual(out["permissionDecision"], "deny")
        self.assertIn("guard-commit: ", r.stderr)
        self.assertIn("git commit", r.stderr)

    def test_missing_pre_commit_says_what_to_run(self):
        (self.repo / ".pre-commit-config.yaml").write_text("repos: []\n")
        r = run("git commit -m x", self.repo)
        self.assertIn("pre-commit install", r.stderr)
        self.assertEqual(json.loads(r.stdout)["hookSpecificOutput"]["permissionDecision"], "deny")

    def test_other_commands_pass_silently(self):
        r = run("git status", self.repo)
        self.assertEqual((r.returncode, r.stdout, r.stderr), (0, "", ""))

    def test_unreadable_input_passes_with_a_message(self):
        r = subprocess.run([sys.executable, str(SCRIPT)], input="not json", capture_output=True, text=True)
        self.assertEqual((r.returncode, r.stdout), (0, ""))
        self.assertIn("guard-commit: ", r.stderr)


if __name__ == "__main__":
    unittest.main()
