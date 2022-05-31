#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 512
#define MAX_IMAGE_VAL 255

//////////////////////////////////////////////////
typedef struct {
    int width;
    int height;
    int max_val;
    int** content;
} Image;

Image parse_image_header(FILE* file) {
    char* buffer = NULL;
    size_t line_size = 0;

    getline(&buffer, &line_size, file);
    if (strcmp(buffer, "P2\n") != 0) exit(1);

    Image result;

    fscanf(file, "%d %d\n", &result.width, &result.height);

    fscanf(file, "%d", &result.max_val);

    result.content = malloc(sizeof(*result.content) * result.width);
    for (int i = 0; i < result.width; ++i) {
        result.content[i] = malloc(sizeof(*result.content[i]) * result.height);
    }

    free(buffer);

    return result;
}

void parse_image_content(Image* image, FILE* file) {
    for (int y = 0; y < image->height; ++y) {
        for (int x = 0; x < image->width; ++x) {
            fscanf(file, "%d", &image->content[x][y]);
        }
    }
}

Image load_image(const char* file_path) {
    FILE* file = fopen(file_path, "r");
    if (file == NULL) exit(1);

    Image image = parse_image_header(file);
    parse_image_content(&image, file);

    return image;
}

void save_image(Image* image, const char* file_path) {
    FILE* file = fopen(file_path, "w+");
    if (file == NULL) exit(1);

    fprintf(file, "P2\n");
    fprintf(file, "%d %d\n", image->width, image->height);
    fprintf(file, "%d\n", image->max_val);

    for (int y = 0; y < image->height; ++y) {
        for (int x = 0; x < image->width; ++x) {
            fprintf(file, "%d ", image->content[x][y]);
        }
        fprintf(file, "\n");
    }
}

//////////////////////////////////////////////////
typedef struct {
    Image* image;
    Image* out;
    int min;
    int max;
} ThreadArgs;

void* negate_numbers(void* arg) {
    ThreadArgs* args = arg;

    for (int x = 0; x < args->image->width; ++x) {
        for (int y = 0; y < args->image->height; ++y) {
            if (args->image->content[x][y] >= args->min && args->image->content[x][y] < args->max) {
                args->out->content[x][y] = MAX_IMAGE_VAL - args->image->content[x][y];
            }
        }
    }

    free(args);

    return NULL;
}

void* negate_block(void* arg) {
    ThreadArgs* args = arg;

    for (int x = args->min; x < args->max; ++x) {
        for (int y = 0; y < args->image->height; ++y) {
            args->out->content[x][y] = MAX_IMAGE_VAL - args->image->content[x][y];
        }
    }

    free(args);

    return NULL;
}

void block_action(Image* image, Image* out, int thread_count) {
    const int range = image->width / thread_count;

    pthread_t* threads = malloc(sizeof(*threads) * thread_count);

    for (int i = 0; i < thread_count; ++i) {
        ThreadArgs* args = malloc(sizeof(*args));
        args->image = image;
        args->out = out;
        args->min = range * i;
        args->max = (i + 1 == thread_count)
                        ? (image->width)
                        : (range * (i + 1));

        pthread_create(&threads[i], NULL, negate_block, args);
    }

    for (int i = 0; i < thread_count; ++i) {
        pthread_join(threads[i], NULL);
    }

    free(threads);
}

void numbers_action(Image* image, Image* out, int thread_count) {
    const int range = image->max_val / thread_count;

    pthread_t* threads = calloc(sizeof(pthread_t), thread_count);
    for (int i = 0; i < thread_count; ++i) {
        ThreadArgs* args = calloc(sizeof(ThreadArgs), 1);
        args->image = image;
        args->out = out;
        args->min = range * i;
        args->max = (i + 1 == thread_count)
                        ? (image->max_val + 1)
                        : (range * (i + 1));
        pthread_create(&threads[i], NULL, negate_numbers, args);
    }

    for (int i = 0; i < thread_count; ++i) {
        pthread_join(threads[i], NULL);
    }

    free(threads);
}
//////////////////////////////////////////////////

typedef enum {
    arg__program_name,
    arg__thread_count,
    arg__program_mode,
    arg__program_in,
    arg__program_out,
    ProgramArgsSize
} ProgramArgs;

typedef enum {
    mode__numbers,
    mode__block,
} Mode;

Mode parse_mode(const char* mode_str) {
    if (strcmp(mode_str, "numbers") == 0) return mode__numbers;
    if (strcmp(mode_str, "block") == 0) return mode__block;

    exit(1);
}

int main(int argc, char** argv) {
    if (argc != ProgramArgsSize) return 1;

    const int thread_count = atoi(argv[arg__thread_count]);
    const Mode mode = parse_mode(argv[arg__program_mode]);
    Image image = load_image(argv[arg__program_in]);

    Image out;
    out.height = image.height;
    out.width = image.width;
    out.max_val = MAX_IMAGE_VAL;
    out.content = malloc(sizeof(*out.content) * image.width);
    for (int i = 0; i < image.width; ++i) {
        out.content[i] = malloc(sizeof(*out.content[i]) * image.height);
    }

    if (mode == mode__block) block_action(&image, &out, thread_count);
    if (mode == mode__numbers) numbers_action(&image, &out, thread_count);

    save_image(&out, argv[arg__program_out]);

    for (int i = 0; i < image.width; ++i) {
        free(out.content[i]);
        free(image.content[i]);
    }
    free(image.content);
    free(out.content);
}