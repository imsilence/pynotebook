#encoding: utf-8


class Dog(object):
    pass

wangwang = Dog()
doudou = Dog()


# 类属性可以动态添加, 修改
Dog.name = ''
Dog.age = 0

print(Dog.name, Dog.age)

# 实例的属性 如果实例属性不存在，则直接访问对应类的属性
print(wangwang.name, wangwang.age)
print(doudou.name, doudou.age)


# 实例的属性 可以动态修改，修改以后不影响类的属性
wangwang.name = 'wangwang'
wangwang.age = 2

print(Dog.name, Dog.age)
print(wangwang.name, wangwang.age)
print(doudou.name, doudou.age)

Dog.name = 'dog'
Dog.age = 1

print(Dog.name, Dog.age)
print(wangwang.name, wangwang.age)
print(doudou.name, doudou.age)

# 如果添加对象属性，类和其他对象是不添加的
doudou.sex = 1
try:
    print(doudou.sex)
except BaseException as e:
    print(e)
try:
    print(Dog.sex)
except BaseException as e:
    print(e)

try:
    print(wangwang.sex)
except BaseException as e:
    print(e)
