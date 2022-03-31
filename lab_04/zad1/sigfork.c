#include <string.h>
#include <signal.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <wait.h>

typedef enum {
    ignore_action, 
    handler_action, 
    mask_action,
    pending_action,
    NONE_ACTION
} ActionType;

ActionType parseAction(char* input) {
    if(strcmp(input, "ignore") == 0)
        return ignore_action;
    if(strcmp(input, "handler") == 0)
        return handler_action;
    if(strcmp(input, "mask") == 0)
        return mask_action;
    if(strcmp(input, "pending") == 0)
        return pending_action;
    return NONE_ACTION;
}

void handle_signal() {
    puts("Handling signal!");
}

void do_mask_action() {
    sigset_t oldmask, blockmask;
    sigemptyset(&blockmask);
    sigaddset(&blockmask, SIGUSR1);
    sigprocmask(SIG_SETMASK, &blockmask, &oldmask);
}

void do_pending_action(const char* tag) {
    sigset_t pending_set;
    sigpending(&pending_set);
    
    const char* message = sigismember(&pending_set, SIGUSR1) ?  "Pending" : "Not pending";
    printf("[%s] %s\n", tag, message);
}


int main(int argc, char** argv) {
    if(argc != 2) {
        return 1;
    }

    const ActionType action = parseAction(argv[1]);
        
    #ifndef EXEC
    switch(action) {
        case ignore_action:
            signal(SIGUSR1, SIG_IGN);
            break;
        case handler_action:
            signal(SIGUSR1, handle_signal);
            break;
        case mask_action: 
            do_mask_action();
            break;
        case pending_action:
            do_mask_action();
            do_pending_action("Main");
            break;
        default: 
            return 1;
    }
    #endif 


    raise(SIGUSR1);

    #ifndef EXEC
    const pid_t pid = fork();
    if(pid == 0 && action != pending_action) {
        raise(SIGUSR1);
    }

    if(action == pending_action)
        do_pending_action(pid == 0 ? "Child" : "Main");   

    if(pid == 0 && action != handler_action) {
        puts("Running exec...");
        
        char** args = malloc(2 * sizeof(*args));
        args[0] = "./out/sigexec";
        args[1] = argv[1];
        execv(args[0], args);
    }
    #else
    if(action == pending_action)
        do_pending_action("Exec");   
    #endif 

    int status = 0;
    while (wait(&status) > 0);
}
