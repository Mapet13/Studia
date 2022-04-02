#ifndef COMMON
#define COMMON

#include <string.h>
#include <signal.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <wait.h>

void send_signals(pid_t, size_t, int);
sigset_t create_mask();
void handle_signal_counter();
void setup_signal_handlers(void (*finish_signal_handler)());

extern size_t g_signalCatchedCount;
extern int g_shouldListen;

#endif