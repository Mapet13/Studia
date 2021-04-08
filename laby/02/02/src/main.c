#include <math.h>
#include <stdio.h>
#include <stdlib.h>

const char DIGITS_CHARS[] = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'A', 'B', 'C', 'D', 'E', 'F' };

int is_narcism(int num, int* digits, int digits_count) {
    int sum = 0;

    int i;
    for (i = 0; i < digits_count; ++i) {
        sum += pow(digits[i], digits_count);
    }

    return num == sum;
}

void increase(int* digits, int digits_count, int base) {
    int i = digits_count - 1;
    int carry;
    do {
        carry = 0;
        digits[i] += 1;
        if (digits[i] >= base) {
            digits[i] = digits[i] % base;
            carry = 1;
        }
        --i;
    } while (carry && i >= 0);
}

void print_num(int* digits, int digits_count) {
    int i;
    for (i = 0; i < digits_count; ++i) {
        printf("%c", DIGITS_CHARS[digits[i]]);
    }
    printf(" ");
}

int* get_digits_arr(int digits_count) {
    int* digits = malloc(digits_count * sizeof(int));
    digits[0] = 1;

    int i;
    for (i = 1; i < digits_count; ++i) {
        digits[i] = 0;
    }

    return digits;
}

int main(void) {
    int digits_count;
    int base;

    if (scanf("%d %d", &digits_count, &base) != 2) {
        return 1;
    }
    int* digits = get_digits_arr(digits_count);

    int current_num = pow(base, digits_count - 1);
    int upper_bound = pow(base, digits_count);
    int exists = 0;

    while (current_num < upper_bound) {
        if (is_narcism(current_num, digits, digits_count)) {
            print_num(digits, digits_count);
            exists = 1;
        }

        ++current_num;
        increase(digits, digits_count, base);
    }
    if (exists) {
        printf("\n");
    } else {
        printf("NO\n");
    }

    free(digits);
    return 0;
}