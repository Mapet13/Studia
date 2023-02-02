package com.tw;

public class Main {

    public static void main(String[] args) throws InterruptedException {
        var buffor_size = 500;

        var threads_count = 3;
        var buffor = new Buffor4(buffor_size * 2);

        var runable = new MyRunnable[threads_count];
        var threads = new Thread[threads_count];

        runable[0] = new Producer(buffor, 1, 1);
        runable[1] = new Consumer(buffor, 1, 1);
        runable[2] = new Consumer(buffor, buffor_size, buffor_size);

        for (var i = 0; i < threads_count; i++) {
            threads[i] = new Thread(runable[i]);
            threads[i].start();
        }

        while (true) {
            Thread.sleep(1000);
            for (var i = 0; i < threads_count; i++) {
                System.out.println(
                        threads[i].getName() + " (" + runable[i].getThreadName() + ") " + runable[i].getMinMax()
                                + "  - "
                                + runable[i].getIncrements());
            }
            System.out.println("-----------------------");
        }
    }
}

/*
 * 
 * dzieje sie to w czasie wysylania sygnalow
 * 
 * P:
 * [_]
 * [_____________]
 * 
 * C:
 * [C1] -> po sygnale [] C1 - ready to run - i potem wchodzi tam nowy kosument
 * igdy nowy ma zasoby to jest zagłodzenie a gdy nie ma to sie C5 sie ustawia w
 * kolejce
 * [C2_C3___C4_______]
 * 
 * buffer:1
 *
 * 
 * --------------
 * i teraz pytanie kiedy sie powiessza wszystkie
 * 
 */
