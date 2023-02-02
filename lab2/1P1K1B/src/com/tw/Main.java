package com.tw;

public class Main {

    public static void main(String[] args) throws InterruptedException {
        var buffor = new Buffor();
        var increments = 10;

        var producent = new Thread(new Producer(increments, buffor));
        var producent2 = new Thread(new Producer(increments, buffor));
        var consume = new Thread(new Consumer(increments, buffor));

        producent.start();
        producent2.start();
        consume.start();
    }
}
