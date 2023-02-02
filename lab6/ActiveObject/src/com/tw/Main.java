package com.tw;

import java.util.Random;

public class Main {
    public static void main(String[] args)
    {
        final int buffer_size = 10;
        final int hard_work_amount = 100;
        final int min = 1;
        final int max = buffer_size / 2;
        final Random rand = new Random();

        PKProxy proxy = new PKProxy(buffer_size);

        Producer producer = new Producer(proxy, rand, hard_work_amount, min, max);
        Consumer consumer = new Consumer(proxy, rand, hard_work_amount, min, max);

        var thread_Producer = new Thread(producer::run);
        var thread_Consumer = new Thread(consumer::run);

        thread_Producer.start();
        thread_Consumer.start();

        final boolean is_running = true;
        while (is_running) {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(producer.getWorkSummary());
            System.out.println(consumer.getWorkSummary());
            System.out.println("-----------------------");
        }
    }
}