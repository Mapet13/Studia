package com.tw;

public class Main {
    public static void main(String[] args) throws InterruptedException
    {
        final var buffor_size = 10;
        final var threads_count = 3;

        var buffor = new Buffor4(buffor_size * 2);

        var threads = new Thread[threads_count];
        threads[0] = new Thread(new Producer(15, buffor, 1, 1)); // mały producent produkujacy po 1
        threads[1] = new Thread(new Consumer(10, buffor, 1, 1)); // mały knsumenent konsumujacy po 1

        // duży konsumenent konsumujacy maksymalną ilość
        threads[2] = new Thread(new Consumer(1, buffor, buffor_size, buffor_size));

        for (var i = 0; i < threads_count; i++) {
            threads[i].start();
        }

        // jak widzimy dzięki zastosowaniu 4 condition duzy konsument nie jest
        // zagłodzony i jest w stanie skonsumowac swoja porcje
    }
}