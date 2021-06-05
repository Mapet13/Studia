#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ERROR_HANDLE_PLACEHOLDER exit(1)
#define MIN(x, y) (((x) < (y)) ? (x) : (y))

typedef struct {
    unsigned capacity;
    unsigned top;
    unsigned* data;
} Stack;

Stack* stack_construct(unsigned capacity) {
    Stack* stack = malloc(sizeof(Stack));
    if (!stack) ERROR_HANDLE_PLACEHOLDER;  // error

    stack->data = malloc(capacity * sizeof(stack->data));
    if (!stack->data) ERROR_HANDLE_PLACEHOLDER;  // error

    stack->capacity = capacity;
    stack->top = 0;

    return stack;
}

void stack_destruct(Stack* stack) {
    if (stack && stack->data) free(stack->data);
    if (stack) free(stack);
}

void stack_push(Stack* stack, unsigned value) {
    if (!stack) ERROR_HANDLE_PLACEHOLDER;
    if (!stack->data) ERROR_HANDLE_PLACEHOLDER;

    while (stack->top >= stack->capacity) {
        stack->capacity *= 2;
        stack->data =
            realloc(stack->data, stack->capacity * sizeof(stack->data));
        if (!stack->data) ERROR_HANDLE_PLACEHOLDER;
    }

    stack->data[stack->top] = value;
    stack->top++;
}

unsigned stack_get(Stack* stack) {
    if (!stack) ERROR_HANDLE_PLACEHOLDER;
    if (!stack->data) ERROR_HANDLE_PLACEHOLDER;

    return stack->data[stack->top - 1];
}

unsigned stack_pop(Stack* stack) {
    unsigned c = stack_get(stack);
    stack->top--;
    return c;
}

void stack_clear(Stack* stack) { stack->top = 0; }

int stack_is_empty(Stack* stack) {
    if (!stack) ERROR_HANDLE_PLACEHOLDER;
    return stack->top == 0;
}

#define STD_STRING_CAPACITY 5
typedef struct {
    char* string;
    unsigned int capacity;
    unsigned int length;
} SimpleString;

SimpleString* string_construct(unsigned capacity) {
    SimpleString* str = malloc(sizeof(*str));
    str->capacity = capacity;
    str->length = 0;
    str->string = malloc(str->capacity * sizeof(char));

    if (!str->string) ERROR_HANDLE_PLACEHOLDER;

    return str;
}

void string_destruct(SimpleString* str) {
    if (str && str->string) free(str->string);
    if (str) free(str);
}

void string_append(SimpleString* str, char character) {
    while (str->capacity <= str->length) {
        str->capacity = 2 * str->capacity;
        str->string = realloc(str->string, str->capacity * sizeof(char));
        if (!str->string) ERROR_HANDLE_PLACEHOLDER;
    }

    str->string[str->length] = character;
    ++(str->length);
}

int string_compare(SimpleString* a, SimpleString* b) {
    return strcmp(a->string, b->string);
}

void string_clear(SimpleString* str) {
    str->length = 0;
    str->string[0] = '\0';
}

int is_break_char(char c) { return c == '\n' || c == '\r' || c == '\0'; }

SimpleString* get_input(void) {
    SimpleString* str = string_construct(STD_STRING_CAPACITY);
    char current_character;

    while (1) {
        if (scanf("%c", &current_character) != 1) {
            ERROR_HANDLE_PLACEHOLDER;
        }
        if (is_break_char(current_character)) break;
        string_append(str, current_character);
    }
    string_append(str, '\0');

    return str;
}

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

SimpleString* create_result(
    SimpleString* result, SimpleString* input, unsigned o, unsigned p) {
    string_clear(result);

    for (unsigned i = 0; i < input->length - 1; ++i) {
        string_append(
            result, input->string[(o + (p * i)) % (input->length - 1)]);
    }
    string_append(result, '\0');

    return result;
}

int main(void) {
    SimpleString* str = get_input();
    const int* eratosthenes_sieve = get_eratosthenes_sieve(str->length - 1);
    Stack* stack = stack_construct(str->length - 1);

    char current = '255';
    for (unsigned i = 0; i < str->length - 1; ++i) {
        if (stack_is_empty(stack) || current > str->string[i]) {
            stack_clear(stack);
            current = str->string[i];
        }
        if (current == str->string[i]) stack_push(stack, i);
    }

    char* result = malloc(str->length * sizeof(*result));
    int has_result = 0;
    SimpleString* temp = string_construct(str->length);
    while (!stack_is_empty(stack)) {
        unsigned o = stack_pop(stack);

        for (unsigned p = 2; p < str->length - 1; ++p) {
            if (!eratosthenes_sieve[p]) {
                create_result(temp, str, o, p);
                if (!has_result || strcmp(temp->string, result) < 0) {
                    has_result = 1;
                    strcpy(result, temp->string);
                }
            }
        }
    }

    if (result) printf("%s\n", result);

    string_destruct(str);
    string_destruct(temp);
    stack_destruct(stack);
    if (result) free(result);
    if (eratosthenes_sieve) free(eratosthenes_sieve);
    return 0;
}