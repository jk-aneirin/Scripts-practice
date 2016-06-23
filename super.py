#coding:UTF-8

class Base(object):
    def __init__(self):
        pass
    def super_method(self,name):
        self.name=name
        print self.name

class A(Base):
    def __init__(self):
        Base.__init__(self)#因为调用类方法，所以要传self

class B(Base):
    def __init__(self):
        super(B,self).__init__()
    def callsuper(self,name):
        super(B,self).super_method(name)#因为调用实例方法，所以不要加self。super(B,self)返回Base类的实例
b=B()
b.callsuper('hello')

