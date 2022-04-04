#include "common.h"

#define ARGS_COUNT 3
#define ERROR_CODE -1


void nothing(){}
void(*g_additional_handler)(void) = nothing;

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

pid_t g_senderPID;
sigset_t g_wait_mask;
int g_recived_signal_back = 1;

void wait_action() {
    while(!g_recived_signal_back)
        sigsuspend(&g_wait_mask);
    g_recived_signal_back = 0;
}

void wait_signal_handler() {
    g_recived_signal_back = 1;
}

void prepare_wait_env() {
    sigfillset(&g_wait_mask);
    sigdelset(&g_wait_mask, SIGUSR1);
    sigprocmask(SIG_SETMASK, &g_wait_mask, NULL);
    signal(SIGUSR1, wait_signal_handler);
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

    prepare_wait_env();

    send_signals(mode, catcher_pid, sends_count, signal_id, finished_signal_id, wait_action);
    puts("sending finished");

    setup_signal_handlers(handle_signal_finish, signal_id, finished_signal_id);

    sigset_t mask = create_mask(signal_id, finished_signal_id);
    while(g_shouldListen)
        sigsuspend(&mask);
}
