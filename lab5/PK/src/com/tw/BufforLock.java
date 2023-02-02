package com.tw;

import java.util.Random;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public class BufforLock extends AbstractBuffor {
    public int bufferCount = 0;
    public final int bufferSize;

    final Random rand;

    final ReentrantLock lockP = new ReentrantLock();
    final ReentrantLock lockC = new ReentrantLock();
    final ReentrantLock lockInner = new ReentrantLock();

    final Condition cond = lockInner.newCondition();

    public BufforLock(int seed, int bufferSize) {
        this.bufferSize = bufferSize;
        rand = new Random(seed);
    }

    public void produce(int min, int max) {
        try {
            lockP.lock();
            lockInner.lock();
            int toProduce = getRandValue(min, max);
            while (!canProduce(toProduce)) {
                cond.await();
            }
            bufferCount += toProduce;
            cond.signal();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            lockInner.unlock();
            lockP.unlock();
        }
    }

    public void consume(int min, int max) {
        try {
            lockC.lock();
            lockInner.lock();
            int toConsume = getRandValue(min, max);
            while (!canConsume(toConsume)) {
                cond.await();
            }

            bufferCount -= toConsume;
            cond.signal();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            lockInner.unlock();
            lockC.unlock();
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
