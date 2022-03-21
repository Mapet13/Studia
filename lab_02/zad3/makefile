#remove all default echoes
ifndef VERBOSE
.SILENT:
endif

#Vars
CC         := gcc
CFLAGS     := -c -g -std=c11 -Wall

INC_DIR    := 
LDFLAGS    :=

OUT_FOLDER := out
OBJ_DIR    := obj

SRC    	   := fwalk.c
EXE_NAME   := fwalk

STAT_EXE_NAME := $(EXE_NAME)_stat
SYS_EXE_NAME := $(EXE_NAME)_sys

OBJECTS_STAT  := $(SRC:%.c=$(OBJ_DIR)/stat/%.o)
OBJECTS_SYS  := $(SRC:%.c=$(OBJ_DIR)/sys/%.o)

EXECUTABLE_STAT := $(OUT_FOLDER)/$(STAT_EXE_NAME)
EXECUTABLE_SYS := $(OUT_FOLDER)/$(SYS_EXE_NAME)


.PHONY: default
default: $(SRC) $(EXECUTABLE)

.PHONY: stat
stat: $(SRC) $(EXECUTABLE_STAT)

.PHONY: sys
sys: $(SRC) $(EXECUTABLE_SYS)

.PHONY: all
all: clean lib sys

.PHONY: clean
clean:
	@echo "Cleaning..."
	-rm -f -r $(OBJ_DIR)/*
	-rm -f -r $(EXECUTABLE)

.PHONY: help
help:
	@echo "make \t\t - build test app"
	@echo "make all \t - clean and then build test app"
	@echo "make clean \t - clear all outputed files"

$(OUT_FOLDER):
	mkdir -p $@

$(OBJ_DIR)/stat/%.o: %.c
	@echo "Compiling: $<"
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) $(INC_DIR) $< -o $@

$(EXECUTABLE_STAT): $(OBJECTS_STAT) $(OUT_FOLDER)
	@echo "EXECUTABLE: $@"
	$(CC) $(OBJECTS_STAT) $(LDFLAGS) -o $@
