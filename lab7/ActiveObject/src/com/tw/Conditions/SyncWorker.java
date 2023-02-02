package com.tw.Conditions;

import com.tw.Clock;
import java.util.Random;
import java.util.function.IntConsumer;

public abstract class SyncWorker {
    public final Clock clock = new Clock();
    protected final BufferLock buffer;
    protected final Random rand;
    protected final int min;
    protected final int max;
    protected final long time_ms;
    protected int work_count = 0;
    protected boolean is_running;
    protected int iterations = 0;

    protected SyncWorker(BufferLock buffer, Random rand, long time_ms, int min, int max)
    {
        this.buffer = buffer;
        this.time_ms = time_ms;
        this.rand = rand;
        this.min = min;
        this.max = max;
    }

    public synchronized long get_start_time()
    {
        return start_run_time;
    }

    public void run()
    {
        is_running = true;
        iterations = 0;
        clock.start();
        while (is_running && clock.get_time() < time_ms) {
            final int count = getRandomCount();
            getWorkFunction().accept(count);
            if (clock.get_time() > time_ms)
                break;
            iterations++;
            work_count += count;
        }

        is_running = false;
    }

    public boolean is_running()
    {
        return is_running;
    }

    public int get_work_count()
    {
        return work_count;
    }

    public int get_iterations()
    {
        return iterations;
    }

    protected int getRandomCount()
    {
        return rand.nextInt((max - min) + 1) + min;
    }

    public String getWorkSummary()
    {
        return String.format("[%s] (minmax: %5s) -> %8s in %8s iterations",
            getWorkName(),
            getMinMax(),
            Integer.toString(work_count),
            Integer.toString(iterations));
    }

    private String getMinMax()
    {
        return String.format("%d-%d", min, max);
    }

    protected abstract IntConsumer getWorkFunction();
    protected abstract String getWorkName();
}
