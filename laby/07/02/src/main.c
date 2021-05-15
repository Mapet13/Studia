#include <stdio.h>
#include <stdlib.h>

#define IDX(x, y, n) (((x) * (n)) + (y))
#define MAX(x, y) (((x) > (y)) ? (x) : (y))

unsigned* get_matrix(unsigned size) {
    unsigned* arr = calloc(size * size, sizeof(*arr));
    if (!arr) exit(1);

    for (unsigned i = 0; i < (size * size); ++i) {
        if (scanf("%u", &arr[i]) != 1) {
            exit(1);
        }
    }

    return arr;
}

int main(void) {
    unsigned n, k;
    if (scanf("%u %u", &n, &k) != 2) {
        return 1;
    }
    unsigned* matrix = get_matrix(n);

    unsigned max_sum = 0;
    unsigned current_sum = 0;

    // top-down
    for (unsigned i = 0; i < n; ++i) {
        current_sum = 0;
        for (unsigned j = 0; j < k; ++j) {
            current_sum += matrix[IDX(j, i, n)];
        }
        max_sum = i == 0 ? current_sum : MAX(max_sum, current_sum);
        for (unsigned j = k; j < n + k - 1; ++j) {
            current_sum -= matrix[IDX(j - k, i, n)];
            current_sum += matrix[IDX(j % n, i, n)];
            max_sum = MAX(max_sum, current_sum);
        }
    }

    // left-right
    for (unsigned i = 0; i < n; ++i) {
        current_sum = 0;
        for (unsigned j = 0; j < k; ++j) {
            current_sum += matrix[IDX(i, j, n)];
        }
        max_sum = MAX(max_sum, current_sum);
        for (unsigned j = k; j < n + k - 1; ++j) {
            current_sum -= matrix[IDX(i, j - k, n)];
            current_sum += matrix[IDX(i, j % n, n)];
            max_sum = MAX(max_sum, current_sum);
        }
    }

    // top-right
    for (unsigned i = 0; i < n; ++i) {
        current_sum = 0;
        for (unsigned j = 0; j < k; ++j) {
            current_sum += matrix[IDX(j, (i + j) % n, n)];
        }
        max_sum = MAX(max_sum, current_sum);
        for (unsigned j = k; j < n + k - 1; ++j) {
            current_sum -= matrix[IDX(j - k, (i + j - k) % n, n)];
            current_sum += matrix[IDX(j % n, (i + j) % n, n)];
            max_sum = MAX(max_sum, current_sum);
        }
    }

    // down-right
    for (unsigned i = 0; i < n; ++i) {
        current_sum = 0;
        for (unsigned j = 0; j < k; ++j) {
            current_sum += matrix[IDX(n - j - 1, ((i + j) % n), n)];
        }
        max_sum = MAX(max_sum, current_sum);
        for (unsigned j = k; j < n + k - 1; ++j) {
            current_sum -=
                matrix[IDX(n - ((j - k) % n) - 1, ((i + j - k) % n), n)];
            current_sum += matrix[IDX(n - (j % n) - 1, ((i + j) % n), n)];
            max_sum = MAX(max_sum, current_sum);
        }
    }

    printf("%d \n", max_sum);

    if (matrix) free(matrix);
    return 0;
}