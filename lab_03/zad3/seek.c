#define _XOPEN_SOURCE 500

#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

static size_t g_begin_path_len;

char* seek_in_dir(const char* dir_path, const char* target);

int main(int argc, char** argv) {
    if (argc != 4)
        return -1;

    char* target = argv[2];

    printf("szukana fraza: %s\n", target);

    int deep = atoi(argv[3]);

    char* path = malloc(strlen(argv[1]) + 1);
    strncpy(path, argv[1], strlen(argv[1]) + 1);

    g_begin_path_len = strlen(path);

    while (path && deep > 0) {
        char* next_target = seek_in_dir(path, target);
        free(path);
        path = next_target;
        deep -= 1;
    }

    if (path)
        free(path);

    while (wait(NULL) > 0)
        ;
}

char* get_file_path(const char* dir_path, const char* file_name) {
    char* file_path = malloc((strlen(dir_path) + strlen(file_name) + 2) * sizeof(*file_path));
    strcpy(file_path, dir_path);
    strcat(file_path, "/");
    strcat(file_path, file_name);
    return file_path;
}

int is_special_dir(const char* dir_name) {
    return strcmp(dir_name, ".") == 0 || strcmp(dir_name, "..") == 0;
}

int is_text_file(const char* file_path) {
    return strlen(file_path) > 5 && strcmp(&file_path[strlen(file_path) - 4], ".txt") == 0;
}

void seek_in_file(const char* file_path, const char* target) {
    size_t target_size = strlen(target);
    size_t buffer_size = 2 * target_size;

    size_t read_chars;

    char* chunk = malloc(sizeof(*chunk) * buffer_size);
    FILE* file = fopen(file_path, "r");

    do {
        read_chars = fread(chunk, sizeof(char), buffer_size, file);
        if (read_chars < target_size)
            break;

        if (strstr(chunk, target)) {
            const char* relative_path = &(file_path[g_begin_path_len]);
            printf("[%s] - [%d]\n", relative_path, getpid());
            return;
        }

        fseek(file, -target_size, SEEK_CUR);
    } while (read_chars == buffer_size);

    free(chunk);
    fclose(file);
}

char* seek_in_dir(const char* dir_path, const char* target) {
    DIR* dir = opendir(dir_path);

    if (!dir)
        return NULL;

    struct stat stat_buf;
    struct dirent* obj;

    while ((obj = readdir(dir))) {
        char* file_path = get_file_path(dir_path, obj->d_name);
        stat(file_path, &stat_buf);

        switch (stat_buf.st_mode & S_IFMT) {
            case S_IFREG:
                if (is_text_file(file_path))
                    seek_in_file(file_path, target);
            case S_IFDIR:
                if (!is_special_dir(obj->d_name)) {
                    pid_t pid = fork();
                    if (pid == 0) {  // to avoid unnecesary recrsion
                        return file_path;
                    }
                }
                break;
        }

        free(file_path);
    }

    closedir(dir);
    return NULL;
}