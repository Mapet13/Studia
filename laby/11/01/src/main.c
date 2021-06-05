#include <stdio.h>
#include <stdlib.h>

#define ERROR_HANDLE_PLACEHOLDER (exit(1))

#define CycleMod(a, b) ((a) < 0 ? (a + b) : (a) >= b ? (a - b) : a)

typedef struct {
    long x;
    long y;
} Point;

typedef struct {
    unsigned vertices_count;
    Point* vertices;
} Polygon;

void initial_center(Point* result, Point* a, Point* b) {
    result->x = (a->x + b->x) >> 1;
    result->y = (a->y + b->y) >> 1;
}

Polygon* get_polygons(unsigned short t) {
    Polygon* polygons = malloc(t * sizeof(*polygons));
    if (!polygons) ERROR_HANDLE_PLACEHOLDER;

    unsigned count;
    int x, y;
    for (unsigned short i = 0; i < t; ++i) {
        if (scanf("%u", &count) != 1) ERROR_HANDLE_PLACEHOLDER;
        polygons[i].vertices_count = 2u * count;
        polygons[i].vertices = malloc(
            polygons[i].vertices_count * sizeof(*(polygons[i].vertices)));
        if (!polygons[i].vertices) ERROR_HANDLE_PLACEHOLDER;

        for (unsigned j = 0; j < count; ++j) {
            if (scanf("%d %d", &x, &y) != 2) ERROR_HANDLE_PLACEHOLDER;
            polygons[i].vertices[2u * j].x = (x << 1);
            polygons[i].vertices[2u * j].y = (y << 1);
        }

        for (unsigned j = 0; j < count; ++j) {
            initial_center(&polygons[i].vertices[(2u * j) + 1],
                &polygons[i].vertices[(2u * j)],
                &polygons[i]
                     .vertices[((2u * j) + 2u) % polygons[i].vertices_count]);
        }
    }

    return polygons;
}

void free_polygons(Polygon* polygons, unsigned short t) {
    if (polygons) {
        for (unsigned short i = 0; i < t; ++i) {
            if (polygons[i].vertices) free(polygons[i].vertices);
        }
        free(polygons);
    }
}

long sqr(long x) { return x * x; }

long dist_sqr(Point* a, Point* b) {
    return sqr(a->x - b->x) + sqr(a->y - b->y);
}

int are_images_of_symmetry(Point* p, Point* q, Point* a, Point* b) {
    return (dist_sqr(p, a) == dist_sqr(p, b)) &&
           (dist_sqr(q, a) == dist_sqr(q, b));
}

unsigned get_axis(Polygon* polygon) {
    unsigned result = 0;

    Point *p, *q, *a, *b;
    for (long i = 0; i < (polygon->vertices_count / 2); ++i) {
        p = &polygon->vertices[i];
        q = &polygon->vertices[CycleMod(
            i + (polygon->vertices_count / 2), polygon->vertices_count)];

        int flag = 1;
        long j = 1;

        do {
            a = &polygon->vertices[CycleMod((i + j), polygon->vertices_count)];
            b = &polygon
                     ->vertices[(CycleMod((i - j), polygon->vertices_count))];

            if (!are_images_of_symmetry(p, q, a, b)) {
                flag = 0;
                break;
            }

            ++j;
        } while (j < (polygon->vertices_count / 2));

        if (flag) ++result;
    }

    return result;
}

int main(void) {
    unsigned short t;
    if (scanf("%hu", &t) != 1) return 1;

    Polygon* polygons = get_polygons(t);

    for (unsigned short i = 0; i < t; ++i) {
        printf("%u \n", get_axis(&(polygons[i])));
    }

    free_polygons(polygons, t);
    return 0;
}