#include <math.h>  // sqrt
#include <stdio.h>

int main(void) {
    int lower_bound;
    int upper_bound;
    int count = 0;
    int arr[5];  // there are only 5 perfect numbers in range [1, 10^8]

    if (scanf("%d %d", &lower_bound, &upper_bound) != 2) {
        return 1;
    }

    int i;
    for (i = lower_bound; i <= upper_bound; ++i) {
        int current_number_sqrt = sqrt(i);
        int current_sum = 1;

        int divisor = 2;
        while (divisor <= current_number_sqrt && current_sum <= i) {
            if (i % divisor == 0) {
                current_sum += (divisor + (i / divisor));
            }
            ++divisor;
        }

        if (current_sum == i && i != 1) {
            arr[count] = i;
            count += 1;
        }
    }

    printf("%d\n", count);
    for (i = 0; i < count; ++i) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}