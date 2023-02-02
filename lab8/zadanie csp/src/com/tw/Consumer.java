package com.tw;

import java.util.Random;
import org.jcsp.lang.*;

public class Consumer implements CSProcess {
    private ChannelInputInt[] read_chanels;
    private ChannelOutputInt[] request_send_chanels;
    private ChannelInputInt request_recieve_chanel;
    Random random = new Random();
    private int buffer_to_try;
    private boolean should_finish = false;

    final int id;
    public int consumed;

    public Consumer(ClientChanels chanels, int id)
    {
        this.id = id;
        this.read_chanels = new ChannelInputInt[chanels.work_chanels.length];
        this.request_send_chanels = new ChannelOutputInt[chanels.request_send_chanels.length];

        for (int i = 0; i < read_chanels.length; ++i) {
            this.read_chanels[i] = chanels.work_chanels[i].in();
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
        consume();
        finish_comunication();
        //System.out.println("\tConsumer " + id + " finished");
    }

    private void consume()
    {
        while (true) {
            try {
                Thread.sleep(300);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            var buffer_id = get_free_buffer_id();
            if (should_finish) {
                break;
            }
            var value = read_chanels[buffer_id].read();
            if (value == SpecialMessageType.FINISH.getValue()) {
                break;
            }
            buffer_to_try = request_recieve_chanel.read();
            System.out.println("Consumer " + id + " consumed [" + value + "] from buffer: [" + buffer_id + "] and next buffer to try is: [" + buffer_to_try + "]");
            ++consumed;
        }
    }

    private void finish_comunication()
    {
        for (int i = 0; i < read_chanels.length; ++i) {
            request_send_chanels[i].write(RequestType.CONSUME_FINISH.getValue());
        }
    }

    private int get_free_buffer_id()
    {
        while (true) {
            request_send_chanels[buffer_to_try].write(RequestType.CONSUME.getValue());
            var recived_message = request_recieve_chanel.read();
            if (recived_message == SpecialMessageType.WORK_ACCEPTED.getValue()) {
                return buffer_to_try;
            } else if (recived_message == SpecialMessageType.FINISH.getValue()) {
                should_finish = true;
                return buffer_to_try;
            } else {
                buffer_to_try = recived_message;
            }
        }
    }
}
