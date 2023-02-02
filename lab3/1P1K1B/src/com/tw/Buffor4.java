package com.tw;

import java.util.Random;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public class Buffor4 extends AbstractBuffor {
    public int bufferCount = 0;
    public int bufferSize;

    public Buffor4(int bufferSize) {
        this.bufferSize = bufferSize;
    }

    Random rand = new Random();

    final ReentrantLock lock = new ReentrantLock();
    final Condition P1 = lock.newCondition();
    final Condition PN = lock.newCondition();
    final Condition C1 = lock.newCondition();
    final Condition CN = lock.newCondition();

    boolean hasFirstProducer = false;
    boolean hasFirstConsument = false;

    public void produce() {
        try {
            lock.lock();
            while (hasFirstProducer) {
                PN.await();
            }
            hasFirstProducer = true;
            int toProduce = getRandValue();
            while (!canProduce(toProduce)) {
                System.out.println(
                        "Waiting for producing " + Integer.toString(toProduce));
                P1.await();
            }
            System.out.println(
                    "Produced - " + Integer.toString(bufferCount) + " -> " +
                            Integer.toString(bufferCount + toProduce));
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

    public void consume() {
        try {
            lock.lock();
            while (hasFirstConsument) {
                CN.await();
            }
            hasFirstConsument = true;
            int toConsume = getRandValue();
            while (!canConsume(toConsume)) {
                System.out.println(
                        "Waiting for consuming " + Integer.toString(toConsume));
                C1.await();
            }
            System.out.println(
                    "Consumed - " + Integer.toString(bufferCount) + " -> " +
                            Integer.toString(bufferCount - toConsume));
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
