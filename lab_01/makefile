#remove all default echoes
ifndef VERBOSE
.SILENT:
endif

DEFAULT_LINKING := shared

#Vars
CC         := gcc
AR         := ar crs
CFLAGS     := -c -std=gnu11 -Wall 

INC_DIR    := 
LDFLAGS    := 

OUT_FOLDER := out
OBJ_DIR    := obj

SRC        := wc_test.c
EXE_NAME   := wc_test

LIB_SRC    := wc_lib.c
LIB_NAME   := wc

LIB_OBJECTS    := $(LIB_SRC:%.c=$(OBJ_DIR)/%.o)
STATIC_LIB_FILE := $(OUT_FOLDER)/lib$(LIB_NAME).a
DYNAMIC_LIB_FILE := $(OUT_FOLDER)/lib$(LIB_NAME)_dynamic.so
SHARED_LIB_FILE := $(OUT_FOLDER)/lib$(LIB_NAME)_shared.so

OBJECTS := $(SRC:%.c=$(OBJ_DIR)/%.o)
EXECUTABLE := $(OUT_FOLDER)/$(EXE_NAME)
EXECUTABLE_STATIC := $(EXECUTABLE)_static
EXECUTABLE_DYNAMIC := $(EXECUTABLE)_dynamic
EXECUTABLE_SHARED := $(EXECUTABLE)_shared

DEFAULT_LINKING_LIB_RULE := 
ifeq ($(DEFAULT_LINKING),static)
       	DEFAULT_LINKING_LIB_RULE = static_lib
else ifeq ($(DEFAULT_LINKING),shared)
       	DEFAULT_LINKING_LIB_RULE = shared_lib
else
		DEFAULT_LINKING_LIB_RULE = dynamic_lib
endif


.PHONY: default
default: $(LIB_SRC) $(DEFAULT_LINKING_LIB_RULE) $(DEFAULT_LINKING)

.PHONY: static
static: $(SRC) $(EXECUTABLE_STATIC)

.PHONY: dynamic
dynamic: $(SRC) $(EXECUTABLE_DYNAMIC)

.PHONY: shared
shared: $(SRC) $(EXECUTABLE_SHARED)

.PHONY: static_lib
static_lib: $(STATIC_LIB_FILE)

.PHONY: dynamic_lib
dynamic_lib: $(DYNAMIC_LIB_FILE)

.PHONY: shared_lib
shared_lib: $(SHARED_LIB_FILE)

.PHONY: clean
clean:
	@echo "Cleaning..."
	-rm -f -r $(OBJ_DIR)/*
	-rm -f -r $(STATIC_LIB_FILE)
	-rm -f -r $(DYNAMIC_LIB_FILE)
	-rm -f -r $(EXECUTABLE_SHARED)
	-rm -f -r $(EXECUTABLE_DYNAMIC)
	-rm -f -r $(EXECUTABLE_STATIC)

.PHONY: run_static
run_static: static
#TODO

.PHONY: help
help:
#TODO 

$(OUT_FOLDER):
	mkdir -p $@

$(STATIC_LIB_FILE): $(OUT_FOLDER) $(LIB_OBJECTS)
	@echo "STATIC LIBARY: $@"
	$(AR) $@ $(LIB_OBJECTS)

$(DYNAMIC_LIB_FILE): $(OUT_FOLDER) $(LIB_OBJECTS)
	@echo "DYNAMIC LIBARY: $@"
	$(CC) -fPIC -o $@ $(LIB_OBJECTS) -shared  

$(SHARED_LIB_FILE): $(OUT_FOLDER) $(LIB_OBJECTS)
	@echo "SHARED LIBARY: $@"
	$(CC) -fPIC -o $@ $(LIB_OBJECTS) -shared  

$(OBJ_DIR)/%.o: %.c
	@echo "Compiling: $<"
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) $(INC_DIR) $< -o $@

$(EXECUTABLE_STATIC): $(STATIC_LIB_FILE) $(OUT_FOLDER) $(OBJECTS)
	@echo "ECUTABLE: $@"
	$(CC) $(OBJECTS) $(LDFLAGS) -o $@ $(STATIC_LIB_FILE)

	
$(EXECUTABLE_SHARED): $(SHARED_LIB_FILE) $(OUT_FOLDER) $(OBJECTS)
	@echo "ECUTABLE: $@"
	$(CC) $(OBJECTS) $(LDFLAGS) -o $@ $(SHARED_LIB_FILE)

$(EXECUTABLE_DYNAMIC): $(DYNAMIC_LIB_FILE) $(OUT_FOLDER) $(OBJECTS)
	@echo "ECUTABLE: $@"
	$(CC) $(OBJECTS) $(LDFLAGS) -ldl -o $@