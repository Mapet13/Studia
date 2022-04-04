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

SENDER_SRC        := sender.c common.c
SENDER_EXE_NAME   := sender

CATCHER_SRC        := catcher.c common.c
CATCHER_EXE_NAME   := catcher

SENDER_OBJECTS  := $(SENDER_SRC:%.c=$(OBJ_DIR)/%.o)
CATCHER_OBJECTS  := $(CATCHER_SRC:%.c=$(OBJ_DIR)/%.o)

SENDER_EXECUTABLE := $(OUT_FOLDER)/$(SENDER_EXE_NAME)
CATCHER_EXECUTABLE := $(OUT_FOLDER)/$(CATCHER_EXE_NAME)

.PHONY: default
default: $(SENDER_SRC) $(SENDER_EXECUTABLE) $(CATCHER_SRC) $(CATCHER_EXECUTABLE)

.PHONY: all
all: clean default

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

$(SENDER_EXECUTABLE): $(SENDER_OBJECTS) $(OUT_FOLDER)
	@echo "EXECUTABLE: $@"
	$(CC) $(SENDER_OBJECTS) $(LDFLAGS) -o $@

$(CATCHER_EXECUTABLE): $(CATCHER_OBJECTS) $(OUT_FOLDER)
	@echo "EXECUTABLE: $@"
	$(CC) $(CATCHER_OBJECTS) $(LDFLAGS) -o $@
