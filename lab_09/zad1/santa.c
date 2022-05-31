#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define WORKSHOP_ELVES_MAX_COUNT 3

#define GIFTS_COUNT 3
#define REINDEERS_COUNT 9
#define ELVES_COUNT 10

#define ELVES_WORK_MIN 2
#define ELVES_WORK_MAX 5

#define ELVES_SANTA_MEET_MIN 1
#define ELVES_SANTA_MEET_MAX 2

#define REINDEERS_HOLIDAY_MIN 5
#define REINDEERS_HOLIDAY_MAX 10

#define DELIVER_MIN 2
#define DELIVER_MAX 4

typedef struct {
    pthread_mutex_t santaWakeUpMutex;
    pthread_mutex_t reindeersWaitingMutex;
    pthread_mutex_t reindeersGoMutex;
    pthread_mutex_t elvesWaitingMutex;
    pthread_mutex_t elvesGoMutex;

    pthread_cond_t santaWakeUpCond;
    pthread_cond_t reindeersGoCond;
    pthread_cond_t elvesWaitingCond;
    pthread_cond_t elvesGoCond;
    
    int delivered_gifts_count;
    int shouldSantaWake;
    int reindeersWaitingCount;
    int elvesWaitingCount;
    int reindeersToGo[REINDEERS_COUNT];
    int elvesWaiting[WORKSHOP_ELVES_MAX_COUNT];
    int elvesToGo[ELVES_COUNT];
} ThreadArgs;

void wait_for_time(int min, int max) {
    int time_to_work = (rand() % (max - min)) + min;
    sleep(time_to_work);
}

void santa_sleep(ThreadArgs* threadArgs) {
    pthread_mutex_lock(&threadArgs->santaWakeUpMutex);
    while(threadArgs->shouldSantaWake == 0){
        pthread_cond_wait(&threadArgs->santaWakeUpCond, &threadArgs->santaWakeUpMutex);
    }
    threadArgs->shouldSantaWake = 0;
    pthread_mutex_unlock(&threadArgs->santaWakeUpMutex);
}

void* santa_work(void* args) {
    ThreadArgs* threadArgs = (ThreadArgs*)args;

    while(threadArgs->delivered_gifts_count < GIFTS_COUNT) {
        santa_sleep(threadArgs);
        puts("Mikołaj: budzę się");
        
        int should_deliver = 0;
        pthread_mutex_lock(&threadArgs->reindeersWaitingMutex);
        if(threadArgs->reindeersWaitingCount >= REINDEERS_COUNT){
            should_deliver = 1;
            threadArgs->reindeersWaitingCount = 0;
            pthread_mutex_lock(&threadArgs->reindeersGoMutex);
            for(int i = 0; i < REINDEERS_COUNT; i++){
                threadArgs->reindeersToGo[i] = 1;
            }
            ++(threadArgs->delivered_gifts_count);
            pthread_mutex_unlock(&threadArgs->reindeersGoMutex);
            pthread_cond_broadcast(&threadArgs->reindeersGoCond);
        }
        pthread_mutex_unlock(&threadArgs->reindeersWaitingMutex);

        if(should_deliver){
            puts("Mikołaj: dostarczam zabawki");
            wait_for_time(DELIVER_MIN, DELIVER_MAX);
        }

        int should_meet_elves = 0;
        pthread_mutex_lock(&threadArgs->elvesWaitingMutex);
        if(threadArgs->elvesWaitingCount == WORKSHOP_ELVES_MAX_COUNT){
            should_meet_elves = 1;
        }
        pthread_mutex_unlock(&threadArgs->elvesWaitingMutex);

        if(should_meet_elves) {
            pthread_mutex_lock(&threadArgs->elvesGoMutex);
            pthread_mutex_lock(&threadArgs->elvesWaitingMutex);
            
            printf("Mikołaj: rozwiązuję problemy elfów %d %d %d\n",
            threadArgs->elvesWaiting[0],
            threadArgs->elvesWaiting[1],
            threadArgs->elvesWaiting[2]);
            
            for(int i = 0; i < WORKSHOP_ELVES_MAX_COUNT; ++i){
                threadArgs->elvesToGo[threadArgs->elvesWaiting[i]] = 1;
            }
            
            pthread_cond_broadcast(&threadArgs->elvesGoCond);
            pthread_mutex_unlock(&threadArgs->elvesGoMutex);
            wait_for_time(ELVES_SANTA_MEET_MIN, ELVES_SANTA_MEET_MAX);
            for(int i = 0; i < WORKSHOP_ELVES_MAX_COUNT; ++i){
                threadArgs->elvesWaiting[i] = -1;
            }
            threadArgs->elvesWaitingCount = 0;
            pthread_cond_broadcast(&threadArgs->elvesWaitingCond);
            pthread_mutex_unlock(&threadArgs->elvesWaitingMutex);
        }

        if(threadArgs->delivered_gifts_count < GIFTS_COUNT)
            puts("Mikołaj: zasypiam"); 
    }

    puts("Mikołaj: kończe prace"); 

    return NULL;
}

