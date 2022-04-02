#include "common.h"

size_t g_signalCatchedCount = 0;
int g_shouldListen = 1;

void send_signals(pid_t pid, size_t count, int signal_id) {
    for(int i = 0; i < count; ++i) {
        kill(pid, signal_id);
    }
} 

sigset_t create_mask()
{
    sigset_t mask;
    sigfillset(&mask);

    sigdelset(&mask, SIGUSR1);
    sigdelset(&mask, SIGUSR2);

    return mask;
}

void handle_signal_counter() {
    g_signalCatchedCount += 1;
}

void setup_signal_handlers(void (*finish_signal_handler)()) {
    signal(SIGUSR1, handle_signal_counter);

    struct sigaction sig;
	sig.sa_sigaction = finish_signal_handler;
	sigemptyset(&sig.sa_mask);
	sigaddset(&sig.sa_mask, SIGUSR2);
	sig.sa_flags = SA_SIGINFO;
	sigaction(SIGUSR2, &sig, NULL);
}