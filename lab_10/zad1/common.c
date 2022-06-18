#include "common.h"

#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

void err(char* format, ...) {
    char message[BUFFER_SIZE];
    va_list myargs;
    va_start(myargs, format);
    vsprintf(message, format, myargs);
    printf("ERR: %s\n", message);
    va_end(myargs);
    fflush(stdout);
    exit(1);
}

int is_move_mess(const char* msg) {
    return strlen(msg) == 1 && isdigit(msg[0]);
}