#include "common.h"

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <stdlib.h>


typedef struct {
	Queue_data server_data;
	Queue_data client_data;
	int id;
} ClientContext;
ClientContext g_context;

Queue_data create_queue(int id) {
	Queue_data data;

	struct mq_attr attr;
	attr.mq_maxmsg = 10;
	attr.mq_msgsize = sizeof(Message);
	attr.mq_flags = 0;
	attr.mq_curmsgs = 0;

    sprintf(data.name, "/client_%d", id);

    data.id = mq_open(data.name,  O_RDWR | O_CREAT | O_NONBLOCK, 0666, &attr);

	return data;
}

int is_queue_empty(int queue_id) {
	struct mq_attr attr;
    mq_getattr(queue_id, &attr);

    return attr.mq_curmsgs == 0;
}

int register_in_server(int server_id, int client_id) {
	puts("[CLIENT INFO] Sending INIT to server");

	Message mess;
	mess.type = INIT_MESS;
	strcpy(mess.message_body, g_context.client_data.name);

	send_message(server_id, &mess);

	printf("[CLIENT INFO] Waitnig for server response on queue %d....\n", client_id);

	while(is_queue_empty(client_id));

	mq_receive(client_id, (char*)&mess, sizeof(mess), 0);

	printf("[CLIENT INFO] Registration process finished (id: %d)\n", mess.client_id);

	return mess.client_id;
}

MESSAGE_TYPE parse_message(const char* buffer) {
	if(strcmp("LIST\n", buffer) == 0) return LIST_MESS; 
	if(strcmp("2ALL\n", buffer) == 0) return ALL_MESS; 
	if(strcmp("2ONE\n", buffer) == 0) return ONE_MESS; 
	if(strcmp("STOP\n", buffer) == 0) return STOP_MESS; 
	return ERROR_MESS; 
}

MESSAGE_TYPE read_action() {
	char buffer[BUFFER_SIZE];
    fgets(buffer, BUFFER_SIZE, stdin);

	return parse_message(buffer);
}

void send_message_to_server(MESSAGE_TYPE type, int id, Queue_data server_data) {
	Message mess;
	mess.type = type;
	mess.client_id = id;

	// intended fallthrough
	switch(type) {
		case ONE_MESS:
			fflush(stdout);
			printf("ID: ");
			scanf("%d", &mess.additional_id);
		case ALL_MESS:
			fflush(stdout);
			printf("Message: ");
			scanf("%s", mess.message_body);
		case LIST_MESS: 
		case STOP_MESS: 
			send_message(server_data.id, &mess);
			break;
		default: puts("Unknown! Try again...");
	}
}

void clear() {
	mq_close(g_context.client_data.id);
    mq_close(g_context.server_data.id);
    mq_unlink(g_context.client_data.name);
}

void stop_action() {
	Message mess;
	mess.type = STOP_MESS;
	mess.client_id = g_context.id;
	send_message(g_context.server_data.id, &mess);

	clear();

	exit(0);
}

void handle_response(const Message* mess) {
	switch (mess->type)
	{
		case STOP_MESS:
			stop_action();
			break;
		case ALL_MESS:
		case ONE_MESS:
			printf("[%d] %s\n>>> ", mess->client_id, mess->message_body);
			fflush(stdout);
			break;
		default: break;
	}
}

void catch_response(Queue_data client_data) {
	while(!is_queue_empty(client_data.id)) {
		Message mess;
		mq_receive(client_data.id, (char*)&mess, sizeof(mess), 0);
		handle_response(&mess);
	}
}

int has_input() {
	// https://stackoverflow.com/questions/34479795/make-c-not-wait-for-user-input/34479916
	fd_set readfds;
    FD_ZERO(&readfds);

    struct timeval timeout;
    timeout.tv_sec = 0;
    timeout.tv_usec = 0;

    FD_SET(STDIN_FILENO, &readfds);
    select(STDIN_FILENO + 1, &readfds, NULL, NULL, &timeout);

    return (FD_ISSET(0, &readfds));
}

void client_loop(Queue_data client_data, Queue_data server_data, int id) {
	printf(">>> ");
	fflush(stdout);

	while(1) {	
		if(has_input()) {
			MESSAGE_TYPE type = read_action(); 
			send_message_to_server(type, id, server_data);
			
			if(type == STOP_MESS) {
				clear();
				break;
			} 

			printf(">>> ");
			fflush(stdout);
		}

		sleep(1);
		catch_response(client_data);
	}

}


int main(int argc, char** argv) {
	puts("[CLIENT INFO] Starting...");

	g_context.client_data = create_queue(getpid());
	g_context.server_data.id = mq_open(SERVER_QUEUE_NAME, O_WRONLY);

	if(g_context.client_data.id == -1 || g_context.server_data.id == -1)
		return 1;

	printf("[CLIENT INFO] Client queue id: %d, name: %s\n", g_context.client_data.id, g_context.client_data.name);
	printf("[CLIENT INFO] Server queue id: %d\n", g_context.server_data.id);

	g_context.id = register_in_server(g_context.server_data.id, g_context.client_data.id);
	
	signal(SIGINT, stop_action);
	
	client_loop(g_context.client_data, g_context.server_data, g_context.id);
}
