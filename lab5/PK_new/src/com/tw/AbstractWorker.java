package com.tw;

import java.util.function.BiFunction;

public abstract class AbstractWorker implements Runnable {
    private final int max;
    private final int min;
    private int increments = 0;
    private int work_amount = 0;
    private String name = "";
    private boolean is_running = false;

    protected AbstractWorker(int max, int min)
    {
        this.max = max;
        this.min = min;
    }

    protected abstract BiFunction<Integer, Integer, Integer> getWorkFunction();

    protected abstract String getWorkName();

    @Override
    public void run()
    {
        is_running = true;
        name = Thread.currentThread().getName();
        while (is_running) {
            work_amount += getWorkFunction().apply(min, max);
            increments++;
        }
    }

    public void stop()
    {
        is_running = false;
    }

    public void reset()
    {
        increments = 0;
        work_amount = 0;
    }

    public String getWorkSummary()
    {
        return String.format("[(%s)-(%s)] (%8s) - %8s", name, getWorkName(),
            getMinMax(),
            Integer.toString(increments));
    }

    public int getIncrements()
    {
        return increments;
    }

    public int getWorkAmount()
    {
        return work_amount;
    }

    private String getMinMax()
    {
        return String.format("%d-%d", min, max);
    }
}

/*














*/
