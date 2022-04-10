#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define BUFFER_SIZE 256

const char* commandSortMode(const char* str) {
	if(strcmp(str, "data") == 0)
		return "mail | tail -n +2";
	if(strcmp(str, "nadawca") == 0)
		return "mail | tail -n +2 | sort -k3d -";

	puts("Error!");
	exit(1);
}

int main(int argc, char** argv) {
	FILE* mail;
	if(argc == 2) {
		mail = popen(commandSortMode(argv[1]), "w");
		fputs("exit", mail);
		pclose(mail);
	} else if (argc == 4) {
		char command[BUFFER_SIZE];
		sprintf(command, "mail -s %s %s", argv[2], argv[1]);

		mail = popen(command, "w");

		fputs(argv[3], mail);
		
		pclose(mail);
	}
}
