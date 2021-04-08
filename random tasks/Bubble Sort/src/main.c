/*
Input: Size of the array

It allocates an array with an random values,
then sorting it with the Bubble Sort method.
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int* arr, const int x, const int y) {
    const int temp = arr[y];
    arr[y] = arr[x];
    arr[x] = temp;
}

void bouble_sort(int* arr, const int len) {
    int i;
    int j;

    for (i = 0; i < (len - 1); ++i) {
        for (j = 0; j < (len - 1 - i); ++j) {
            if (arr[j] > arr[j + 1]) {
                swap(arr, j, j + 1);
            }
        }
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
    scanf("%d", &len);

    int* array = get_array(len);

    print_array(array, len);
    bouble_sort(array, len);
    print_array(array, len);

    free(array);

    return 0;
}
