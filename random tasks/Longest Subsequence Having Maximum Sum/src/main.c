#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX(x, y) (((x) > (y)) ? (x) : (y))

int* get_array(const int len) {
    int* arr = malloc(sizeof(int) * len);

    srand(time(NULL));

    int i;
    for (i = 0; i < len; ++i) {
        arr[i] = (rand() % 100) - 50;
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

int find_maximum_sum(const int* arr, const int len) {
    int max_sum = 0;
    int current_sum = 0;

    int i = 0;
    for (i = 0; i < len; ++i) {
        current_sum += arr[i];

        if (current_sum < 0) {
            current_sum = 0;
        }

        max_sum = MAX(current_sum, max_sum);
    }

    return max_sum;
}

int main(void) {
    int len;
    printf("Length of array: ");
    scanf("%d", &len);

    int* array = get_array(len);
    print_array(array, len);

    printf("Max sum: %d \n", find_maximum_sum(array, len));

    free(array);

    return 0;
}