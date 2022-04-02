#ifndef COMMON
#define COMMON

#include <string.h>
#include <signal.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <wait.h>

typedef enum {
    KILL_MODE,
    SIGQUEUE_MODE,
    SIGRT_MODE,
    ERROR_MODE
} ModeType;

ModeType parseMode(const char*);
void send_signals(ModeType, pid_t, size_t, int, int);
sigset_t create_mask();
void handle_signal_counter(int signo, siginfo_t* info, void* context);
void setup_signal_handlers(void (*)(int, siginfo_t*, void*));

extern size_t g_signalCatchedCount;
extern int g_shouldListen;

#endif