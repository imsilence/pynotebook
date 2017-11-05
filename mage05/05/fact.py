#encoding: utf-8



def fact(n):
    '''
    n! = 1 * 2 * 3 * ... * n (n > 0)
    n! = 1 (n = 0)
    '''
    if n == 0:
        return 1
    elif n > 0:
        rt_value = 1
        for i in range(1, n + 1):
            rt_value *= i
        return rt_value
    else:
        return None


print(fact(5))

'''
n! = 1 * 2 * 3 * .... * n - 1* n
n! = n * (n - 1)!

f(n) = n * f(n - 1)

n! =  n * (n - 1)! (n > 0)
n! = 1 (n = 0)
'''

def fact2(n):
    if n == 0:
        return 1
    elif n > 0:
        return n * fact2(n - 1)
    else:
        return None

fact2(5)
