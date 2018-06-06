import time
from functools import wraps
#implement using "with" context
class Timer(object):
    def __init__(self,verbose=False):
        self.verbose=verbose

    def __enter__(self):
        self.start=time.time()  #start seconds
        return self

    def __exit__(self,*args):
        self.end=time.time()   #end seconds
        self.secs=self.end-self.start #spends seconds
        self.msecs=self.secs*1000 #convert milliseconds
        if self.verbose:
            print 'elaplsed time:%f ms'%self.msecs
"""Example
with Timer() as t:
    foo()
print "=>foo() spends %s"%t.secs
"""
#implement using decorator

def timer(func):
    @wraps(func)
    def function_timer(*args,**kwargs):
        t0=time.time()
        result=func(*args,**kwargs)
        t1=time.time()
        print "Total time running %s: %s seconds"%(func.func_name,str(t1-t0))
        return result
    return function_timer
"""
cProfile module
line_profiler https://github.com/rkern/line_profiler
"""





