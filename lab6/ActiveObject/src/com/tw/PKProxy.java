package com.tw;

public class PKProxy extends Proxy {
    private PKBuffer bufor;

    public PKProxy(int size)
    {
        super(new PKScheduler());
        bufor = new PKBuffer(size);
        scheduler.start();
    }

    public Future produce(int count)
    {
        return shedule(() -> bufor.can_produce(count), () -> bufor.produce(count));
    }

    public Future consume(int count)
    {
        return shedule(() -> bufor.can_consume(count), () -> bufor.consume(count));
    }
}
