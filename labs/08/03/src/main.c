#include <stdio.h>
#include <stdlib.h>

#define ERROR_HANDLE_PLACEHOLDER exit(1)

typedef struct {
    unsigned capacity;
    unsigned top;
    char* data;
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

void stack_push(Stack* stack, char value) {
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

char stack_get(Stack* stack) {
    if (!stack) ERROR_HANDLE_PLACEHOLDER;
    if (!stack->data) ERROR_HANDLE_PLACEHOLDER;

    return stack->data[stack->top - 1];
}

char stack_pop(Stack* stack) {
    char c = stack_get(stack);
    stack->top--;
    return c;
}

int stack_is_empty(Stack* stack) {
    if (!stack) ERROR_HANDLE_PLACEHOLDER;
    return stack->top == 0;
}

typedef struct {
    char* string;
    unsigned int capacity;
    unsigned int length;
} SimpleString;

SimpleString* string_construct(void) {
    SimpleString* str = malloc(sizeof(*str));
    str->capacity = 5;
    str->length = 0;
    str->string = malloc(str->capacity * sizeof(char));

    if (!str->string) ERROR_HANDLE_PLACEHOLDER;  // error handle placeholder

    return str;
}

int is_break_char(char c) { return c == '\n' || c == '\r' || c == '\0'; }

void string_append(SimpleString* str, char character) {
    while (str->capacity <= str->length) {
        str->capacity = 2 * str->capacity;
        str->string = realloc(str->string, str->capacity * sizeof(char));
        if (!str->string) exit(1);  // error handle placeholder
    }

    str->string[str->length] = character;
    ++(str->length);
}

SimpleString* get_input(void) {
    SimpleString* str = string_construct();
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

void string_destruct(SimpleString* str) {
    if (str && str->string) free(str->string);
    if (str) free(str);
}

void print_result(Stack* stack) {
    for (unsigned i = 0; i < stack->top; ++i) printf("%c", stack->data[i]);
    printf("\n");
}

int main(void) {
    SimpleString* str = get_input();
    Stack* stack = stack_construct(str->length);

    stack_push(stack, str->string[0]);
    for (unsigned i = 1; i < str->length - 1; ++i) {
        while (!stack_is_empty(stack) && stack_get(stack) < str->string[i]) {
            stack_pop(stack);
        }
        stack_push(stack, str->string[i]);
    }

    print_result(stack);

    string_destruct(str);
    stack_destruct(stack);
}