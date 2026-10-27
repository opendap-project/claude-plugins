---
name: license-check
description: Check and fix REUSE licensing in an OpenDAP repository. Use after adding files or folders, or before committing.
---

# Check licensing (REUSE)

Every public OpenDAP repository follows the [REUSE](https://reuse.software) layout: license texts in `LICENSES/`, path-to-license mapping in `REUSE.toml`. In `REUSE.toml`, the last matching `[[annotations]]` entry wins.

License policy:

| Content | SPDX identifier |
|---|---|
| Hardware of OpenDAP products: schematics, PCB, mechanics | `CERN-OHL-S-2.0` |
| Hardware building blocks others combine: part libraries, HAT Case Standard reference designs, `export/` | `CERN-OHL-W-2.0` |
| Software | `GPL-3.0-or-later` |
| Software libraries others build on: SDK, design system, schemas | `MPL-2.0` |
| Firmware, project templates | `MIT` |
| Documentation, specifications, manuals, renders, project assets | `CC-BY-SA-4.0` |
| Generic shared assets others can build on (`blender-lib/shared/`) | `CC-BY-4.0` |

Principle: changes to anything OpenDAP publishes stay open; what others add on top is theirs to license.

Copyright line: `2026 The OpenDAP Project` (use the current year for new entries).

Steps:

1. Run `reuse lint` in the repository root. If `reuse` is not installed, tell the user and stop; do not install it without asking.
2. License texts are kept in `LICENSES/` only while some file uses them, so `reuse lint` passes:
   - "Missing licenses": a file now uses a license whose text is absent. Add it from <https://github.com/spdx/license-list-data> (`text/<id>.txt`). For MIT, replace `<year> <copyright holders>` with the copyright line.
   - "Unused licenses": remove that text from `LICENSES/`.
3. For a new top-level folder, add an `[[annotations]]` entry with the license from the policy, before the `docs/**` entry.
4. Keep the README `## License` section in sync with `REUSE.toml`.
5. Private repositories are proprietary: they have a `LICENSE` file and no REUSE layout. Never copy private content into a public repository.
