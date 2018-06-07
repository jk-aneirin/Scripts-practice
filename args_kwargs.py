#!/usr/bin/env python
#coding:UTF-8
'''该脚本演示*args和**kwargs的用法'''

def pargs(*args):
    for k,v in enumerate(args):
        print '{0}.{1}'.format(k,v)

pargs('one','two','three')

def pkwargs(**kwargs):
    for k,v in kwargs.items():
        print '{0}={1}'.format(k,v)

pkwargs(one=1,two=2,three=3)

#调用函数时也可以用'*'和'**'

def p1(a,b,c):
    print 'a={0},b={1},c={2}'.format(a,b,c)
li=['apple','peach','pear']
p1(*li)

di={'one':1,'two':2,'three':3,'four':4}
pkwargs(**di)
