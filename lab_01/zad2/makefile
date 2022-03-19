#remove all default echoes
ifndef VERBOSE
.SILENT:
endif

DEFAULT_MODE := lib

#Vars
CC         := gcc
CFLAGS     := -c -std=gnu11 -Wall

INC_DIR    := 
LDFLAGS    :=

OUT_FOLDER := out
OBJ_DIR    := obj

SRC    	   := wc_lib.c wc_test.c
EXE_NAME   := wc_test

LIB_EXE_NAME := $(EXE_NAME)_lib
SYS_EXE_NAME := $(EXE_NAME)_sys

OBJECTS_LIB    := $(SRC:%.c=$(OBJ_DIR)/lib/%.o)
OBJECTS_SYS    := $(SRC:%.c=$(OBJ_DIR)/sys/%.o)

EXECUTABLE_LIB := $(OUT_FOLDER)/$(LIB_EXE_NAME)
EXECUTABLE_SYS := $(OUT_FOLDER)/$(SYS_EXE_NAME)

.PHONY: default
default:  $(DEFAULT_MODE)

.PHONY: lib
lib: $(SRC) $(EXECUTABLE_LIB)

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

$(OBJ_DIR)/%.o: %.c
	@echo "Compiling: $<"
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) $(INC_DIR) $< -o $@

$(EXECUTABLE_LIB): $(OBJECTS) $(OUT_FOLDER)
	@echo "EXECUTABLE: $@"
	$(CC) $(OBJECTS) $(LDFLAGS) -o $@

$(EXECUTABLE_SYS): $(OBJECTS_SYS) $(OUT_FOLDER)
	@echo "EXECUTABLE: $@"
	$(CC) $(OBJECTS) $(LDFLAGS) -o $@

	