package com.tw.ActiveObject;

import java.util.Random;

public class Consumer extends Worker {
    final PKProxy proxy;

    public Consumer(PKProxy proxy, Random rand, long time_ms, int min, int max)
    {
        super(rand, time_ms, min, max);
        this.proxy = proxy;
    }

    @Override
    protected Future getTaskFeature(int count)
    {
        return proxy.consume(count);
    }

    @Override
    protected String getWorkName()
    {
        return "Consumer";
    }
}
