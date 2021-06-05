/*
Napisz program, który dla danej liczby całkowitej, n, alokuje tablicę
kwadratową, T[n][n], wypełnia ją kolejnymi liczbami naturalnymi po spirali
zaczynając od lewego górnego rogu a następnie wypisuje ją na standardowe
wyjście.
*/

#include <stdio.h>
#include <stdlib.h>

#define IDX(x, y, n) (((x) * (n)) + (y))

int* get_arr(int n) {
    int* arr = calloc((unsigned)(n * n), sizeof(int));
    if (!arr) {
        exit(1);
    }

    int x = 0, y = 0;
    int dx = 0, dy = 1;
    int i = 1;
    while (arr[IDX(x, y, n)] == 0) {
        arr[IDX(x, y, n)] = i;

        if ((x + dx) >= n || (dx != 0 && arr[IDX(x + dx, y, n)] != 0)) {
            dy = -dx;
            dx = 0;
        }
        if ((y + dy) >= n || (dy != 0 && arr[IDX(x, y + dy, n)] != 0)) {
            dx = dy;
            dy = 0;
        }

        x += dx;
        y += dy;
        ++i;
    }

    return arr;
}

void print_arr(int* arr, int n) {
    int i;
    for (i = 0; i < (n * n); ++i) {
        printf("%d ", arr[i]);
        if ((i + 1) % n == 0) printf("\n");
    }
}

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        return 1;
    }

    int* arr = get_arr(n);

    print_arr(arr, n);

    free(arr);
    return 0;
}