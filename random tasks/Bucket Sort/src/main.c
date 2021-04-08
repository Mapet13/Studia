#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

struct Node {
    struct Node* next;
    float value;
};

void push_front(struct Node** lists, int idx, float value) {
    struct Node* node = malloc(sizeof(struct Node));
    node->value = value;
    node->next = lists[idx];
    lists[idx] = node;
}

float pop_front(struct Node** lists, int idx) {
    struct Node* node = lists[idx];
    float value = node->value;
    lists[idx] = node->next;
    free(node);
    return value;
}

struct Node* insert_node(struct Node* head, struct Node* node) {
    if (head == NULL) {
        return node;
    }
    if (head->value > node->value) {
        node->next = head;
        return node;
    }

    struct Node* prev = head;
    while (prev->next != NULL && node->value > prev->next->value) {
        prev = prev->next;
    }

    node->next = prev->next;
    prev->next = node;

    return head;
}

void insertion_sort(struct Node** lists, unsigned int idx) {
    struct Node* sorted = lists[idx];
    lists[idx] = NULL;

    while (sorted != NULL) {
        struct Node* node = sorted;
        sorted = sorted->next;
        node->next = NULL;
        lists[idx] = insert_node(lists[idx], node);
    }
}

void bucket_sort(float* arr, unsigned int len, unsigned int upper_bound) {
    struct Node** buckets = calloc(len, sizeof(struct Node*));

    unsigned int i;
    for (i = 0; i < len; ++i) {
        push_front(
            buckets, (int)(arr[i] / ((float)upper_bound / (float)len)), arr[i]);
    }

    for (i = 0; i < len; ++i) {
        insertion_sort(buckets, i);
    }

    int b_idx = 0;
    for (i = 0; i < len; ++i) {
        while (buckets[b_idx] == NULL) {
            ++b_idx;
        }
        arr[i] = pop_front(buckets, b_idx);
    }

    free(buckets);
}

float* get_array(const unsigned int len) {
    float* arr = malloc(sizeof(float) * len);

    srand((unsigned)time(NULL));

    unsigned int i;
    for (i = 0; i < len; ++i) {
        arr[i] = ((float)(rand() % 1000)) / 100.0f;
    }

    return arr;
}

void print_array(const float* arr, const unsigned int len) {
    printf("[ ");

    unsigned int i;
    for (i = 0; i < len; ++i) {
        printf("%.2f ", arr[i]);
    }

    printf("]\n");
}

int main(void) {
    unsigned int len;
    printf("Length of array: ");
    if (scanf("%u", &len) != 1) {
        return 1;
    }

    float* array = get_array(len);

    print_array(array, len);
    bucket_sort(array, len, 10);
    print_array(array, len);

    free(array);
    return 0;
}