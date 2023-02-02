package com.tw;

import java.util.LinkedList;
import java.util.Queue;

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
            if (inner_queue.isEmpty()) {
                inner_queue.add(get_from_activation_queue());
            }

            // jeżeli moge to zajmuję sie tylko wewnetrzną kolejką
            if (inner_queue.peek().can_execute()) {
                inner_queue.remove().call();
            } else {
                final var new_request = get_from_activation_queue();
                // sprawdzenie typu requestu jest ważne żeby uniknąć zagłodzenia
                // nie chcemy żeby mały konsument podebrał zasoby czekającemu duzemu konsumentowi
                if (!inner_queue.peek().is_same(new_request) && new_request.can_execute()) {
                    new_request.call();
                } else {
                    inner_queue.add(new_request);
                }
            }
        }
    }

    private MethodRequest get_from_activation_queue()
    {
        if (activationQueue.size() == 0) {
            // jedyne miejsce gdzie Scheduler może sie zawiesić
            activationQueue.wait_untill_not_empty();
        }
        return activationQueue.dequeue();
    }
}