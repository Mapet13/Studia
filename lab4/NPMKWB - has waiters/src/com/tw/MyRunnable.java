package com.tw;

public interface MyRunnable extends Runnable {
    public abstract int getIncrements();

    public abstract String getMinMax();

    public abstract String getThreadName();
}
