#encoding: utf-8
import random

class Dog(object):

    def __init__(self, name, blood=100):
        self.name = name
        self.blood = blood

    def get_blood(self):
        return self.blood

    def drop_blood(self, drop):
        self.blood -= drop

    def attack(self, rival):
        drop = random.randint(0, 20)
        print(self.name, '攻击', rival.name, '掉血', drop)
        rival.drop_blood(drop)


class Cat(object):

    def __init__(self, name, blood=100):
        self.name = name
        self.blood = blood

    def get_blood(self):
        return self.blood

    def drop_blood(self, drop):
        self.blood -= drop

    def attack(self, rival):
        drop = random.randint(0, 20)
        print(self.name, '攻击', rival.name, '掉血', drop)
        rival.drop_blood(drop)


if __name__ == '__main__':
    wangwang = Dog('wangwang')
    miaomiao = Cat('miaomiao', 120)

    while True:
        wangwang.attack(miaomiao)
        if miaomiao.get_blood() <= 0:
            print(wangwang.name, ' is win')
            break
        miaomiao.attack(wangwang)
        if wangwang.get_blood() <= 0:
            print(miaomiao.name, ' is win')
            break
