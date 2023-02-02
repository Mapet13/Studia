package com.tw;

import java.util.Random;
import org.jcsp.lang.*;

public class Producer implements CSProcess {
    private ChannelOutputInt[] write_chanels;
    private ChannelOutputInt[] request_send_chanels;
    private ChannelInputInt request_recieve_chanel;
    private int itemsToProduce;
    private int id;
    private int buffer_to_try;
    final Random random = new Random();
    public int produced;

    public Producer(ClientChanels chanels, int itemsToProduce, int id)
    {
        this.id = id;
        this.itemsToProduce = itemsToProduce;
        this.write_chanels = new ChannelOutputInt[chanels.work_chanels.length];
        this.request_send_chanels = new ChannelOutputInt[chanels.request_send_chanels.length];

        for (int i = 0; i < write_chanels.length; ++i) {
            this.write_chanels[i] = chanels.work_chanels[i].out();
        }
        for (int i = 0; i < request_send_chanels.length; ++i) {
            this.request_send_chanels[i] = chanels.request_send_chanels[i].out();
        }
        this.request_recieve_chanel = chanels.request_recieve_chanel.in();

        this.buffer_to_try = Math.abs(random.nextInt()) % request_send_chanels.length;
    }

    @Override
    public void run()
    {
        produce();
        finish_comunication();
        System.out.println("\tProducer " + id + " finished");
    }

    private void produce()
    {
        for (int i = 0; i < itemsToProduce; ++i) {
            var value = Math.abs(random.nextInt());
            var buffer_id = get_free_buffer_id();

            write_chanels[buffer_id].write(value);
            buffer_to_try = request_recieve_chanel.read();
            System.out.println("Producer " + id + " producing finished [" + value + "] into buffer: [" + buffer_id + "] and next buffer to try is: " + buffer_to_try);
            produced++;
        }
    }

    private void finish_comunication()
    {
        for (int i = 0; i < write_chanels.length; ++i) {
            request_send_chanels[i].write(RequestType.PRODUCE_FINISH.getValue());
        }
    }

    private int get_free_buffer_id()
    {
        while (true) {
            request_send_chanels[buffer_to_try].write(RequestType.PRODUCE.getValue());
            var recived_message = request_recieve_chanel.read();
            if (recived_message == SpecialMessageType.WORK_ACCEPTED.getValue()) {
                return buffer_to_try;
            } else {
                buffer_to_try = recived_message;
            }
        }
    }
}
