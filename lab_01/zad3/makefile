#remove all default echoes
# ifndef VERBOSE
# .SILENT:
# endif

DEFAULT_LINKING := static

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

LIB_OBJECTS_STATIC    := $(LIB_SRC:%.c=$(OBJ_DIR)/STATIC/%.o)
LIB_OBJECTS_SHARED    := $(LIB_SRC:%.c=$(OBJ_DIR)/SHARED/%.o)
LIB_OBJECTS_DYNAMIC   := $(LIB_SRC:%.c=$(OBJ_DIR)/DYNAMIC/%.o)
STATIC_LIB_FILE := $(OUT_FOLDER)/lib$(LIB_NAME).a
DYNAMIC_LIB_FILE := $(OUT_FOLDER)/lib$(LIB_NAME)_dynamic.so
SHARED_LIB_FILE := $(OUT_FOLDER)/lib$(LIB_NAME)_shared.so

OBJECTS_STATIC := $(SRC:%.c=$(OBJ_DIR)/STATIC/%.o)
OBJECTS_SHARED := $(SRC:%.c=$(OBJ_DIR)/SHARED/%.o)
OBJECTS_DYNAMIC := $(SRC:%.c=$(OBJ_DIR)/DYNAMIC/%.o)
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
default: $(DEFAULT_LINKING_LIB_RULE) $(DEFAULT_LINKING)

.PHONY: all
all: clean static shared dynamic

.PHONY: static
static: $(SRC) $(EXECUTABLE_STATIC)

.PHONY: dynamic
dynamic: $(SRC) $(EXECUTABLE_DYNAMIC)

.PHONY: shared
shared: $(SRC) $(EXECUTABLE_SHARED)

add_o1:
	$(eval CFLAGS += -O1)
	@echo "adding -O1 flag"

add_os:
	$(eval CFLAGS += -Os)
	@echo "adding -Os flag"

.PHONY: static_O1
static_O1: add_o1 $(SRC) $(EXECUTABLE_STATIC)

.PHONY: dynamic_O1
dynamic_O1: add_o1 $(SRC) $(EXECUTABLE_DYNAMIC)

.PHONY: shared_O1
shared_O1: add_o1 $(SRC) $(EXECUTABLE_SHARED)

.PHONY: static_Os
static_Os: add_os $(SRC) $(EXECUTABLE_STATIC)

.PHONY: dynamic_Os
dynamic_Os: add_os $(SRC) $(EXECUTABLE_DYNAMIC)

.PHONY: shared_Os
shared_Os: add_os $(SRC) $(EXECUTABLE_SHARED)

.PHONY: static_lib
static_lib: $(LIB_SRC) $(STATIC_LIB_FILE)

.PHONY: dynamic_lib
dynamic_lib: $(LIB_SRC) $(DYNAMIC_LIB_FILE)

.PHONY: shared_lib
shared_lib: $(LIB_SRC) $(SHARED_LIB_FILE)

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

$(STATIC_LIB_FILE): $(OUT_FOLDER) $(LIB_OBJECTS_STATIC)
	@echo "STATIC LIBARY: $@"
	$(AR) $@ $(LIB_OBJECTS_STATIC)

$(DYNAMIC_LIB_FILE): $(OUT_FOLDER) $(LIB_OBJECTS_DYNAMIC)
	@echo "DYNAMIC LIBARY: $@"
	$(CC) -fPIC -o $@ $(LIB_OBJECTS_DYNAMIC) -shared  

$(SHARED_LIB_FILE): $(OUT_FOLDER) $(LIB_OBJECTS_SHARED)
	@echo "SHARED LIBARY: $@"
	$(CC) -fPIC -o $@ $(LIB_OBJECTS_SHARED) -shared  

$(OBJ_DIR)/SHARED/%.o: %.c
	@echo "Compiling: $<"
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) $(INC_DIR) $< -o $@

$(OBJ_DIR)/STATIC/%.o: %.c
	@echo "Compiling: $<"
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) $(INC_DIR) $< -o $@

$(OBJ_DIR)/DYNAMIC/%.o: %.c
	@echo "Compiling: $<"
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) -DDYNAMIC -DLIB_PATH=$(DYNAMIC_LIB_FILE) $(INC_DIR) $< -o $@


$(EXECUTABLE_STATIC): $(STATIC_LIB_FILE) $(OUT_FOLDER) $(OBJECTS_STATIC)
	@echo "ECUTABLE: $@"
	$(CC) $(OBJECTS_STATIC) $(LDFLAGS) -o $@ $(STATIC_LIB_FILE)
	
$(EXECUTABLE_SHARED): $(SHARED_LIB_FILE) $(OUT_FOLDER) $(OBJECTS_SHARED)
	@echo "ECUTABLE: $@"
	$(CC) $(OBJECTS_SHARED) $(LDFLAGS) -o $@ $(SHARED_LIB_FILE)

$(EXECUTABLE_DYNAMIC): $(DYNAMIC_LIB_FILE) $(OUT_FOLDER) $(OBJECTS_DYNAMIC)
	@echo "ECUTABLE: $@"
	$(CC) $(OBJECTS_DYNAMIC) $(LDFLAGS) -ldl -o $@