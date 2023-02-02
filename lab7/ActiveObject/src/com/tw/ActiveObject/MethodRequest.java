package com.tw.ActiveObject;

import java.util.function.BooleanSupplier;

public class MethodRequest {
    public enum Type {
        PRODUCE,
        CONSUME
    }

    private final BooleanSupplier can_execute_fn;
    private final Runnable task;
    private final Future feature;
    private final Type type;

    public MethodRequest(BooleanSupplier can_execute, Runnable task, Future feature, Type type)
    {
        this.can_execute_fn = can_execute;
        this.task = task;
        this.feature = feature;
        this.type = type;
    }

    public void finish()
    {
        feature.to_ready();
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

    public boolean is_same(MethodRequest other)
    {
        return this.type == other.type;
    }
}
