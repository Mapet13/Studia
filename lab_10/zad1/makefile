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

S_SRC    	 := server.c common.c
S_EXE_NAME   := server

C_SRC    	 := client.c common.c
C_EXE_NAME   := client

S_OBJECTS  := $(S_SRC:%.c=$(OBJ_DIR)/S/%.o)
C_OBJECTS  := $(C_SRC:%.c=$(OBJ_DIR)/C/%.o)

S_EXECUTABLE := $(OUT_FOLDER)/$(S_EXE_NAME)
C_EXECUTABLE := $(OUT_FOLDER)/$(C_EXE_NAME)

.PHONY: default
default: $(SRC) $(S_EXECUTABLE) $(C_EXECUTABLE)

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

$(OBJ_DIR)/C/%.o: %.c
	@echo "Compiling: $<"
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) $(INC_DIR) $< -o $@

$(OBJ_DIR)/S/%.o: %.c
	@echo "Compiling: $<"
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) $(INC_DIR) $< -o $@

$(S_EXECUTABLE): $(S_OBJECTS) $(OUT_FOLDER)
	@echo "EXECUTABLE: $@"
	$(CC) $(S_OBJECTS) $(LDFLAGS) -o $@

$(C_EXECUTABLE): $(C_OBJECTS) $(OUT_FOLDER)
	@echo "EXECUTABLE: $@"
	$(CC) $(C_OBJECTS) $(LDFLAGS) -o $@
