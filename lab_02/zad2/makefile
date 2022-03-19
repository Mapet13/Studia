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

SRC    	   := fcount.c
EXE_NAME   := fcount

LIB_EXE_NAME := $(EXE_NAME)_lib
SYS_EXE_NAME := $(EXE_NAME)_sys

OBJECTS_LIB  := $(SRC:%.c=$(OBJ_DIR)/lib/%.o)
OBJECTS_SYS  := $(SRC:%.c=$(OBJ_DIR)/sys/%.o)

EXECUTABLE_LIB := $(OUT_FOLDER)/$(LIB_EXE_NAME)
EXECUTABLE_SYS := $(OUT_FOLDER)/$(SYS_EXE_NAME)


.PHONY: default
default: $(SRC) $(EXECUTABLE)

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

$(OBJ_DIR)/lib/%.o: %.c
	@echo "Compiling: $<"
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) $(INC_DIR) $< -o $@

$(OBJ_DIR)/sys/%.o: %.c
	@echo "Compiling: $<"
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) -DSYS_MODE $(INC_DIR) $< -o $@

$(EXECUTABLE_LIB): $(OBJECTS_LIB) $(OUT_FOLDER)
	@echo "EXECUTABLE: $@"
	$(CC) $(OBJECTS_LIB) $(LDFLAGS) -o $@

$(EXECUTABLE_SYS): $(OBJECTS_SYS) $(OUT_FOLDER)
	@echo "EXECUTABLE: $@"
	$(CC) $(OBJECTS_SYS) $(LDFLAGS) -o $@