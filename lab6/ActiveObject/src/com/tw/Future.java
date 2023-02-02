package com.tw;

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

    public synchronized void wait_until_ready()
    {
        while (!is_ready) {
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
