#define _USE_MATH_DEFINES
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#define M_E 2.71828182845904523536
#endif

// Kamenetsky’s formula, to get the approximate count of digits n!
unsigned int get_factorial_digit_count(unsigned int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    double result =
        (floor((n * log10(n / M_E) + log10(2 * M_PI * n) / 2.0))) + 1.0;

    return (unsigned int)result;
}

unsigned int* get_factrial_array(unsigned int n) {
    unsigned int* factorial = calloc(n, sizeof(unsigned int));
    if (!factorial) {
        exit(1);
    }

    factorial[0] = 1;
    return factorial;
}

// return carry when factorial have to increase its size
// (happens only when Kamenetsky’s formula failed)
unsigned int multiply(unsigned int* factorial, unsigned int size,
    unsigned int* dc, unsigned int* zc, unsigned int x) {
    unsigned int i = *zc;
    int flag = 1;
    unsigned int carry = 0;

    while (i < *dc) {
        unsigned int a = (factorial[i] * x) + carry;
        carry = a / 10;
        factorial[i] = a % 10;
        if (flag) {
            if (factorial[i] == 0)
                ++(*zc);
            else
                flag = 0;
        }
        ++i;
    }
    while (carry > 0) {
        if (*dc == size) {  // happens only when Kamenetsky’s formula failed
            return carry;
        }
        ++(*dc);
        factorial[i] = carry % 10;
        i += 1;
        carry /= 10;
    }

    return 0;
}

void print_factorial(unsigned int* factorial, unsigned int dc) {
    unsigned int i;
    for (i = 0; i < dc; ++i) {
        printf("%u", factorial[dc - 1 - i]);
    }
    printf("\n");
}

int main(void) {
    unsigned int n;
    if (scanf("%u", &n) != 1) {
        return 1;
    }

    unsigned int digits_count = get_factorial_digit_count(n);
    unsigned int* factorial = get_factrial_array(digits_count);
    unsigned int current_dc = 1;
    unsigned int starting_zeros_count = 0;

    unsigned int i;
    for (i = 1; i <= n; ++i) {
        unsigned int carry = multiply(
            factorial, digits_count, &current_dc, &starting_zeros_count, i);
        while (carry) {  // happens only when Kamenetsky’s formula failed
            ++digits_count;
            ++current_dc;
            factorial = realloc(factorial, digits_count * sizeof(unsigned int));
            factorial[digits_count - 1] = carry;
            carry /= 10;
        }
    }

    print_factorial(factorial, current_dc);

    free(factorial);
}