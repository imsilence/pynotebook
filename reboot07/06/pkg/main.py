#encoding: utf-8

'''
import a

print globals()
print a.NAME
a.print_a()

a.NAME = 'b'

print a.NAME
a.print_a()


from a import NAME, print_a
from a import *

print globals()

print NAME
print_a()

NAME = 'b'

print NAME
print_a()
'''
import pkga
print pkga.NAME

import pkga.b
print globals()

print pkga.b.NAME
'''

from pkga import b
print globals()
print b.NAME
from pkga import *

print globals()
'''