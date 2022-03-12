#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/times.h>
#include <time.h>
#include <unistd.h>

#include "wc_lib.h"

#define INPUT_SIZE 256

#define LOG \
    log__(stdout, __FILE__, __LINE__)

void log__(FILE* fd, char* file, int line) {
    fprintf(fd, "%s:%d\n", file, line);
}

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

CommandDesc read_command(void);
void execute_command(CommandDesc, ArrayWC*);
void timer_start(void);
void timer_check(void);

int main(void) {
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
}

CommandType parse_command_type(void) {
    char command_in[INPUT_SIZE];
    scanf("%s", command_in);

    if (strcmp(command_in, "create_table") == 0) {
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

void create_table_action(const char* argument, ArrayWC* array) {
    const size_t size = atoi(argument);

    if (size == 0) {
        puts("WRONG ARGUMENT!");
        return;
    }

    if (array->data != NULL)
        wc_array_destroy(array);

    timer_start();
    ArrayWC result = wc_array_create(size);
    timer_check();

    array->data = result.data;
    array->size = result.size;

    if (array->data == NULL)
        puts("ERROR OCCURES WHILE CREATING TABLE!");
}

void wc_files_action(const char* argument, ArrayWC* array) {
    timer_start();
    wc_array_read(array, argument);
    timer_check();
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

void remove_block_action(const char* argument, ArrayWC* array) {
    ID_type id;

    if (read_id(&id, argument) == -1) {
        return;
    }

    timer_start();
    wc_array_remove(array, id);
    timer_check();
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

void timer_check(void) {
    struct tms tms_now;
    clock_t time_end = times(&tms_now);

    printf("Time Real: %f\n", get_time_diff(g_time, time_end));
    printf("Time User: %f\n", get_time_diff(g_tms.tms_utime, tms_now.tms_utime));
    printf("Time Sys: %f\n", get_time_diff(g_tms.tms_stime, tms_now.tms_stime));
}