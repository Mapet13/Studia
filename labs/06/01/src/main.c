#include <stdio.h>
#include <stdlib.h>

#define MIN(x, y) (((x) < (y)) ? (x) : (y))
#define MAX(x, y) (((x) > (y)) ? (x) : (y))

#define SIZE 200
#define OFFSET 100

struct Rect {
    int x1, x2, y1, y2;
};

void get_rect_from_input(struct Rect* rect) {
    if (scanf("%d %d %d %d", &(rect->x1), &(rect->y1), &(rect->x2),
            &(rect->y2)) != 4) {
        exit(1);
    }
    rect->x1 = MIN(rect->x1, rect->x2);
    rect->x2 = MAX(rect->x1, rect->x2);
    rect->y1 = MIN(rect->y1, rect->y2);
    rect->y2 = MAX(rect->y1, rect->y2);
}

void fill_plot(int field[SIZE][SIZE], struct Rect* rect, int* changed) {
    for (int x = rect->x1; x < rect->x2; ++x) {
        for (int y = rect->y1; y < rect->y2; ++y) {
            if (field[x + OFFSET][y + OFFSET]) {
                --(*changed);
            } else {
                ++(*changed);
            }
            field[x + OFFSET][y + OFFSET] = !field[x + OFFSET][y + OFFSET];
        }
    }
}

int main(void) {
    int field[SIZE][SIZE] = { 0 };  // 0 - white, 1 - black

    unsigned int n;
    if (scanf("%u", &n) != 1) {
        return 1;
    }

    int changed = 0;

    struct Rect rect;
    for (unsigned int i = 0; i < n; ++i) {
        get_rect_from_input(&rect);
        fill_plot(field, &rect, &changed);
    }

    printf("%d \n", changed);

    return 0;
}