#include <stdio.h>
#include <stdlib.h>

#define IDX(x, y, n) (((x) * (n)) + (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))
#define MAX(x, y) (((x) > (y)) ? (x) : (y))

int* get_matrix(unsigned size, unsigned m) {
    int* arr = calloc(size * size, sizeof(*arr));
    if (!arr) exit(1);

    unsigned p, q;
    for (unsigned i = 0; i < m; ++i) {
        if (scanf("%u %u", &p, &q) != 2) {
            exit(1);
        }

        arr[IDX(MAX(p, q) - 1, MIN(p, q) - 1, size)] = 1;
    }

    return arr;
}

unsigned count_triangles(int* arr, unsigned size) {
    unsigned counter = 0;  // starting with all black triangles
    int current_val;
    for (unsigned i = 1; i < size; ++i) {
        for (unsigned j = 0; j < i; ++j) {
            current_val = arr[IDX(i, j, size)];
            for (unsigned k = 0; k < j; ++k) {
                if (arr[IDX(j, k, size)] == current_val &&
                    arr[IDX(i, k, size)] == current_val) {
                    ++counter;
                }
            }
        }
    }

    return counter;
}

int main(void) {
    unsigned n, m;
    if (scanf("%u %u", &n, &m) != 2) {
        return 1;
    }

    int* arr = get_matrix(n, m);

    printf("%u \n", count_triangles(arr, n));

    if (arr) free(arr);
    return 0;
}