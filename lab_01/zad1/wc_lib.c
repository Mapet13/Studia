#include "wc_lib.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// ----UTILITIES--------------------------
typedef struct {
    FILE* handle;
    const char* name;
} FileDesc;

ID_type find_first_free_id(ArrayWC* array);
int create_temp_file(FileDesc* file);
char* read_whole_file(FILE* file);
// ---------------------------------------

ArrayWC wc_array_create(size_t size) {
    ArrayWC array;
    array.data = calloc(size, sizeof(*(array.data)));
    array.size = size;

    return array;
}

void wc_array_destroy(ArrayWC* array) {
    free(array->data);
    free(array);
}

// if returned i == array->size there was an error
ID_type wc_array_read(ArrayWC* array, const char* files_paths) {
    const ID_type ERROR_CODE = array->size;
    
    const ID_type id = find_first_free_id(array);

    FileDesc tmp;
    if (id == ERROR_CODE || create_temp_file(&tmp) == -1)
        return ERROR_CODE;


    const size_t additional_commnad_buffer_size = 9;
    char* command = calloc(sizeof(*command), additional_commnad_buffer_size + strlen(files_paths) + strlen(tmp.name));
    sprintf(command,"wc %s > %s", files_paths, tmp.name); 
    system(command);

    array->data[id] = read_whole_file(tmp.handle);

    fclose(tmp.handle);
    return id;
}

void wc_array_remove(ArrayWC* array, ID_type id) {
    if (id >= array->size)
        return;

    free(array->data[id]);
}

// ----UTILITIES--------------------------
ID_type find_first_free_id(ArrayWC* array) {
    for (ID_type i = 0; i < array->size; ++i)
        if(array->data[i] == NULL) 
            return i;

    return array->size;
}

int create_temp_file(FileDesc* file) {
    char buffer [L_tmpnam];
    tmpnam(buffer);

    file->handle = fopen(buffer, "w+");
    
    if (file->handle == NULL)
        return -1;

    file->name = buffer;

    return 0;
}

char* read_whole_file(FILE* file) {
    fseek(file, 0, SEEK_END);
    long fsize = ftell(file);
    rewind(file);

    char *str = calloc(sizeof(*str), fsize + 1);
    fread(str, fsize, 1, file);
    
    return str;
}
// ---------------------------------------