package com.tw;

public class Producer implements MyRunnable {
    private int increments = 0;
    private final AbstractBuffor buffor;

    int min;
    int max;

    public Producer(AbstractBuffor buffor, int min, int max) {
        super();
        this.buffor = buffor;
        this.min = min;
        this.max = max;
    }

    @Override
    public void run() {
        while (true) {
            buffor.produce(min, max);
            increments += 1;
        }
    }

    @Override
    public int getIncrements() {
        return increments;
    }

    @Override
    public String getMinMax() {
        return "(" + min + " " + max + ")";
    }

    @Override
    public String getThreadName() {
        return "Producer";
    }
}
