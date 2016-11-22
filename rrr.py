from funcperfstat import timer

@timer
def foo():
    for i in range(100):
        print i

foo()


