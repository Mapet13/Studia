package com.tw;

import org.jcsp.lang.One2OneChannelInt;

public class ClientChanels {
    public One2OneChannelInt[] work_chanels;
    public One2OneChannelInt[] request_send_chanels;
    public One2OneChannelInt request_recieve_chanel;

    public ClientChanels(int BuffersCount)
    {
        this.work_chanels = new One2OneChannelInt[BuffersCount];
        this.request_send_chanels = new One2OneChannelInt[BuffersCount];
    }
}
