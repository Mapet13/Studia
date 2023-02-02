package com.tw;

import org.jcsp.lang.One2OneChannelInt;

public class BufferChanels {
    public One2OneChannelInt[] produce_chanels;
    public One2OneChannelInt[] consume_chanels;
    public One2OneChannelInt[] request_send_chanels;
    public One2OneChannelInt[] request_recieve_chanels;

    public BufferChanels(int ProducersCount, int ConsumersCount)
    {
        this.produce_chanels = new One2OneChannelInt[ProducersCount];
        this.consume_chanels = new One2OneChannelInt[ConsumersCount];
        this.request_send_chanels = new One2OneChannelInt[ConsumersCount + ProducersCount];
        this.request_recieve_chanels = new One2OneChannelInt[ConsumersCount + ProducersCount];
    }
}
