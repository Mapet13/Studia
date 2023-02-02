package com.tw;

import java.util.Random;

public abstract class Worker {
    protected final Random rand;
    protected final int hard_work_amount;
    protected final int min;
    protected final int max;
    protected int work_count;
    protected boolean is_running;

    protected Worker(Random rand, int hard_work_amount, int min, int max)
    {
        this.rand = rand;
        this.hard_work_amount = hard_work_amount;
        this.min = min;
        this.max = max;
    }

    public void run()
    {
        is_running = true;
        while (is_running) {
            final int count = getRandomCount();
            work_count += count;
            var feature = getTaskFeature(count);
            do_hard_work();
            feature.wait_until_ready();
        }
    }

    protected void stop()
    {
        is_running = false;
    }

    protected void do_hard_work()
    {
        for (int i = 0; i < hard_work_amount; i++) {
            Math.sin(Math.cos(i) * i);
        }
    }

    protected int getRandomCount()
    {
        return rand.nextInt((max - min) + 1) + min;
    }

    public String getWorkSummary()
    {
        return String.format("[%s] (%8s) - %8s", getWorkName(),
            getMinMax(),
            Integer.toString(work_count));
    }

    private String getMinMax()
    {
        return String.format("%d-%d", min, max);
    }

    protected abstract Future getTaskFeature(int count);
    protected abstract String getWorkName();
}
