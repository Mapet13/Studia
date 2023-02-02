package com.tw;

import java.util.LinkedList;
import java.util.Queue;
import java.util.stream.IntStream;

public class PKScheduler extends Scheduler {
    private Queue<MethodRequest> inner_queue = new LinkedList<>();
    protected boolean is_active = true;

    public PKScheduler()
    {
        super(new ActivationQueue());
    }

    @Override
    public void run()
    {
        while (is_active) {
            if (activationQueue.size() == 0) {
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                continue;
            }

            inner_queue.add(activationQueue.dequeue());
            IntStream.range(0, inner_queue.size()).forEach(i -> {
                final var request = inner_queue.remove();
                if (request.can_execute()) {
                    request.call();
                } else {
                    inner_queue.add(request);
                }
            });
        }
    }
}
