package com.tw;

public class Buffor {
    public int count = 0;
    public int bufferCount = 0;

    public synchronized void produce() {
        while (!canProduce()) {
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        count++;
        bufferCount++;
        System.out.println("Produced - " + Integer.toString(bufferCount));
        notify();
    }

    public synchronized void consume() {
        while (!canConsume()) {
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        count--;
        bufferCount--;
        System.out.println("Consumed - " + Integer.toString(bufferCount));
        notify();
    }

    private boolean canProduce() {
        return bufferCount == 0;
    }

    private boolean canConsume() {
        return bufferCount == 1;
    }
}