int get_reindeer_id(ThreadArgs* threadArgs) {
    for(int i = 0; i < REINDEERS_COUNT; ++i){
        if(threadArgs->reindeersToGo[i] == 0){
            threadArgs->reindeersToGo[i] = 1;
            return i;
        }
    }
    return -1;
}

void unlock_reindeers_to_work(ThreadArgs* threadArgs) {
    for(int i = 0; i < REINDEERS_COUNT; ++i)
        threadArgs->reindeersToGo[i] = 0;
    pthread_cond_broadcast(&threadArgs->reindeersGoCond);
}

int register_reindeer(ThreadArgs* threadArgs) {
    pthread_mutex_lock(&threadArgs->reindeersGoMutex);
    const int entityID = get_reindeer_id(threadArgs);
    if(entityID + 1 == REINDEERS_COUNT) {
        unlock_reindeers_to_work(threadArgs);
    }
    pthread_mutex_unlock(&threadArgs->reindeersGoMutex);

    pthread_mutex_lock(&threadArgs->reindeersGoMutex);
    while(threadArgs->reindeersToGo[entityID] == 1){
        pthread_cond_wait(&threadArgs->reindeersGoCond, &threadArgs->reindeersGoMutex);
    }
    pthread_mutex_unlock(&threadArgs->reindeersGoMutex);
    
    return entityID;
}

void* reindeers_work(void* args) {
    ThreadArgs* threadArgs = (ThreadArgs*)args;

    const int entityID = register_reindeer(threadArgs);

    while(1) {
        wait_for_time(REINDEERS_HOLIDAY_MIN, REINDEERS_HOLIDAY_MAX);

        pthread_mutex_lock(&threadArgs->reindeersWaitingMutex);
        ++(threadArgs->reindeersWaitingCount);
        printf("Renifer: czeka %d reniferów na Mikołaja, %d\n", threadArgs->reindeersWaitingCount, entityID);

        if(threadArgs->reindeersWaitingCount == REINDEERS_COUNT) {
            printf("Renifer: wybudzam Mikołaja, %d\n", entityID);
            pthread_mutex_lock(&threadArgs->santaWakeUpMutex);
            threadArgs->shouldSantaWake = 1;
            pthread_mutex_unlock(&threadArgs->santaWakeUpMutex);
            pthread_cond_signal(&threadArgs->santaWakeUpCond);
        }
        pthread_mutex_unlock(&threadArgs->reindeersWaitingMutex);
        
        wait_for_time(DELIVER_MIN, DELIVER_MAX);

        pthread_mutex_lock(&threadArgs->reindeersGoMutex);
        while(threadArgs->reindeersToGo[entityID] == 0){
            pthread_cond_wait(&threadArgs->reindeersGoCond, &threadArgs->reindeersGoMutex);
        }
        threadArgs->reindeersToGo[entityID] = 0;
        pthread_mutex_unlock(&threadArgs->reindeersGoMutex);

    }

    return NULL;
}

int get_elf_id(ThreadArgs* threadArgs) {
    for(int i = 0; i < ELVES_COUNT; ++i){
        if(threadArgs->elvesToGo[i] == 0){
            threadArgs->elvesToGo[i] = 1;
            return i;
        }
    }
    return -1;
}

void unlock_elves_to_work(ThreadArgs* threadArgs) {
    for(int i = 0; i < ELVES_COUNT; ++i)
        threadArgs->elvesToGo[i] = 0;
    pthread_cond_broadcast(&threadArgs->elvesGoCond);
}

int register_elf(ThreadArgs* threadArgs) {
    pthread_mutex_lock(&threadArgs->elvesGoMutex);
    const int entityID = get_elf_id(threadArgs);
    if(entityID + 1 == ELVES_COUNT) {
        unlock_elves_to_work(threadArgs);
    }
    pthread_mutex_unlock(&threadArgs->elvesGoMutex);

    pthread_mutex_lock(&threadArgs->elvesGoMutex);
    while(threadArgs->elvesToGo[entityID] == 1){
        pthread_cond_wait(&threadArgs->elvesGoCond, &threadArgs->elvesGoMutex);
    }
    pthread_mutex_unlock(&threadArgs->elvesGoMutex);
    
    return entityID;
}

