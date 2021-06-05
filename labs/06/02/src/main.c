#include <stdio.h>
#include <stdlib.h>

struct SimpleString {
    char* string;
    unsigned int allocated_size;
    unsigned int length;
};

struct SimpleString* construct_string(void) {
    struct SimpleString* str = malloc(sizeof(*str));
    str->allocated_size = 5;
    str->length = 0;
    str->string = malloc(str->allocated_size * sizeof(char));

    if (!str->string) exit(1);  // error handle placeholder

    return str;
}

void append_to_string(struct SimpleString* str, char character) {
    while (str->allocated_size <= str->length) {
        str->allocated_size = 2 * str->allocated_size;
        str->string = realloc(str->string, str->allocated_size * sizeof(char));
        if (!str->string) exit(1);  // error handle placeholder
    }

    str->string[str->length] = character;
    ++(str->length);
}

struct SimpleString* input_until(char break_char) {
    struct SimpleString* str = construct_string();
    char current_character;

    while (1) {
        if (scanf("%c", &current_character) != 1) {
            exit(1);
        }
        if (current_character == break_char) break;
        append_to_string(str, current_character);
    }
    append_to_string(str, '\0');

    return str;
}

char pop_last(struct SimpleString* str) {
    if (str->length <= 0) return 0;

    --(str->length);
    char c = str->string[str->length];
    str->string[str->length] = '\0';

    return c;
}

void destruct_string(struct SimpleString* str) {
    if (str && str->string) free(str->string);
    if (str) free(str);
}

int get_value_from_roman_sign(char sign) {
    switch (sign) {
        case 'I':
            return 1;
        case 'V':
            return 5;
        case 'X':
            return 10;
        case 'L':
            return 50;
        case 'C':
            return 100;
        case 'D':
            return 500;
        case 'M':
            return 1000;
        default:
            return 0;
    }
}

char get_roman_sign_from_value(int value) {
    switch (value) {
        case 1:
            return 'I';
        case 5:
            return 'V';
        case 10:
            return 'X';
        case 50:
            return 'L';
        case 100:
            return 'C';
        case 500:
            return 'D';
        case 1000:
            return 'M';
        default:
            return '?';
    }
}

int convert_from_roman(struct SimpleString* roman_numeral) {
    int value = 0;
    int current_quantity = 1;

    while (roman_numeral->length > 0) {
        int sign_value = get_value_from_roman_sign(pop_last(roman_numeral));
        if (sign_value < current_quantity)
            value -= sign_value;
        else {
            value += sign_value;
            current_quantity = sign_value;
        }
    }

    return value;
}

struct SimpleString* convetr_into_roman(int number) {
    struct SimpleString* str = construct_string();

    char sign = 'M';
    char predecessor_sign = 'C';
    int quantity = get_value_from_roman_sign(sign);
    int predecessor = get_value_from_roman_sign(predecessor_sign);

    while (number > 0) {
        if (number < quantity) {
            if (number >= (quantity - predecessor)) {
                append_to_string(str, predecessor_sign);
                append_to_string(str, sign);

                number -= (quantity - predecessor);
            } else {
                if (quantity == 5 || quantity == 50 || quantity == 500) {
                    quantity /= 5;
                    predecessor = quantity / 10;
                } else {
                    quantity /= 2;
                    predecessor = quantity / 5;
                }

                sign = get_roman_sign_from_value(quantity);
                predecessor_sign = get_roman_sign_from_value(predecessor);
            }
        } else {
            number -= quantity;
            append_to_string(str, sign);
        }
    }

    append_to_string(str, '\0');
    return str;
}

int main(void) {
    struct SimpleString* roman_numeral_a = input_until(' ');
    struct SimpleString* roman_numeral_b = input_until('\n');

    int a, b;
    a = convert_from_roman(roman_numeral_a);
    b = convert_from_roman(roman_numeral_b);

    struct SimpleString* roman_numeral_sum = convetr_into_roman(a + b);

    printf("%s \n", roman_numeral_sum->string);

    destruct_string(roman_numeral_a);
    destruct_string(roman_numeral_b);
    destruct_string(roman_numeral_sum);
    return 0;
}