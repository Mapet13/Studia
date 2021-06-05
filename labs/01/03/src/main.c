#include <stdio.h>

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        return 1;
    }

    int a = 0;
    int b = 1;
    int c;
    while (a * b < n) {
        c = a + b;
        a = b;
        b = c;
    }

    if (a * b == n) {
        printf("YES");
    } else {
        printf("NO");
    }

    return 0;
}