package com.tw;

public class Consumer implements Runnable {
    private final int increments;
    private final AbstractBuffor buffor;

    int min;
    int max;

    public Consumer(int increments, AbstractBuffor buffor, int min, int max) {
        this.increments = increments;
        this.buffor = buffor;
        this.min = min;
        this.max = max;
    }

    @Override
    public void run() {
        for (var i = 0; i < increments; i++) {
            System.out.println(Thread.currentThread().getName() + " starting to consuming " + i + '/' + increments);
            buffor.consume(min, max);
        }
        System.out
                .println("\t" + Thread.currentThread().getName() + " - finish consuming - (" + min + ", " + max + ")");
    }
}
