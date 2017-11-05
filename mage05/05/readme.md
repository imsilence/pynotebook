def add(a, b):
    print('a={}, b={}'.format(a, b))
    return a + b

#标准调用(位置参数调用)
print(add(1, 2))
print(add(100, 2))


#关键字参数调用
print(add(b=1, a=2))
print(add(b=100, a=2))


def add(a, b, c=0):
    print('a={}, b={}, c={}'.format(a, b, c))
    return a + b + c

add(1, 2)
add(1, 2, 3)

def add(a, b, *args):
    print(a, b, args)

add(1, 2)
add(1, 2, 3)
add(1, 2, 3, 4, 5)


def test(a, b, **kwargs):
    print(a, b, kwargs)

test(1, 2)
test(1, 2, c=1, d=2)

test(1,2, 3, 4, 5, c=1, d=2, e=3)
