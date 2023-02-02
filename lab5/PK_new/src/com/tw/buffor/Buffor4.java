package com.tw.buffor;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public class Buffor4 extends AbstractBuffor {
    final ReentrantLock lock = new ReentrantLock();
    final Condition P1 = lock.newCondition();
    final Condition PN = lock.newCondition();
    final Condition C1 = lock.newCondition();
    final Condition CN = lock.newCondition();

    boolean has_first_producer = false;
    boolean has_first_consument = false;

    public Buffor4(int seed, int buffer_size)
    {
        super(buffer_size, seed);
    }

    @Override
    protected void produceLogic(int toProduce)
    {
        try {
            lock.lock();
            while (has_first_producer) {
                PN.await();
            }
            has_first_producer = true;
            while (!canProduce(toProduce)) {
                P1.await();
            }
            buffer_count += toProduce;
            has_first_producer = false;
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
            while (has_first_consument) {
                CN.await();
            }
            has_first_consument = true;
            while (!canConsume(toConsume)) {
                C1.await();
            }

            buffer_count -= toConsume;
            has_first_consument = false;
            P1.signal();
            CN.signal();
        } catch (final InterruptedException e) {
            e.printStackTrace();
        } finally {
            lock.unlock();
        }
    }
}
