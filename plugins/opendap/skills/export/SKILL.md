---
name: export
description: Generate a component's export/ folder (the component as one unit, for other components and the T1 integration) following the OpenDAP component export contract. Use when a component's design reaches a state others must consume, and before a release.
---

# Export a component

The contract is `hardware/docs/specs/component-export.md` in the `tools` repository (`<tools-hardware>` is `public/tools/hardware` in the workspace, or `$ODAP_TOOLS_DIR/hardware`). Read it first. Consumers read only `export/`; never copy sources there.

1. Generate what the component has, as one unit:
   - **Mechanics** (FreeCAD): one STEP body per component with
     `freecadcmd <tools>/mechanical/freecad_export.py -- <part>.FCStd export/<component>.step`.
     It prints volume and center of mass; record them.
   - **Electronics** (KiCad): PCBA STEP with `kicad-cli pcb export step`, glTF with `kicad-cli pcb export glb`, and the netlist with `kicad-cli sch export netlist`.
   - **Renders** (Blender): the component's collection, to be linked by consumers.
   - **Signal paths, power and thermal**: only when the component's simulations produced them.
2. Write `export/component.yaml` with: name, version (the tag being prepared), implemented interfaces with their versions, the exported files, and mass properties. The schema is not defined yet: show the user the draft and ask before treating any field as final.
3. Run `/opendap:license-check`, then commit `export/` together with the tag being released.
