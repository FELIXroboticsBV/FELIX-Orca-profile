XLSX := FELIX_OrcaSlicer_DataSource.xlsx
OUT_MACHINES  := FELIX Printers/machine
OUT_APPLY := ../profiles

.PHONY: build all
 
all: machines apply
 
machines:
	python compile_spec_machines.py $(XLSX) $(OUT)

apply:
	which python
	pwd
	python apply.py "$(OUT_APPLY)"
 
