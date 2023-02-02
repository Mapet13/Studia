package com.tw.ActiveObject;

import com.tw.Clock;
import java.text.DecimalFormat;
import java.util.Random;

public abstract class Worker {
    public final Clock clock = new Clock();

    protected final Random rand;
    protected final int min;
    protected final int max;
    protected final long time_ms;
    protected int work_count;
    protected boolean is_running;
    protected int iterations;
    protected long time_saved;

    protected Worker(Random rand, long time_ms, int min, int max)
    {
        this.rand = rand;
        this.time_ms = time_ms;
        this.min = min;
        this.max = max;
    }

    public void run()
    {
        is_running = true;
        iterations = 0;
        time_saved = 0;
        clock.start();

        // odmierzam czas ile zaoszczędzi klient gdy jego request jest wykonywany
        while (is_running && clock.get_time() < time_ms) {
            final int count = getRandomCount();
            var feature = getTaskFeature(count);
            long start = System.nanoTime();
            feature.wait_until_ready(time_ms);
            if (clock.get_time() > time_ms)
                break;
            time_saved += System.nanoTime() - start;
            iterations++;
            work_count += count;
        }

        is_running = false;
    }

    public boolean is_running()
    {
        return is_running;
    }

    protected int getRandomCount()
    {
        return rand.nextInt((max - min) + 1) + min;
    }

    public String getWorkSummary()
    {
        var dec_format = new DecimalFormat("#.###");
        dec_format.setDecimalSeparatorAlwaysShown(true);
        dec_format.setMinimumFractionDigits(3);
        return String.format("[%s] (minmax: %5s) -> %8s in %8s iterations - saved %8s ms",
            getWorkName(),
            getMinMax(),
            Integer.toString(work_count),
            Integer.toString(iterations),
            dec_format.format(time_saved / 1000000.0));
    }

    public int get_work_count()
    {
        return work_count;
    }

    public int get_iterations()
    {
        return iterations;
    }

    public double get_time_saved()
    {
        return time_saved / 1000000.0;
    }

    private String getMinMax()
    {
        return String.format("%d-%d", min, max);
    }

    protected abstract Future getTaskFeature(int count);
    protected abstract String getWorkName();
}
