package com.tw.buffor;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public class Buffor4HasWaiters extends AbstractBuffor {
    final ReentrantLock lock = new ReentrantLock();
    final Condition P1 = lock.newCondition();
    final Condition PN = lock.newCondition();
    final Condition C1 = lock.newCondition();
    final Condition CN = lock.newCondition();

    public Buffor4HasWaiters(int seed, int bufferSize)
    {
        super(bufferSize, seed);
    }

    @Override
    protected void produceLogic(int toProduce)
    {
        try {
            lock.lock();
            while (lock.hasWaiters(P1)) {
                PN.await();
            }
            while (!canProduce(toProduce)) {
                P1.await();
            }
            buffer_count += toProduce;
            C1.signal();
            PN.signal();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            lock.unlock();
        }
    }

    @Override
    protected void consumeLogic(int toConsume)
    {
        try {
            lock.lock();
            while (lock.hasWaiters(C1)) {
                CN.await();
            }
            while (!canConsume(toConsume)) {
                C1.await();
            }

            buffer_count -= toConsume;
            P1.signal();
            CN.signal();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            lock.unlock();
        }
    }
}
