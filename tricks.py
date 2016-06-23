'''将列表数据分割成大小相同的块'''
def chunks(li,n):   #将列表li分割成大小为n的块
    for i in xrange(0,len(li),n):
        yield li[i:i+n]

'''查找列表下某个元素的下标'''
['foo','bar','baz'].index('bar')

'''合并列表中的列表,列表li里面包含有子列表'''
[item for sublist in li for item in sublist]

'''从列表中随机取一个元素'''
import random
foo=[1,2,3,4,5,6]
print random.choice(foo)

'''获取实例的类名'''
#方法一
type(x).__name__
#方法二
x.__class__.__name__

'''通过函数名的字符串来调用这个函数'''
class A():
    def __init__():
        pass
    @staticmethod  #类方法也是可以的@classmethod
    def add(a,b):
        return a+b
ret=getattr(A,'add')(1,2)
print ret

'''测量脚本运行的时间'''
import cProfile
cProfile.run('function()')
#或者
python -m cProfile myscript.py

'''pip升级所有包'''
pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs pip install -U


