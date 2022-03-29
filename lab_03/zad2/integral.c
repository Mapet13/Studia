#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#define MIN_DOMAIN 0
#define MAX_DOMAIN 1

#define BUFFER_SIZE 32
#define DOUBLE_PRECISION 8

double f(double x) {
    return 4.0 / ((x * x) + 1.0);
}

void child_work(int id, double start, double end, double width);
double read_segment_sum(int id);

int main(int argc, char** argv) {
    if (argc != 3)
        return -1;

    double WIDTH = atof(argv[1]);
    int N = atoi(argv[2]);

    double proces_segment_width = (double)(MAX_DOMAIN - MIN_DOMAIN) / (double)N;

    double start = 0.0f;
    double end = proces_segment_width;
    for (int i = 1; i <= N; ++i, start = end, end += proces_segment_width) {
        pid_t pid = fork();
        if (pid == 0) {
            child_work(i, start, end, WIDTH);
            exit(0);
        }
    }

    while (wait(NULL) > 0)
        ;

    double sum = 0.0f;
    for (int i = 1; i <= N; ++i)
        sum += read_segment_sum(i);

    printf("Calculation result: %f \n", sum);
}

void save_sum(int id, double sum);
char* get_file_name(int id);

void child_work(int id, double start, double end, double width) {
    double sum = 0.0f;

    while (start + width < end) {
        sum += f(start) * width;
        start += width;
    }

    sum += f(start) * (end - start);

    save_sum(id, sum);
}

void save_sum(int id, double sum) {
    char* file_name = get_file_name(id);
    FILE* file = fopen(file_name, "w+");

    fprintf(file, "%f", sum);

    free(file_name);
    fclose(file);
}

char* get_file_name(int id) {
    char* file_name = malloc(BUFFER_SIZE * sizeof(*file_name));
    sprintf(file_name, "w%d.txt", id);
    return file_name;
}

double read_segment_sum(int id) {
    char* file_name = get_file_name(id);
    FILE* file = fopen(file_name, "r");

    char sum[BUFFER_SIZE];
    fread(sum, sizeof(*sum), BUFFER_SIZE, file);

    free(file_name);
    fclose(file);

    return atof(sum);
}