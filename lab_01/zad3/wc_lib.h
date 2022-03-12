#ifndef WC_LIB_H
#define WC_LIB_H

#include <stddef.h>
#include <stdio.h>

typedef unsigned ID_type;
typedef struct {
    char** data;
    ID_type size;
} ArrayWC;

ArrayWC wc_array_create(size_t size);
void wc_array_destroy(ArrayWC* array);

ID_type wc_array_read(ArrayWC* array, const char* file_path);

void wc_array_remove(ArrayWC* array, ID_type id);

#endif