#include <stdio.h>
#include <stdlib.h>

#define ERROR_HANDLE_PLACEHOLDER (exit(1))
#define UNINITIALIZED_RESULT (-1)
#define INPUT_LEN (2)

struct Gate;

typedef char ByteType;

typedef union {
    unsigned id;
    struct Gate* gate;
} LinkNodeValue;

typedef struct {
    LinkNodeValue value;
    int is_gate;
} LinkNode;

typedef struct Gate {
    LinkNode input[INPUT_LEN];
    int visited;
    ByteType* deps;
} Gate;

Gate gate_create(unsigned N) {
    Gate gate;
    gate.visited = 0;
    gate.deps = calloc(N, sizeof(ByteType));
    return gate;
}

void gate_destruct(Gate* gate) {
    if (gate) free(gate->deps);
}

Gate* get_net(unsigned M, unsigned N) {
    Gate* net = malloc(M * sizeof(*net));
    if (!net) ERROR_HANDLE_PLACEHOLDER;

    for (unsigned i = 0; i < M; ++i) {
        net[i] = gate_create(N);
    }

    for (unsigned i = 0; i < M; ++i) {
        int x;
        for (unsigned j = 0; j < INPUT_LEN; ++j) {
            if (scanf("%d", &x) != 1) ERROR_HANDLE_PLACEHOLDER;
            net[i].input[j].is_gate = x > 0;

            if (net[i].input[j].is_gate) {
                net[i].input[j].value.gate = &net[x - 1];
            } else {
                net[i].input[j].value.id = (unsigned)abs(x) - 1;
            }
        }
    }

    return net;
}

ByteType* create_word(unsigned N) {
    ByteType* a = calloc(N, sizeof(*a));
    if (!a) ERROR_HANDLE_PLACEHOLDER;
    return a;
}

void get_byte_word(ByteType* word, unsigned N) {
    for (unsigned i = 0; i < N; ++i) {
        char x;
        if (scanf("%c", &x) != 1) ERROR_HANDLE_PLACEHOLDER;
        if (x == '0' || x == '1')
            word[i] = (x == '1') ? 1 : 0;
        else
            --i;
    }
}

int compare_less_or_eq(ByteType* x, ByteType* y, unsigned N) {
    unsigned i = 0;
    while (i < N && x[i] == y[i]) {
        ++i;
    }

    return i == N || x[i] < y[i];
}

int increment(ByteType* x, unsigned N) {
    unsigned i = 0;
    while (x[N - i - 1] == 1) {
        x[N - i - 1] = 0;
        ++i;
        if ((N - i - 1) > N) return 1;
    }
    x[N - i - 1] = 1;
    return 0;
}

void byte_union(ByteType* dest, ByteType* x, unsigned N) {
    for (unsigned i = 0; i < N; ++i) dest[i] ^= x[i];
}

void create_dependencies_vec_recur(Gate* gate, unsigned N) {
    if (!gate->visited) {
        for (unsigned i = 0; i < INPUT_LEN; ++i) {
            if (gate->input[i].is_gate) {
                create_dependencies_vec_recur(gate->input[i].value.gate, N);
                byte_union(gate->deps, gate->input[i].value.gate->deps, N);
            } else {
                gate->deps[gate->input[i].value.id] ^= 1;
            }
        }
        gate->visited = 1;
    }
}

ByteType* create_dependencies_vec(Gate* net, unsigned last, unsigned N) {
    create_dependencies_vec_recur(&net[last - 1], N);
    return net[last - 1].deps;
}

ByteType evaluate(ByteType* deps, ByteType* word, unsigned N) {
    ByteType result = 2;
    for (unsigned i = 0; i < N; ++i) {
        if (deps[i]) {
            if (result > 1)
                result = word[i];
            else
                result ^= word[i];
        }
    }

    return result;
}

void net_destroy(Gate* net, unsigned M) {
    for (unsigned i = 0; i < M; ++i) {
        gate_destruct(&net[i]);
    }
    free(net);
}

int main(void) {
    unsigned N, M, LastID;
    if (scanf("%u %u %u", &N, &M, &LastID) != 3) return 1;

    Gate* net = get_net(M, N);
    ByteType* output_dependencies = create_dependencies_vec(net, LastID, N);

    ByteType* a = create_word(N);
    ByteType* b = create_word(N);
    get_byte_word(a, N);
    get_byte_word(b, N);

    unsigned counter = 0;
    while (compare_less_or_eq(a, b, N)) {
        if (evaluate(output_dependencies, a, N)) ++counter;
        if (increment(a, N)) break;
    };

    printf("%u\n", counter);

    net_destroy(net, M);
    free(a);
    free(b);
}