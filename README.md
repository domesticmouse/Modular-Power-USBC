# Modular-Power-USBC

## Project Overview
This project provides a compact, high-efficiency power solution for modular electronics (such as Eurorack synthesizers or analog prototyping boards). It converts standard **5V USB-C power** into clean, dual **±12V rails**.

### Key Features
- **USB-C Input:** Uses a power-only 6-pin receptacle for durability and simplicity.
- **Dual Rail Output:** Provides ±12V at up to 83mA per rail (2W total).
- **Comprehensive Protection:** Features overcurrent, reverse polarity, and back-drive protection.
- **Controlled Startup:** Integrated load switch with a physical toggle for safe power-up.
- **Indicator LEDs:** Visual confirmation for both positive and negative rails.

### Main Technologies
- **EDA Tool:** KiCad (Project files version 20260306, KiCad 10.0 or newer).
- **Major Components:**
  - **DC-DC Converter:** `A0512S-2WR2` (Isolated 2W module).
  - **Ideal Diode:** `LM66100` (Reverse polarity & back-drive protection).
  - **Load Switch:** `TPS22918` (Gated power control).
  - **Filtering:** Ferrite bead and 0805 SMD decoupling capacitors.
  - **Protection:** Resettable Polyfuse (`F1`).

## Circuit Architecture
The power path is designed for reliability and safety:

1.  **Input & Filtering:** 5V enters via `J1`. It is immediately protected by a Polyfuse and filtered by a Ferrite Bead to reduce high-frequency noise.
2.  **Polarity Protection:** An `LM66100` ideal diode provides extremely low-loss protection against reverse voltage on the input.
3.  **Gated Control:** The `TPS22918` load switch acts as the master gate. A physical SPDT slide switch (`SW1`) controls the enable pin, allowing the user to safely toggle the ±12V rails.
4.  **Isolated Conversion:** The `A0512S-2WR2` performs the heavy lifting, converting the 5V input to isolated ±12V outputs. This isolation helps prevent ground loops between the USB source and the analog circuitry.
5.  **Output Rail:** The dual rails are broken out to 2.54mm headers (`J2`, `J3`) for plugging into a breadboard.

## Directory Structure
- `Modular-Power-USBC.kicad_sch`: Main schematic file.
- `Modular-Power-USBC.kicad_pcb`: PCB layout file.
- `Modular-Power-USBC.pretty/`: Local footprint library for custom components.
- `ModularPower.kicad_sym`: Local symbol library.
- `production/`: Fabrication-ready files (Gerbers, BOM, Pick-and-Place).

## Project Status
- **Schematic:** Functional design complete.
- **ERC Status:** 1 Error (Pin 2 of PS1 not driven). Note: This is an ERC artifact due to a missing `PWR_FLAG` on the `GND` net; the electrical connection is correct.
- **Layout:** Complete.

## Building and Production
### KiCad Workflow
1. Open `Modular-Power-USBC.kicad_pro` in KiCad 10.0+.
2. Fabrication files are generated using the **KiCad Fabrication Toolkit** in the `production/` folder.
3. An **Interactive HTML BOM** is available in `bom/ibom.html` for hand-assembly.

## Development Conventions
- **Components:** Prefer LCSC part numbers (documented in `bom.csv` and component properties) for optimized sourcing via JLCPCB.
- **Footprints:** Custom footprints are maintained in the local `.pretty` library.
