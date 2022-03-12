#define DYNAMIC

#ifdef DYNAMIC
#include "wc_dynamic_defs.h"
#else
#include "wc_lib.h"
#endif

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#ifdef DYNAMIC
#include <dlfcn.h>
#endif

#define INPUT_SIZE 256

typedef enum {
    invalid,
    create_table,
    wc_files,
    print,
    remove_block
} CommandType;

typedef struct {
    CommandType type;
    const char* arguments;
} CommandDesc;


CommandDesc read_command(void); 
void execute_command(CommandDesc, ArrayWC*);

#ifdef DYNAMIC
void *g_handle;
#endif

int main(void) {
    #ifdef DYNAMIC
    g_handle = dlopen("libwc_dynamic.so", RTLD_LAZY);
    if(!g_handle) puts("ERROR WHILE LOADING LIBARY");

    if(dlerror() != NULL) puts("ERROR WITH LIBARY");
    #endif


    ArrayWC* context = malloc(sizeof(context));

    while(1) {
        printf(">>> ");
        CommandDesc command = read_command();

        if(command.type == invalid) {
            printf("INVALID COMMAND!\n");
        }
        if ((context->data == NULL) && command.type != create_table) {
            printf("ERROR: You need to create_table first!\n");
        } else {
            execute_command(command, context);
        }
    }
    
    #ifdef DYNAMIC
    dlclose(g_handle);
    #endif
}

CommandType parse_command_type(void) {
    char command_in[INPUT_SIZE];
    scanf("%s", command_in);
    
    if(strcmp(command_in, "create_table") == 0) {
        return create_table;
    } else if (strcmp(command_in, "wc_files") == 0) {
        return wc_files;
    } else if (strcmp(command_in, "remove_block") == 0) {
        return remove_block;
    } else if (strcmp(command_in, "print") == 0) {
        return print;
    } else {
        return invalid;
    }
}

const char* read_command_arguments(void) {
    char* args = calloc(sizeof(*args), INPUT_SIZE);
    fgets(args, INPUT_SIZE, stdin);
    args[strlen(args)-1] = '\0';
    return args;
}

CommandDesc read_command(void) {
    CommandDesc command;

    command.type = parse_command_type();

    if (command.type != invalid)
        command.arguments = read_command_arguments();
    
    return command;
}

void create_table_action(const char* argument, ArrayWC* array) {
    const size_t size = atoi(argument);
    
    if(size == 0) {
        puts("WRONG ARGUMENT!");
        return;
    }

    #ifdef DYNAMIC
    LOAD_DYNAMIC_FN(g_handle, wc_array_create, ArrayWC, size_t);
    LOAD_DYNAMIC_FN(g_handle, wc_array_destroy, void, ArrayWC*);
    #endif

    if(array->data != NULL)
        wc_array_destroy(array);    

    ArrayWC result = wc_array_create(size);

    array->data = result.data;
    array->size = result.size;

    if(array->data == NULL)
        puts("ERROR OCCURES WHILE CREATING TABLE!");
}

void wc_files_action(const char* argument, ArrayWC* array) {
    #ifdef DYNAMIC
    LOAD_DYNAMIC_FN(g_handle, wc_array_read, ID_type, ArrayWC*, const char*);
    #endif

    wc_array_read(array, argument);
}

int read_id(ID_type* id, const char* argument) {
    if(strcmp(argument, "0")) {
        *id = 0;
    } else {
        *id = atoi(argument);
        if(*id == 0) {
            puts("WRONG ARGUMENT!");
            return -1;
        }
    }

    return 0;
}

void remove_block_action(const char* argument, ArrayWC* array) {
    ID_type id;
    
    if (read_id(&id, argument) == -1) {
        return;
    } 

    #ifdef DYNAMIC
    LOAD_DYNAMIC_FN(g_handle, wc_array_remove, void, ArrayWC*, ID_type);
    #endif
    
    wc_array_remove(array, id);
}

void print_action(ArrayWC* array) {
    puts("---------------------");
    for(ID_type i = 0; i < array->size; ++i) {
        printf("%d - [%p]: \n'%s' \n", i, array->data[i], array->data[i]);
    }
    puts("---------------------");
}

void execute_command(CommandDesc command, ArrayWC* array) {
    switch(command.type) {
    case create_table: {
        create_table_action(command.arguments, array);
        break;
    }
    case wc_files: {
        wc_files_action(command.arguments, array);
        break;
    }
    case remove_block: {
        remove_block_action(command.arguments, array);
        break;
    }
    case print: {
        print_action(array);
    }
    default: {}
    }
}