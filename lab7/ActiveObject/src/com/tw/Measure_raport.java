package com.tw;

import java.util.ArrayList;

public class Measure_raport {
    private final ArrayList<Single_run_raport> ao_raports = new ArrayList<>();
    private final ArrayList<Single_run_raport> sync_raports = new ArrayList<>();
    private final Run_parameters run_parameters;

    public Measure_raport(Run_parameters run_parameters)
    {
        this.run_parameters = run_parameters;
    }

    public void add_ao_raport(Single_run_raport raport)
    {
        ao_raports.add(raport);
    }

    public void add_sync_raport(Single_run_raport raport)
    {
        sync_raports.add(raport);
    }

    public Run_parameters get_run_parameters()
    {
        return run_parameters;
    }

    public Double get_ao_average_work_count()
    {
        return ao_raports.stream().mapToDouble(Single_run_raport::work_count).average().orElse(0);
    }

    public Double get_ao_average_iterations()
    {
        return ao_raports.stream().mapToDouble(Single_run_raport::iterations).average().orElse(0);
    }

    public Double get_ao_average_time_saved()
    {
        return ao_raports.stream().mapToDouble(Single_run_raport::time_saved).average().orElse(0);
    }

    public Double get_average_sync_work_count()
    {
        return sync_raports.stream().mapToDouble(Single_run_raport::work_count).average().orElse(0);
    }

    public Double get_average_sync_iterations()
    {
        return sync_raports.stream().mapToDouble(Single_run_raport::iterations).average().orElse(0);
    }
}
