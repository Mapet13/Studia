package com.tw;

import com.tw.buffor.AbstractBuffor;
import java.util.function.BiFunction;

public class Producer extends AbstractWorker {
    private final AbstractBuffor buffor;

    public Producer(AbstractBuffor buffor, int min, int max)
    {
        super(max, min);
        this.buffor = buffor;
    }

    @Override
    protected BiFunction<Integer, Integer, Integer> getWorkFunction()
    {
        return buffor::produce;
    }

    @Override
    protected String getWorkName()
    {
        return "Producer";
    }
}
