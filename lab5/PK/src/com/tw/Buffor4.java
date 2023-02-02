package com.tw;

import java.util.Random;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public class Buffor4 extends AbstractBuffor {
    public int bufferCount = 0;
    public final int bufferSize;

    final Random rand;

    final ReentrantLock lock = new ReentrantLock();
    final Condition P1 = lock.newCondition();
    final Condition PN = lock.newCondition();
    final Condition C1 = lock.newCondition();
    final Condition CN = lock.newCondition();

    boolean hasFirstProducer = false;
    boolean hasFirstConsument = false;

    public Buffor4(int seed, int bufferSize) {
        this.bufferSize = bufferSize;
        rand = new Random(seed);
    }

    public void produce(int min, int max) {
        try {
            lock.lock();
            while (hasFirstProducer) {
                PN.await();
            }
            hasFirstProducer = true;
            int toProduce = getRandValue(min, max);
            while (!canProduce(toProduce)) {
                P1.await();
            }
            bufferCount += toProduce;
            hasFirstProducer = false;
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
            while (hasFirstConsument) {
                CN.await();
            }
            hasFirstConsument = true;
            int toConsume = getRandValue(min, max);
            while (!canConsume(toConsume)) {
                C1.await();
            }

            bufferCount -= toConsume;
            hasFirstConsument = false;
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
