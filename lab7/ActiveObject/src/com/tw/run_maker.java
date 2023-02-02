package com.tw;

import com.tw.ActiveObject.Consumer;
import com.tw.ActiveObject.Future;
import com.tw.ActiveObject.PKProxy;
import com.tw.ActiveObject.Producer;
import com.tw.ActiveObject.Worker;
import com.tw.Conditions.BufferLock;
import com.tw.Conditions.SyncConsumer;
import com.tw.Conditions.SyncProducer;
import com.tw.Conditions.SyncWorker;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class run_maker {
    public Single_run_raport active_object(int buffer_size,
        int buffer_hard_work_amount, int min, int max, long time_ms, int seed, int threads_count)
    {
        Random rand = new Random(seed);
        Buffer buffer = new Buffer(buffer_size, buffer_hard_work_amount);
        buffer.max_time = time_ms;
        PKProxy proxy = new PKProxy(buffer);
        List<Worker> workers = new ArrayList<>();

        for (int i = 0; i < threads_count; i++) {
            workers.add(new Producer(proxy, rand, time_ms, min, max));
            workers.add(new Consumer(proxy, rand, time_ms, min, min));
        }
        List<Thread> client_threads = workers.stream().map(worker -> new Thread(worker::run)).toList();
        client_threads.forEach(Thread::start);

        while (workers.stream().anyMatch(worker -> !worker.clock.is_active() || worker.clock.get_time() < time_ms)) {
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        proxy.stop();

        while (client_threads.stream().anyMatch(Thread::isAlive)) {
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        return new Single_run_raport(
            workers.stream().mapToInt(Worker::get_work_count).average().getAsDouble(),
            workers.stream().mapToInt(Worker::get_iterations).average().getAsDouble(),
            workers.stream().mapToDouble(Worker::get_time_saved).average().getAsDouble());
    }

    public Single_run_raport sync(int buffer_size,
        int buffer_hard_work_amount, int min, int max, long time_ms, int seed, int threads_count)
    {
        Random rand = new Random(seed);
        BufferLock buffer = new BufferLock(buffer_size, buffer_hard_work_amount);
        buffer.max_time = time_ms;
        List<SyncWorker> workers = new ArrayList<>();
        for (int i = 0; i < threads_count; i++) {
            workers.add(new SyncProducer(buffer, rand, time_ms, min, max));
            workers.add(new SyncConsumer(buffer, rand, time_ms, min, min));
        }
        List<Thread> client_threads = workers.stream().map(worker -> new Thread(worker::run)).toList();
        client_threads.forEach(Thread::start);

        while (workers.stream().anyMatch(worker -> !worker.clock.is_active() || worker.clock.get_time() < time_ms)) {
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        buffer.finish();

        while (client_threads.stream().anyMatch(Thread::isAlive)) {
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        return new Single_run_raport(
            workers.stream().mapToInt(SyncWorker::get_work_count).average().getAsDouble(),
            workers.stream().mapToInt(SyncWorker::get_iterations).average().getAsDouble(),
            0.0);
    }
}
