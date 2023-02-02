package com.tw;

import java.util.function.Supplier;

class RaportMaker implements Runnable {
    final Supplier<Single_run_raport> raport_fn;
    Single_run_raport raport = null;

    public RaportMaker(Supplier<Single_run_raport> raport_fn)
    {
        this.raport_fn = raport_fn;
    }

    @Override
    public void run()
    {
        raport = raport_fn.get();
    }

    public Single_run_raport get_raport()
    {
        return raport;
    }
}