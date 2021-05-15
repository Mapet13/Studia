#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define ERROR_HANDLE_PLACEHOLDER exit(1)

typedef long long Type;

Type get_input(void) {
    Type x;
    if (scanf("%lld", &x) != 1) {
        ERROR_HANDLE_PLACEHOLDER;
    }
    return x;
}

unsigned get_digit_count(Type x) { return (unsigned)floor(log10((double)x)); }

Type get_divisor(unsigned dc) {
    Type divisor = 0;
    for (unsigned i = 0; i <= dc; ++i) {
        divisor *= 10;
        divisor += 1;
    }

    return divisor;
}

Type get_result(Type S, unsigned dc, Type divisor) {
    if (divisor == 1 && S < 10 && S >= 0) {
        return S;
    } else if (divisor == 1) {
        return -1;
    }

    if (divisor > S) {
        return get_result(S, dc - 1, divisor / 10);
    } else {
        Type temp = S / divisor;
        if (temp >= 10) {
            return -1;
        }

        Type res = get_result(S - (divisor * temp), dc - 1, divisor / 10);

        if (res != -1) {
            return (temp * (Type)pow(10, (double)dc)) + res;
        } else {
            return -1;
        }
    }
}

int main(void) {
    Type S = get_input();
    unsigned digit_count = get_digit_count(S);
    Type divisor = get_divisor(digit_count);

    printf("%lld\n", get_result(S, digit_count, divisor));
    return 0;
}