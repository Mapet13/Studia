package com.tw;

import java.util.function.BooleanSupplier;

public class Proxy {
    protected final Scheduler scheduler;

    protected Proxy(Scheduler scheduler)
    {
        this.scheduler = scheduler;
    }

    protected Future shedule(BooleanSupplier can_execute, Runnable task)
    {
        var feature = new Future();
        scheduler.enqueue(new MethodRequest(can_execute, task, feature));
        return feature;
    }
}
