package com.tw.Conditions;

import java.util.Random;
import java.util.function.IntConsumer;

public class SyncConsumer extends SyncWorker {

    public SyncConsumer(BufferLock buffer, Random rand, long time_ms, int min, int max)
    {
        super(buffer, rand, time_ms, min, max);
    }

    @Override
    protected IntConsumer getWorkFunction()
    {
        return buffer::consume;
    }

    @Override
    protected String getWorkName()
    {
        return "Consumer";
    }
}
