#ifndef WC_DYNAMIC_DEFS
#define WC_DYNAMIC_DEFS

typedef unsigned ID_type;
typedef struct {
    char** data;
    ID_type size;
} ArrayWC;

#define STRINGIFY(x) #x
#define TOSTRING(x) STRINGIFY(x)
#define LOAD_DYNAMIC_FN(handle, fn, out, ...) out (*fn)(__VA_ARGS__) = (out(*)(__VA_ARGS__))dlsym((handle), TOSTRING(fn))

#endif