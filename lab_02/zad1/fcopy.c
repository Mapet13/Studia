#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <fcntl.h> 
#include <sys/types.h>
#include <sys/stat.h>

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

#ifdef SYS_MODE
typedef int FILE_HANDLER;
#else
typedef FILE* FILE_HANDLER;
#endif

void get_files_from_user(char** files);
void copy_file(char** files_names);
void my_write(FILE_HANDLER file, char* str, size_t size);
size_t my_read(FILE_HANDLER file, char* str, size_t size);

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

int is_empty(char* line) {
    // LF || CRLF
    return strlen(line) == 0 || strcmp(line, "\r") == 0;
}

int is_first_line_empty(char* str) {
    return str[0] == '\n' || strncmp(str, "\r\n", 2) == 0;
}

void append_new_line_to_file(FILE_HANDLER out) {
    my_write(out, "\n", 1);
}

int write_without_empty_lines(char* chunk, size_t read_chars, FILE_HANDLER out, int was_last_endl) {
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
                my_write(out, line, strlen(line));
            }
            else {
                was_last_endl = 1;
                my_write(out, line, strlen(line));
                append_new_line_to_file(out);
            }
         }

        line = next_line;
    }

    free(str);
    return was_last_endl;
}


void copy_file(char** files_names) {
    #ifdef SYS_MODE
        FILE_HANDLER in = open(files_names[0], O_RDONLY);
        FILE_HANDLER out = open(files_names[1], O_WRONLY | O_CREAT);
    #else
        FILE* in = fopen(files_names[0], "r");
        FILE* out = fopen(files_names[1], "w+");
    #endif


    char chunk[BUFFER_SIZE];
    int was_last_endl = 1;
    size_t read_chars;
    do {
        read_chars = my_read(in, chunk, BUFFER_SIZE);
        was_last_endl = write_without_empty_lines(chunk, read_chars, out, was_last_endl);
    } while (read_chars == BUFFER_SIZE);

    #ifdef SYS_MODE
        close(in);
        close(out);
    #else
        fclose(in);
        fclose(out);
    #endif
}

#ifdef SYS_MODE
void my_write(FILE_HANDLER file, char* str, size_t size) {
    write(file, str, size);
}
size_t my_read(FILE_HANDLER file, char* str, size_t size) {
    return read(file, str, size);
} 
#else
void my_write(FILE_HANDLER file, char* str, size_t size) {
    fwrite(str, sizeof(char), size, file);
}
size_t my_read(FILE_HANDLER file, char* str, size_t size) {
    return fread(str, sizeof(char), size, file);
}
#endif