package com.tw.buffor;

import java.util.Random;
import java.util.function.IntConsumer;

public abstract class AbstractBuffor {
    protected int buffer_count = 0;
    public final int buffer_size;
    private final Random rand;

    protected AbstractBuffor(int bufferSize, int seed)
    {
        this.buffer_size = bufferSize;
        this.rand = new Random(seed);
    }

    protected abstract void produceLogic(int to_produce);

    protected abstract void consumeLogic(int to_consume);

    public int getBufferCount()
    {
        return buffer_count;
    }

    public int produce(int min, int max)
    {
        return applyLogic(min, max, this::produceLogic);
    }

    public int consume(int min, int max)
    {
        return applyLogic(min, max, this::consumeLogic);
    }

    public void reset()
    {
        buffer_count = 0;
    }

    protected int getRandValue(int min, int max)
    {
        return rand.nextInt((max - min) + 1) + min;
    }

    protected boolean canProduce(int x)
    {
        return buffer_count + x < buffer_size;
    }

    protected boolean canConsume(int x)
    {
        return buffer_count >= x;
    }

    protected int applyLogic(int min, int max, IntConsumer logic_fn)
    {
        int to_work = getRandValue(min, max);
        logic_fn.accept(to_work);
        return to_work;
    }
}
