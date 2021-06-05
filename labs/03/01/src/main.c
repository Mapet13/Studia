#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    return (*(const int*)a - *(const int*)b);
}

void swap(int* arr, unsigned int x, unsigned int y) {
    int temp = arr[x];
    arr[x] = arr[y];
    arr[y] = temp;
}

int* get_array(unsigned int len) {
    int* arr = malloc(len * sizeof(int));

    unsigned int i;
    for (i = 0; i < len; ++i) {
        if (scanf("%d", &arr[i]) != 1) {
            exit(1);
        }
    }

    return arr;
}

int get_sum(int* arr, unsigned int len) {
    int sum = 0;

    unsigned int i;
    for (i = 0; i < len; ++i) {
        sum += arr[i];
    }

    return sum;
}

int main(void) {
    unsigned int n, k;

    if (scanf("%u %u", &n, &k) != 2) {
        return 1;
    }
    int* array = get_array(n);
    qsort((void*)array, n, sizeof(int), compare);

    // zmniejsze sume najbardziej jeśli wykonam operacje na najwiekszej liczbie
    unsigned int i;
    while (k != 0) {
        i = n - 1;
        array[i] = array[i] / 2;
        while (i > 1 && array[i] < array[i - 1] && (n - 1 - k) < i) {
            swap(array, i, i - 1);
            --i;
        }
        k -= 1;
    }

    printf("%d \n", get_sum(array, n));

    free(array);
    return 0;
}