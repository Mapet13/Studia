package com.tw;

public class Buffer {
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
        hard_worker.do_hard_work();
        buffer_count += count;
    }

    public void consume(int count)
    {
        hard_worker.do_hard_work();
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
