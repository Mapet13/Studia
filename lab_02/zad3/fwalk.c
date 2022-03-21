#define _XOPEN_SOURCE 500

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <unistd.h> 
#include <sys/stat.h>
#include <ftw.h>

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

Counter* g_counter;

void print_info(const char* dir_path);

int main(int argc, char** argv) {
    if (argc != 2)
        return -1;
    
    char* root_path = argv[1];  

    g_counter = calloc(sizeof(*g_counter), 1);

    print_info(root_path);

    puts("**********************");
    printf("reg: %ld \n", g_counter->reg);
    printf("chr: %ld \n", g_counter->chr);
    printf("dir: %ld \n", g_counter->dir);
    printf("fifo: %ld \n", g_counter->fifo);
    printf("sock: %ld \n", g_counter->sock);
    puts("**********************");

    free(g_counter);
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

#ifdef NFTW_MODE
int action(const char* file_path, const struct stat* stat_buf, int fileflags, struct FTW* pfwt) {
    switch(stat_buf->st_mode & S_IFMT) {
        case S_IFREG: 
            printf("%s: %ld, %d, %ld, %ld, %ld \n", file_path, stat_buf->st_nlink, stat_buf->st_mode, stat_buf->st_size, stat_buf->st_atime, stat_buf->st_mtime);
            g_counter->reg++;
            break;
        case S_IFCHR: 
            g_counter->chr++;
            break;
        case S_IFDIR: 
            g_counter->dir++;
            break;
        case S_IFIFO: 
            g_counter->fifo++;
            break;
        case S_IFSOCK: 
            g_counter->sock++;
            break;
    }
    return 0;
}

void print_info(const char* dir_path) {
    nftw(dir_path, &action, 100, 0);
}
#else
void print_info(const char* dir_path) {
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
                g_counter->reg++;
                break;
            case S_IFCHR: 
                g_counter->chr++;
                break;
            case S_IFDIR: 
                if(!is_special(obj->d_name)) {
                    g_counter->dir++;
                    print_info(file_path);
                }
                break;
            case S_IFIFO: 
                g_counter->fifo++;
                break;
            case S_IFSOCK: 
                g_counter->sock++;
                break;
        }

        free(file_path);
    }

    closedir(dir);
}
#endif