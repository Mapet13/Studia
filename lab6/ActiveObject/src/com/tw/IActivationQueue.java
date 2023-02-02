package com.tw;

public interface IActivationQueue {
    void enqueue(MethodRequest a);
    MethodRequest dequeue();
    int size();
}