#include "common.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#include <signal.h>
#include <sys/un.h>
#include <netinet/in.h>
#include <poll.h>
#include <ctype.h>

#define BOARD_SIZE 9
#define BOARD_SIDE_SIZE 3

char g_name[CLIENT_NAME_LENGTH];
int g_server_fd;


int* g_board;

typedef enum {
	arg__program_name,
    arg__client_name,
	arg__connect_mode,
	arg__server_address,
    ProgramArgsSize
} ProgramArgs;

typedef enum {
	figure_x = 1,
	figure_o = 2,
} Figures;
Figures g_figure;

Figures opponent_figure() {
	return g_figure == figure_x ? figure_o : figure_x;
}

int get_socket(int domain) {
	int fd = socket(domain, SOCK_STREAM, 0);
	if(fd < 0) {
		err("socket() failed");
	}
	return fd;
}

void init_board() {
	g_board = calloc(BOARD_SIZE, sizeof(*g_board));
}

void safe_connect(int socket_fd, struct sockaddr* addr, socklen_t addr_len) {
	if(connect(socket_fd, addr, addr_len) < 0) {
		err("connect() failed");
	}
}

void connect_to_server(const char* mode, const char* path_or_port) {
	if(strcmp(mode, "unix") == 0) {
		g_server_fd = get_socket(AF_UNIX);
		struct sockaddr_un addr;
		addr.sun_family = AF_UNIX;
		strcpy(addr.sun_path, path_or_port);
		safe_connect(g_server_fd, (struct sockaddr*)&addr, sizeof(addr));			
	}
	else if(strcmp(mode, "inet") == 0) {
		g_server_fd = get_socket(AF_INET);
		struct sockaddr_in addr;
		addr.sin_family = AF_INET;
		addr.sin_port = htons(atoi(path_or_port));
		addr.sin_addr.s_addr = INADDR_ANY;
		safe_connect(g_server_fd, (struct sockaddr*)&addr, sizeof(addr));			
	}
	else {
		err("wrong connect mode");
	} 
}

void get_client_name(const char* name) {
	if(strlen(name) != CLIENT_NAME_LENGTH)
		err("wrong client name length");
	strcpy(g_name, name);
}

void register_in_server() {
    send(g_server_fd, g_name, BUFFER_SIZE, 0);
}

int is_same_line() {
	for (int i = 0; i < BOARD_SIDE_SIZE; i++) {
		int coll = g_board[i * BOARD_SIDE_SIZE];
		int row = g_board[i];
		for (int i = 1; i < BOARD_SIDE_SIZE; i++) {
			if(coll != g_board[i * BOARD_SIDE_SIZE]) {
				coll = 0;
			} 
			if (row != g_board[i]) {
				row = 0;
			}
		}
		if(coll || row) {
			return coll || row;
		}
	}
	return 0;
}

int is_same_diagonal() {
	int left_to_right = g_board[0];
	int right_to_left = g_board[BOARD_SIDE_SIZE - 1];

	for (int i = 1; i < BOARD_SIDE_SIZE; i++) {
		if(left_to_right != g_board[i * (BOARD_SIDE_SIZE + 1)]) {
			left_to_right = 0;
		}
		if(right_to_left != g_board[i * (BOARD_SIDE_SIZE - 1)]) {
			right_to_left = 0;
		}
	}

	return left_to_right || right_to_left;
}

int is_draw() {
	for (int i = 0; i < BOARD_SIZE; i++) {
		if(g_board[i] == 0) {
			return 0;
		}
	}
	return 1;
}

int is_game_finished() {
	int line = is_same_line() || is_same_diagonal();
	if(line) {
		if(line == g_figure) {
			send(g_server_fd, WIN_MESS, BUFFER_SIZE, 0);
		} else {
			send(g_server_fd, LOSE_MESS, BUFFER_SIZE, 0);
		}
		return 1;
	}
	if(is_draw()) {
		send(g_server_fd, DRAW_MESS, BUFFER_SIZE, 0);
		return 1;
	}

	return 0;
}

void make_move() {
	char msg[BUFFER_SIZE];
	
	while(!is_move_mess(msg)) {
		printf("\nEnter move: ");
		scanf("%s", msg);
	}

	g_board[msg[0] - '0'] = g_figure;

	if (!is_game_finished()) {
		send(g_server_fd, msg, BUFFER_SIZE, 0);
	}
}

void client_loop(){
	char msg[BUFFER_SIZE];

	struct pollfd* socket_poll = malloc(sizeof(*socket_poll));
    socket_poll->fd = g_server_fd;
    socket_poll->events = POLLIN;

	while(1) {
		poll(socket_poll, 1, -1);

		if(recv(g_server_fd, msg, BUFFER_SIZE, 0) == -1) {
			continue;
		}

		if (strcmp(msg, PING_MESS) == 0) {
            send(g_server_fd, PING_MESS, BUFFER_SIZE, 0);
        } else if (strcmp(msg, NAME_TAKEN_MESS) == 0) {
            err("Client name(%s) already taken", g_name);
        } else if (strcmp(msg, SERVER_FULL_MESS) == 0) {
            err("Server is full");
		}else if (strcmp(msg, NO_OPPONENT_MESS) == 0) {
            puts("There is no opponent, waiting for someone...");
        } else if (strcmp(msg, SET_X_MESS) == 0) {
			puts("Your figure is X");
			g_figure = figure_x;
			init_board();
        } else if (strcmp(msg, SET_O_MESS) == 0) {
			puts("Your figure is O");
			g_figure = figure_o;
			init_board();
			make_move();
        } else if (strcmp(msg, WIN_MESS) == 0) {
			puts("You win");
			exit(0);
		} else if (strcmp(msg, LOSE_MESS) == 0) {
			puts("You lose");
			exit(0);
		} else if (strcmp(msg, DRAW_MESS) == 0) {
			puts("You draw");
			exit(0);
		} else if (is_move_mess(msg)) {
			g_board[msg[0] - '0'] = opponent_figure();
			make_move();
		} else {
			printf("Unknown message: %s\n", msg);
		}
	}
}

int main(int argc, char** argv) {
	if(argc != ProgramArgsSize)
		err("wrong args count");	

	get_client_name(argv[arg__client_name]);
	connect_to_server(argv[arg__connect_mode], argv[arg__server_address]);
	
	register_in_server();

	client_loop();
}