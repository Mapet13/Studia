#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void merge(int* arr, const int x, const int c, const int y) {
    const int temp_len = y + 1 - x;
    int* temp = malloc(sizeof(int) * temp_len);

    int i;
    for (i = 0; i < temp_len; ++i) {
        temp[i] = arr[x + i];
    }

    i = x;
    int l = x;
    int r = c + 1;
    while (l <= c && r <= y) {
        if (temp[l - x] < temp[r - x]) {
            arr[i] = temp[l - x];
            ++l;
        } else {
            arr[i] = temp[r - x];
            ++r;
        }

        ++i;
    }

    while (l <= c) {
        arr[i] = temp[l - x];
        ++l;
        ++i;
    }

    while (r <= c) {
        arr[i] = temp[r - x];
        ++r;
        ++i;
    }

    free(temp);
}

void merge_sort(int* arr, const int x, const int y) {
    if (x < y) {
        const int c = (x + y) / 2;
        merge_sort(arr, x, c);
        merge_sort(arr, c + 1, y);
        merge(arr, x, c, y);
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
    merge_sort(array, 0, len - 1);
    print_array(array, len);

    free(array);

    return 0;
}