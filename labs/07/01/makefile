#remove all default echoes
ifndef VERBOSE
.SILENT:
endif

#Vars
CC         := gcc
CFLAGS     := -c -std=gnu11 -pedantic -Wall \
			-Wno-missing-braces -Wextra -Wno-missing-field-initializers -Wformat=2 \
			-Wswitch-default -Wswitch-enum -Wcast-align -Wpointer-arith \
			-Wbad-function-cast -Wstrict-overflow=5 -Winline \
			-Wundef -Wnested-externs -Wcast-qual -Wshadow -Wunreachable-code \
			-Wlogical-op -Wfloat-equal -Wstrict-aliasing=2 -Wredundant-decls \
			-Wold-style-definition \
			-Wconversion \
			-ggdb3 \
			-O2 \
			-Werror=implicit-function-declaration \
			-fno-omit-frame-pointer -ffloat-store -fno-common -fstrict-aliasing

INC_DIR    := -Isrc
LDFLAGS    := -lm
SRC 	   := $(wildcard src/*.c) \
			  $(wildcard src/*/*.c) \
			  $(wildcard src/*/*/*.c)
OBJ_DIR    := obj
OBJECTS    := $(SRC:%.c=$(OBJ_DIR)/%.o)
EXE_NAME   := app
OUT_FOLDER := out
EXECUTABLE := $(OUT_FOLDER)/$(EXE_NAME)

#default compile and link into exe
.PHONY: default
default: $(SRC) $(EXECUTABLE)

#clean, compile and link into exe
.PHONY: all
all: clean default

#default compile, link into exe and then run it
.PHONY: run
run: default
	$(V)-cp $(EXECUTABLE) $(EXECUTABLE) 1>&2 2>/dev/null || :
	$(V)chmod +x $(EXECUTABLE)
	$(V)-cd ./$(OUT_FOLDER) ; ./$(EXE_NAME) $(PARAMS)

#print all sources and tests files
.PHONY: info
info:
	@echo "\033[92mSources:\033[0m"
	@echo "\033[0;36m\t$(subst ${NULL} ${NULL},\n\t,$(SRC))\033[m"

#clean all .o and the exe files
.PHONY: clean
clean:
	@echo "\033[0;31mCleaning...\033[m"
	-rm -f -r $(OBJ_DIR)/*
	-rm -f -r $(EXECUTABLE)

#check memory
.PHONY: memcheck
memcheck: default
	valgrind -s --leak-check=full ./$(EXECUTABLE)
	
 
#print all comments you allow to use
.PHONY: help
help:
	@echo "\033[0;33minfo\033[m"
	@echo "\033[0;33mrun\033[m"
	@echo "\033[0;33mall\033[m"
	@echo "\033[0;33mclean\033[m"
	@echo "\033[0;33mmemcheck\033[m"

$(OUT_FOLDER):
	mkdir -p $@

#link into exe
$(EXECUTABLE): $(OUT_FOLDER) $(OBJECTS)
	@echo "\033[0;32mEXECUTABLE:\033[m\033[0;34m $@\033[m"
	$(CC) $(OBJECTS) $(LDFLAGS) -o $@

#compile
$(OBJ_DIR)/%.o: %.c
	@echo "\033[0;33mCompiling:\033[m\033[0;36m $<\033[m"
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) $(INC_DIR) $< -o $@
	