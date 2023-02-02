package com.tw;

public class Clock {
    private long start_time = -1;

    public synchronized boolean is_active()
    {
        return start_time != -1;
    }

    public synchronized void start()
    {
        start_time = System.nanoTime();
    }

    public synchronized long get_time()
    {
        return System.nanoTime() - start_time;
    }
}
