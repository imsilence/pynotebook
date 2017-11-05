#encoding: utf-8

from multiprocessing import Process
import os
import time

g = []

def test(n):
    g.append(n)
    time.sleep(n)


p = Process(target=test, args=(30, ))
p.start()
print(p.ident)
print(os.getpid())

time.sleep(10)
print(g)