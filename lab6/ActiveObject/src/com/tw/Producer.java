package com.tw;

import java.util.Random;

public class Producer extends Worker {
    final PKProxy proxy;

    public Producer(PKProxy proxy, Random rand, int hard_work_amount, int min, int max)
    {
        super(rand, hard_work_amount, min, max);
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
