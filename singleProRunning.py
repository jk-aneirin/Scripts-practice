#!/usr/bin/python
import time,os,sys
import signal
import functools

pidfile='/tmp/process.pid'

def sig_handler(sig,frame):
    if os.path.exists(pidfile):
        os.remove(pidfile)
    sys.exit(0)

def SingleProcess(func):
    @functools.wraps(func)
    def fun(*args,**kwargs):
        signal.signal(signal.SIGTERM,sig_handler)
        signal.signal(signal.SIGINT,sig_handler)
        signal.signal(signal.SIGQUIT,sig_handler)

        try:
            pf=file(pidfile,'r')
            pid=int(pf.read().strip())
            pf.close()
        except IOError:
            pid=None

        if pid:
            sys.stdout.write('instance is running...\n')
            sys.exit(0)

        file(pidfile,'w+').write('%s\n'%os.getpid())
        return func(*args,**kwargs)
    return fun


@SingleProcess
def _run(a,b):
    while True:
        file('/home/user1/ret.txt','a+').write('{0} and {1}\n'.format(a,b))
        time.sleep(3)

if __name__=='__main__':
    _run(2,3)

