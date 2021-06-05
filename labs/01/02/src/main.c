#include <math.h>  // sqrt
#include <stdio.h>
#include <stdlib.h>  // malloc, free
#include <string.h>  // memset

int has_decreasing_digits(int x) {
    int last_digit = x % 10;
    x /= 10;

    while (x > 0) {
        int d = x % 10;
        if (d > last_digit) {
            return 0;  // return false
        }
        x /= 10;
        last_digit = d;
    }

    return 1;  // return true
}

int* get_eratosthenes_sieve(int n) {
    int* tab = malloc((n + 1) * sizeof(int));
    memset(tab, 0, sizeof(int) * n);

    if (n >= 1) {
        tab[0] = tab[1] = 1;
    }

    int i;
    for (i = 2; i <= sqrt(n); ++i) {
        if (!tab[i]) {
            int j;
            for (j = i * i; j <= n; j += i) {
                tab[j] = 1;
            }
        }
    }

    return tab;
}

int main(void) {
    int n;

    if (scanf("%d", &n) != 1) {
        return 1;
    }

    int* tab = get_eratosthenes_sieve(n - 1);

    int i;
    for (i = 0; i < n; ++i) {
        if (tab[i] == 0 && has_decreasing_digits(i)) {
            printf("%d\n", i);
        }
    }

    free(tab);
    return 0;
}