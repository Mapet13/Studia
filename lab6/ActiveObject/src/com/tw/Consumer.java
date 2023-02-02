package com.tw;

import java.util.Random;

public class Consumer extends Worker {
    final PKProxy proxy;

    public Consumer(PKProxy proxy, Random rand, int hard_work_amount, int min, int max)
    {
        super(rand, hard_work_amount, min, max);
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