void* elves_work(void* args) {
    ThreadArgs* threadArgs = (ThreadArgs*)args;
    
    const int entityID = register_elf(threadArgs);

    
    while(1) {
        wait_for_time(ELVES_WORK_MIN, ELVES_WORK_MAX);
        int has_printed_waiting_message = 0;
        int is_in_workshop = 0;
        pthread_mutex_lock(&threadArgs->elvesWaitingMutex);
        while(!is_in_workshop) {
            if(threadArgs->elvesWaitingCount < WORKSHOP_ELVES_MAX_COUNT) {
                threadArgs->elvesWaiting[threadArgs->elvesWaitingCount] = entityID;
                is_in_workshop = 1;
                ++(threadArgs->elvesWaitingCount);
                printf("Elf: czeka %d elfów na mikołaja, %d\n", threadArgs->elvesWaitingCount, entityID);
                if(threadArgs->elvesWaitingCount == WORKSHOP_ELVES_MAX_COUNT){
                    printf("Elf: wybudzam Mikołaja, %d\n", entityID);
                    pthread_mutex_lock(&threadArgs->santaWakeUpMutex);
                    threadArgs->shouldSantaWake = 1;
                    pthread_mutex_unlock(&threadArgs->santaWakeUpMutex);
                    if(threadArgs->delivered_gifts_count < GIFTS_COUNT)
                        pthread_cond_signal(&threadArgs->santaWakeUpCond);
                }
            }
            else {
                has_printed_waiting_message = 1;
                if(has_printed_waiting_message == 0)
                    printf("Elf: czeka na powrót elfów, %d\n", entityID);
                pthread_cond_wait(&threadArgs->elvesWaitingCond, &threadArgs->elvesWaitingMutex);
            }
        }
        pthread_mutex_unlock(&threadArgs->elvesWaitingMutex);

        pthread_mutex_lock(&threadArgs->elvesGoMutex);
        while(!threadArgs->elvesToGo[entityID]){
            pthread_cond_wait(&threadArgs->elvesGoCond, &threadArgs->elvesGoMutex);
        }
        threadArgs->elvesToGo[entityID] = 0;
        printf("Elf: Mikołaj rozwiązuje problem, %d\n", entityID);
        pthread_mutex_unlock(&threadArgs->elvesGoMutex);  
    }
    
    return NULL; 
}

ThreadArgs* create_thread_args() {
    ThreadArgs* result = calloc(sizeof(*result), 1);
    
    result->santaWakeUpCond = (pthread_cond_t)PTHREAD_COND_INITIALIZER,
    result->reindeersGoCond = (pthread_cond_t)PTHREAD_COND_INITIALIZER,
    result->elvesGoCond = (pthread_cond_t)PTHREAD_COND_INITIALIZER;

    result->elvesGoMutex = (pthread_mutex_t)PTHREAD_MUTEX_INITIALIZER;
    result->reindeersGoMutex = (pthread_mutex_t)PTHREAD_MUTEX_INITIALIZER;
    result->santaWakeUpMutex = (pthread_mutex_t)PTHREAD_MUTEX_INITIALIZER;
    result->elvesWaitingMutex = (pthread_mutex_t)PTHREAD_MUTEX_INITIALIZER;
    result->reindeersWaitingMutex = (pthread_mutex_t)PTHREAD_MUTEX_INITIALIZER;

    for(int i = 0; i < WORKSHOP_ELVES_MAX_COUNT; ++i) {
        result->elvesWaiting[i] = -1;    
    }

    return result;
}

void create_threads(ThreadArgs* args, pthread_t* santa, pthread_t* reindeers, pthread_t* elves) {
    pthread_create(santa, NULL, santa_work, args);
    for(int i = 0; i < REINDEERS_COUNT; i++){
        pthread_create(reindeers + i, NULL, reindeers_work, args);
    }
    for(int i = 0; i < ELVES_COUNT; i++){
        pthread_create(elves + i, NULL, elves_work, args);
    }
}

int main(int argc, char** argv) {
    
    srand(time(NULL));
    
    ThreadArgs* args = create_thread_args();
    
    pthread_t santa;
    pthread_t reindeers[REINDEERS_COUNT];
    pthread_t elves[ELVES_COUNT];   
    
    create_threads(args, &santa, reindeers, elves);
    pthread_join(santa, NULL);
    for(int i = 0; i < REINDEERS_COUNT; i++){
        pthread_detach(*(reindeers + i));
    }
    for(int i = 0; i < ELVES_COUNT; i++){
        pthread_detach(*(elves + i));
    }
    
    free(args);
}