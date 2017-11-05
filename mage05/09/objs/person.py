#encoding: utf-8


class Person(object):
    pass



me = Person()

print(type(Person), type(me))

Person.name = ''
print(Person.name, me.name)
print(id(Person.name), id(me.name))

me.name = 'kk'
print(Person.name, me.name)
print(id(Person.name), id(me.name))


me.age = 29
print(me.age, Person.age)
