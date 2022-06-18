#include "common.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#include <sys/un.h>
#include <netinet/in.h>
#include <pthread.h>
#include <poll.h>

#define MAX_CLIENTS_COUNT 10
#define PING_SLEEP_TIME 5

typedef struct{
    char* name;
    int socket_fd;
	int is_active;
	int opponent;
} client;

size_t g_client_count = 0;
client g_clients[MAX_CLIENTS_COUNT];
pthread_mutex_t g_mutex = PTHREAD_MUTEX_INITIALIZER;

typedef enum {
	arg__program_name,
    arg__port,
	arg__socket_path,
    ProgramArgsSize
} ProgramArgs;

typedef enum {
	client__local,
    client__web,
	AdditionalClientsSize
} AdditionalClients;

struct pollfd* get_clients_poll(int local_socket_fd, int web_socket_fd) {
	struct pollfd* sockets_fds = calloc(g_client_count + AdditionalClientsSize, sizeof(struct pollfd));
	sockets_fds[client__local].fd = local_socket_fd;
	sockets_fds[client__web].fd = web_socket_fd;
    for (int i = 0; i < g_client_count + AdditionalClientsSize; ++i) {
		sockets_fds[i].events = POLLIN;
    }
	pthread_mutex_lock(&g_mutex);
	for (int i = AdditionalClientsSize; i < g_client_count + AdditionalClientsSize; ++i) {
		sockets_fds[i].fd = g_clients[i - AdditionalClientsSize].socket_fd;
    }
	pthread_mutex_unlock(&g_mutex);

	return sockets_fds;
}

int poll_client_fd(struct pollfd* sockets_fds) {
	poll(sockets_fds, g_client_count + AdditionalClientsSize, -1);
	for(int i = 0; i < g_client_count + AdditionalClientsSize; ++i) {
		if(sockets_fds[i].revents & POLLIN) {
			return sockets_fds[i].fd;
		}
	}	

	return -1;
}

int get_client_fd(int local_socket_fd, int web_socket_fd) {
	struct pollfd* sockets_fds = get_clients_poll(local_socket_fd, web_socket_fd);
	poll(sockets_fds, g_client_count + AdditionalClientsSize, -1);
	const int client_fd = poll_client_fd(sockets_fds);
	free(sockets_fds);
	
	return (client_fd == local_socket_fd || client_fd == web_socket_fd)
		? accept(client_fd, NULL, NULL)
		: client_fd;
}

void remove_offline_clients() {
	int i = 0;
	while(i < g_client_count) {
		if (!g_clients[i].is_active) {
			if (i < g_client_count - 1) {
				g_clients[i] = g_clients[g_client_count - 1];
			}
			--g_client_count;
		} else {
			++i;
		}
	}
}

void ping_all_clients() {
	for (int i = 0; i < g_client_count; i++){
		if(g_clients[i].is_active) {
			send(g_clients[i].socket_fd, PING_MESS, BUFFER_SIZE, 0);
			g_clients[i].is_active = 0;
		}
	}
}

void* ping_handler(void* args){
    while(1){
        pthread_mutex_lock(&g_mutex);
        remove_offline_clients();
        ping_all_clients();
        pthread_mutex_unlock(&g_mutex);
        sleep(PING_SLEEP_TIME);
    }

	return NULL;
}

int is_finishing_mess(const char* message) {
	return strcmp(message, WIN_MESS) == 0
		|| strcmp(message, LOSE_MESS) == 0
		|| strcmp(message, DRAW_MESS) == 0;
}

int is_name_mess(const char* message) {
	return strlen(message) == CLIENT_NAME_LENGTH;
}

int is_name_taken(const char* name) {
	for(int i = 0; i < g_client_count; ++i) {
		if(strcmp(name, g_clients[i].name) == 0) {
			return 1;
		}
	}
	return 0;
}

int find_opponent(int id) {
	for(int i = 0; i < g_client_count; ++i) {
		if(g_clients[i].is_active && i != id) {
			return i;
		}
	}
	return -1;
}

