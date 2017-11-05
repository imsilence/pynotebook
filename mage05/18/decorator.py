#encoding: utf-8
import time
from functools import wraps


def logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__, 'before')
        rt = func(*args, **kwargs)
        print(func.__name__, 'after')
        return rt

    return wrapper


def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        s = time.time()
        rt = func(*args, **kwargs)
        print(func.__name__, 'total time:', time.time() - s)
        return rt

    return wrapper

@logging
def test():
    time.sleep(2)

@logging
@timing
def test2():
    time.sleep(4)


test()
test2()
