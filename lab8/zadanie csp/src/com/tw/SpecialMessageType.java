package com.tw;

public enum SpecialMessageType {
    WORK_ACCEPTED(-1),
    FINISH(-10),
    UNKNOWN(-11);

    private int value;

    private SpecialMessageType(int value)
    {
        this.value = value;
    }

    public int getValue()
    {
        return value;
    }
}
