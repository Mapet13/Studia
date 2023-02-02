package com.tw;

import org.jcsp.lang.*;

public class Main {
    public static void main(String[] args)
    {
        new Main();
    }

    final int ProducersCount = 10;
    final int ItemsToProudce = 100;
    final int ConsumersCount = 8;
    final int BuffersCount = 8;
    final int BuffersSize = 2;

    public Main()
    {
        final One2OneChannelInt[] consume_chanels = Channel.one2oneIntArray(ConsumersCount);
        final One2OneChannelInt[] produce_chanels = Channel.one2oneIntArray(ProducersCount);
        final One2OneChannelInt[] from_clients_to_buffers_chanels = Channel.one2oneIntArray(BuffersCount * (ProducersCount + ConsumersCount));
        final One2OneChannelInt[] from_buffer_to_clients_chanels = Channel.one2oneIntArray(ProducersCount + ConsumersCount);

        final ClientChanels[] clents_chanels = new ClientChanels[ProducersCount + ConsumersCount];
        final BufferChanels[] buffers_chanels = new BufferChanels[BuffersCount];

        for (int i = 0; i < BuffersCount; ++i) {
            buffers_chanels[i] = new BufferChanels(ProducersCount, ConsumersCount);
        }
        for (int i = 0; i < ProducersCount + ConsumersCount; ++i) {
            clents_chanels[i] = new ClientChanels(BuffersCount);
        }

        for (int i = 0; i < produce_chanels.length; ++i) {
            for (int j = 0; j < BuffersCount; ++j) {
                clents_chanels[i].work_chanels[j] = produce_chanels[i];
                buffers_chanels[j].produce_chanels[i] = produce_chanels[i];
            }
            clents_chanels[i].request_recieve_chanel = from_buffer_to_clients_chanels[i];
        }

        for (int i = 0; i < consume_chanels.length; ++i) {
            for (int j = 0; j < BuffersCount; ++j) {
                clents_chanels[i + ProducersCount].work_chanels[j] = consume_chanels[i];
                buffers_chanels[j].consume_chanels[i] = consume_chanels[i];
            }
            clents_chanels[i + ProducersCount].request_recieve_chanel = from_buffer_to_clients_chanels[i + ProducersCount];
        }

        for (int i = 0; i < BuffersCount; ++i) {
            for (int j = 0; j < ProducersCount + ConsumersCount; ++j) {
                clents_chanels[j].request_send_chanels[i] = from_clients_to_buffers_chanels[i * (ProducersCount + ConsumersCount) + j];
                buffers_chanels[i].request_recieve_chanels[j] = from_clients_to_buffers_chanels[i * (ProducersCount + ConsumersCount) + j];
            }
            for (int j = 0; j < ProducersCount + ConsumersCount; ++j) {
                buffers_chanels[i].request_send_chanels[j] = from_buffer_to_clients_chanels[j];
            }
        }

        var producers = new Producer[ProducersCount];
        var consumers = new Consumer[ConsumersCount];
        var buffers = new Buffer[BuffersCount];
        var procList = new CSProcess[ProducersCount + ConsumersCount + BuffersCount];
        for (int i = 0; i < BuffersCount; ++i) {
            buffers[i] = new Buffer(buffers_chanels[i], BuffersCount, ProducersCount, ConsumersCount, i, BuffersSize);
            procList[i] = buffers[i];
        }
        for (int i = 0; i < ProducersCount; ++i) {
            producers[i] = new Producer(clents_chanels[i], ItemsToProudce, i);
            procList[BuffersCount + i] = producers[i];
        }
        for (int i = 0; i < ConsumersCount; ++i) {
            consumers[i] = new Consumer(clents_chanels[i + ProducersCount], i + ProducersCount);
            procList[BuffersCount + ProducersCount + i] = consumers[i];
        }

        Parallel par = new Parallel(procList);
        par.run();

        for (int i = 0; i < ProducersCount; ++i) {
            System.out.println("Producer " + i + " produced " + producers[i].produced + " items");
        }

        for (int i = 0; i < ConsumersCount; ++i) {
            System.out.println("Consumer " + i + " consumed " + consumers[i].consumed + " items");
        }
        for (int i = 0; i < BuffersCount; ++i) {
            System.out.println("Buffer " + i + " has " + buffers[i].interactions_count + " interactions");
        }
    }
}
