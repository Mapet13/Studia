package com.tw;

import com.tw.buffor.AbstractBuffor;
import java.util.ArrayList;

public class AbstractRunner {
    final AbstractBuffor buffor;
    final ArrayList<AbstractWorker> workers = new ArrayList<>();

    public AbstractRunner(AbstractBuffor buffor)
    {
        this.buffor = buffor;
    }

    public void addConsumer(int min, int max)
    {
        workers.add(new Consumer(buffor, min, max));
    }

    public void addProducer(int min, int max)
    {
        workers.add(new Producer(buffor, min, max));
    }

    protected ArrayList<Thread> initialise_threads()
    {
        final var threads = new ArrayList<Thread>();
        for (var worker : workers) {
            threads.add(new Thread(worker));
        }
        for (var thread : threads) {
            thread.start();
        }
        return threads;
    }

    protected void reset()
    {
        buffor.reset();
        workers.forEach(AbstractWorker::reset);
    }
}
