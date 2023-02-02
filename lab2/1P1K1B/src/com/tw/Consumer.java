package com.tw;

public class Consumer implements Runnable {
    private final int increments;
    private final Buffor buffor;

    public Consumer(int increments, Buffor buffor) {
        this.increments = increments;
        this.buffor = buffor;
    }

    @Override
    public void run() {
        for (var i = 0; i < increments; i++) {
            buffor.consume();
        }
    }
}
