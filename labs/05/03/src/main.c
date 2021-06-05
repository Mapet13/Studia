/*
Dana jest tablica kwadratowa T[n][n] wypełniona liczbami naturalnymi oraz liczba
naturalna k. Kwadratem zawartym w tablicy będziemy nazywać kwadrat o bokach
złożonych z nieparzystej i większej od 1 liczby elementów całkowicie zawartych w
tablicy. Proszę napisać program, który w poszukuje w tablicy T kwadratów w niej
zawartych, których suma elementów na obwodzie wynosi k. Program powinien wypisać
liczbę znalezionych kwadratów oraz współrzędne (indeks wiersza i kolumny) ich
środków.
Uwaga: Dany element tablicy może być środkiem kilku poszukiwanych kwadratów
*/

#include <stdio.h>
#include <stdlib.h>
#define IDX(x, y, n) (((x) * (n)) + (y))

struct Node {
    unsigned int x;
    unsigned int y;
    struct Node* next;
};

struct LinkedList {
    struct Node* head;
    unsigned int count;
};

struct LinkedList* create_list(void) {
    struct LinkedList* list = malloc(sizeof(*list));
    if (!list) {
        exit(1);
    }

    list->head = NULL;
    list->count = 0;

    return list;
}

void push(struct LinkedList* list, unsigned int x, unsigned int y) {
    struct Node* node = malloc(sizeof(*node));
    if (!node) {
        exit(1);
    }
    list->count += 1;

    node->x = x;
    node->y = y;

    if (list->head == NULL || list->head->x > x ||
        (list->head->x == x && list->head->y > y)) {
        node->next = list->head;
        list->head = node;
    } else {
        int has_been_inserted = 0;
        struct Node* prev = list->head;
        while (prev->next != NULL) {
            if (prev->next->x > x ||
                (prev->next->x == x && prev->next->y > y)) {
                node->next = prev->next;
                prev->next = node;
                has_been_inserted = 1;
                break;
            }

            prev = prev->next;
        }

        if (!has_been_inserted) {
            node->next = prev->next;
            prev->next = node;
        }
    }
}

struct Node* pop_front(struct LinkedList* list) {
    struct Node* node = list->head;

    if (list->count > 0) {
        list->count -= 1;
        if (list->head) list->head = list->head->next;
        if (node) node->next = NULL;
    }

    return node;
}

unsigned int* get_matrix(unsigned int size) {
    unsigned int* arr = malloc(size * size * sizeof(*arr));
    if (!arr) {
        exit(1);
    }

    // using array linearization technique
    unsigned int i;
    for (i = 0; i < (size * size); ++i) {
        if (scanf("%u", &arr[i]) != 1) {
            exit(1);
        }
    }

    return arr;
}

unsigned int get_sum(unsigned int* matrix, unsigned int size, unsigned int x,
    unsigned int y, unsigned int radius) {
    unsigned int sum = 0;

    unsigned int i;
    for (i = 0; i < (radius - 1); ++i) {
        sum +=
            matrix[IDX(x - (radius - 1) / 2, y - (radius - 1) / 2 + i, size)];
        sum +=
            matrix[IDX(x - (radius - 1) / 2 + i, y + (radius - 1) / 2, size)];
        sum +=
            matrix[IDX(x + (radius - 1) / 2 - i, y - (radius - 1) / 2, size)];
        sum +=
            matrix[IDX(x + (radius - 1) / 2, y + (radius - 1) / 2 - i, size)];
    }

    return sum;
}

struct LinkedList* get_result(
    unsigned int* matrix, unsigned int size, unsigned int k) {
    struct LinkedList* list = create_list();

    unsigned int radius, x, y;
    for (radius = 3; radius < size; radius += 2) {
        for (x = (radius - 1) / 2; x < size - (radius - 1) / 2; ++x) {
            for (y = (radius - 1) / 2; y < size - (radius - 1) / 2; ++y) {
                if (get_sum(matrix, size, x, y, radius) == k) {
                    push(list, x, y);
                }
            }
        }
    }
    return list;
}

void print_result(struct LinkedList* list) {
    if (!list) return;

    printf("%u \n", list->count);

    while (list->count) {
        struct Node* node = pop_front(list);
        if (node) {
            printf("%u %u \n", node->x, node->y);
            free(node);
        }
    }
}

int main(void) {
    unsigned int n, k;
    if (scanf("%u %u", &n, &k) != 2) {
        return 1;
    }

    unsigned int* matrix = get_matrix(n);

    struct LinkedList* list = get_result(matrix, n, k);
    print_result(list);

    if (list) free(list);
    if (matrix) free(matrix);
    return 0;
}