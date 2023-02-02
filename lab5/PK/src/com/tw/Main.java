package com.tw;

import java.nio.Buffer;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        final var buffor_size = 10;
        final var threads_count = 3;
        final var seed = 0;

        var buffor_with_4cond = new Buffor4(seed, buffor_size * 2);
        var buffor_with_locks = new BufforLock(seed, buffor_size * 2);

        var threads_4cond = get_2small_1big(threads_count, buffor_with_4cond, 1, buffor_size);
        var threads_locks = get_2small_1big(threads_count, buffor_with_locks, 1, buffor_size);

        var time_4cond = measure(threads_4cond);
        System.out.println("---------------------------------------");
        var time_lock = measure(threads_locks);

        System.out.println("4 cond: " + time_4cond + "ns");
        System.out.println(" locks: " + time_lock + "ns");
    }

    static ArrayList<Thread> get_2small_1big(int size, AbstractBuffor buffor, int min, int max) {
        var threads = new ArrayList<Thread>(size);
        threads.add(0, new Thread(new Producer(20, buffor, min, min)));
        threads.add(1, new Thread(new Consumer(10, buffor, min, min)));
        threads.add(2, new Thread(new Consumer(1, buffor, max, max)));
        return threads;
    }

    static long measure(ArrayList<Thread> threads) {
        long start = System.nanoTime();
        for (var thread : threads) {
            thread.start();
        }
        long finish = System.nanoTime();
        for (var thread : threads) {
            try {
                thread.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        return finish - start;
    }

}