void server_loop(int local_socket_fd, int web_socket_fd) {
	char msg[BUFFER_SIZE];

	while(1) {
		int client_socket_fd = get_client_fd(local_socket_fd, web_socket_fd);
		if (recv(client_socket_fd, msg, BUFFER_SIZE, 0) == -1) {
            sleep(1);
            continue;
        }

		pthread_mutex_lock(&g_mutex);
		if (strcmp(msg, PING_MESS) == 0) {
            for (int i = 0; i < g_client_count; ++i) {
                if (g_clients[i].socket_fd == client_socket_fd) {
                    g_clients[i].is_active = 1;
					break;
                }
            }
        } else if (is_finishing_mess(msg)) {
            for (int i = 0; i < g_client_count; i++) {
				if (g_clients[i].socket_fd == client_socket_fd) {
					g_clients[i].is_active = 0;
					g_clients[g_clients[i].opponent].is_active = 0;
					printf("Game (%s vs %s) finished\n", g_clients[i].name, g_clients[g_clients[i].opponent].name);
				}
			}
			remove_offline_clients();
		} else if (is_move_mess(msg)) {
            for (int i = 0; i < g_client_count; i++) {
				if (g_clients[i].socket_fd == client_socket_fd) {
					if (g_clients[g_clients[i].opponent].socket_fd == -1) {
                        send(client_socket_fd, WIN_MESS, BUFFER_SIZE, 0);
						g_clients[i].is_active = 0;
						printf("Game with %s finished (opponent left the game)\n", g_clients[i].name);
						remove_offline_clients();
					} else {
						printf("Move [%s] from %s in game against %s\n", msg, g_clients[i].name, g_clients[g_clients[i].opponent].name);
                        send(g_clients[g_clients[i].opponent].socket_fd, msg, BUFFER_SIZE, 0);
                    }
				}
			}
        } else if (is_name_mess(msg)) {
			if (is_name_taken(msg)) {
				printf("Registration failed: name(%s) is already taken\n", msg);
				send(client_socket_fd, NAME_TAKEN_MESS, BUFFER_SIZE, 0);
			} else if (g_client_count == MAX_CLIENTS_COUNT) {
				printf("Registration failed: server is full\n");
				send(client_socket_fd, SERVER_FULL_MESS, BUFFER_SIZE, 0);
			} else {
				g_clients[g_client_count].socket_fd = client_socket_fd;
				strcpy(g_clients[g_client_count].name, msg);
				g_clients[g_client_count].is_active = 1;
				printf("Client %s registered\n", g_clients[g_client_count].name);
				++g_client_count;

				int opponent_id = find_opponent(g_client_count - 1);
				if (opponent_id != -1) {
					g_clients[opponent_id].opponent = g_client_count - 1;
					g_clients[g_client_count - 1].opponent = opponent_id;
					send(g_clients[opponent_id].socket_fd, SET_O_MESS, BUFFER_SIZE, 0);
					send(client_socket_fd, SET_X_MESS, BUFFER_SIZE, 0);
					printf("New game started: %s vs %s\n", g_clients[g_client_count - 1].name, g_clients[opponent_id].name);
				} else {
					send(client_socket_fd, NO_OPPONENT_MESS, BUFFER_SIZE, 0);
				}
			}
		} else {
			printf("Unknown message: %s\n", msg);
		}
		pthread_mutex_unlock(&g_mutex);
	}
}

void listen_and_bind(int socket_fd, struct sockaddr* socket_addr, socklen_t socket_len) {
	int socket_bind = bind(socket_fd, socket_addr, socket_len);
	if(socket_bind == -1)
		err("bind failed");
	int socket_listen = listen(socket_fd, MAX_CLIENTS_COUNT);
	if(socket_listen == -1)
		err("listen failed");
}

int main(int argc, char** argv) {
	if(argc != ProgramArgsSize)
		err("wrong args count");

	int port = atoi(argv[arg__port]);
	char* socket_path = argv[arg__socket_path];

	int local_socket_fd = socket(AF_UNIX, SOCK_STREAM, 0);
	int web_socket_fd = socket(AF_INET, SOCK_STREAM, 0);
	if(local_socket_fd == -1 || web_socket_fd == -1) 
		err("socket() failed");

	struct sockaddr_un local_socket_addr;
	local_socket_addr.sun_family = AF_UNIX;
	strcpy(local_socket_addr.sun_path, socket_path);
	listen_and_bind(local_socket_fd, (struct sockaddr*)&local_socket_addr, sizeof(local_socket_addr));

	struct sockaddr_in web_socket_addr;
	web_socket_addr.sin_family = AF_INET;
	web_socket_addr.sin_port = htons(port);
	web_socket_addr.sin_addr.s_addr = INADDR_ANY;
	listen_and_bind(web_socket_fd, (struct sockaddr*)&web_socket_addr, sizeof(web_socket_addr));
	
	pthread_t t;
    if(pthread_create(&t, NULL, ping_handler, NULL))
		err("ping_handler - pthread_create() failed");

	server_loop(local_socket_fd, web_socket_fd);
}