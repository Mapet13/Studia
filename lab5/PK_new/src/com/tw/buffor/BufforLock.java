package com.tw.buffor;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public class BufforLock extends AbstractBuffor {
    final ReentrantLock lock_producents = new ReentrantLock();
    final ReentrantLock lock_consuments = new ReentrantLock();
    final ReentrantLock lock_buffer = new ReentrantLock();

    final Condition cond = lock_buffer.newCondition();

    public BufforLock(int seed, int bufferSize)
    {
        super(bufferSize, seed);
    }

    @Override
    protected void produceLogic(int toProduce)
    {
        try {
            lock_producents.lock();
            lock_buffer.lock();
            while (!canProduce(toProduce)) {
                cond.await();
            }
            buffer_count += toProduce;
            cond.signal();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            lock_buffer.unlock();
            lock_producents.unlock();
        }
    }

    @Override
    protected void consumeLogic(int toConsume)
    {
        try {
            lock_consuments.lock();
            lock_buffer.lock();
            while (!canConsume(toConsume)) {
                cond.await();
            }

            buffer_count -= toConsume;
            cond.signal();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            lock_buffer.unlock();
            lock_consuments.unlock();
        }
    }
}
