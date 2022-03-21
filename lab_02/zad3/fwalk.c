#define _XOPEN_SOURCE 500

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <unistd.h> 
#include <sys/stat.h>

/////////////////////////////////////////////////////////////////////////
#define CHECK __log__("CHECK", __TIMESTAMP__, __FILE__, __LINE__)
#define LOG(mess) __log__(mess, __TIMESTAMP__, __FILE__, __LINE__)
void __log__(char* mess, char* time, char* file, int line) {
    printf("%s [%s:%d]: %s\n", time, file, line, mess);
    fflush(stdin);
}
/////////////////////////////////////////////////////////////////////////

typedef struct {
    size_t reg;
    size_t chr;
    size_t dir;
    size_t fifo;
    size_t sock;
} Counter; 

void print_info(const char* dir_path, Counter* counter);

int main(int argc, char** argv) {
    if (argc != 2)
        return -1;
    
    char* root_path = argv[1];  

    Counter* counter = calloc(sizeof(*counter), 1);

    print_info(root_path, counter);

    puts("**********************");
    printf("reg: %ld \n", counter->reg);
    printf("chr: %ld \n", counter->chr);
    printf("dir: %ld \n", counter->dir);
    printf("fifo: %ld \n", counter->fifo);
    printf("sock: %ld \n", counter->sock);
    puts("**********************");

    free(counter);
}

char* get_file_path(const char* dir_path, const char* file_name) {
    char* file_path = malloc((strlen(dir_path) + strlen(file_name) + 2) * sizeof(*file_path)); 
    strcpy(file_path, dir_path);
    strcat(file_path, "/");
    strcat(file_path, file_name);
    return file_path;
}

int is_special(const char* file_name) {
    return strcmp(file_name, ".") == 0 || strcmp(file_name, "..") == 0;
}

void print_info(const char* dir_path, Counter* counter) {
    DIR* dir = opendir(dir_path);    
    
    if(!dir) 
        return;
    
    struct stat stat_buf;

    struct dirent* obj;

    while((obj = readdir(dir))) {
        char* file_path = get_file_path(dir_path, obj->d_name);
        stat(file_path, &stat_buf);

        switch(stat_buf.st_mode & S_IFMT) {
            case S_IFREG: 
                printf("%s: %ld, %d, %ld, %ld, %ld \n", file_path, stat_buf.st_nlink, stat_buf.st_mode, stat_buf.st_size, stat_buf.st_atime, stat_buf.st_mtime);
                (counter->reg)++;
                break;
            case S_IFCHR: 
                (counter->chr)++;
                break;
            case S_IFDIR: 
                if(!is_special(obj->d_name)) {
                    (counter->dir)++;
                    print_info(file_path, counter);
                }
                break;
            case S_IFIFO: 
                (counter->fifo)++;
                break;
            case S_IFSOCK: 
                (counter->sock)++;
                break;
        }

        free(file_path);
    }

    closedir(dir);
}