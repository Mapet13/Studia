#include <stdio.h>

typedef unsigned long DataType;

DataType change_bit(DataType x, unsigned p) {
    DataType bit = (1lu << p);

    if (x & bit) return x -= bit;
    return x += bit;
}

int main(void) {
    unsigned N;
    DataType M;

    if (scanf("%u %lu", &N, &M) != 2) return 1;

    unsigned counter = 0;

    for (DataType i = 0; i < (1lu << N); ++i) {
        if (i % M) {
            for (unsigned j = 0; j < N; ++j) {
                DataType x = change_bit(i, j);
                if (x != 0 && x % M == 0) {
                    ++counter;
                    break;
                }
            }
        }
    }

    printf("%u\n", counter);
}
