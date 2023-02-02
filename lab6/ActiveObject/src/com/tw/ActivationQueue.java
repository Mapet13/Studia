package com.tw;

import java.util.LinkedList;
import java.util.Queue;

public class ActivationQueue implements IActivationQueue {
    private final Queue<MethodRequest> queue = new LinkedList<>();

    @Override
    public synchronized void enqueue(MethodRequest request)
    {
        queue.add(request);
    }

    @Override
    public synchronized MethodRequest dequeue()
    {
        return queue.remove();
    }

    @Override
    public synchronized int size()
    {
        return queue.size();
    }
}
