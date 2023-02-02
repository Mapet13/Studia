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

    public void produce(int min, int max) {
        try {
            lock.lock();
            int toProduce = getRandValue(min, max);
            while (!canProduce(toProduce)) {
                prod_cond.await();
            }

            bufferCount += toProduce;

            cons_cond.signal();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            lock.unlock();
        }
    }

    public void consume(int min, int max) {
        try {
            lock.lock();
            int toConsume = getRandValue(min, max);
            while (!canConsume(toConsume)) {
                cons_cond.await();
            }

            bufferCount -= toConsume;
            prod_cond.signal();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            lock.unlock();
        }
    }

    private int getRandValue(int min, int max) {
        return rand.nextInt((max - min) + 1) + min;
    }

    private boolean canProduce(int x) {
        return bufferCount + x < bufferSize;
    }

    private boolean canConsume(int x) {
        return bufferCount >= x;
    }
}
