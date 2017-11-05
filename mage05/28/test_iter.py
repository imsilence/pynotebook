#encoding: utf-8

def odd(num):
    for i in range(num):
        if i % 2 == 0:
            yield i

def odd_print(num):
    for i in range(num):
        if i % 2 == 0:
            print(i)

def odd_total(num):
    total = 0
    for i in range(num):
        if i % 2 == 0:
            total += i

    return total

class Odd(object):
    def __init__(self, start, end):
        self._start = start
        self._end = end
    def __iter__(self):
        return self
    def __next__(self):
        while self._start < self._end:
            if self._start % 2 == 0:
                tmp = self._start
                self._start += 1
                return tmp
            self._start += 1
        raise StopIteration()


class MySQLConnection(object):
    def __init__(self, *args, **kwargs):
        print('__init__')
    def __enter__(self):
        print('__enter__')
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        print('关闭资源')
        print(exc_type, exc_value, exc_tb)

class ObjectCall(object):
    def __call__(self, *args, **kwargs):
        print(args, kwargs)


if __name__ == '__main__':
    odd_print(100)
    odd_total(100)

    f = None
    try:
        f = open(path, 'r')
        f.read()
    except BaseException as e:
        pass
    finally:
        if f:
            f.close()

    with open(path, 'r') as f:
        f.read()