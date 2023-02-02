package com.tw;

import org.jcsp.lang.Alternative;
import org.jcsp.lang.AltingChannelInputInt;
import org.jcsp.lang.CSProcess;
import org.jcsp.lang.ChannelOutputInt;
import org.jcsp.lang.Guard;
import org.jcsp.lang.One2OneChannelInt;

public class Buffer implements CSProcess
{
    private AltingChannelInputInt[] in;
    private AltingChannelInputInt[] req;
    private ChannelOutputInt[] out;
    private int[] buffer = new int[10];
    int hd = -1;
    int tl = -1;

    public Buffer (final One2OneChannelInt[] in, final One2OneChannelInt[] req, final One2OneChannelInt[] out)
    {
        this.in = new AltingChannelInputInt[in.length];
        this.req = new AltingChannelInputInt[req.length];
        this.out = new ChannelOutputInt[out.length];

        for (int i = 0; i < in.length; i++)
        {
            this.in[i] = in[i].in();
            this.req[i] = req[i].in();
            this.out[i] = out[i].out();
        }
    } 

    public void run ()
    { 
        final Guard[] guards = { in[0], in[1], req[0], req[1] };
        final Alternative alt = new Alternative(guards);
        
        int countdown = 4;
        while (countdown > 0)
        { 
            int index = alt.select();
            switch (index)
            { 
            case 0:
            case 1: 
                if (hd < tl + 11) 
                { 
                    int item = in[index].read();
                    if (item < 0) {
                        countdown--;
                    }
                    else { 
                        hd++;
                        buffer[hd % buffer.length] = item;
                    }
                }
                break;
            case 2:
            case 3: 
                int req_id = index-2;
                if (tl < hd) 
                { 
                    req[req_id].read();
                    tl++;
                    int item = buffer[tl % buffer.length];
                    out[req_id].write(item);
                }
                else if (countdown <= 2) { 
                    req[req_id].read(); 
                    out[req_id].write(-1); 
                    countdown--;
                }
                break;
            } 
        } 
        System.out.println("Buffer ended.");
    } 


}
