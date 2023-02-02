package com.tw;

import com.tw.buffor.AbstractBuffor;

public class VerboseEndlessRunner extends AbstractRunner {
    public VerboseEndlessRunner(AbstractBuffor buffor)
    {
        super(buffor);
    }

    public void run() throws InterruptedException
    {
        initialise_threads();

        while (true) {
            Thread.sleep(1000);
            for (var worker : workers) {
                System.out.println(worker.getWorkSummary());
            }
            System.out.println("-----------------------");
        }
    }
}
