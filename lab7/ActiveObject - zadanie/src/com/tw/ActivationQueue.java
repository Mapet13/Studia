package com.tw;

import java.util.LinkedList;
import java.util.Queue;

public class ActivationQueue {
    private final Queue<MethodRequest> queue = new LinkedList<>();

    public synchronized void enqueue(MethodRequest request)
    {
        queue.add(request);
        notifyAll(); // budzi Schedulera jeśli czeka na requesty
    }

    public synchronized MethodRequest dequeue()
    {
        return queue.remove();
    }

    public synchronized int size()
    {
        return queue.size();
    }

    public synchronized void wait_untill_not_empty()
    {
        while (size() == 0) {
            try {
                // jedyne miesce gdzie Scheduler może sie zawiesić
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
