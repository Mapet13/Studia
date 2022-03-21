#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <fcntl.h> 
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/times.h>
#include <time.h>
#include <unistd.h>

#define BUFFER_SIZE 256

#ifdef SYS_MODE
typedef int FILE_HANDLER;
#else
typedef FILE* FILE_HANDLER;
#endif

static clock_t g_time;
void timer_start(void);
void timer_check();

void count_in_file(char* file_name, char demanded);
size_t my_read(FILE_HANDLER file, char* str, size_t size);

int main(int argc, char** argv) {
    if (argc != 3)
        return -1;
    
    char* file_name = argv[2];  
    char character = *(argv[1]);  

    timer_start();
    count_in_file(file_name, character);
    timer_check();
}

int count_demanded(char demanded, char* chunk, size_t read_chars, size_t* char_count, size_t* line_count, int was_counted) {
    for(size_t i = 0; i < read_chars; ++i ) {
        if(chunk[i] == demanded) {
            (*char_count)++;
            was_counted = 1;
        }
        if(chunk[i] == '\n') {
            if(was_counted)
                (*line_count)++;
            was_counted = 0;
        }
    }

    return was_counted;
}

void count_in_file(char* file_name, char demanded) {
    #ifdef SYS_MODE
        FILE_HANDLER file = open(file_name, O_RDONLY);
    #else
        FILE_HANDLER file = fopen(file_name, "r");
    #endif

    int was_counted = 0;
    
    size_t char_count = 0;
    size_t line_count = 0;

    char chunk[BUFFER_SIZE];
    size_t read_chars;

    do {
        #ifdef SYS_MODE
            read_chars = read(file, chunk, BUFFER_SIZE);
        #else
            read_chars =  fread(chunk, sizeof(char), BUFFER_SIZE, file);
        #endif

        was_counted = count_demanded(demanded, chunk, read_chars, &char_count, &line_count, was_counted);
    } while (read_chars == BUFFER_SIZE);


    printf("Character was present %ld times in %ld lines\n", char_count, line_count);

    #ifdef SYS_MODE
        close(file);
    #else
        fclose(file);
    #endif
}

////////////////////////////////////////////////////////////////////////////////
void timer_start(void) {
    struct tms tms_now;
    g_time = times(&tms_now);
}

double get_time_diff(clock_t start, clock_t end) {
    return (double)(end - start) / (double)sysconf(_SC_CLK_TCK);
}

void write_timer_results(FILE* out, double real) {
    fprintf(out, "----------------------------------\n");
    fprintf(out, "Time Real: %f\n", real);
    fprintf(out, "----------------------------------\n");
}

void timer_check() {
    struct tms tms_now;
    clock_t time_end = times(&tms_now);

    double real = get_time_diff(g_time, time_end);
    write_timer_results(stdout, real);
}
////////////////////////////////////////////////////////////////////////////////