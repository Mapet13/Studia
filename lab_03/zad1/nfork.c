#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

void print_pid(const char* tag) {
    printf("%s proces: %d\n", tag, (int)getpid());
}

int main(int argc, char** argv) {
    if(argc != 2)
        return -1;

    int n = atoi(argv[1]);

    print_pid("Main");

    for(int i = 0; i < n; ++i) {
        pid_t pid = fork();
        if(pid == 0) {
            print_pid("Child");
            break;
        }
    }
}
