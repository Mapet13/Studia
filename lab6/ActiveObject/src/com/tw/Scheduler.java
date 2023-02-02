package com.tw;

public abstract class Scheduler extends Thread {
    protected IActivationQueue activationQueue;

    protected Scheduler(IActivationQueue activationQueue)
    {
        this.activationQueue = activationQueue;
    }

    public void enqueue(MethodRequest request)
    {
        activationQueue.enqueue(request);
    }

    @Override
    public abstract void run();
}
