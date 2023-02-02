package com.tw;

import java.util.ArrayList;
import java.util.Random;

public class Measure_runner {
    public ArrayList<Measure_raport> raports = new ArrayList<>();

    final int buffer_size = 10;
    final int min = 1;
    final int max = buffer_size / 2;
    final long time_ms = 2 * 1000000000L;

    public void run()
    {
        Integer[] buffer_hard_work_amounts = { 0, 10, 100, 1000, 10000, 100000 };
        Integer[] threads_counts = { 1, 2, 4, 8, 16, 32, 64, 128 };

        Random rand = new Random(123);

        for (Integer buffer_hard_work_amount : buffer_hard_work_amounts) {
            for (Integer threads_count : threads_counts) {
                System.out.println("RUN: hw: " + buffer_hard_work_amount + " tc: " + threads_count);

                Run_parameters run_parameters = new Run_parameters(buffer_hard_work_amount, threads_count, rand.nextInt());
                Measure_raport raport = new Measure_raport(run_parameters);

                for (int i = 0; i < 5; i++) {
                    raport.add_ao_raport(run_ao(run_parameters));
                    raport.add_sync_raport(run_sync(run_parameters));
                }

                raports.add(raport);
            }
        }
    }

    private Single_run_raport run_sync(Run_parameters run_parameters)
    {
        return new run_maker().sync(buffer_size, run_parameters.buffer_hard_work_amount(), min, max, time_ms, run_parameters.seed(), run_parameters.threads_count());
    }

    private Single_run_raport run_ao(Run_parameters run_parameters)
    {
        return new run_maker().active_object(buffer_size, run_parameters.buffer_hard_work_amount(), min, max, time_ms, run_parameters.seed(), run_parameters.threads_count());
    }
}
