#include <string.h>
#include <signal.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <wait.h>

#define MAX_CALLS 3
#define TESTING_SIGNAL SIGUSR1

void siginfo_handler(int signal_id, siginfo_t* info, void* context) {
	puts("---------------------------------------------------");
    printf("Signal ID: %d\n", signal_id);
	printf("PID: %d\n", info->si_pid);
	printf("UID: %d\n", info->si_uid);
	printf("Signal number: %u\n", info->si_signo);
	printf("Count of attempted syscalls: %u\n", info->si_syscall);
	printf("System time consumed: %ld\n", info->si_stime);
	puts("---------------------------------------------------");
}

int g_call_id = 0;

void rising_handler(int signal_id, siginfo_t* info, void* context) {
	if(g_call_id < MAX_CALLS) {
        printf("call id: %d\n", g_call_id);
        g_call_id++;
        raise(TESTING_SIGNAL);
    }
}

void run_test(int flag_id, void (*handler)(int, siginfo_t*, void*)) {
    printf(" >>> Testing flag %#x with signal %d <<< \n", flag_id, TESTING_SIGNAL);

	struct sigaction sig;
	sigemptyset(&sig.sa_mask);
	sig.sa_flags = flag_id;
	sig.sa_sigaction = handler;
	sigaction(TESTING_SIGNAL, &sig, NULL);

    g_call_id = 0;
	raise(TESTING_SIGNAL);
}

int main() {
    run_test(SA_SIGINFO, siginfo_handler);
    run_test(SA_NODEFER, rising_handler);
    run_test(SA_RESETHAND, rising_handler);
}
