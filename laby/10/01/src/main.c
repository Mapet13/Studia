#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE (33)
#define ATM_COUNT (100)

typedef unsigned char DigitType;

typedef struct {
    DigitType num[BUFFER_SIZE];
    size_t len;
} BigNum;

void increment(BigNum* num) {
    if (num->len == 0) return;

    DigitType rest = 1;
    size_t i = num->len - 1;
    while (rest == 1) {
        num->num[i] = (DigitType)(num->num[i] + 1u);
        num->num[i] = num->num[i] % 10;
        if (num->num[i] != 0) rest = 0;
        if (i == 0) {
            if (rest != 0) {
                num->len += 1;
                for (size_t j = num->len; j > 0; --j) {
                    num->num[j] = num->num[j - 1u];
                }
                num->num[0] = 1;
            }
            break;
        }
        --i;
    }
}

int mod(BigNum* num) { return (num->num[num->len - 1] % 2); }

int is_zero(BigNum* num) {
    for (size_t i = 0; i < num->len; ++i)
        if (num->num[i] != 0) return 0;

    return 1;
}

unsigned divide_by_2(BigNum* num) {
    unsigned remainder = 0;
    for (size_t i = 0; i < num->len; ++i) {
        remainder = (remainder * 10) + num->num[i];
        num->num[i] = (DigitType)(remainder / 2);
        remainder %= 2;
    }
    return remainder;
}

int get_result(DigitType* res, BigNum* num, unsigned control) {
    for (size_t i = 0; i < ATM_COUNT && is_zero(num) == 0; ++i) {
        res[i] = (DigitType)mod(num);
        if (i % 2u == control && res[i] == 1) increment(num);
        divide_by_2(num);
    }

    return is_zero(num);
}

void solve(const BigNum* const input, unsigned control) {
    BigNum num = { .len = input->len };
    for (size_t i = 0; i < input->len; ++i) {
        num.num[i] = input->num[i];
    }

    DigitType result[ATM_COUNT] = { 0 };
    if (get_result(result, &num, control)) {
        for (int j = 0; j < ATM_COUNT; ++j)
            if (result[j]) printf("%d ", j);
    } else {
        printf("NO");
    }
    printf("\n");
}

int main(void) {
    char arr[BUFFER_SIZE];
    if (scanf("%s", arr) != 1) return 1;

    BigNum input = { .len = strlen(arr) };
    for (size_t i = 0; i < input.len; ++i) {
        input.num[i] =
            (DigitType)(arr[i] - '0');  // assumption of correct input
    }

    solve(&input, 1);
    solve(&input, 0);
}