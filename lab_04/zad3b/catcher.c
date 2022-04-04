#include "common.h"

pid_t g_senderPID;
ModeType g_mode;

void nothing(){}

void print_pid() {
    printf("catcher pid: [%d]\n", getpid());
}


void handle_signal_finish(int signo, siginfo_t* info, void* context) {
    g_senderPID = info->si_pid;
    printf("Catched %lu signals from %d\n", g_signalCatchedCount, g_senderPID);
    g_shouldListen = 0;
}

void additional_handler(void) {
    printf("g_senderPID: %d\n",g_senderPID);
    send_signal(g_mode, g_senderPID, SIGUSR1, 0);
}
void(*g_additional_handler)(void) = additional_handler;


int main(int argc, char** argv) {
    if(argc != 2)
        return 1;
    
    g_mode = parseMode(argv[1]);
    if(g_mode == ERROR_MODE)
        return 1;

    int signal_id;
    int finished_signal_id;
    getSignals(&g_mode, &signal_id, &finished_signal_id);
    
    print_pid();
    setup_signal_handlers(handle_signal_finish, signal_id, finished_signal_id);

    sigset_t mask = create_mask(signal_id, finished_signal_id);
    while(g_shouldListen)
        sigsuspend(&mask);


    send_signals(g_mode, g_senderPID, g_signalCatchedCount, signal_id, finished_signal_id, nothing);
}