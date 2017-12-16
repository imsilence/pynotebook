#encoding: utf-8
from functools import wraps

def log2(func):
    @wraps(func)
    def wrapper():
        print 'wrapper before2', func.__name__
        func()
        print 'wrapper after2'

    return wrapper

def log(func):
    @wraps(func)
    def wrapper():
        print 'wrapper before', func.__name__
        func()
        print 'wrapper after'

    return wrapper

@log2
@log
def test():
    print 'test'

if __name__ == '__main__':
    test()
