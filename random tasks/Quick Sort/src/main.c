#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int* arr, int x, int y) {
    int temp = arr[x];
    arr[x] = arr[y];
    arr[y] = temp;
}

int partition(int* arr, int p, int r) {
    int pivot = arr[r];
    int i = p;
    int j;
    for (j = p; j < r; ++j) {
        if (arr[j] <= pivot) {
            swap(arr, i, j);
            ++i;
        }
    }
    swap(arr, i, r);
    return i;
}

void quick_sort(int* arr, int p, int r) {
    int q;
    while (p < r) {
        q = partition(arr, p, r);
        quick_sort(arr, p, q - 1);
        p = q + 1;
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
    quick_sort(array, 0, len - 1);
    print_array(array, len);

    free(array);

    return 0;
}