#!/usr/bin/env python3
"""
NOTE: this is videoed 

Copies FELIX Printers profiles into an OrcaSlicer resources/profiles folder.

Usage:
    python3 apply.py /path/to/OrcaSlicer/resources/profiles
"""

import shutil
import sys
from pathlib import Path

VENDOR_FOLDER = "FELIX Printers"
VENDOR_MANIFEST = "FELIX Printers.json"


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 apply.py /path/to/resources/profiles")
        sys.exit(1)

    target_dir = Path(sys.argv[1])
    if not target_dir.is_dir():
        print(f"Target folder does not exist: {target_dir}")
        sys.exit(1)

    source_dir = Path(__file__).parent

    src_folder = source_dir / VENDOR_FOLDER
    src_manifest = source_dir / VENDOR_MANIFEST

    dst_folder = target_dir / VENDOR_FOLDER
    dst_manifest = target_dir / VENDOR_MANIFEST

    # Copy the vendor folder (machine/process/filament), overwriting if it exists
    if dst_folder.exists():
        shutil.rmtree(dst_folder)
    shutil.copytree(src_folder, dst_folder)
    print(f"Copied '{VENDOR_FOLDER}' -> {dst_folder}")

    # Copy the vendor manifest json, overwriting if it exists
    shutil.copy2(src_manifest, dst_manifest)
    print(f"Copied '{VENDOR_MANIFEST}' -> {dst_manifest}")

    print("Done. Delete the OrcaSlicer 'system' cache folder and restart to see changes.")


if __name__ == "__main__":
    main()