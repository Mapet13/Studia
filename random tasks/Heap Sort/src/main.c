#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define LEFT(i) ((2 * (i)) + 1)
#define RIGHT(i) ((2 * (i)) + 2)
#define PARENT(i) ((i) / 2)

void swap(int* arr, int x, int y) {
    int temp = arr[x];
    arr[x] = arr[y];
    arr[y] = temp;
}

void heapify(int* arr, int n, int i) {
    int l = LEFT(i);
    int r = RIGHT(i);
    int m = i;

    if (l < n && arr[l] > arr[m]) m = l;
    if (r < n && arr[r] > arr[m]) m = r;
    if (m != i) {
        swap(arr, i, m);
        heapify(arr, n, m);
    }
}

void build_heap(int* arr, int len) {
    int i;
    for (i = PARENT(len - 1); i >= 0; --i) {
        heapify(arr, len, i);
    }
}

void heap_sort(int* arr, int len) {
    build_heap(arr, len);

    unsigned int i;
    for (i = len - 1; i > 0; --i) {
        swap(arr, 0, i);
        heapify(arr, i, 0);
    }
}

int* get_array(const int len) {
    int* arr = malloc(sizeof(int) * len);

    srand(time(NULL));

    int i;
    for (i = 0; i < len; ++i) {
        arr[i] = rand() % 100;
    }

    return arr;
}

void print_array(const int* arr, const int len) {
    printf("[ ");

    int i;
    for (i = 0; i < len; ++i) {
        printf("%d ", arr[i]);
    }

    printf("]\n");
}

int main(void) {
    int len;
    printf("Length of array: ");
    if (scanf("%d", &len) != 1) {
        return 1;
    }

    int* array = get_array(len);

    print_array(array, len);
    heap_sort(array, len);
    print_array(array, len);

    free(array);
    return 0;
}