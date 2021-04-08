#include "stack.h"

#include <stdlib.h>

typedef int DataType;

struct Node {
    DataType value;
    struct Node* next;
};

struct Stack {
    struct Node* top;
};

void init_stack(struct Stack* stack) {
    stack->top = malloc(sizeof(struct Node*));
    stack->top->next = NULL;
}

struct Stack* create_stack() {
    struct Stack* stack = malloc(sizeof(struct Stack*));
    init_stack(stack);
    return stack;
}

void destroy_stack(struct Stack* stack) {
    if (stack) {
        while (stack->top) {
            struct Node* node = stack->top;
            stack->top = stack->top->next;
            free(node);
        }
        free(stack);
    }
}

void push(struct Stack* stack, DataType value) {
    struct Node* node = malloc(sizeof(struct Node*));
    node->value = value;
    node->next = stack->top;
    stack->top = node;
}

DataType pop(struct Stack* stack) {
    if (!is_empty(stack)) {
        struct Node* node = stack->top;
        DataType value = node->value;
        stack->top = stack->top->next;
        free(node);
        return value;
    }
    return (DataType)0;
}

int is_empty(struct Stack* stack) { return stack->top->next == NULL; }