package com.tw;

public class HardWorker {
    int hard_work_amount;

    public HardWorker(int hard_work_amount)
    {
        this.hard_work_amount = hard_work_amount;
    }

    public void do_hard_work()
    {
        for (int i = 0; i < hard_work_amount; i++) {
            Math.sin(Math.cos(i) * i);
        }
    }

    public int getHardWorkAmount()
    {
        return hard_work_amount;
    }
}
