package com.tw.ActiveObject;

public class Future {
    private boolean is_ready = false;

    public synchronized void to_ready()
    {
        is_ready = true;
        notifyAll();
    }

    public boolean is_ready()
    {
        return is_ready;
    }

    public synchronized void wait_until_ready(long max_time)
    {
        long start_run_time = System.nanoTime();

        while (!is_ready && System.nanoTime() - start_run_time < max_time) {
            try {
                wait(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
