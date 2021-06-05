#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int x;
    long long count;
    struct Node* next;
    struct Node* prev;
} Node;

typedef struct {
    Node* head;
    Node* last;
} LinkedList;

LinkedList* create_list(void) {
    LinkedList* list = malloc(sizeof(*list));
    if (!list) {
        exit(1);
    }

    list->head = NULL;

    return list;
}

void append(LinkedList* list, int x, long long count) {
    Node* node = malloc(sizeof(*node));
    if (!node) {
        exit(1);
    }

    node->x = x;
    node->count = count;
    if (list->head == NULL) {
        if (list->head == NULL) list->last = node;
        node->next = list->head;
        node->prev = NULL;
        if (list->head != NULL) list->head->prev = node;
        list->head = node;
    } else {
        node->next = NULL;
        list->last->next = node;
        node->prev = list->last;
        list->last = node;
    }
}

void list_destruct(LinkedList* list) {
    Node* node = list->head;
    while (node) {
        Node* next = node->next;
        free(node);
        node = next;
    }

    free(list);
}

Node* create_node(int x, long long count) {
    Node* node = malloc(sizeof(Node));
    if (!node) {
        exit(1);
    }
    node->x = x;
    node->count = count;
    return node;
}

Node* get_node_at_x_offset(LinkedList* list, Node* node, int offset) {
    if (offset == 0) return node;
    if (offset > 0) {
        if (node == list->last) {
            append(list, node->x + offset, 0);
            return list->last;
        }
        if (node->next->x <= node->x + offset)
            return get_node_at_x_offset(
                list, node->next, offset - (node->next->x - node->x));
        else {
            Node* n = create_node(node->x + offset, 0);

            node->next->prev = n;
            n->next = node->next;
            n->prev = node;
            node->next = n;

            return n;
        }
    } else {
        if (node == list->head) {
            Node* n = create_node(node->x + offset, 0);

            n->next = node;
            n->prev = NULL;
            node->prev = n;
            list->head = n;

            return n;
        }
        if (node->prev->x >= node->x + offset)
            return get_node_at_x_offset(
                list, node->prev, offset + (node->x - node->prev->x));
        else {
            Node* n = create_node(node->x + offset, 0);

            node->prev->next = n;
            n->prev = node->prev;
            n->next = node;
            node->prev = n;

            return n;
        }
    }
}

int unload(LinkedList* list, Node* node) {
    int result = 0;
    long long k = node->count / 3;
    node->count -= k * 3;

    Node* n = get_node_at_x_offset(list, node, -2);
    n->count += k;
    if (n->count >= 3) result = 1;

    get_node_at_x_offset(list, node, 2)->count += k;

    return result;
}

void move_right(LinkedList* list, Node* node) {
    node->count -= 1;
    get_node_at_x_offset(list, node, 1)->count -= 1;
    get_node_at_x_offset(list, node, 2)->count += 1;
}
void move_left(LinkedList* list, Node* node) {
    node->count -= 1;
    get_node_at_x_offset(list, node, -1)->count += 1;
    get_node_at_x_offset(list, node, -2)->count += 1;
}

Node* get_real_prev(Node* node) {
    node = node->prev;
    while (node) {
        if (node->count > 0) return node;
        node = node->prev;
    }
    return NULL;
}

int main(void) {
    unsigned n;
    int p;
    long long m;

    if (scanf("%u", &n) != 1) return 1;

    LinkedList* list = create_list();

    for (unsigned i = 0; i < n; ++i) {
        if (scanf("%d %lld", &p, &m) != 2) return 1;
        append(list, p, m);
    }

    int need_to_iterate;
    do {
        need_to_iterate = 0;
        Node* node = list->head;
        while (node) {
            if (node->count >= 3) {
                if (unload(list, node)) need_to_iterate = 1;
            }
            node = node->next;
        }
    } while (need_to_iterate);

    Node* node = list->last->prev;
    while (1) {
        if (node->count > 0 && get_node_at_x_offset(list, node, 1)->count > 0) {
            move_right(list, node);
            node = get_node_at_x_offset(list, node, 2);
        } else if (node->count == 2 &&
                   get_node_at_x_offset(list, node, -1)->count > 0) {
            node = get_node_at_x_offset(list, node, -1);
        } else if (node->count == 2 &&
                   get_node_at_x_offset(list, node, 1)->count == 0) {
            move_left(list, node);
            move_right(list, get_node_at_x_offset(list, node, -1));
            node = get_node_at_x_offset(list, node, 1);
        } else if (node->count == 3) {
            unload(list, node);
            node = get_node_at_x_offset(list, node, 2);
        } else if (!get_real_prev(node)) {
            break;
        } else {
            node = get_real_prev(node);
        }
    }

    node = list->head;
    while (node) {
        if (node->count > 0) {
            printf("%d ", node->x);
        }
        node = node->next;
    }
    printf("\n");

    list_destruct(list);
}