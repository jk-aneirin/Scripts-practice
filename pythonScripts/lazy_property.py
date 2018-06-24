#!/usr/bin/env python
#-*- coding: utf-8 -*-
#python对象的延迟初始化是指，当它第一次被创建时才进行初始化，或者保存第一次创建的结果，然后每次调用的时候直接返回该结果，延迟初始化主要用于提高性能，避免浪费计算，减少程序的内存需求
#method 1
class lazy():
    def __init__(self,func):
        self.func = func

    def __get__(self,instance,cls):
        val = self.func(instance)
        setattr(instance,self.func.__name__,val)
        return val

class Circle_one():
    def __init__(self,radius):
        self.radius = radius

    @lazy
    def area(self):
        print("evalute")
        return 3.14 * self.radius ** 2

c = Circle_one(4)
print(c.radius)
print(c.area)
print(c.area)

#method 2
def lazy_property(func):
    attr_name = "_lazy_" + func.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self,attr_name):
            setattr(self,attr_name,func(self))
        return getattr(self,attr_name)
    return _lazy_property

class Circle_two():
    def __init__(self,radius):
        self.radius = radius

    @lazy_property
    def area(self):
        print("evalue")
        return 3.14 * self.radius ** 2

d = Circle_two(4)
print("before first visit")
print(d.__dict__)
d.area
print("after first visit")
print(d.__dict__)
