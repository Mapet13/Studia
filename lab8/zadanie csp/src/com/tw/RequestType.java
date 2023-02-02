package com.tw;

public enum RequestType {
    PRODUCE(0),
    CONSUME(1),
    PRODUCE_FINISH(2),
    CONSUME_FINISH(3);

    private int value;

    private RequestType(int value){
        this.value = value;
    }

    public int getValue() {
        return value;
    }

    public static RequestType fromInt(int value) {
        return java.util.Arrays.stream(RequestType.values())
            .filter(type -> type.getValue() == value)
            .findFirst()
            .orElseThrow(() -> new IllegalArgumentException("Invalid value: " + value));
    }
}
