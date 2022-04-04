#include "common.h"

size_t g_signalCatchedCount = 0;
int g_shouldListen = 1;

static ModeType g_mode; 

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
        default: break;
    }
}

void send_signals(ModeType mode, pid_t pid, size_t count, int signal_id, int finishing_signal_id, void(*wait_action)()) {
    for(int i = 0; i < count; ++i) {
        send_signal(mode, pid, signal_id, i);
        wait_action();
    }
    send_signal(mode, pid, finishing_signal_id, count);
} 

sigset_t create_mask(int signal_id, int finish_signal_id)
{
    sigset_t mask;
    sigfillset(&mask);

    sigdelset(&mask, signal_id);
    sigdelset(&mask, finish_signal_id);

    return mask;
}

void handle_signal_counter(int signo, siginfo_t* info, void* context) {
    g_signalCatchedCount += 1;

    g_senderPID = info->si_pid;

    g_additional_handler();
    
    if(g_mode == SIGQUEUE_MODE)
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

void setup_signal_handlers(void (*finish_signal_handler)(int, siginfo_t*, void*), int signal_id, int finish_signal_id) {
    set_signal_handler(signal_id, handle_signal_counter);
    set_signal_handler(finish_signal_id, finish_signal_handler);
}

void getSignals(ModeType* mode, int* signal_id, int* finish_signal_id) {
    if(*mode == SIGRT_MODE) {
        *mode = KILL_MODE;
        *signal_id = SIGRTMIN;
        *finish_signal_id = SIGRTMAX;
    } else {
        *signal_id = SIGUSR1;
        *finish_signal_id = SIGUSR2;
    }

    g_mode = *mode;
} 