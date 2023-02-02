package com.tw;

public class Producer implements Runnable {
    private final int increments;
    private final AbstractBuffor buffor;

    int min;
    int max;

    public Producer(int increments, AbstractBuffor buffor, int min, int max) {
        this.increments = increments;
        this.buffor = buffor;
        this.min = min;
        this.max = max;
    }

    @Override
    public void run() {
        for (var i = 0; i < increments; i++) {
            System.out.println(Thread.currentThread().getName() + " starting to producing " + i + '/' + increments);
            buffor.produce(min, max);
        }
        System.out
                .println("\t" + Thread.currentThread().getName() + " - finish producing - (" + min + ", " + max + ")");
    }
}
