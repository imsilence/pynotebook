#复习

def func_name(p1, p2, p3, ..., pn):
    func_body
    return rt


def rt_func(i):
    print('before')
    if i < 60:
        return 0
    else:
        return 1
    print('after')
    return -1

rt_func(50)
rt_func(60)


a = 1
b = [1]
c = [1]

def test(p1, p2, p3):
    p1 = 1
    p2 = [2]
    p3.append(2)


test(a, b, c)
print(a)
print(b)
print(c)


rt = None
if a:
    rt = b
else:
    rt = c


[translate(x) for x in list_name if filter(x)]

rt_list = []
for x in list_name:
    if filter(x):
        rt_list.append(translate(x))


条件


__name__


python需要运行  __main__
模块导入不需要运行: 模块名称

if __name__ == '__main__':
    main()
