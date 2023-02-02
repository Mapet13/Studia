package com.tw;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        var counter = new Counter();
        var increments = 9000;

        var increments_thread = new Thread(() -> {
            for (var i = 0; i < increments; i++) {
                counter.increment();
            }
        });
        var decrements_thread = new Thread(() -> {
            for (var i = 0; i < increments; i++) {
                counter.decrement();
            }
        });

        increments_thread.start();
        decrements_thread.start();

        increments_thread.join();
        decrements_thread.join();

        counter.print();
    }
}
