#include <stdio.h>
#include <stdlib.h>

int get_data_count(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        exit(1);
    }
    return n;
}

int main(void) {
    int n = get_data_count();
    int* arr = malloc(n * sizeof(int));
    int left_sum = 0;
    int right_sum = 0;

    int i;
    for (i = 0; i < n; ++i) {
        if (scanf("%d", &arr[i]) != 1) {
            return 1;
        }
        if (i > 0) {
            right_sum += arr[i];
        }
    }

    i = 0;
    while (left_sum != right_sum && i < n) {
        left_sum += arr[i];
        right_sum -= arr[i + 1];
        ++i;
    }

    printf("%d\n", i);

    free(arr);
    return 0;
}