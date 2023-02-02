package com.tw;

import com.tw.buffor.AbstractBuffor;
import java.util.function.BiFunction;

public class Consumer extends AbstractWorker {
    private final AbstractBuffor buffor;

    public Consumer(AbstractBuffor buffor, int min, int max)
    {
        super(max, min);
        this.buffor = buffor;
    }

    @Override
    protected BiFunction<Integer, Integer, Integer> getWorkFunction()
    {
        return buffor::consume;
    }

    @Override
    protected String getWorkName()
    {
        return "Consumer";
    }
}
