#------------------------------------
# change this to where you profiles

OUT_APPLY := ../profiles

#-----------------------------------

#========================================

XLSX := FELIX_OrcaSlicer_DataSource.xlsx

OUT_MACHINES  := FELIX Printers/machine

PLASTIC_SHEET := Plastic_Material_Data
OUT_PLASTIC := FELIX Printers/filament/FELIXPlastic

FOOD_SHEET := Food_Material_Data
OUT_FOOD := FELIX Printers/filament/FELIXFood

PROCESS_SHEET := Process_Data
OUT_PROCESS := FELIX Printers/process

#========================================

.PHONY: build all
 
all: machines plastic food process apply
 
GREEN  := \033[0;32m
NC     := \033[0m
BANNER := ======================================================

machines:
	@printf "$(GREEN)$(BANNER)$(NC)\n"
	@printf "$(GREEN)  Generating machines$(NC)\n"
	@printf "$(GREEN)$(BANNER)$(NC)\n"
	python compile_spec_machines.py "$(XLSX)" "$(OUT_MACHINES)"
	@printf "$(GREEN)  Done$(NC)\n\n"

plastic:
	@printf "$(GREEN)$(BANNER)$(NC)\n"
	@printf "$(GREEN)  Generating PLASTIC filaments$(NC)\n"
	@printf "$(GREEN)$(BANNER)$(NC)\n"
	python compile_spec_plastic_materials.py "$(XLSX)" "$(OUT_PLASTIC)" "$(PLASTIC_SHEET)"
	@printf "$(GREEN)  Done$(NC)\n\n"

food:
	@printf "$(GREEN)$(BANNER)$(NC)\n"
	@printf "$(GREEN)  Generating FOOD filaments$(NC)\n"
	@printf "$(GREEN)$(BANNER)$(NC)\n"
	python compile_spec_food_materials.py "$(XLSX)" "$(OUT_FOOD)" "$(FOOD_SHEET)"
	@printf "$(GREEN)  Done$(NC)\n\n"

process:
	@printf "$(GREEN)$(BANNER)$(NC)\n"
	@printf "$(GREEN)  Generating Processes$(NC)\n"
	@printf "$(GREEN)$(BANNER)$(NC)\n"
	python compile_spec_processes.py "$(XLSX)" "$(OUT_PROCESS)" "$(PROCESS_SHEET)"
	@printf "$(GREEN)  Done$(NC)\n\n"

apply:
	@printf "$(GREEN)$(BANNER)$(NC)\n"
	@printf "$(GREEN)  Applying changes$(NC)\n"
	@printf "$(GREEN)$(BANNER)$(NC)\n"
	python apply.py "$(OUT_APPLY)"
	@printf "$(GREEN) SUCCESSFULLY GENERATED ALL PROFILES$(NC)\n\n"