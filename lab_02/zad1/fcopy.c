#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <unistd.h>
#include <time.h>

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

    if(argc != FILE_COUNT + 1) 
        get_files_from_user(files_names);
    else 
        files_names = &(argv[1]); // First arg is program name

    copy_file(files_names); 
}

void get_files_from_user(char** files) {
    int has_input = 0;

    char buffer[BUFFER_SIZE];

    files = calloc(FILE_COUNT, sizeof(*files));
    assert(files);
        
    while (!has_input) {
        puts("Provide file names:");

        for(int i = 0; i < FILE_COUNT; ++i) {
            scanf("%s", buffer);
            files[i] = calloc(strlen(buffer), sizeof(*files[i]));
        }

        // assume that first file must exist
        if( access( files[0], F_OK ) != -1 ) 
            has_input = 0;  
    }
}   

#ifdef SYS_MODE
// todo
#else 

int is_empty(char* line) {
    return strlen(line) == 0 || strcmp(line, "\r") == 0;
}

char* write_without_empty_lines(char* prev_line, char* chunk, size_t read_chars, FILE* out) {
    char* delim = "\n";
    char* line = strtok(chunk, delim);
    
    while (line != NULL) {
        if(!is_empty(line)) {
            puts(line);
        }

        line = strtok(NULL, delim); 
    }

    
    return line;
}

void copy_file(char** files_names) {
    FILE* in = fopen(files_names[0], "r");
    FILE* out = fopen(files_names[1], "w+");

    assert(in && out);

    char chunk[BUFFER_SIZE];
    size_t read_chars;
    char* prev_line = NULL;
    do {
        read_chars = fread(chunk, sizeof(*chunk), BUFFER_SIZE, in);
        prev_line = write_without_empty_lines(prev_line, chunk, read_chars, out);
    } while(read_chars == BUFFER_SIZE);


    fclose(in);
    fclose(out);

}

#endif