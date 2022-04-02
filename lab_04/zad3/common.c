#include "common.h"

size_t g_signalCatchedCount = 0;
int g_shouldListen = 1;

ModeType parseMode(const char* str) {
    if(strcmp(str, "KILL") == 0) return KILL_MODE;
    if(strcmp(str, "SIGQUEUE") == 0) return SIGQUEUE_MODE;
    if(strcmp(str, "SIGRT") == 0) return SIGRT_MODE;

    return ERROR_MODE;
}

void send_signal(ModeType mode, pid_t pid, int signal_id, int message) {
    switch(mode) {
        case KILL_MODE: 
            kill(pid, signal_id);
            break;
        case SIGQUEUE_MODE:
            sigval_t sigval = { message };
            sigqueue(pid, signal_id, sigval);
            break;
    }
}

void send_signals(ModeType mode, pid_t pid, size_t count, int signal_id, int finishing_signal_id) {
    for(int i = 0; i < count; ++i) {
        send_signal(mode, pid, signal_id, i);
    }
    send_signal(mode, pid, finishing_signal_id, count);
} 

sigset_t create_mask()
{
    sigset_t mask;
    sigfillset(&mask);

    sigdelset(&mask, SIGUSR1);
    sigdelset(&mask, SIGUSR2);

    return mask;
}

void handle_signal_counter(int signo, siginfo_t* info, void* context) {
    g_signalCatchedCount += 1;
    printf("Recived signal's id: [%d]\n", info->si_value.sival_int);
}

void set_signal_handler(int signal_id, void (*handler)(int, siginfo_t*, void*)) {
    struct sigaction sig;
	sig.sa_sigaction = handler;
	sigemptyset(&sig.sa_mask);
	sigaddset(&sig.sa_mask, signal_id);
	sig.sa_flags = SA_SIGINFO;
	sigaction(signal_id, &sig, NULL);
}

void setup_signal_handlers(void (*finish_signal_handler)(int, siginfo_t*, void*)) {
    set_signal_handler(SIGUSR1, handle_signal_counter);
    set_signal_handler(SIGUSR2, finish_signal_handler);
}