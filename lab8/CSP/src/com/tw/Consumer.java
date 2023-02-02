package com.tw;

import org.jcsp.lang.*;

public class Consumer implements CSProcess {
    private ChannelInputInt in;
    private ChannelOutputInt req;

    public Consumer(final ChannelOutputInt req, final ChannelInputInt in)
    {
        this.in = in;
        this.req = req;
    } 

    @Override
    public void run()
    {
        int item;
        while (true)
        { 
            req.write(0); 
            item = in.read();
            if (item < 0)
                break;
            System.out.println(item);
        } 
        System.out.println("Consumer ended.");
    } 
}
