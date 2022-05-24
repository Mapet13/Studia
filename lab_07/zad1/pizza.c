#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/sem.h>
#include <sys/shm.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <time.h>
#include <unistd.h>

#define BUFFER_SIZE 256

#define PIZZA_OVEN_CAPACITY 5
#define TABLE_CAPACITY 5
#define MAX_PIZZA_ID 9

#define MIN_TIME_TO_PREPARE 1
#define MAX_TIME_TO_PREPARE 2

#define MIN_TIME_TO_BAKE 4
#define MAX_TIME_TO_BAKE 5

#define MIN_DELIVERY_TIME 4
#define MAX_DELIVERY_TIME 5

#define SEM_KEY (ftok(getenv("HOME"), 'A'))
#define OVEN_KEY (ftok(getenv("HOME"), 'B'))
#define TABLE_KEY (ftok(getenv("HOME"), 'C'))

#define MAX(a, b) (((a) > (b)) ? (a) : (b))

typedef struct {
    int pizza[MAX(PIZZA_OVEN_CAPACITY, TABLE_CAPACITY)];
} PizzaHolder;

typedef enum {
    OvenAccesSemID,
    OvenPizzaCountSemID,
    OvenPizzaFreeCountSemID,
    TableAccesSemID,
    TablePizzaCountSemID,
    TablePizzaFreeCountSemID,
    SEMAFORS_COUNT
} SemaforType;

static int g_time_start;
static int g_sem_id;

static PizzaHolder* g_oven;
static PizzaHolder* g_table;

void print_message(char* format, ...) {
    char message[BUFFER_SIZE];
    va_list myargs;
    va_start(myargs, format);
    vsprintf(message, format, myargs);
    printf("(%d %u) %s \n", getpid(), (unsigned)time(NULL) - g_time_start, message);
    va_end(myargs);
    fflush(stdout);
}

int getRandomPizza() { return rand() % MAX_PIZZA_ID; }
int getPrepareTime() { return (rand() % (MAX_TIME_TO_PREPARE - MIN_TIME_TO_PREPARE)) + MIN_TIME_TO_PREPARE; }
int getBakeTime() { return (rand() % (MAX_TIME_TO_BAKE - MIN_TIME_TO_BAKE)) + MIN_TIME_TO_BAKE; }
int getDeliveryTime() { return (rand() % (MAX_DELIVERY_TIME - MIN_DELIVERY_TIME)) + MIN_DELIVERY_TIME; }

///////////////////////////////////////////////////////////////////////////////////////////
struct sembuf inrementSemaphore(SemaforType type) {
    struct sembuf operation;
    operation.sem_num = type;
    operation.sem_op = 1;
    operation.sem_flg = 0;
    return operation;
}

struct sembuf decrementSemaphore(SemaforType type) {
    struct sembuf operation;
    operation.sem_num = type;
    operation.sem_op = -1;
    operation.sem_flg = 0;
    return operation;
}


int putPizzaIntoOven(int pizza_id) {
    struct sembuf operations[3];

    operations[0] = decrementSemaphore(OvenAccesSemID);
    operations[1] = inrementSemaphore(OvenPizzaCountSemID);
    operations[2] = decrementSemaphore(OvenPizzaFreeCountSemID);
    
    semop(g_sem_id, operations, 3);

    int size = semctl(g_sem_id, OvenPizzaCountSemID, GETVAL);
    g_oven->pizza[size - 1] = pizza_id;

    operations[0] = inrementSemaphore(OvenAccesSemID);
    semop(g_sem_id, operations, 1);

    return size;
}

int takePizzaFromOven() {
    struct sembuf operations[3];
    operations[0] = decrementSemaphore(OvenAccesSemID);
    operations[1] = decrementSemaphore(OvenPizzaCountSemID);
    operations[2] = inrementSemaphore(OvenPizzaFreeCountSemID);

    semop(g_sem_id, operations, 3);
    
    int size = semctl(g_sem_id, OvenPizzaCountSemID, GETVAL);
    int pizza_id = g_oven->pizza[size];
    g_oven->pizza[size] = -1;

    operations[0] = inrementSemaphore(OvenAccesSemID);
    semop(g_sem_id, operations, 1);

    return pizza_id;
}

int putPizzaOnTable(int pizza_id) {
    struct sembuf operations[3];
    operations[0] = decrementSemaphore(TableAccesSemID);
    operations[1] = inrementSemaphore(TablePizzaCountSemID);
    operations[2] = decrementSemaphore(TablePizzaFreeCountSemID);
    
    semop(g_sem_id, operations, 3);
    
    int size = semctl(g_sem_id, TablePizzaCountSemID, GETVAL);
    g_table->pizza[size - 1] = pizza_id;

    operations[0] = inrementSemaphore(TableAccesSemID);
    semop(g_sem_id, operations, 1);

    return size;
}

