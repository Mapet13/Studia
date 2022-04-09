#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

#define BUFFER_SIZE 64

typedef struct {
    char* name;
    char* command;
} Component;

typedef struct {
    Component* components;
    size_t size;
} ComponentArray;

typedef struct {
    char** commands;
    size_t size;
} Command;

typedef struct {
    Command* commands;
    size_t size;
} CommandArray;

typedef struct {
    ComponentArray components_array;
    CommandArray commands_array;
} ParsedData;

//////////////////////////////////////////
// from: https://stackoverflow.com/questions/779875/what-function-is-to-replace-a-substring-from-a-string-in-c
char* replace(
    char* original,
    char* pattern,
    char* replacement) {
    size_t const replen = strlen(replacement);
    size_t const patlen = strlen(pattern);
    size_t const orilen = strlen(original);

    size_t patcnt = 0;
    const char* oriptr;
    const char* patloc;

    // find how many times the pattern occurs in the original string
    for (oriptr = original; patloc = strstr(oriptr, pattern); oriptr = patloc + patlen) {
        patcnt++;
    }

    {
        // allocate memory for the new string
        size_t const retlen = orilen + patcnt * (replen - patlen);
        char* const returned = (char*)malloc(sizeof(char) * (retlen + 1));

        if (returned != NULL) {
            // copy the original string,
            // replacing all the instances of the pattern
            char* retptr = returned;
            for (oriptr = original; patloc = strstr(oriptr, pattern); oriptr = patloc + patlen) {
                size_t const skplen = patloc - oriptr;
                // copy the section until the occurence of the pattern
                strncpy(retptr, oriptr, skplen);
                retptr += skplen;
                // copy the replacement
                strncpy(retptr, replacement, replen);
                retptr += replen;
            }
            // copy the rest of the string.
            strcpy(retptr, oriptr);
        }
		free(original);
        return returned;
    }
}
//////////////////////////////////////////

size_t count_char(const char* str, char target) {
    size_t count = 0;

    while (*str)
        if (*str++ == target) ++count;

    return count;
}

void count_lines(FILE* file, size_t* first_part_size, size_t* second_part_size) {
    size_t* current_counter = first_part_size;

    size_t read = 0;
    size_t len = 0;
    char* line;
    while ((read = getline(&line, &len, file)) != -1) {
        if (strcmp(line, "\n") == 0 || strcmp(line, "\n\r") == 0)
            current_counter = second_part_size;
        else
            ++(*current_counter);
    }

    fseek(file, 0, SEEK_SET);
}

Component parse_line(const char* line) {
    Component* component = malloc(sizeof(*component));

    char* end_of_name = strchr(line, ' ');
    (*end_of_name) = '\0';
    component->name = malloc(sizeof(*(component->name)) * strlen(line) + 1);
    strcpy(component->name, line);

    const size_t command_offset = 3;
    const char* command = end_of_name + command_offset;
    char* end_of_commnad = strchr(command, '\n');
    if (end_of_commnad)
        (*end_of_commnad) = '\0';

    component->command = malloc(sizeof(*(component->command)) * (strlen(command) + 1));
    strcpy(component->command, command);

    return *component;
}

ParsedData parse_file(const char* file_path) {
    FILE* file = fopen(file_path, "r");

    ParsedData data;
    count_lines(file, &data.components_array.size, &data.commands_array.size);

    data.components_array.components = malloc(data.components_array.size * sizeof(*(data.components_array.components)));
    data.commands_array.commands = malloc(data.commands_array.size * sizeof(*(data.commands_array.commands)));

    size_t len = 0;
    char* line;

    for (int i = 0; i < data.components_array.size; ++i) {
        getline(&line, &len, file);
        data.components_array.components[i] = parse_line(line);
    }

    // blank line
    getline(&line, &len, file);

    for (int i = 0; i < data.commands_array.size; ++i) {
        getline(&line, &len, file);

        char* line_cpy = malloc(sizeof(*line_cpy) * (strlen(line) + 1));
        strcpy(line_cpy, line);

		for(int c_id = 0; c_id < data.components_array.size; ++c_id) {
			line_cpy = replace(line_cpy, data.components_array.components[c_id].name, data.components_array.components[c_id].command);
		}

        char* end_of_commands = strchr(line_cpy, '\n');
        if (end_of_commands)
             (*end_of_commands) = '\0';

        Command command;
        command.size = count_char(line_cpy, '|') + 1;
        command.commands = malloc(sizeof(*(command.commands)) * command.size);

        char* end_of_current_command;
        for (size_t j = 0; j < command.size; j++) {
            end_of_current_command = strstr(line_cpy, " | ");

            if (end_of_current_command)
                *end_of_current_command = '\0';

            command.commands[j] = line_cpy;

            if (j + 1 < command.size)
                line_cpy = end_of_current_command + 3;
        }

        data.commands_array.commands[i] = command;
    }

    fclose(file);
    free(line);
	
    return data;
}

void free_data(ParsedData data) {
    for (int i = 0; i < data.commands_array.size; ++i) {
        free(data.commands_array.commands[i].commands[0]);
        free(data.commands_array.commands[i].commands);
    }

    for (int i = 0; i < data.components_array.size; ++i) {
        free(data.components_array.components[i].command);
        free(data.components_array.components[i].name);
    }
}

int** get_fd(size_t size) {
    int** fd = malloc(sizeof(*fd) * size);
    for (int i = 0; i < size; i++) {
        fd[i] = malloc(sizeof(*(fd[i])) * 2);
        if(i != size - 1)
            pipe(fd[i]);
    }

    fd[size - 1][0] = STDIN_FILENO;
    fd[size - 1][1] = STDOUT_FILENO;

    return fd;
}

void fd_free(int** fd, size_t size) {
    for (int i = 0; i < size; i++)
        free(fd[i]);
    free(fd);
}

void do_action(Command command) {
    int** fd = get_fd(command.size);

    for (int i = 0; i < command.size; i++) {
        int prev_id = (i - 1 + command.size) % command.size;

        int pid = fork();
        if (pid == 0) {
            for (int j = 0; j < command.size; ++j) {
                if (j != i && j != prev_id) {
                    if(fd[j][0] != STDIN_FILENO)
                        close(fd[j][0]);
                    if(fd[j][1] != STDOUT_FILENO)
                        close(fd[j][1]);
                }
            }

            if(fd[prev_id][1] != STDOUT_FILENO)
                close(fd[prev_id][1]);
            if(fd[i][0] != STDIN_FILENO)
                close(fd[i][0]);

            if(prev_id != command.size - 1)
                dup2(fd[prev_id][0], STDIN_FILENO);
            dup2(fd[i][1], STDOUT_FILENO);

            char* component = command.commands[i];
            size_t argc = count_char(component, ' ') + 1;
            char** argv = calloc(sizeof(*argv), argc + 1);

            argv[0] = strtok(component, " ");
            for (int i = 1; i < argc; ++i)
                argv[i] = strtok(NULL, " ");


            execvp(argv[0], argv);
            exit(1);
        }
    }

    for (int i = 0; i < command.size-1; ++i) {
        close(fd[i][0]);
        close(fd[i][1]);
    }

    int status = 0;
    while ((wait(&status)) > 0)
        ;

    fd_free(fd, command.size);
}

int main(int argc, char** argv) {
    if (argc != 2)
        return -1;

    const char* file_path = argv[1];
    const ParsedData data = parse_file(file_path);

    for (int i = 0; i < data.commands_array.size; ++i) {
        do_action(data.commands_array.commands[i]);
    }

    free_data(data);
}
