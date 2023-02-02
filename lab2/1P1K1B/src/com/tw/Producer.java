package com.tw;

public class Producer implements Runnable {
    private final int increments;
    private final Buffor buffor;

    public Producer(int increments, Buffor buffor) {
        this.increments = increments;
        this.buffor = buffor;
    }

    @Override
    public void run() {
        for (var i = 0; i < increments; i++) {
            buffor.produce();
        }
    }
}
