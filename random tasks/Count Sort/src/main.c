#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX(a, b) ((a) > (b) ? (a) : (b))

void count_sort(int* arr, int len, int upper_bound) {
    int* C = malloc(sizeof(int) * upper_bound + 1);
    int* B = malloc(sizeof(int) * len);
    memset(C, 0, sizeof(int) * upper_bound + 1);

    int i;
    for (i = 0; i < len; ++i) ++C[arr[i]];
    for (i = 1; i <= upper_bound; ++i) C[i] += C[i - 1];
    for (i = 0; i < len; ++i) {
        B[C[arr[len - 1 - i]]] = arr[len - 1 - i];
        --C[arr[len - 1 - i]];
    }
    for (i = 0; i < len; ++i) arr[i] = B[i];

    free(B);
    free(C);
}

int get_upper_bound(const int* arr, int len) {
    int current_max = arr[0];
    int i;
    for (i = 1; i < len; ++i) {
        current_max = MAX(arr[i], current_max);
    }
    return current_max;
}

int* get_array(const int len) {
    int* arr = malloc(sizeof(int) * len);

    srand(time(NULL));

    int i;
    for (i = 0; i < len; ++i) {
        arr[i] = rand() % 10;
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
    count_sort(array, len, get_upper_bound(array, len));
    print_array(array, len);

    free(array);
    return 0;
}