#encoding: utf-8

import time

cached = {}

def fact(n):
    rt = cached.get(n)
    if rt is not None:
        return rt

    rt = 1
    for i in range(1, n + 1):
        rt *= i
        time.sleep(0.5)

    cached[n] = rt
    
    return rt


if __name__ == '__main__':
    s = time.time()
    fact(10)
    e = time.time()

    print(e - s)
    
    s = time.time()
    fact(10)
    e = time.time()
    
    print(e - s)
    
    s = time.time()
    fact(10)
    e = time.time()
    
    print(e - s)