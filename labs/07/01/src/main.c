#include <stdio.h>
#include <stdlib.h>

void print_binary_representation(int num, unsigned len) {
    for (int i = 1 << (len - 1); i > 0; i >>= 1) {
        printf((num & i) ? "1" : "0");  // just print current bit
    }
    printf("\n");
}

void print_error_message(void) {
    printf("-1\n");
    exit(0);
}

int get_number(unsigned n, unsigned k) {
    int num = 0;
    for (unsigned i = 1; i < k; ++i) {
        do {
            ++num;
        } while ((num & (num >> 1)));  // while there are adjacent 1's

        if (num >= 1 << n) print_error_message();  // out of range
    }
    return num;
}

int main(void) {
    unsigned n, k;
    if (scanf("%u %u", &n, &k) != 2) {
        return 1;
    }

    print_binary_representation(get_number(n, k), n);
}