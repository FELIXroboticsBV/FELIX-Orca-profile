# FELIX-Orca-profile

Repository with our Orca profile.

## Usage

Clone this repo inside Orca's `/resources` folder.

> You need to have Orca Slicer installed either from source or as a built .zip in order to do this. In other words, you need access to Orca's internals.

```sh
git clone https://github.com/FELIXroboticsBV/FELIX-Orca-profile.git
```

Go to the repository:

```sh
cd FELIX-Orca-profile
```

### Configure the `system` folder path

1. Open Orca Slicer and select **Help → Show Configuration Folder**.

<img alt="where-to-find" src="./assets/image.png" width=400>

2. Copy the path to the configuration folder.
3. Open the Python script:

```sh
# or use a GUI editor
nano apply.py
```

4. Fill in the script's `ORCA_SYSTEM_CACHE_PATH` variable.

> **Add `/system` at the very end of the path.**

```python
ORCA_SYSTEM_CACHE_PATH = "/path/to/config/OrcaSlicer/system"
```

5. Open the Makefile:

```sh
# or use a GUI editor
nano Makefile
```

and set the `OUT_APPLY` variable to the folder where the profiles are located:

```Makefile
OUT_APPLY := ../profiles
```

7. Download dependencies

```sh
pip install openpyxl
```

8. Run the make script

```sh
make
```

You should see following output

```sh
======================================================
  Generating machines
======================================================
python compile_spec_machines.py "FELIX_OrcaSlicer_DataSource.xlsx" "FELIX Printers/machine"
Wrote 31 machine files to FELIX Printers/machine
  Done

======================================================
  Generating PLASTIC filaments
======================================================
python compile_spec_plastic_materials.py "FELIX_OrcaSlicer_DataSource.xlsx" "FELIX Printers/filament/FELIXPlastic" "Plastic_Material_Data"
Wrote 54 filament files to FELIX Printers/filament/FELIXPlastic
  Done

======================================================
  Generating FOOD filaments
======================================================
python compile_spec_food_materials.py "FELIX_OrcaSlicer_DataSource.xlsx" "FELIX Printers/filament/FELIXFood" "Food_Material_Data"
Wrote 39 food material files to FELIX Printers/filament/FELIXFood
  Done

======================================================
  Generating Processes
======================================================
python compile_spec_processes.py "FELIX_OrcaSlicer_DataSource.xlsx" "FELIX Printers/process" "Process_Data"
Wrote 37 process files to FELIX Printers/process
  Done

======================================================
  Applying changes
======================================================
python apply.py "../profiles"
System cache folder already deleted
Regenerating manifest lists from disk
/home/simon/Desktop/FelixPrinter/Orca/squashfs-root/resources/FELIX-Orca-profile/FELIX Printers/filament/FELIXFood
Recursively traversing the directory FELIXFood
/home/simon/Desktop/FelixPrinter/Orca/squashfs-root/resources/FELIX-Orca-profile/FELIX Printers/filament/FELIXPlastic
Recursively traversing the directory FELIXPlastic
  machine_model_list: 7 entries
  machine_list:       40 entries
  process_list:       40 entries
  filament_list:       108 entries
Copied 'FELIX Printers' -> ../profiles/FELIX Printers
Copied 'FELIX Printers.json' -> ../profiles/FELIX Printers.json
 ☑ Done.
 SUCCESSFULLY GENERATED ALL PROFILES
```
