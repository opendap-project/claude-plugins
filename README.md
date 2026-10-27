# Claude Plugins

Claude Code plugin marketplace for OpenDAP repositories.

Every OpenDAP repository enables the `opendap` plugin in its `.claude/settings.json`. Claude Code offers to install it the first time you trust the repository folder.

## Plugins

- `opendap`: project conventions for contributors.
  - `/opendap:requirement` records a requirement in `docs/requirements/`.
  - `/opendap:adr` records a decision in `docs/adr/`.
  - `/opendap:license-check` checks REUSE licensing.
  - `/opendap:export` generates a component's `export/` folder.
  - `/opendap:fab-package` builds a KiCad project's fab and assembly package locally.
  - A `PreToolUse` hook blocks `git commit --no-verify` and commits in clones without `pre-commit install`; it says on stderr what to run instead. Its tests (`plugins/opendap/tests`, standard library only) run in pre-commit.

Each skill applies a public specification or convention (the workspace `CONTRIBUTING.md`, the component export contract, REUSE) and points to it instead of copying it.

## Install manually

```sh
claude plugin marketplace add opendap-project/claude-plugins
claude plugin install opendap@opendap
```

## License

This repository follows the [REUSE](https://reuse.software) layout: license texts live in `LICENSES/` and `REUSE.toml` maps each path to its license.

- Default: **GNU GPL v3.0 or later** (`GPL-3.0-or-later`)
- Markdown files (including skills): **Creative Commons Attribution-ShareAlike 4.0** (`CC-BY-SA-4.0`)

Copyright © 2026 The OpenDAP Project.
