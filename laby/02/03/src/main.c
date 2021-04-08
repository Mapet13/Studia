#include <stdio.h>
#include <stdlib.h>

int can_weigh(int* arr, int size, int current, int rest, int idx) {
    if (current == 0) {
        return 1;
    }
    if (idx >= size || current - rest > 0 || current + rest < 0) {
        return 0;
    }

    return can_weigh(arr, size, current - arr[idx], rest - arr[idx], idx + 1) ||
           can_weigh(arr, size, current, rest - arr[idx], idx + 1) ||
           can_weigh(arr, size, current + arr[idx], rest - arr[idx], idx + 1);
}

int main(void) {
    int n;
    int weight;
    int sum = 0;
    if (scanf("%d %d", &n, &weight) != 2) {
        return 1;
    }
    int* arr = malloc(n * sizeof(int));
    int i;
    for (i = 0; i < n; ++i) {
        if (scanf("%d", &arr[i]) != 1) {
            return 1;
        }
        sum += arr[i];
    }

    if (can_weigh(arr, n, weight, sum, 0)) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }

    free(arr);
    return 0;
}