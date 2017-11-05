#encoding: utf-8

import traceback
print('before')

try:
    1/1
except BaseException as e:
    print(e)

print('after')


def test1():
    print('test1 before')
    try:
        l = []
        l[1]
    except BaseException as e:
        print(e)
        print(traceback.format_exc())
        return

    print('test1 after')


def test2():
    print('test2 before')
    try:
        d = {}
        d['kk']
    except BaseException as e:
        print(e)
        print(traceback.format_exc())
        return
    finally:
        print('test2 after')


test1()
test2()
