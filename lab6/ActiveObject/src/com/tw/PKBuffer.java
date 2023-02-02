package com.tw;

// Servant
public class PKBuffer {
    private final int buffer_size;
    private int buffer_count = 0;

    public PKBuffer(int buffer_size)
    {
        this.buffer_size = buffer_size;
    }

    public void produce(int count)
    {
        buffer_count += count;
    }

    public void consume(int count)
    {
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
