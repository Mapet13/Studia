#remove all default echoes
ifndef VERBOSE
.SILENT:
endif

#Vars
CC         := gcc
CFLAGS     := -c -std=gnu11 -Wall

INC_DIR    := 
LDFLAGS    :=

OUT_FOLDER := out
OBJ_DIR    := obj

SRC    	   := sigfork.c
EXE_NAME   := sigfork
EXE_EXEC_NAME   := sigexec

OBJECTS  := $(SRC:%.c=$(OBJ_DIR)/fork/%.o)
EXEC_OBJECTS  := $(SRC:%.c=$(OBJ_DIR)/exec/%.o)

EXECUTABLE := $(OUT_FOLDER)/$(EXE_NAME)
EXEC_EXECUTABLE := $(OUT_FOLDER)/$(EXE_EXEC_NAME)

.PHONY: default
default: $(SRC) $(EXECUTABLE) $(EXEC_EXECUTABLE)

.PHONY: all
all: clean default

.PHONY: clean
clean:
	@echo "Cleaning..."
	-rm -f -r $(OBJ_DIR)/*
	-rm -f -r $(EXECUTABLE)
	-rm -f -r $(EXEC_EXECUTABLE)

.PHONY: help
help:
	@echo "make \t\t - build test app"
	@echo "make all \t - clean and then build test app"
	@echo "make clean \t - clear all outputed files"

$(OUT_FOLDER):
	mkdir -p $@

$(OBJ_DIR)/fork/%.o: %.c
	@echo "Compiling: $<"
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) $(INC_DIR) $< -o $@


$(OBJ_DIR)/exec/%.o: %.c
	@echo "Compiling: $<"
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) -DEXEC $(INC_DIR) $< -o $@

$(EXECUTABLE): $(OBJECTS) $(OUT_FOLDER)
	@echo "EXECUTABLE: $@"
	$(CC) $(OBJECTS) $(LDFLAGS) -o $@

$(EXEC_EXECUTABLE): $(EXEC_OBJECTS) $(OUT_FOLDER)
	@echo "EXECUTABLE: $@"
	$(CC) $(EXEC_OBJECTS) $(LDFLAGS) -o $@