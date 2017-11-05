class Person(object):
    name = ''
    age = 0

    def __init__(self, sex):
        self.sex = sex

    @classmethod
    def gen_id(cls):
        #属性
        #方法
        pass

me = Person(sex=1)


class Animal(object):

    def __init__(self, name):
        self.name = name

    def jiao(self):
        print('wowo')

class Person(Animal):
    def __init__(self, id, name, age):
        super(Person, self).__init__(name)
        self.id = id
        self.age = age

    def jiao(self):
        super(Person, self).jiao()
        print('wawa')

wowo, wawa
