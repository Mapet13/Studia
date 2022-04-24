#include <sys/msg.h>
#include <sys/ipc.h>

#include <stdlib.h>
#include <errno.h>
#include <stdio.h>

#define MAX_ID 10
#define KEY_PATH getenv("HOME")

#define PROJ_ID 'D'

#define BUFFER_SIZE 256

typedef enum {
    ERROR_MESS,
    INIT_MESS,
    LIST_MESS,
    ALL_MESS,
    ONE_MESS,
    STOP_MESS
} MESSAGE_TYPE;

typedef struct {
    key_t key;
    int id;
} Queue_data;

typedef struct {
    long type;
    int queue_id;
    int client_id;
    char message_body[BUFFER_SIZE];
    int additional_id;
} Message;

void send_message(int queue_id, const Message* message) {
    if(msgsnd(queue_id, message, sizeof(*message) - sizeof(long), 0) == -1) {
        switch(errno) {
            case EAGAIN: puts("Error! - Queue is full"); break;
            case EACCES: puts("Error! - No acces to writing in queue"); break;
            case EFAULT: puts("Error! - Invalid message address"); break;
            case EIDRM: puts("Error! - Queue was removed"); break;
            case EINTR: puts("Error! - Gets signal while waiting"); break;
            case EINVAL: puts("Error! - Invalid queue/Invalid message"); break;
            case ENOMEM: puts("Error! - No momory"); break;
            default: puts("Error!"); break;
        }
    }
}