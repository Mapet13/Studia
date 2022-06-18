#define CLIENT_NAME_LENGTH 5
#define BUFFER_SIZE 64

#define PING_MESS "[PING]"
#define SERVER_FULL_MESS "[SERVER_FULL]"
#define NAME_TAKEN_MESS "[TAKEN]"
#define NO_OPPONENT_MESS "[NO OPPONENT]"
#define SET_X_MESS "[SET] X"
#define SET_O_MESS "[SET] O"
#define WIN_MESS "[WIN]"
#define LOSE_MESS "[LOSE]"
#define DRAW_MESS "[DRAW]"

void err(char* format, ...);
int is_move_mess(const char* msg);
