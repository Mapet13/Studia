package com.tw;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.Random;

public class Buffor2 extends AbstractBuffor {
    public int bufferCount = 0;
    public int bufferSize;

    public Buffor2(int bufferSize) {
        this.bufferSize = bufferSize;
    }

    final Lock lock = new ReentrantLock();
    final Condition prod_cond = lock.newCondition();
    final Condition cons_cond = lock.newCondition();

    Random rand = new Random();

    public void produce() {
        try {
            lock.lock();
            int toProduce = getRandValue();
            while (!canProduce(toProduce)) {
                System.out.println("Waiting for producing - " + Integer.toString(toProduce));
                prod_cond.await();
            }

            System.out.println(
                    "Produced - " + Integer.toString(bufferCount) + " -> " +
                            Integer.toString(bufferCount + toProduce));
            bufferCount += toProduce;

            cons_cond.signal();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            lock.unlock();
        }
    }

    public void consume() {
        try {
            lock.lock();
            int toConsume = getRandValue();
            while (!canConsume(toConsume)) {
                System.out.println("Waiting for consuming - " + Integer.toString(toConsume));
                cons_cond.await();
            }

            System.out.println(
                    "Consumed - " + Integer.toString(bufferCount) + " -> " +
                            Integer.toString(bufferCount - toConsume));

            bufferCount -= toConsume;
            prod_cond.signal();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            lock.unlock();
        }
    }

    private int getRandValue() {
        return rand.nextInt(bufferSize / 2);
    }

    private boolean canProduce(int x) {
        return bufferCount + x < bufferSize;
    }

    private boolean canConsume(int x) {
        return bufferCount >= x;
    }
}
