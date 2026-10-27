---
name: fab-package
description: Build the fab and assembly package (Gerbers, drill, pick-and-place, turn-key assembly BOM, Interactive HTML BOM, schematic and assembly PDFs, STEP, IPC-2581) for a KiCad project, locally. Use before ordering boards or attaching a release.
---

# Build a fab package

Everything runs on the local machine. There is no CI.

1. Find the KiCad project (`*.kicad_pro`) the user means. If there are several, ask.
2. Find the hardware toolkit: `public/toolkit/hardware` in the OpenDAP workspace, or `$OPENDAP_TOOLKIT_HARDWARE`. It runs ERC/DRC through toolkit-hooks, found as `public/toolkit/hooks` or `$OPENDAP_TOOLKIT_HOOKS`, which must be at the tag pinned in the repository's `.pre-commit-config.yaml`.
3. Make sure the project uses the right fab rules: a `<project>.kicad_dru` copied from `kicad-lib/design-rules/` for the target fab and process. If none is present, stop and ask which fab and process.
4. Run:

   ```sh
   <toolkit-hardware>/tools/fab-package.sh <project>.kicad_pro
   ```

   The script runs ERC and DRC first and stops on errors. Never pass `--skip-checks` unless the user explicitly asks; a skipped package is marked `UNCHECKED`.
5. Report the package folder (`<project>/fab/<name>-<revision>/`), its `MANIFEST.txt`, and every warning. Missing Manufacturer or MPN fields block turn-key assembly; list the affected designators.
6. Never commit `fab/`. Packages are attached to GitHub Releases by the maintainers.
