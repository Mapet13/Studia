package com.tw;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Main {

    public static void main(String[] args)
    {
        final int buffer_size = 10;
        final int buffer_hard_work_amount = 9000;
        final int min = 1;
        final int max = buffer_size / 2;
        final int time_ms = 5 * 1000;
        final int seed = 999;

        final Random rand = new Random(seed);
        final PKProxy proxy = new PKProxy(new Buffer(buffer_size, buffer_hard_work_amount));
        final List<Worker> workers = new ArrayList<>();
        workers.add(new Producer(proxy, time_ms, rand, min, max));
        workers.add(new Producer(proxy, time_ms, rand, min, max));
        workers.add(new Producer(proxy, time_ms, rand, min, max));
        workers.add(new Producer(proxy, time_ms, rand, min, max));
        workers.add(new Producer(proxy, time_ms, rand, min, max));
        workers.add(new Consumer(proxy, time_ms, rand, min, max));
        workers.add(new Consumer(proxy, time_ms, rand, min, max));
        workers.add(new Consumer(proxy, time_ms, rand, min, max));
        workers.add(new Consumer(proxy, time_ms, rand, min, max));
        workers.add(new Consumer(proxy, time_ms, rand, min, max));
        final List<Thread> client_threads = workers.stream().map(worker -> new Thread(worker::run)).toList();
        client_threads.forEach(Thread::start);

        while (workers.stream().allMatch(Worker::is_running)) {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        System.out.println(workers.stream().map(Worker::getWorkSummary).reduce("", (a, b) -> a + "\n" + b));
    }
}
