#include "common.h"

#include <stdio.h>
#include <signal.h>
#include <string.h>


typedef struct {
	int is_connected;
	int queue_id;
	char queue_name[BUFFER_SIZE];
} ClientData;

typedef struct {
	ClientData clients[MAX_ID];
	size_t next_free_id;
	Queue_data server_data;
} ServerContext;
ServerContext g_context;


void shutdown();

Queue_data create_queue() {
	struct mq_attr attr;
	attr.mq_maxmsg = 10;
	attr.mq_msgsize = sizeof(Message);
	attr.mq_flags = 0; 
	attr.mq_curmsgs = 0;

	Queue_data data;
    data.id = mq_open(SERVER_QUEUE_NAME,  O_RDWR | O_CREAT, 0666, &attr);

	return data;
}

void find_next_free_id() {
	size_t id = g_context.next_free_id;
	
	do  {
		++g_context.next_free_id;
		g_context.next_free_id %= MAX_ID; 
		
		if(!g_context.clients[g_context.next_free_id].is_connected)
			return;
	} while(g_context.next_free_id != id);

	g_context.next_free_id = MAX_ID;
}

void init_action(const Message* message) {
	if(g_context.next_free_id == MAX_ID) {
		puts("[SERVER ERROR] maximum number of clients is already registered in server");
	}
	
	puts("[SERVER INFO] Init action - start");

	size_t id = g_context.next_free_id;
	find_next_free_id();

	g_context.clients[id].is_connected = 1;

	strcpy(g_context.clients[id].queue_name, message->message_body);
	g_context.clients[id].queue_id = mq_open(message->message_body, O_WRONLY);

	printf("[SERVER INFO] Init action - sending id(%ld) to client via %d(%s) \n", id, g_context.clients[id].queue_id, message->message_body);

	Message mess;
	mess.client_id = id;
	mess.type = INIT_MESS;
	send_message(g_context.clients[id].queue_id, &mess);

	puts("[SERVER INFO] Init action - end");
}

void list_action(const Message* message){
	puts("Clients:");
    for(int i = 0; i < MAX_ID; ++i){
        if (g_context.clients[i].is_connected){
            printf("%d\n", i);
        }
    }
}

void all_action(const Message* message){
	printf("[SERVER INFO] 2ALL action (from %d) - star\n", message->client_id);
	for(int i = 0; i < MAX_ID; ++i){
        if (g_context.clients[i].is_connected && i != message->client_id){
			printf("[SERVER INFO] sending message to %d\n", i);
			send_message(g_context.clients[i].queue_id, message);
		}	
    }
	puts("[SERVER INFO] 2ALL action - end");
}

void one_action(const Message* message){
	puts("[SERVER INFO] 2ONE action - start");
	if (g_context.clients[message->additional_id].is_connected){
		send_message(g_context.clients[message->additional_id].queue_id, message);
    }
	puts("[SERVER INFO] 2ONE action - end");
}

void stop_action(const Message* message) {
	printf("[SERVER INFO] STOP action from %d\n", message->client_id);
	mq_close(g_context.clients[message->client_id].queue_id);
	g_context.clients[message->client_id].is_connected = 0;
}

void server_loop() {
	int is_running = 1;

	while(is_running) {
		Message mess;
		mess.type = ERROR_MESS;

		unsigned int type;
		mq_receive(g_context.server_data.id, (char*)&mess, sizeof(mess), &type);

		switch(mess.type) {
			case INIT_MESS: init_action(&mess); break;
			case LIST_MESS:list_action(&mess); break;
			case ALL_MESS: all_action(&mess); break;
			case ONE_MESS: one_action(&mess); break;
			case STOP_MESS: stop_action(&mess);  break;
			default:
				break;
		}

	}
}

void shutdown() {
    Message message;
	message.type = STOP_MESS;

    for(int i = 0; i < MAX_ID; ++i){
		if (g_context.clients[i].is_connected) {
			send_message(g_context.clients[i].queue_id, &message);
			mq_close(g_context.clients[i].queue_id);
        }
    }

    mq_close(g_context.server_data.id);
    mq_unlink(SERVER_QUEUE_NAME);

	exit(0);
}

int main(int argc, char** argv) {
	puts("[SERVER INFO] Starting...");
	
	g_context.next_free_id = 0;
	g_context.server_data = create_queue();

	if(g_context.server_data.id == -1) 
		return 1;

	printf("[SERVER INFO] Queue id: %d\n", g_context.server_data.id);

	signal(SIGINT, shutdown);

	puts("[SERVER INFO] Loop - starts");

	server_loop(g_context.server_data);

}
