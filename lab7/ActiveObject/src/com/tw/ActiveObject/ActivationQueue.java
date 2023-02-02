package com.tw.ActiveObject;

import java.util.LinkedList;
import java.util.Queue;

public class ActivationQueue {
    private final Queue<MethodRequest> queue = new LinkedList<>();

    private boolean should_finish = false;

    public synchronized void enqueue(MethodRequest request)
    {
        queue.add(request);
        notifyAll();
    }

    public synchronized MethodRequest dequeue()
    {
        return queue.remove();
    }

    public synchronized int size()
    {
        return queue.size();
    }

    public synchronized void finish()
    {
        should_finish = true;
        for (MethodRequest request : queue) {
            request.finish();
        }
        notifyAll();
    }

    public synchronized void wait_untill_not_empty()
    {
        while (size() == 0 && !should_finish) {
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
