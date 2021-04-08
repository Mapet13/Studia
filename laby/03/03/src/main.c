#include <stdio.h>
#include <stdlib.h>

int* get_eratosthenes_sieve(unsigned int n) {
    int* tab = calloc(n + 1, sizeof(int));

    if (n >= 1) {
        tab[0] = tab[1] = 1;
    }

    unsigned int i;
    for (i = 2; i * i <= n; ++i) {
        if (!tab[i]) {
            unsigned int j;
            for (j = i * i; j <= n; j += i) {
                tab[j] = 1;
            }
        }
    }

    return tab;
}

int check_nr(unsigned int i) {
    unsigned int x;
    while (i != 1 && i != 4) {
        x = i;
        i = 0;
        while (x > 0) {
            unsigned int d = (x % 10);
            i += d * d;
            x /= 10;
        }
    }
    return i == 1;
}

int main(void) {
    unsigned int l, u, k;
    if (scanf("%u %u %u", &l, &u, &k) != 3) {
        return 1;
    }

    // generuje sito do sprawdzania liczb pierwszych
    int* tab = get_eratosthenes_sieve(u);

    unsigned int i;
    for (i = l; i <= u; ++i) {
        // sprawdzam czy jest pierwsza i jednokwadratowa
        if (tab[i] == 0 && check_nr(i)) {
            --k;
            if (k == 0) {
                printf("%u \n", i);
                break;
            }
        }
    }

    if (k != 0) {
        printf("-1 \n");
    }
    free(tab);
    return 0;
}