#include <math.h>
#include <stdio.h>
#include <stdlib.h>

typedef unsigned long DataType;

#define MIN(x, y) (((x) < (y)) ? (x) : (y))

typedef struct {
    DataType* arr;
    unsigned count;
} Array;

Array get_array(unsigned len, DataType G) {
    Array a = { .arr = calloc(len, sizeof(DataType)), .count = 0 };

    DataType temp;
    for (unsigned i = 0; i < len; ++i) {
        if (scanf("%lu", &temp) == 1 && (G | temp) == G) {
            a.arr[a.count] = temp;
            ++a.count;
        }
    }

    return a;
}

unsigned count(Array* T, DataType G) {
    unsigned len = floor(log2((double)G)) + 1;
    unsigned* array = calloc(len, sizeof(unsigned));

    for (unsigned i = 0; i < T->count; ++i) {
        DataType x = 1;
        unsigned j = 0;
        while (x <= T->arr[i]) {
            if ((unsigned)(x & T->arr[i])) array[j] += 1;
            j += 1;
            x <<= 1;
        }
    }

    unsigned result = T->count;
    for (unsigned i = 0; i < len; ++i) {
        if (array[i] > 0) {
            result = MIN(result, array[i]);
            G &= ((1lu << len) - 1lu) & ~(1lu << i);
        };
    }

    return G == 0 ? result : 0;
}

int main(void) {
    unsigned N;
    DataType G;
    if (scanf("%u %lu", &N, &G) != 2) return 1;
    Array T = get_array(N, G);

    printf("%u \n", count(&T, G));

    free(T.arr);
    return 0;
}