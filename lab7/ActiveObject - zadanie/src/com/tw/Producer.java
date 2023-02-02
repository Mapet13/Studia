package com.tw;

import java.util.Random;

public class Producer extends Worker {
    final PKProxy proxy;

    public Producer(PKProxy proxy, int time_ms, Random rand, int min, int max)
    {
        super(rand, time_ms, min, max);
        this.proxy = proxy;
    }

    @Override
    protected Future getTaskFeature(int count)
    {
        return proxy.produce(count);
    }

    @Override
    protected String getWorkName()
    {
        return "Producer";
    }
}
