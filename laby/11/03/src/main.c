#include <stdio.h>
#include <string.h>

#define MAX_OP 100
#define GUARD_VALUE 9999999

void one_register(int n, char* operations, int index, int t, int* helper_count,
    char* helper) {
    if (index > MAX_OP - 2) return;
    if (n == t) {
        if (index < *helper_count) {
            *helper_count = index;
            strcpy(helper, operations);
        } else if (index == *helper_count) {
            if (strcmp(operations, helper) < 0) {
                strcpy(helper, operations);
            }
        }
        return;
    }
    if (n == 0 || n > t) {
        return;
    }
    if (n < t) {
        if (n + n <= t) {
            operations[index] = '+';
            one_register(n + n, operations, index + 1, t, helper_count, helper);
        }
        if (n * n <= t) {
            operations[index] = '*';
            one_register(n * n, operations, index + 1, t, helper_count, helper);
        }
        return;
    }

    return;
}

int main(void) {
    int helper_count = GUARD_VALUE;

    char helper[MAX_OP];
    char operations[MAX_OP] = { 0 };

    int s, t;
    if (scanf("%d %d", &s, &t) != 2) return 1;

    one_register(s, operations, 0, t, &helper_count, helper);
    memset(operations, 0, sizeof(char));

    int prev = helper_count;
    one_register(1, operations, 0, t, &helper_count, helper);

    if (helper_count == GUARD_VALUE) {
        printf("NO");
    } else {
        if (helper_count < prev) printf("/");
        for (int i = 0; i < helper_count; i++) {
            printf("%c", helper[i]);
        }
        printf("\n");
    }

    return 0;
}