# Modular-Power-USBC

## Project Overview
This project provides a compact power solution for modular electronics (such as Eurorack synthesizers) by converting 5V USB power into dual +/- 12V rails.

### Main Technologies
- **EDA Tool:** KiCad (Project files version 20260306, KiCad 10.0 or newer).
- **Core Components:**
  - **DC-DC Converter:** A0512S-2WR2 (Isolated 2W module, 5V input, +/- 12V output).
  - **Power Protection:** LM66100 (Ideal Diode) for reverse polarity and back-drive protection.
  - **Load Control:** TPS22918 load switch.
  - **Input:** USB-C (Power-only 6-pin receptacle).

## Directory Structure
- `Modular-Power-USBC.kicad_sch`: Main schematic file.
- `Modular-Power-USBC.kicad_pcb`: PCB layout file.
- `Modular-Power-USBC.kicad_pro`: KiCad project file.
- `Modular-Power-USBC.pretty/`: Local footprint library containing custom components (e.g., Ferrite Bead).
- `ModularPower.kicad_sym`: Local symbol library.
- `production/`: Contains fabrication-ready files:
  - `bom.csv`: Bill of Materials.
  - `positions.csv`: Pick-and-place component positions.
  - `Modular-Power-USBC.zip`: Gerber and Drill files.
- `bom/`:
  - `ibom.html`: Interactive BOM for hand-assembly.

## Building and Production
### KiCad Workflow
1. Open `Modular-Power-USBC.kicad_pro` in KiCad.
2. Use **Eeschema** for schematic modifications.
3. Use **Pcbnew** for layout modifications.

### Production
Fabrication files are generated using the **KiCad Fabrication Toolkit**. 
- Settings are stored in `fabrication-toolkit-options.json`.
- Output is automatically placed in the `production/`.

### Interactive BOM
Interactive BOM generated using **Generate Interactive HTML BOM** plugin.
- Output is stored in `bom/`.

## Development Conventions
- **Open Source:** Adhere to CERN-OHL-S requirements when distributing modifications.
- **Components:** Prefer LCSC part numbers (documented in `bom.csv` and component properties) for easy ordering through JLCPCB or similar services.
- **Footprints:** Custom footprints should be added to the `Modular-Power-USBC.pretty` library.
