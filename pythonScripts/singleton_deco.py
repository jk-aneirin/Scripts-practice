def singleton(cls,*args,**kwargs):
    instance = {}
    def _singleton():
        if cls not in instance:
            instance[cls]=cls(*args,**kwargs)
        return instance[cls]
    return _singleton

@singleton
class test_singleton():
    def __init__(self):
        self.num_sum = 0

if __name__ == '__main__':
    cls1 = test_singleton()
    cls2 = test_singleton()

    print(cls1)
    print(cls2)