int takePizzaFromUnlockedTable() {
    struct sembuf operations[3];
    operations[0] = decrementSemaphore(TableAccesSemID);
    operations[1] = decrementSemaphore(TablePizzaCountSemID);
    operations[2] = inrementSemaphore(TablePizzaFreeCountSemID);
    
    semop(g_sem_id, operations, 3);
    
    int size = semctl(g_sem_id, TablePizzaCountSemID, GETVAL);
    int pizza_id = g_table->pizza[size];
    g_table->pizza[size] = -1;

    operations[0] = inrementSemaphore(TableAccesSemID);
    semop(g_sem_id, operations, 1);

    return pizza_id;
}
///////////////////////////////////////////////////////////////////////////////////////////

void init() {
    srand(time(NULL) * getpid());
    g_sem_id = semget(SEM_KEY, 0, 0666);
    g_time_start = (unsigned)time(NULL);
    g_oven = shmat(shmget(OVEN_KEY, 0, 0666), NULL, 0);
    g_table = shmat(shmget(TABLE_KEY, 0, 0666), NULL, 0);
}

void bake(int pizza_id) {
    int current_pizza_count = putPizzaIntoOven(pizza_id);

    print_message("[C] Dodałem pizze: %d. Liczba pizz w piecu: %d.", pizza_id, current_pizza_count);
    sleep(getBakeTime());
}

void preparePizza(int pizza_id) {
    sleep(getPrepareTime());
    print_message("[C] Przygotowuje pizze: %d", pizza_id);
}

void takePizzaAndPutOnTable() {
    int pizza_id = takePizzaFromOven();
    int current_pizza_in_oven_count = semctl(g_sem_id, OvenPizzaCountSemID, GETVAL);
    
    int current_pizza_on_table_count = putPizzaOnTable(pizza_id);

    print_message("[C] Wyjmuję pizze: %d. Liczba pizz w piecu: %d. Liczba pizz na stole: %d.", pizza_id, current_pizza_in_oven_count, current_pizza_on_table_count);
}

void cookLoop() {
    init();
    while (1) {
        const int pizza_id = getRandomPizza();
        preparePizza(pizza_id);
        bake(pizza_id);
        takePizzaAndPutOnTable();
    }
}

int takePizzaFromTable() {
    int pizza_id = takePizzaFromUnlockedTable();
    int current_pizza_count = semctl(g_sem_id, TablePizzaCountSemID, GETVAL);

    print_message("[S] Pobieram pizze: %d Liczba pizz na stole: %d.", pizza_id, current_pizza_count);

    return pizza_id;
}

void deliverPizza(int pizza_id) {
    int deliveryTime = getDeliveryTime();
    sleep(deliveryTime);
    print_message("[S] Dostarczam pizze: %d.", pizza_id);
    sleep(deliveryTime);
}

void supplierLoop() {
    init();
    while (1) {
        int pizza_id = takePizzaFromTable();
        deliverPizza(pizza_id);
    }
}

int main(int argc, char** argv) {
    if (argc != 3) return 1;
    
    srand(time(NULL));
    
    int oven = shmget(OVEN_KEY, sizeof(PizzaHolder), IPC_CREAT | 0666);
    int table = shmget(TABLE_KEY, sizeof(PizzaHolder), IPC_CREAT | 0666);
    
    const int CookCount = atoi(argv[1]);
    const int SupplierCount = atoi(argv[2]);
    
    g_oven = shmat(oven, NULL, 0);
    g_table = shmat(table, NULL, 0);
    for(int i = 0; i < PIZZA_OVEN_CAPACITY; ++i){
        g_oven->pizza[i] = -1;
        g_table->pizza[i] = -1;
    }

    g_oven = NULL;
    g_table = NULL;

    int sem = semget(SEM_KEY, SEMAFORS_COUNT, IPC_CREAT | 0600);
    semctl(sem, OvenPizzaCountSemID, SETVAL, 0);
    semctl(sem, TablePizzaCountSemID, SETVAL, 0);
    semctl(sem, OvenPizzaFreeCountSemID, SETVAL, PIZZA_OVEN_CAPACITY);
    semctl(sem, TablePizzaFreeCountSemID, SETVAL, TABLE_CAPACITY);
    semctl(sem, OvenAccesSemID, SETVAL, 1);
    semctl(sem, TableAccesSemID, SETVAL, 1);

    for (int i = 0; i < CookCount; ++i) {
        if (fork() == 0) cookLoop();
    }

    for (int i = 0; i < SupplierCount; ++i) {
        if (fork() == 0) supplierLoop();
    }

    int status = 0;
    while (wait(&status) > 0)
        ;
}
