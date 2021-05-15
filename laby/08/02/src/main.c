#include <stdio.h>
#include <stdlib.h>

#define ERROR_HANDLE_PLACEHOLDER exit(1)

typedef unsigned long long Type;

Type sum(Type x) {
    if (x == 1) return x;
    if (x % 2) return (((x + 1) * (x + 1)) / 4 + sum(x / 2));
    return ((x * x / 4) + sum(x / 2));
}

int main(void) {
    Type n;
    if (scanf("%llu", &n) != 1) {
        ERROR_HANDLE_PLACEHOLDER;
    }

    Type result = sum(n);

    printf("%llu\n", result);

    return 0;
}