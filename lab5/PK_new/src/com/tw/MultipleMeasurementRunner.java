package com.tw;

import com.tw.buffor.AbstractBuffor;
import com.tw.buffor.Buffor4;
import com.tw.buffor.BufforLock;
import java.util.ArrayList;
import java.util.function.ToDoubleFunction;

class MultipleMeasurementRunner {
    public record MeasurmentRunData(String name, int buffer_size, int seed, ToDoubleFunction<AbstractBuffor> measurment) { }
    public record MeasurmentResult(String name, Double locks_result, Double cond4_result) { }

    private final ArrayList<MeasurmentRunData> run_data = new ArrayList<>();
    private final ArrayList<MeasurmentResult> result_data = new ArrayList<>();

    public void addMeasurment(MeasurmentRunData data)
    {
        run_data.add(data);
    }

    public void performMeasurments()
    {
        for (final var data : run_data) {
            result_data.add(runMeasurment(data));
        }
    }

    public void printResults()
    {
        System.out.println("--- Results ---");
        for (final var result : result_data) {
            System.out.println(result.name);
            System.out.println("locks:  " + result.locks_result);
            System.out.println("4 cond: " + result.cond4_result);
            System.out.println("---------------");
        }
    }

    private MeasurmentResult runMeasurment(MeasurmentRunData data)
    {
        final var buffor_lock = new BufforLock(data.seed, data.buffer_size);
        final var buffor_4cond = new Buffor4(data.seed, data.buffer_size);

        return new MeasurmentResult(data.name, data.measurment.applyAsDouble(buffor_lock), data.measurment.applyAsDouble(buffor_4cond));
    }
}