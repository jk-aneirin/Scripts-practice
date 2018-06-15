#!/usr/bin/env python
"""ThreadLocal解决了全局变量需要加锁，局部变量传递麻烦的问题，下例演示了它的用法"""
import threading

local=threading.local()
def func(name):
    print 'current thread:%s'%threading.currentThread().name
    local.name=name
    print '%s in %s' %(local.name,threading.currentThread().name)

t1=threading.Thread(target=func,args=('haobo',))
t2=threading.Thread(target=func,args=('lina',))
t1.start()
t2.start()
t1.join()
t2.join()
