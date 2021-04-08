#include <stdio.h>
#include <stdlib.h>

#define IDX(x, y, n) (((x) * (n)) + (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))
#define MAX(x, y) (((x) > (y)) ? (x) : (y))

int* get_matrix(unsigned int size) {
    int* arr = malloc(size * size * sizeof(int));
    if (!arr) {
        exit(1);
    }

    // using array linearization technique
    unsigned int i;
    for (i = 0; i < (size * size); ++i) {
        if (scanf("%d", &arr[i]) != 1) {
            exit(1);
        }
    }

    return arr;
}

int* create_result_matrix(unsigned int size) {
    int* arr = malloc(size * size * sizeof(*arr));
    if (!arr) {
        exit(1);
    }
    return arr;
}

int get_cell_neighbours_sum(int* matrix, int size, int radius, int x, int y) {
    int i, j;
    int sum = 0;

    for (i = MAX(0, x - radius); i < MIN(size, x + (radius + 1)); ++i) {
        for (j = MAX(0, y - radius); j < MIN(size, y + (radius + 1)); ++j) {
            sum += matrix[IDX(i, j, size)];
        }
    }

    return sum;
}

void fill_result_matrix(int* res, int* matrix, int size, int radius) {
    int x, y;
    for (x = 0; x < size; ++x) {
        for (y = 0; y < size; ++y) {
            res[IDX(x, y, size)] =
                get_cell_neighbours_sum(matrix, size, radius, x, y);
        }
    }
}

void print_result(int* matrix, int size) {
    int i, j;
    for (i = 0; i < size; ++i) {
        for (j = 0; j < size; ++j) {
            printf("%d ", matrix[IDX(i, j, size)]);
        }
        printf("\n");
    }
}

int main(void) {
    int n, r;
    if (scanf("%d %d", &n, &r) != 2) {
        return 1;
    }

    int* matrix = get_matrix((unsigned)n);
    int* res_matrix = create_result_matrix((unsigned)n);

    fill_result_matrix(res_matrix, matrix, n, r);
    print_result(res_matrix, n);

    free(matrix);
    free(res_matrix);
    return 0;
}