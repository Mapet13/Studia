package com.tw;

import com.tw.ActiveObject.HardWorker;

// Servant
public class Buffer {
    public long max_time = Long.MAX_VALUE;
    private final int buffer_size;
    private int buffer_count = 0;
    private HardWorker hard_worker;

    public Buffer(int buffer_size, int hard_work_amount)
    {
        this.buffer_size = buffer_size;
        this.hard_worker = new HardWorker(hard_work_amount);
    }

    public void produce(int count)
    {
        hard_worker.do_hard_work(max_time);
        buffer_count += count;
    }

    public void consume(int count)
    {
        hard_worker.do_hard_work(max_time);
        buffer_count -= count;
    }

    public boolean can_produce(int count)
    {
        return buffer_count + count < buffer_size;
    }

    public boolean can_consume(int count)
    {
        return buffer_count - count >= 0;
    }

    public int getCount()
    {
        return buffer_count;
    }
}
