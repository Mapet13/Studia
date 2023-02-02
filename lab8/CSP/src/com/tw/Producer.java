package com.tw;

import org.jcsp.lang.*;

public class Producer implements CSProcess {
    private ChannelOutputInt channel;
    private int start;

    public Producer(final ChannelOutputInt out, final int start)
    {
        channel = out;
        this.start = start;
    }

    @Override
    public void run()
    {
        int item;
        for (int k = 0; k < 100; k++)
        { 
            item = (int)(Math.random()*100)+1+start;
            channel.write(item);
        } 
        channel.write(-1);
        System.out.println("Producer" + start + " ended.");

    }
}
