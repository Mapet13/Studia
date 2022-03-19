#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define FILE_COUNT 2
#define BUFFER_SIZE 256

/////////////////////////////////////////////////////////////////////////
#define CHECK __log__("CHECK", __TIMESTAMP__, __FILE__, __LINE__)
#define LOG(mess) __log__(mess, __TIMESTAMP__, __FILE__, __LINE__)
void __log__(char* mess, char* time, char* file, int line) {
    printf("%s [%s:%d]: %s\n", time, file, line, mess);
    fflush(stdin);
}
/////////////////////////////////////////////////////////////////////////

void get_files_from_user(char** files);
void copy_file(char** files_names);

int main(int argc, char** argv) {
    char** files_names;

    if (argc != FILE_COUNT + 1)
        get_files_from_user(files_names);
    else
        files_names = &(argv[1]);  // First arg is program name

    copy_file(files_names);
}

void get_files_from_user(char** files) {
    int has_input = 0;

    char buffer[BUFFER_SIZE];

    files = calloc(FILE_COUNT, sizeof(*files));
    assert(files);

    while (!has_input) {
        puts("Provide file names:");

        for (int i = 0; i < FILE_COUNT; ++i) {
            scanf("%s", buffer);
            files[i] = calloc(strlen(buffer), sizeof(*files[i]));
        }

        // assume that first file must exist
        if (access(files[0], F_OK) != -1)
            has_input = 0;
    }
}

#ifdef SYS_MODE
// todo
#else

int is_empty(char* line) {
    // LF || CRLF
    return strlen(line) == 0 || strcmp(line, "\r") == 0;
}

int is_first_line_empty(char* str) {
    return str[0] == '\n' || strncmp(str, "\r\n", 2) == 0;
}

void append_new_line_to_file(FILE* out) {
    fwrite("\n", sizeof(char), 1, out);
} 

int write_without_empty_lines(char* chunk, size_t read_chars, FILE* out, int was_last_endl) {
    char* str = malloc(sizeof(*str) * (read_chars + 1));
    strncpy(str, chunk, read_chars);
    
    char last = chunk[read_chars-1];

    if(!was_last_endl && is_first_line_empty(chunk)) 
        append_new_line_to_file(out);
    
    char* delim = "\n";
    char* line = strtok(str, delim);
    
    char* next_line;
    
    while(line) {
        next_line = strtok(NULL, delim);

        if(!is_empty(line)) {
            if(!next_line && !(last == '\n' || last == 0)) {
                was_last_endl = 0;
                fwrite(line, sizeof(char), strlen(line), out);
            }
            else {
                was_last_endl = 1;
                fwrite(line, sizeof(char), strlen(line), out);
                append_new_line_to_file(out);
            }
         }

        line = next_line;
    }


    free(str);
    return was_last_endl;
}
    
void copy_file(char** files_names) {
    FILE* in = fopen(files_names[0], "r");
    FILE* out = fopen(files_names[1], "w+");

    assert(in && out);

    char chunk[BUFFER_SIZE];
    int was_last_endl = 1;
    size_t read_chars;
    do {
        read_chars = fread(chunk, sizeof(*chunk), BUFFER_SIZE, in);
        was_last_endl = write_without_empty_lines(chunk, read_chars, out, was_last_endl);
    } while (read_chars == BUFFER_SIZE);

    fclose(in);
    fclose(out);
}

#endif