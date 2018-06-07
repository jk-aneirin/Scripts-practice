#!/usr/bin/env python
def outer(fn):
    def new():
        return '<outer>'+fn()+'</outer>'    
    return new

def inner(fn):
    def new():
        return '<inner>'+fn()+'</inner>'
    return new

@outer
@inner
def ded():
    return 'hello,world'

ret=ded()
print ret
