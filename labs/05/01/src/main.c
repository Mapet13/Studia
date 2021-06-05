/*
Dane jest pole w kształcie kwadratu o boku n. Pole jest podzielone na n
kwadratów o boku 1. Każdy kwadrat jest albo użytkowy, albo nieużytkowy. Na polu
wyznaczamy działkę. Ma ona kształt prostokąta i może się składać wyłącznie z
kwadratów użytkowych. Powierzchnia działki jest równa polu odpowiadającego jej
prostokąta. Szukamy działki o jak największej powierzchni.
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX(x, y) (((x) > (y)) ? (x) : (y))

unsigned int* get_matrix(unsigned int size) {
    unsigned int* arr = malloc(size * size * sizeof(*arr));
    if (!arr) {
        exit(1);
    }

    // using array linearization technique
    unsigned int i;
    for (i = 0; i < (size * size); ++i) {
        if (scanf("%u", &arr[i]) != 1) {
            exit(1);
        }
    }

    return arr;
}

unsigned int calculate_current_max_area(unsigned int* arr, unsigned int size) {
    unsigned int current_max = 0;

    unsigned int max_height = 0;
    unsigned int i;
    for (i = 0; i < size; ++i) {
        max_height = MAX(max_height, arr[i]);
    }

    unsigned int height, current_width;
    for (height = 1; height <= max_height; ++height) {
        current_width = 0;
        for (i = 0; i < size; ++i) {
            if (arr[i] < height) {
                current_max = MAX(current_max, current_width * height);
                current_width = 0;
            } else {
                current_width += 1;
            }
        }
        current_max = MAX(current_max, current_width * height);
    }

    return MAX(current_max, current_width * max_height);
}

unsigned int get_max_area(unsigned int* matrix, unsigned int size) {
    unsigned int* arr =
        calloc(size, sizeof(*arr));  // for dynamic programming purposes
    if (!arr) {
        exit(1);
    }

    unsigned int max_area = 0;

    unsigned int i;
    for (i = 0; i < size * size; ++i) {
        if (matrix[i]) {
            arr[i % size] = 0;
        } else {
            arr[i % size] += 1;
        }

        if (i % size == (size - 1)) {  // check each row
            max_area = MAX(max_area, calculate_current_max_area(arr, size));
        }
    }

    free(arr);
    return max_area;
}

int main(void) {
    unsigned int n;
    if (scanf("%u", &n) != 1) {
        return 1;
    }
    unsigned int* matrix = get_matrix(n);

    unsigned int max_area = get_max_area(matrix, n);

    printf("%u \n", max_area);

    free(matrix);
    return 0;
}