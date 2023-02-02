package com.tw;

import com.tw.Buffer;

public class PKProxy extends Proxy {
    private Buffer buffer;

    public PKProxy(Buffer buffer)
    {
        super(new PKScheduler());
        this.buffer = buffer;
        scheduler.start();
    }

    public Future produce(int count)
    {
        return shedule(() -> buffer.can_produce(count), () -> buffer.produce(count), MethodRequest.Type.PRODUCE);
    }

    public Future consume(int count)
    {
        return shedule(() -> buffer.can_consume(count), () -> buffer.consume(count), MethodRequest.Type.CONSUME);
    }
}
