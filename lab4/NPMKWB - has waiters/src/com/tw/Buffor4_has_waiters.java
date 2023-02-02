package com.tw;

import java.util.Random;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public class Buffor4_has_waiters extends AbstractBuffor {
    public int bufferCount = 0;
    public int bufferSize;

    public Buffor4_has_waiters(int bufferSize) {
        this.bufferSize = bufferSize;
    }

    Random rand = new Random();

    final ReentrantLock lock = new ReentrantLock();
    final Condition P1 = lock.newCondition();
    final Condition PN = lock.newCondition();
    final Condition C1 = lock.newCondition();
    final Condition CN = lock.newCondition();

    public void produce(int min, int max) {
        try {
            lock.lock();
            while (lock.hasWaiters(P1)) {
                PN.await();
            }

            int toProduce = getRandValue(min, max);
            while (!canProduce(toProduce)) {
                P1.await();
            }
            bufferCount += toProduce;

            C1.signal();
            PN.signal();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            lock.unlock();
        }
    }

    public void consume(int min, int max) {
        try {
            lock.lock();
            while (lock.hasWaiters(C1)) {
                CN.await();
            }

            int toConsume = getRandValue(min, max);
            while (!canConsume(toConsume)) {
                C1.await();
            }

            bufferCount -= toConsume;

            P1.signal();
            CN.signal();
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
