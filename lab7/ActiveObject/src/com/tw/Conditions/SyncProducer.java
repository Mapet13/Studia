package com.tw.Conditions;

import java.util.Random;
import java.util.function.IntConsumer;

public class SyncProducer extends SyncWorker {

    public SyncProducer(BufferLock buffer, Random rand, long time_ms, int min, int max)
    {
        super(buffer, rand, time_ms, min, max);
    }

    @Override
    protected IntConsumer getWorkFunction()
    {
        return buffer::produce;
    }

    @Override
    protected String getWorkName()
    {
        return "Producer";
    }
}
