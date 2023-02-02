package com.tw;

public class Counter {
    int count = 0;

    public synchronized void increment() {
        count += 1;
    }

    public synchronized void decrement() {
        count -= 1;
    }

    public void print() {
        System.out.println(count);
    }
}
