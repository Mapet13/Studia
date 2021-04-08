#include <stdio.h>
#include <stdlib.h>

#define LEFT(i) ((2 * (i)) + 1)
#define RIGHT(i) ((2 * (i)) + 2)
#define PARENT(i) ((i) / 2)

unsigned int get_matrix_len(void) {
    unsigned int n;
    if (scanf("%u", &n) != 1) {
        exit(1);
    }
    return n;
}

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

int* create_result_array(unsigned int size) {
    int* arr = malloc(size * size * sizeof(*arr));
    if (!arr) {
        exit(1);
    }
    return arr;
}

void swap(int** x, int** y) {
    int* temp = *x;
    *x = *y;
    *y = temp;
}

void heapify(int** heap, unsigned int n, unsigned int i) {
    unsigned int l = LEFT(i);
    unsigned int r = RIGHT(i);
    unsigned int m = i;

    if (l < n && (*heap[l]) < (*heap[m])) m = l;
    if (r < n && (*heap[r]) < (*heap[m])) m = r;
    if (m != i) {
        swap(&heap[i], &heap[m]);
        heapify(heap, n, m);
    }
}

void build_heap(int** arr, unsigned int len) {
    unsigned int i;
    for (i = PARENT(len - 1) + 1; i > 0; --i) {
        heapify(arr, len, i - 1);
    }
}

unsigned int get_index(int* x, int* matrix) {
    return (unsigned int)(x - matrix);  // pointer arithmetic
}

unsigned int fill_res_array(int* res_arr, int* matrix, unsigned int size) {
    // store poiters to actual elements in matrix
    int** heap = malloc(size * sizeof(*heap));
    if (!heap) {
        exit(1);
    }

    unsigned int heap_size = size;
    unsigned int i;
    for (i = 0; i < size; ++i) {
        heap[i] = &matrix[i * size];
    }
    build_heap(heap, size);

    i = 0;  // store current index of result array
    while (heap_size > 0) {
        int* x = heap[0];
        if (i == 0 || res_arr[i - 1] != *x) {
            res_arr[i] = *x;
            ++i;
        }
        unsigned int next_idx = get_index(x, matrix) + 1;
        if (next_idx % size != 0) {
            heap[0] = &matrix[next_idx];
        } else {  // if one of "small" arrays has been fully merged
            --heap_size;
            heap[0] = heap[heap_size];
        }
        heapify(heap, heap_size, 0);
    }

    free(heap);
    return i;  // return actual size of result array
}

void print_result(int* arr, unsigned int len) {
    unsigned int i = 0;
    for (i = 0; i < len; ++i) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main(void) {
    unsigned int matrix_len = get_matrix_len();
    int* matrix = get_matrix(matrix_len);
    int* res_array = create_result_array(matrix_len);

    unsigned int res_array_len = fill_res_array(res_array, matrix, matrix_len);
    print_result(res_array, res_array_len);

    free(res_array);
    free(matrix);
    return 0;
}