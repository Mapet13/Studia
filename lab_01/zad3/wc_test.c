#ifdef DYNAMIC
#include "wc_dynamic_defs.h"
#else
#include "wc_lib.h"
#endif

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/times.h>
#include <time.h>
#include <unistd.h>

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

static struct tms g_tms;
static clock_t g_time;
static FILE* g_timer_output;

CommandDesc read_command(void);
void execute_command(CommandDesc, ArrayWC*);
void timer_start(void);
void timer_check(CommandDesc);
const char* get_command_name(CommandType command);

#ifdef DYNAMIC
void* g_handle;
#endif

int main(void) {
#ifdef DYNAMIC
    g_handle = dlopen("out/libwc_dynamic.so", RTLD_LAZY);
    if (!g_handle) puts("ERROR WHILE LOADING LIBARY");

    if (dlerror() != NULL) puts("ERROR WITH LIBARY");
#endif

    g_timer_output = fopen("timer_result.txt", "w+");
    if (g_timer_output == NULL)
        puts("ERROR WITH CREATING OUTPUT FILE");

    ArrayWC* context = malloc(sizeof(context));

    while (1) {
        printf(">>> ");
        CommandDesc command = read_command();

        if (command.type == invalid) {
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

    if (strcmp(command_in, get_command_name(create_table)) == 0) {
        return create_table;
    } else if (strcmp(command_in, get_command_name(wc_files)) == 0) {
        return wc_files;
    } else if (strcmp(command_in, get_command_name(remove_block)) == 0) {
        return remove_block;
    } else if (strcmp(command_in, get_command_name(print)) == 0) {
        return print;
    } else {
        return invalid;
    }
}

const char* read_command_arguments(void) {
    char* args = calloc(sizeof(*args), INPUT_SIZE);
    fgets(args, INPUT_SIZE, stdin);
    args[strlen(args) - 1] = '\0';
    return args;
}

CommandDesc read_command(void) {
    CommandDesc command;

    command.type = parse_command_type();

    if (command.type != invalid)
        command.arguments = read_command_arguments();

    return command;
}

void create_table_action(CommandDesc command, ArrayWC* array) {
    const size_t size = atoi(command.arguments);

    if (size == 0) {
        puts("WRONG ARGUMENT!");
        return;
    }

#ifdef DYNAMIC
    LOAD_DYNAMIC_FN(g_handle, wc_array_create, ArrayWC, size_t);
    LOAD_DYNAMIC_FN(g_handle, wc_array_destroy, void, ArrayWC*);
#endif

    if (array->data != NULL)
        wc_array_destroy(array);

    timer_start();
    ArrayWC result = wc_array_create(size);
    timer_check(command);

    array->data = result.data;
    array->size = result.size;

    if (array->data == NULL)
        puts("ERROR OCCURES WHILE CREATING TABLE!");
}

void wc_files_action(CommandDesc command, ArrayWC* array) {
#ifdef DYNAMIC
    LOAD_DYNAMIC_FN(g_handle, wc_array_read, ID_type, ArrayWC*, const char*);
#endif

    timer_start();
    wc_array_read(array, command.arguments);
    timer_check(command);
}

int read_id(ID_type* id, const char* argument) {
    if (strcmp(argument, "0")) {
        *id = 0;
    } else {
        *id = atoi(argument);
        if (*id == 0) {
            puts("WRONG ARGUMENT!");
            return -1;
        }
    }

    return 0;
}

void remove_block_action(CommandDesc command, ArrayWC* array) {
    ID_type id;

    if (read_id(&id, command.arguments) == -1) {
        return;
    }

#ifdef DYNAMIC
    LOAD_DYNAMIC_FN(g_handle, wc_array_remove, void, ArrayWC*, ID_type);
#endif

    timer_start();
    wc_array_remove(array, id);
    timer_check(command);
}

void print_action(ArrayWC* array) {
    puts("---------------------");
    for (ID_type i = 0; i < array->size; ++i) {
        printf("%d - [%p]: \n'%s' \n", i, array->data[i], array->data[i]);
    }
    puts("---------------------");
}

void execute_command(CommandDesc command, ArrayWC* array) {
    switch (command.type) {
        case create_table: {
            create_table_action(command, array);
            break;
        }
        case wc_files: {
            wc_files_action(command, array);
            break;
        }
        case remove_block: {
            remove_block_action(command, array);
            break;
        }
        case print: {
            print_action(array);
            break;
        }
        default: {
        }
    }
}

void timer_start(void) {
    g_time = times(&g_tms);
}

double get_time_diff(clock_t start, clock_t end) {
    return (double)(end - start) / (double)sysconf(_SC_CLK_TCK);
}

void write_timer_results(FILE* out, CommandDesc command, double real, double user, double sys) {
    fprintf(out, "----------------------------------\n");
    fprintf(out, "Command: %s %s \n", get_command_name(command.type), command.arguments);
    fprintf(out, "Time Real: %f\n", real);
    fprintf(out, "Time User: %f\n", user);
    fprintf(out, "Time Sys: %f\n", sys);
    fprintf(out, "----------------------------------\n");
}

void timer_check(CommandDesc command) {
    struct tms tms_now;
    clock_t time_end = times(&tms_now);

    double real = get_time_diff(g_time, time_end);
    double user = get_time_diff(g_tms.tms_utime, tms_now.tms_utime);
    double sys = get_time_diff(g_tms.tms_stime, tms_now.tms_stime);

    write_timer_results(stdout, command, real, user, sys);

    if (g_timer_output != NULL)
        write_timer_results(g_timer_output, command, real, user, sys);
}

const char* get_command_name(CommandType command) {
    switch (command) {
        case create_table:
            return "create_table";
        case wc_files:
            return "wc_files";
        case remove_block:
            return "remove_block";
        case print:
            return "print";
        default:
            return "";
    }
}