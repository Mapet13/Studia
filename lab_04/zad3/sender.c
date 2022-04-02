#include "common.h"

#define ARGS_COUNT 3
#define ERROR_CODE -1

typedef enum {
    KILL_MODE,
    SIGQUEUE_MODE,
    SIGRT_MODE,
    ERROR_MODE
} ModeType;

ModeType parseMode(const char* str) {
    if(strcmp(str, "KILL") == 0) return KILL_MODE;
    if(strcmp(str, "SIGQUEUE") == 0) return SIGQUEUE_MODE;
    if(strcmp(str, "SIGRT") == 0) return SIGRT_MODE;

    return ERROR_MODE;
}

int load_input(int argc, char** argv, pid_t* catcher_pid, int* sends_count, ModeType* mode) {
    if(argc != ARGS_COUNT + 1) {
        return -1;
    }

    *catcher_pid = atoi(argv[1]);
	*sends_count = atoi(argv[2]);
    *mode = parseMode(argv[3]);

    if(*mode == ERROR_MODE || *catcher_pid <= 0 || *sends_count < 0)
        return -1;

    return 0;
}

void handle_signal_finish(int signo, siginfo_t* info, void* context) {
    printf("Catched %lu SIGUSR1 signals in return\n", g_signalCatchedCount);
    g_shouldListen = 0;
}

int main(int argc, char** argv) {
    pid_t catcher_pid;
	int sends_count;
    ModeType mode;

    if(load_input(argc, argv, &catcher_pid, &sends_count, &mode) == ERROR_CODE) 
        return 1;

    printf("sending %d signals to %d...\n", sends_count, catcher_pid);
    send_signals(catcher_pid, sends_count, SIGUSR1);
    kill(catcher_pid, SIGUSR2);
    puts("sending finished");

    setup_signal_handlers(handle_signal_finish);

    sigset_t mask = create_mask();
    while(g_shouldListen)
        sigsuspend(&mask);
}
