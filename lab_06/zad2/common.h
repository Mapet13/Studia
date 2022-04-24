#include <mqueue.h>

#include <stdlib.h>
#include <errno.h>
#include <stdio.h>

#define MAX_ID 10
#define SERVER_QUEUE_NAME "/server_queue"

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
    int id;
    char name[BUFFER_SIZE];
} Queue_data;

typedef struct {
    long type;
    int queue_id;
    int client_id;
    char message_body[BUFFER_SIZE];
    int additional_id;
} Message;

void send_message(int queue_id, const Message* message) {
    mq_send(queue_id, (const char*)message, sizeof(*message), message->type);
}