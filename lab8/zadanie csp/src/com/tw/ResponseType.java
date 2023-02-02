package com.tw;

public enum ResponseType {
    Accepted(-1);

    private int value;

    private ResponseType(int value)
    {
        this.value = value;
    }

    public int getValue()
    {
        return value;
    }
}