#remove all default echoes
ifndef VERBOSE
.SILENT:
endif

#Vars
CC         := gcc
CFLAGS     := -c -std=gnu11 -Wall

INC_DIR    := 
LDFLAGS    := -pthread

OUT_FOLDER := out
OBJ_DIR    := obj

SRC    	 := santa.c
EXE_NAME   := santa

OBJECTS  := $(SRC:%.c=$(OBJ_DIR)/%.o)
EXECUTABLE := $(OUT_FOLDER)/$(EXE_NAME)

.PHONY: default
default: $(SRC) $(EXECUTABLE)

.PHONY: all
all: clean default

.PHONY: clean
clean:
	@echo "Cleaning..."
	-rm -f -r $(OBJ_DIR)/*
	-rm -f -r $(EXECUTABLE)

.PHONY: help
help:
	@echo "make all \t - clean and then build test apps"
	@echo "make clean \t - clear all outputed files"

$(OUT_FOLDER):
	mkdir -p $@

$(OBJ_DIR)/%.o: %.c
	@echo "Compiling: $<"
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) $(INC_DIR) $< -o $@

$(EXECUTABLE): $(OBJECTS) $(OUT_FOLDER)
	@echo "EXECUTABLE: $@"
	$(CC) $(OBJECTS) $(LDFLAGS) -o $@