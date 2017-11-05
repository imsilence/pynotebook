#encoding: utf-8

class Woman(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


    def set_name(self, name):
        self.name = name

ada = Woman('ada', 18)
ada.get_name()
ada.set_name('ada1')
print(ada.name)
ada.name = 'ada2'
