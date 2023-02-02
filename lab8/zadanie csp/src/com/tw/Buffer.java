package com.tw;

import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;
import org.jcsp.lang.Alternative;
import org.jcsp.lang.AltingChannelInputInt;
import org.jcsp.lang.CSProcess;
import org.jcsp.lang.ChannelOutputInt;
import org.jcsp.lang.Guard;
import org.jcsp.lang.Skip;

public class Buffer implements CSProcess {
    private final AltingChannelInputInt[] read_chanels;
    private final ChannelOutputInt[] write_chanels;
    private final ChannelOutputInt[] request_send_chanels;
    private final AltingChannelInputInt[] request_recieve_chanels;
    private final int id;
    private final Random random = new Random();
    private boolean should_run = true;
    private boolean should_responding_with_finish_messages = false;
    private int working_producers_count;
    private int working_consumers_count;
    private int buffers_count;
    private int producers_count;
    private int consumers_count;
    private boolean is_producent_round = false;
    private Queue<Integer> items = new LinkedList<>();
    private int size;

    public int interactions_count = 0;

    private Guard[] producers_guards;
    private Guard[] consumers_guards;

    private Alternative producers_alternative;
    private Alternative consumers_alternative;

    public Buffer(BufferChanels chanels, int buffers_count, int producers_count, int consumers_count, int id, int size)
    {
        this.size = size;
        this.id = id;
        this.buffers_count = buffers_count;
        this.producers_count = producers_count;
        this.consumers_count = consumers_count;
        this.working_producers_count = chanels.produce_chanels.length;
        this.working_consumers_count = chanels.consume_chanels.length;
        this.read_chanels = new AltingChannelInputInt[chanels.produce_chanels.length];
        this.write_chanels = new ChannelOutputInt[chanels.consume_chanels.length];
        this.request_send_chanels = new ChannelOutputInt[chanels.request_send_chanels.length];
        this.request_recieve_chanels = new AltingChannelInputInt[chanels.request_recieve_chanels.length];

        for (int i = 0; i < read_chanels.length; ++i) {
            this.read_chanels[i] = chanels.produce_chanels[i].in();
        }
        for (int i = 0; i < write_chanels.length; ++i) {
            this.write_chanels[i] = chanels.consume_chanels[i].out();
        }
        for (int i = 0; i < request_send_chanels.length; ++i) {
            this.request_send_chanels[i] = chanels.request_send_chanels[i].out();
        }
        for (int i = 0; i < request_recieve_chanels.length; ++i) {
            this.request_recieve_chanels[i] = chanels.request_recieve_chanels[i].in();
        }

        create_guards_for_producers();
        create_guards_for_consumers();

        producers_alternative = new Alternative(producers_guards);
        consumers_alternative = new Alternative(consumers_guards);
    }

    public void run()
    {
        while (should_run) {
            interactions_count++;
            is_producent_round = !is_producent_round;

            if (is_producent_round) {
                var alt = producers_alternative.select();
                if (alt != producers_count) {
                    process_producers_requests(alt);
                }
            } else {
                var alt = consumers_alternative.select();
                if (alt != consumers_count) {
                    process_consumer_requests(alt);
                }
            }
        }
        log("finished");
    }

    private void process_producers_requests(int index)
    {
        var request = request_recieve_chanels[index].read();
        switch (RequestType.fromInt(request)) {
            case PRODUCE -> process_produce_request(index);
            case PRODUCE_FINISH -> process_produce_finish_request(index);
            default -> log("!!!!!!!!!!!!!!!!! Recieved request from producer " + index + " with unknown type " + request);
        }   
    }

    private void process_consumer_requests(int index)
    {
        var id = index + producers_count;
        var request = request_recieve_chanels[id].read();
        switch (RequestType.fromInt(request)) {
            case CONSUME -> process_consume_request(index);
            case CONSUME_FINISH -> process_consume_finish_request(index);
            default -> log("!!!!!!!!!!!!!!!!! Recieved request from consumer " + id + " with unknown type " + request);
        }   
    }

    private void process_produce_request(int index)
    {
        log("Recieved request from producer " + index);
        if (items.size() < size) {
            log("Accepting request from producer " + index);
            request_send_chanels[index].write(SpecialMessageType.WORK_ACCEPTED.getValue());
            log("reading started");
            items.add(read_chanels[index].read());
            log("reading finished");
            this.request_send_chanels[index].write(get_random_buffer());
        } else {
            var next_buffer_id = get_random_buffer();
            log("Rejecting request from producer " + index + ". Try buffer " + next_buffer_id);
            request_send_chanels[index].write(next_buffer_id);
        }

    }

    private void process_produce_finish_request(int index)
    {
        log("Recieved finish request from producer " + index);
        --working_producers_count;
        if (working_producers_count <= 0) {
            log("All producers finished");
            should_responding_with_finish_messages = true;
        }
    }

    private void process_consume_request(int index) 
    {
        var id = index + producers_count;
        log("Recieved request from consumer " + id);
        if (!items.isEmpty()) {
            log("Accepting request from consumer " + id);
            request_send_chanels[id].write(SpecialMessageType.WORK_ACCEPTED.getValue());
            write_chanels[index].write(items.poll());
            request_send_chanels[id].write(get_random_buffer());
        } else if (should_responding_with_finish_messages) {
            log("Accepting request from consumer " + id + " with finish message");
            request_send_chanels[id].write(SpecialMessageType.FINISH.getValue());
        }
        else {
            var next_buffer_id = get_random_buffer();
            log("Rejecting request from consumer " + id + ". Try buffer " + next_buffer_id);
            request_send_chanels[id].write(next_buffer_id);
        }
    }

    private void process_consume_finish_request(int index)
    {
        --working_consumers_count;
        log("Consumer " + index + " finished");
        if (working_consumers_count <= 0) {
            log("All consumers finished");
            should_run = false;
        }
    }

    private void create_guards_for_producers()
    {
        producers_guards = new Guard[producers_count + 1];
        for (int i = 0; i < producers_count; ++i) {
            producers_guards[i] = request_recieve_chanels[i];
        }
        producers_guards[producers_count] = new Skip();
    }

    private void create_guards_for_consumers()
    {
        consumers_guards = new Guard[consumers_count + 1];
        for (int i = 0; i < consumers_count; ++i) {
            consumers_guards[i] = request_recieve_chanels[i + producers_count];
        }
        consumers_guards[consumers_count] = new Skip();
    }

    private int get_random_buffer()
    {
        do {
            var next_buffer_id = random.nextInt(buffers_count);
            if (next_buffer_id != id) {
                return next_buffer_id;
            }
        } while (true);
    }

    private void log(String message)
    {
        System.out.println("\t\t -- Buffer " + id + ": " + message + " interactions: " + interactions_count);
    }
}