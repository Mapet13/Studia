package com.tw.ActiveObject;

public class HardWorker {
    int hard_work_amount;

    public HardWorker(int hard_work_amount)
    {
        this.hard_work_amount = hard_work_amount;
    }

    public void do_hard_work(long max_time)
    {
        long start_time = System.nanoTime();
        for (int i = 0; i < hard_work_amount; i++) {
            if (start_time + max_time < System.nanoTime())
                break;
            Math.sin(Math.cos(i) * i);
        }
    }

    public int getHardWorkAmount()
    {
        return hard_work_amount;
    }
}
