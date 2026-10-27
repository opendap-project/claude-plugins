---
name: requirement
description: Add or update a requirement in an OpenDAP repository (docs/requirements/requirements.toml, or the README table where there is no TOML source). Use when the maintainers state something the project must or should achieve.
---

# Record a requirement

Requirements live in `docs/requirements/` of the repository they belong to. The format and the tool are in the [requirements as data](https://github.com/opendap-project/toolkit-host/blob/main/docs/specs/requirements-data.md) spec (`odapkit req`).

- **With `requirements.toml`** (the source): edit the TOML and render the README from it; never edit `README.md` by hand.
- **Without one:** edit the table in `docs/requirements/README.md`:

| ID | Requirement | Priority | Status |
|---|---|---|---|

1. **Pick the repository.** A requirement goes where it is implemented: product-level requirements and interfaces between components in `t1`, the physical case in `case`, electronics in `board`, the HAT interface in `hat-standard`, and so on. If it spans repositories, record it in each one, scoped to that repository.
2. **Only confirmed content.** Record what the maintainers stated. Do not add inferred details, numbers or wording. If something is needed but not stated, add it under `## Open questions` instead.
3. **ID.** Use the prefix registered for that requirements folder in the workspace [`id-prefixes.tsv`](https://github.com/opendap-project/workspace/blob/main/id-prefixes.tsv) (for example `BRD`, `CASE`, `HCS`; where a prefix has several rows, only the one noted `new ids` takes new ones) and the next free number, zero-padded to three digits. Never reuse or renumber an ID; mark a dropped requirement withdrawn instead of deleting it, and one that belongs elsewhere moved (with its new ID in the note).
4. **Wording.** One testable statement. Use "shall" for **must** and "should" for **should**.
5. **Status.** Confirmed when agreed; draft when the intent is agreed but the detail is still open.
6. **Write the record.**
   - TOML: add or edit a `[[block.requirement]]` record in the right table block, with `id`, `text`, `priority` (`must`, `should`), `status` (`confirmed`, `draft`, `withdrawn`, `moved`) and, when needed, `note` (rendered in parentheses after the status, for example the date and the requirement that replaces a withdrawn one). Prose (introduction, context, open questions) is in the `markdown` blocks. Then run `odapkit req render docs/requirements/requirements.toml`.
   - Table: add or edit the row; the status is capitalised (`Confirmed`, `Draft`, `Withdrawn`, `Moved`).
7. **Check.** Run `odapkit req prefixes` and `odapkit req refs` from the workspace; fix any error they report. Where the repository has a TOML source, its pre-commit runs `odapkit req render --check`.
8. If the `docs/requirements/` folder does not exist, create `README.md` with the heading `# <Project> requirements`, a one-line intro and the table above, link it from `docs/README.md`, and register the prefix in the workspace `id-prefixes.tsv`. To move it to a TOML source, run `odapkit req import docs/requirements/README.md --write` and add the pre-commit check.
9. Context that is not a requirement (ideas, open options, background) goes under `## Context` in the same file. It states facts and cites sources and requirement IDs; it never links research notes or plans, and never records prices, stock, quotes or commercial strategy.
10. Write in English.
