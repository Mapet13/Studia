#remove all default echoes
ifndef VERBOSE
.SILENT:
endif

#Vars
CC         := gcc
AR         := ar crs
CFLAGS     := -c -std=gnu11 -Wall 

INC_DIR    := 
LDFLAGS    := 

OUT_FOLDER := out
OBJ_DIR    := obj

LIB_SRC    := wc_lib.c
LIB_NAME   := wc

OBJECTS    := $(LIB_SRC:%.c=$(OBJ_DIR)/%.o)
STATIC_LIB_FILE := $(OUT_FOLDER)/lib$(LIB_NAME).a
SHARED_LIB_FILE := $(OUT_FOLDER)/lib$(LIB_NAME).so

.PHONY: default
default: $(LIB_SRC) static shared

.PHONY: all
all: clean default

.PHONY: static
static: $(STATIC_LIB_FILE)

.PHONY: shared
shared: $(SHARED_LIB_FILE)

.PHONY: clean
clean:
	@echo "Cleaning..."
	-rm -f -r $(OBJ_DIR)/*
	-rm -f -r $(STATIC_LIB_FILE)
	-rm -f -r $(SHARED_LIB_FILE)

.PHONY: help
help:
	@echo "make \t\t - build static and shared lib"
	@echo "make all \t - clean and then build static and shared lib"
	@echo "make static \t - build static lib"
	@echo "make shared \t - build shared lib"
	@echo "make clean \t - clear all outputed files"

$(OUT_FOLDER):
	mkdir -p $@

$(STATIC_LIB_FILE): $(OUT_FOLDER) $(OBJECTS)
	@echo "STATIC LIBARY: $@"
	$(AR) $@ $(OBJECTS)

$(DYNAMIC_LIB_FILE): $(OUT_FOLDER) $(OBJECTS)
	@echo "SHARED LIBARY: $@"
	$(CC) -fPIC -o $@ $(OBJECTS) -shared

$(OBJ_DIR)/%.o: %.c
	@echo "Compiling: $<"
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) $(INC_DIR) $< -o $@