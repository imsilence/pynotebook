#encoding: utf-8


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name

me = Person('kk', 29)

me.set_name('kk2')
print(me.get_name())
