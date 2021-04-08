#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    return (*(const int*)a - *(const int*)b);
}

int* get_array(unsigned int len) {
    int* arr = calloc(len, sizeof(int));

    unsigned int i;
    for (i = 0; i < len; ++i) {
        if (scanf("%d", &arr[i]) != 1) {
            exit(1);
        }
    }

    return arr;
}

int main(void) {
    unsigned int n;
    int k;
    if (scanf("%u %d", &n, &k) != 2) {
        return 1;
    }
    int* array = get_array(n);
    qsort((void*)array, n, sizeof(int), compare);  // sortuje liczby niemalejąco

    unsigned int j;
    unsigned int i = 0;
    unsigned int counter = 0;
    while (i < n) {
        j = i + 1;

        // szukam liczby wiekszej od array[i]
        while (j < n && array[i] == array[j]) {
            ++j;
        }

        // sprawdzam czy liczby stanowią parę
        if (j < n && array[j] - array[i] <= k) {
            unsigned int x = j;
            while (j < n && array[x] == array[j]) {
                ++j;
            }
            counter += j - i;  // zwiekszam licznik o ilośc wystapien obu liczb
        } else if (i > 0 && array[i] - array[i - 1] <= k) {
            counter += j - i;  // sprawdzam poprzednią liczbę
        }
        i = j;
    }

    printf("%u \n", counter);

    free(array);
    return 0;
}