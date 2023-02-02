package com.tw;

public class Main {

    public static void main(String[] args) throws InterruptedException
    {
        var buffor_size = 10;

        var threads_count = 3;

        var buffor = new Buffor2(buffor_size * 2);

        var threads = new Thread[threads_count];
        threads[0] = new Thread(new Producer(15, buffor, 1, 1));
        threads[1] = new Thread(new Consumer(10, buffor, 1, 1));
        threads[2] = new Thread(new Consumer(1, buffor, buffor_size, buffor_size));

        for (var i = 0; i < threads_count; i++) {
            threads[i].start();
        }
    }
}
