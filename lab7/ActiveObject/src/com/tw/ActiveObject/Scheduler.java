package com.tw.ActiveObject;

public abstract class Scheduler extends Thread {
    protected ActivationQueue activationQueue;

    protected Scheduler(ActivationQueue activationQueue)
    {
        this.activationQueue = activationQueue;
    }

    public void enqueue(MethodRequest request)
    {
        activationQueue.enqueue(request);
    }

    @Override
    public abstract void run();

    public abstract void finish();
}
