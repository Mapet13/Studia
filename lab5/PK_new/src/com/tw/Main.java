package com.tw;

import com.tw.buffor.AbstractBuffor;

public class Main {
    static final int measurement_iterations = 5;
    static final int measurement_sleep_time = 5000;

    public static void main(String[] args)
    {
        final var max_to_produce = 5;
        final var buffor_size = max_to_produce * 2;
        final var seed = 1234;

        var measurments = new MultipleMeasurementRunner();
        measurments.addMeasurment(new MultipleMeasurementRunner.MeasurmentRunData("Standard", buffor_size, seed, buffer -> getStandardMeasurment(buffer, max_to_produce)));
        measurments.addMeasurment(new MultipleMeasurementRunner.MeasurmentRunData("Equal", buffor_size, seed, buffer -> getAllEqualMeasurment(buffer, 1)));
        measurments.addMeasurment(new MultipleMeasurementRunner.MeasurmentRunData("Simple", buffor_size, seed, buffer -> getSimpleMeasurment(buffer, 1)));
        measurments.performMeasurments();
        measurments.printResults();
    }

    static Double getStandardMeasurment(AbstractBuffor buffor, int max)
    {
        final var runner = new MeasureRunner(buffor, measurement_iterations, measurement_sleep_time);

        runner.addProducer(1, 1);
        runner.addConsumer(1, 1);
        runner.addConsumer(1, 1);
        runner.addConsumer(1, 1);
        runner.addConsumer(max, max);
        runner.addConsumer(max, max);

        return runner.measure();
    }

    static Double getAllEqualMeasurment(AbstractBuffor buffor, int value)
    {
        final var runner = new MeasureRunner(buffor, measurement_iterations, measurement_sleep_time);

        runner.addProducer(value, value);
        runner.addProducer(value, value);
        runner.addProducer(value, value);
        runner.addConsumer(value, value);
        runner.addConsumer(value, value);
        runner.addConsumer(value, value);

        return runner.measure();
    }

    static Double getSimpleMeasurment(AbstractBuffor buffor, int value)
    {
        final var runner = new MeasureRunner(buffor, measurement_iterations, measurement_sleep_time);

        runner.addProducer(value, value);
        runner.addConsumer(value, value);

        return runner.measure();
    }
}