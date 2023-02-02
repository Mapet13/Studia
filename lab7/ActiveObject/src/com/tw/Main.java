package com.tw;

import java.util.ArrayList;

public class Main {

    public static void main(String[] args)
    {
        Measure_runner runner = new Measure_runner();
        runner.run();

        ArrayList<Measure_raport> raports = runner.raports;
        for (Measure_raport raport : raports) {
            System.out.println("--------------------------------------------------------");
            System.out.println(raport.get_run_parameters());
            System.out.println("AO average work count: " + raport.get_ao_average_work_count());
            System.out.println("AO average iterations: " + raport.get_ao_average_iterations());
            System.out.println("AO average time saved: " + raport.get_ao_average_time_saved());
            System.out.println("Sync average work count: " + raport.get_average_sync_work_count());
            System.out.println("Sync average iterations: " + raport.get_average_sync_iterations());
            System.out.println();
        }
    }
}

/*
 * 
 * 
 * 
 * Metryki:
 *  - stały czas -> łaczna ilosc produkcji, konsumpcji
 *  - stała liczba produkcji i konsumpcji -
 * 
 * 
 * 
 * - zamiast dodawac dodatkowa prace dla synchronicznego buffera
 * - policzyc ile czasu active object oszczedza
 * 
 * 
 * 
 * 
 * 
 */
