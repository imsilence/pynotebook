#encoding: utf-8

import time

from cache import Cache


def fact(n):
    rt = Cache.get(n)
    if rt is not None:
        return int(rt)

    rt = 1
    for i in range(1, n + 1):
        rt *= i
        time.sleep(0.5)

    Cache.set(n, rt)

    return rt


if __name__ == '__main__':
    s = time.time()
    print(fact(10))
    e = time.time()

    print(e - s)
    
    s = time.time()
    print(fact(10))
    e = time.time()
    
    print(e - s)
    
    s = time.time()
    print(fact(10))
    e = time.time()
    
    print(e - s)