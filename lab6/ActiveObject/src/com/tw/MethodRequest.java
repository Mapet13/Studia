package com.tw;

import java.util.function.BooleanSupplier;

public class MethodRequest {
    private BooleanSupplier can_execute_fn;
    private Runnable task;
    private Future feature;

    public MethodRequest(BooleanSupplier can_execute, Runnable task, Future feature)
    {
        this.can_execute_fn = can_execute;
        this.task = task;
        this.feature = feature;
    }

    public void call()
    {
        task.run();
        feature.to_ready();
    }

    public boolean can_execute()
    {
        return can_execute_fn.getAsBoolean();
    }
}
