package com.tw.Conditions;

import com.tw.Buffer;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

public class BufferLock extends Buffer {

    public BufferLock(int buffer_size, int hard_work_amount)
    {
        super(buffer_size, hard_work_amount);
    }

    final ReentrantLock lock_producents = new ReentrantLock();
    final ReentrantLock lock_consuments = new ReentrantLock();
    final ReentrantLock lock_buffer = new ReentrantLock();
    final Condition cond = lock_buffer.newCondition();

    boolean should_finish = false;

    public synchronized void finish()
    {
        should_finish = true;
    }

    @Override
    public void produce(int count)
    {
        try {
            lock_producents.lock();
            lock_buffer.lock();

            if (should_finish)
                return;

            while (!can_produce(count) && !should_finish) {
                cond.awaitNanos(10000);
            }
            super.produce(count);
            cond.signal();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            lock_buffer.unlock();
            lock_producents.unlock();
        }
    }

    @Override
    public void consume(int count)
    {
        try {
            lock_consuments.lock();
            lock_buffer.lock();

            if (should_finish)
                return;

            while (!can_consume(count) && !should_finish) {
                cond.awaitNanos(10000);
            }

            super.consume(count);
            cond.signal();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            lock_buffer.unlock();
            lock_consuments.unlock();
        }
    }
}
