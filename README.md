# FELIX-Orca-profile

Repository with our orca profile

## Usage

Clone this repo inside the orca's `/resrouces` folder.

> You have to have the orca slicer installed either from the soruce or as a built .zip in order to do this. In other words, you have to have access to the orcas` internals

```sh
git clone https://github.com/FELIXroboticsBV/FELIX-Orca-profile.git
```

go to the repository

```sh
cd FELIX-Orca-profile
```

### Configure `system` folder path.

1. Open orca slicer and select Help->Show Configuration Folder.

<img alt="where-to-find" src="./assets/image.png" width=400>

2. Copy the path to the configuration folder.
3. Open the python script

```sh
# or use GUI
nano apply.py`
```

4. Fill in the script's `ORCA_SYSTEM_CACHE_PATH` variable

> **Add `/system` ad the very end of the path**

```python
ORCA_SYSTEM_CACHE_PATH = "/path/to/config/OrcaSlicer/system"
```

Run the script to apply your chagnes

```sh
# path: FELIX-Orca-profiles (main)

python apply.py ../profiles
```
