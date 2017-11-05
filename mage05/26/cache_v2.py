#encoding: utf-8

import time

import redis

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

cached = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

#key => label:label:label:label
#key => kk:fact:cache:n
key_tpl = 'kk:fact:%s'


def fact(n):
    rt = cached.get(key_tpl % n)
    if rt is not None:
        return int(rt)

    rt = 1
    for i in range(1, n + 1):
        rt *= i
        time.sleep(0.5)

    cached.set(key_tpl % n, rt)

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