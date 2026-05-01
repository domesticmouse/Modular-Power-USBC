#!/usr/bin/env python3

import re

# The name of the KiCad schematic file to scan for missing LCSC part numbers
SCHEMATIC_FILE = "Modular-Power-USBC.kicad_sch"


def natural_sort_key(s):
    """Sort strings containing numbers in human order (R1, R2, R10)."""
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]


def parse_kicad_sch(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    # Find all symbol blocks
    # Note: This is a simplified parser for S-expressions
    symbols = []

    # Symbols start with (symbol ... and end with a matching )
    # However, they can be nested. We only care about the top-level symbols in the sheet.

    # A more robust way is to find (symbol and then count parentheses
    pos = 0
    while True:
        pos = content.find("(symbol", pos)
        if pos == -1:
            break

        # Check if it's a component instance or a library symbol definition
        # Library symbols are usually inside (lib_symbols ...)
        # We want symbols that are NOT inside lib_symbols
        # lib_symbols starts at the beginning of the file.

        # Simple check: does it have a lib_id?
        # Component instances have (lib_id "...")

        start = pos
        bracket_count = 0
        end = -1
        for i in range(pos, len(content)):
            if content[i] == "(":
                bracket_count += 1
            elif content[i] == ")":
                bracket_count -= 1
                if bracket_count == 0:
                    end = i + 1
                    break

        if end != -1:
            symbol_text = content[start:end]
            if "(lib_id" in symbol_text:
                symbols.append(symbol_text)
            pos = end
        else:
            pos += 1

    results = []
    for sym in symbols:
        # Extract Reference
        ref_match = re.search(r'\(property "Reference" "([^"]+)"', sym)
        if not ref_match:
            continue
        ref = ref_match.group(1)

        # Skip power symbols (usually start with #)
        if ref.startswith("#"):
            continue

        # Extract Value
        val_match = re.search(r'\(property "Value" "([^"]+)"', sym)
        val = val_match.group(1) if val_match else "Unknown"

        # Check for LCSC
        has_lcsc = '(property "LCSC"' in sym
        lcsc_val = ""
        if has_lcsc:
            lcsc_match = re.search(r'\(property "LCSC" "([^"]+)"', sym)
            if lcsc_match:
                lcsc_val = lcsc_match.group(1)

        # Extract Footprint
        fp_match = re.search(r'\(property "Footprint" "([^"]*)"', sym)
        fp = fp_match.group(1) if fp_match else ""

        results.append(
            {"reference": ref, "value": val, "lcsc": lcsc_val, "footprint": fp}
        )

    return results


if __name__ == "__main__":
    components = parse_kicad_sch(SCHEMATIC_FILE)

    # Filter to only missing LCSC parts and sort by reference naturally
    missing = [c for c in components if not c["lcsc"]]
    missing.sort(key=lambda x: natural_sort_key(x['reference']))

    print(f"{'Ref':<10} | {'Value':<20} | {'Footprint':<50}")
    print("-" * 100)
    for c in missing:
        print(f"{c['reference']:<10} | {c['value']:<20} | {c['footprint']:<50}")

    if not missing:
        print("All components have LCSC numbers!")
