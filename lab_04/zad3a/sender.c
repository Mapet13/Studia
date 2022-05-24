#include "common.h"

#define ARGS_COUNT 3
#define ERROR_CODE -1

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
    printf("Catched %lu signals in return\n", g_signalCatchedCount);
    g_shouldListen = 0;
}

int main(int argc, char** argv) {
    pid_t catcher_pid;
	int sends_count;
    ModeType mode;

    if(load_input(argc, argv, &catcher_pid, &sends_count, &mode) == ERROR_CODE) 
        return 1;

    int signal_id;
    int finished_signal_id;
    getSignals(&mode, &signal_id, &finished_signal_id);

    printf("sending %d signals to %d...\n", sends_count, catcher_pid);

    send_signals(mode, catcher_pid, sends_count, signal_id, finished_signal_id);
    puts("sending finished");

    setup_signal_handlers(handle_signal_finish, signal_id, finished_signal_id);

    sigset_t mask = create_mask(signal_id, finished_signal_id);
    while(g_shouldListen)
        sigsuspend(&mask);
}