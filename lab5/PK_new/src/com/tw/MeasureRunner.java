package com.tw;

import com.tw.buffor.AbstractBuffor;
import java.util.stream.IntStream;

public class MeasureRunner extends AbstractRunner {
    private final int iterations;
    private final int sleep_time;

    public MeasureRunner(AbstractBuffor buffor, int iterations, int sleep_time)
    {
        super(buffor);

        this.iterations = iterations;
        this.sleep_time = sleep_time;
    }

    public Double measure()
    {
        return IntStream.generate(this::getSingleMeasurment).limit(iterations).average().orElseThrow();
    }

    private int getSingleMeasurment()
    {
        System.out.println("Starting new measurement...");
        try {
            reset();
            initialise_threads();
            Thread.sleep(sleep_time);
            workers.forEach(AbstractWorker::stop);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Measurement finished");

        return workers.stream().mapToInt(AbstractWorker::getWorkAmount).sum();
    }
}
