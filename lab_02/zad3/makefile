#remove all default echoes
ifndef VERBOSE
.SILENT:
endif

#Vars
CC         := gcc
CFLAGS     := -c -std=c11 -Wall

INC_DIR    := 
LDFLAGS    :=

OUT_FOLDER := out
OBJ_DIR    := obj

SRC    	   := fwalk.c
EXE_NAME   := fwalk

STAT_EXE_NAME := $(EXE_NAME)_stat
NFTW_EXE_NAME := $(EXE_NAME)_nftw

OBJECTS_STAT  := $(SRC:%.c=$(OBJ_DIR)/stat/%.o)
OBJECTS_NFTW  := $(SRC:%.c=$(OBJ_DIR)/nftw/%.o)

EXECUTABLE_STAT := $(OUT_FOLDER)/$(STAT_EXE_NAME)
EXECUTABLE_NFTW := $(OUT_FOLDER)/$(NFTW_EXE_NAME)


.PHONY: stat
stat: $(SRC) $(EXECUTABLE_STAT)

.PHONY: nftw
nftw: $(SRC) $(EXECUTABLE_NFTW)

.PHONY: clean
clean:
	@echo "Cleaning..."
	-rm -f -r $(OBJ_DIR)/*
	-rm -f -r $(EXECUTABLE)

.PHONY: help
help:
	@echo "make stat \t - clean and then build app in stat mode"
	@echo "make nftw \t - clean and then build app in nftw mode"
	@echo "make clean \t - clear all outputed files"

$(OUT_FOLDER):
	mkdir -p $@

$(OBJ_DIR)/stat/%.o: %.c
	@echo "Compiling: $<"
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) $(INC_DIR) $< -o $@

$(OBJ_DIR)/nftw/%.o: %.c
	@echo "Compiling: $<"
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) -DNFTW_MODE $(INC_DIR) $< -o $@


$(EXECUTABLE_STAT): $(OBJECTS_STAT) $(OUT_FOLDER)
	@echo "EXECUTABLE: $@"
	$(CC) $(OBJECTS_STAT) $(LDFLAGS) -o $@

$(EXECUTABLE_NFTW): $(OBJECTS_NFTW) $(OUT_FOLDER)
	@echo "EXECUTABLE: $@"
	$(CC) $(OBJECTS_NFTW) $(LDFLAGS) -o $@
