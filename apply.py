#!/usr/bin/env python3
import json
import shutil
import sys
from pathlib import Path

#---------------------------------------------------------------------
# Change this to the path where system folder of the orca is located 
ORCA_SYSTEM_CACHE_PATH = "/home/simon/.config/OrcaSlicer/system"

#---------------------------------------------------------------------


#---------------------------------------------------------------------
# Don`t cahange this

VENDOR_FOLDER = "FELIX Printers"
VENDOR_MANIFEST = "FELIX Printers.json"

MACHINE_SUBFOLDER = "machine"
PROCESS_SUBFOLDER = "process"
FILAMENT_SUBFOLDER = "filament"
#---------------------------------------------------------------------


def scan_type_list(directory: Path, wanted_type: str, root: Path = None, sort: bool = True):
    if root is None:
        root = directory  # first call: this directory IS the root

    entries = []

    if not directory.is_dir():
        print(f"  ! Folder not found, skipping: {directory}")
        return entries

    for f in sorted(directory.glob("*.json")):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            print(f"  ! Skipping {f.name}: {e}")
            continue

        if data.get("type") != wanted_type:
            continue

        name = data.get("name", f.stem)

        # path relative to the top-level root, e.g. "filament/FELIX Food/foo.json"
        rel = f.relative_to(root.parent)  # includes root's own folder name, e.g. "filament/..."
        path = rel.as_posix()

        entries.append({
            "name": name,
            "sub_path": path,
        })

    for d in directory.iterdir():
        if d.is_dir():
            print(d)
            print(f"Recursively traversing the directory {d.name}")
            for item in scan_type_list(d, wanted_type, root, False):
                entries.append(item)

    if sort:
        entries.sort(key=lambda e: (0 if "common" in e["name"].lower() else 1, e["name"].lower()))
    return entries


def regenerate_manifest(src_folder: Path, src_manifest: Path):
    """
    Reads FELIX Printers.json, replaces machine_model_list / machine_list /
    process_list based on what's actually in the machine/ and process/
    folders, and writes the manifest back in place.
    """
    manifest = json.loads(src_manifest.read_text(encoding="utf-8"))

    machine_dir = src_folder / MACHINE_SUBFOLDER
    process_dir = src_folder / PROCESS_SUBFOLDER
    filament_dir = src_folder / FILAMENT_SUBFOLDER

    machine_model_list = scan_type_list(machine_dir, "machine_model")
    machine_list = scan_type_list(machine_dir, "machine")
    process_list = scan_type_list(process_dir, "process")
    filament_list = scan_type_list(filament_dir, "filament")


    manifest["machine_model_list"] = machine_model_list
    manifest["machine_list"] = machine_list
    manifest["process_list"] = process_list
    manifest["filament_list"] = filament_list

    src_manifest.write_text(json.dumps(manifest, indent=4) + "\n", encoding="utf-8")

    print(f"  machine_model_list: {len(machine_model_list)} entries")
    print(f"  machine_list:       {len(machine_list)} entries")
    print(f"  process_list:       {len(process_list)} entries")
    print(f"  filament_list:       {len(filament_list)} entries")



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 apply.py /path/to/resources/profiles")
        sys.exit(1)

    target_dir = Path(sys.argv[1])
    if not target_dir.is_dir():
        print(f"Target folder does not exist: {target_dir}")
        sys.exit(1)

    orca_system_cache = Path(ORCA_SYSTEM_CACHE_PATH)
    if orca_system_cache.is_dir():
        print("Removing orca system cache")
        shutil.rmtree(orca_system_cache)
    else:
        print("System cache folder already deleted")

    source_dir = Path(__file__).parent

    src_folder = source_dir / VENDOR_FOLDER
    src_manifest = source_dir / VENDOR_MANIFEST

    dst_folder = target_dir / VENDOR_FOLDER
    dst_manifest = target_dir / VENDOR_MANIFEST

    print("Regenerating manifest lists from disk")
    regenerate_manifest(src_folder, src_manifest)

    # Copy the vendor folder (machine/process/filament), overwriting if it exists
    if dst_folder.exists():
        shutil.rmtree(dst_folder)
    shutil.copytree(src_folder, dst_folder)
    print(f"Copied '{VENDOR_FOLDER}' -> {dst_folder}")

    # Copy the vendor manifest json, overwriting if it exists
    shutil.copy2(src_manifest, dst_manifest)
    print(f"Copied '{VENDOR_MANIFEST}' -> {dst_manifest}")

    print(" \u2611 Done.")


if __name__ == "__main__":
    main()