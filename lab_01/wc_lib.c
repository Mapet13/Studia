#include "wc_lib.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// ----UTILITIES--------------------------
ID_type find_first_free_id(ArrayWC* array);
char* read_whole_file(const char* file_name);
// ---------------------------------------

ArrayWC wc_array_create(size_t size) {
    ArrayWC array;

    array.data = calloc(sizeof(*(array.data)), size);
    array.size = size;

    return array;
}

void wc_array_destroy(ArrayWC* array) {
    free(array->data);
}

// if returned i == array->size there was an error
ID_type wc_array_read(ArrayWC* array, const char* files_paths) {
    const ID_type ERROR_CODE = array->size;
    
    const ID_type id = find_first_free_id(array);

    if(id == ERROR_CODE)
        return ERROR_CODE;

    char file_name[L_tmpnam];
    tmpnam(file_name);

    const size_t additional_commnad_buffer_size = 9;
    char* command = calloc(sizeof(*command), additional_commnad_buffer_size + strlen(files_paths) + strlen(file_name));
    sprintf(command,"wc %s > %s", files_paths, file_name); 
    system(command);

    array->data[id] = read_whole_file(file_name);

    if(array->data[id] == NULL)
        return ERROR_CODE;

    return id;
}

void wc_array_remove(ArrayWC* array, ID_type id) {
    if (id >= array->size)
        return;

    free(array->data[id]);
    array->data[id] = NULL;
}

// ----UTILITIES--------------------------
ID_type find_first_free_id(ArrayWC* array) {
    for (ID_type i = 0; i < array->size; ++i)
        if(array->data[i] == NULL) 
            return i;

    return array->size;
}

char* read_whole_file(const char* file_name) {
    FILE* file = fopen(file_name, "r");

    if(file == NULL)
        return NULL;

    fseek(file, 0, SEEK_END);
    long fsize = ftell(file);
    rewind(file);

    char *str = calloc(sizeof(*str), fsize + 1);
    fread(str, fsize, 1, file);

    fclose(file);

    return str;
}
// ---------------------------------------