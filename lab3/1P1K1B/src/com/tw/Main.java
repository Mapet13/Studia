package com.tw;

public class Main {

    public static void main(String[] args) throws InterruptedException {
        var buffor_size = 20;

        var producents_count = 6;
        var consuments_count = 3;

        var producingCount = 10;
        var consumingCount = 20;

        var buffor = new Buffor4(buffor_size);

        var threads = new Thread[producents_count + consuments_count];

        for (var i = 0; i < producents_count; i++) {
            threads[i] = new Thread(new Producer(producingCount, buffor));
        }

        for (var i = producents_count; i < producents_count + consuments_count; i++) {
            threads[i] = new Thread(new Consumer(consumingCount, buffor));
        }

        for (var i = 0; i < producents_count + consuments_count; i++) {
            threads[i].start();
        }
    }
}
