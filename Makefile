XLSX := FELIX_OrcaSlicer_DataSource.xlsx
PLASTIC_SHEET := Plastic_Material_Data
OUT_MACHINES  := FELIX Printers/machine
OUT_PLASTIC := FELIX Printers/filament/FELIXPlastic
OUT_APPLY := ../profiles

.PHONY: build all
 
all: machines plastic apply
 
machines:
	python compile_spec_machines.py $(XLSX) $(OUT)

plastic: 
	python compile_spec_plastic_materials.py "$(XLSX)" "$(OUT_PLASTIC)" "$(PLASTIC_SHEET)"

apply:
	which python
	pwd
	python apply.py "$(OUT_APPLY)"
 
