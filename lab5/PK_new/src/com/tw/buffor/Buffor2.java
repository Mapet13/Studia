package com.tw.buffor;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public class Buffor2 extends AbstractBuffor {

    final ReentrantLock lock = new ReentrantLock();
    final Condition prod_cond = lock.newCondition();
    final Condition cons_cond = lock.newCondition();

    public Buffor2(int buffer_size, int seed)
    {
        super(buffer_size, seed);
    }

    @Override
    protected void produceLogic(int to_produce)
    {
        try {
            lock.lock();
            while (!canProduce(to_produce)) {
                prod_cond.await();
            }
            buffer_count += to_produce;
            cons_cond.signal();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            lock.unlock();
        }
    }

    @Override
    protected void consumeLogic(int to_consume)
    {
        try {
            lock.lock();
            while (!canConsume(to_consume)) {
                cons_cond.await();
            }
            buffer_count -= to_consume;
            prod_cond.signal();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            lock.unlock();
        }
    }
}
