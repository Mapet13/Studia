#include <stdio.h>
#include <stdlib.h>

#define IDX(x, y, n) (((x) * (n)) + (y))
#define MAX(x, y) (((x) > (y)) ? (x) : (y))

unsigned* get_matrix(unsigned x, unsigned y) {
    unsigned* arr = malloc(x * y * sizeof(*arr));
    if (!arr) exit(1);

    for (unsigned i = 0; i < (x * y); ++i) {
        if (scanf("%u", &arr[i]) != 1) {
            exit(1);
        }
    }

    return arr;
}

unsigned calculate_rect(unsigned* matrix, unsigned* pattern, unsigned i,
    unsigned j, unsigned n, unsigned k, unsigned l) {
    unsigned current_sum = 0;
    for (unsigned x = 0; x < k; ++x) {
        for (unsigned y = 0; y < l; ++y) {
            if (pattern[IDX(x, y, l)]) {
                current_sum += matrix[IDX(i + x, j + y, n)];
            }
        }
    }
    return current_sum;
}

unsigned calculate_max_sum(
    unsigned* matrix, unsigned* pattern, unsigned n, unsigned k, unsigned l) {
    unsigned max_sum = 0;
    for (unsigned i = 0; i <= (n - k); ++i) {
        for (unsigned j = 0; j <= (n - l); ++j) {
            max_sum =
                MAX(max_sum, calculate_rect(matrix, pattern, i, j, n, k, l));
        }
    }
    return max_sum;
}

int main(void) {
    unsigned n, k, l;
    if (scanf("%u %u %u", &n, &k, &l) != 3) {
        return 1;
    }
    unsigned* matrix = get_matrix(n, n);
    unsigned* pattern = get_matrix(k, l);

    printf("%d\n", calculate_max_sum(matrix, pattern, n, k, l));

    if (pattern) free(pattern);
    if (matrix) free(matrix);
    return 0;
}