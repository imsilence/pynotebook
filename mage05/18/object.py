#encoding: utf-8

#功能扩展, 不能进行实例化
class AMixin(object):
    def test1(self):
        print('AAAAAAAAAAAA')
        super().test1()
        print('-AAAAAAAAAAAAA')
        print('A:test1')

    def test2(self):
        print('A:test2')


class B(object):
    def test1(self):
        print('B:test1')

    def test3(self):
        print('B:test3')
        

class C3(AMixin, B):
    
    def test1(self):
        print('C3:test1')
        super().test1()


c3 = C3()
c3.test1() #调用谁的呢?
c3.test2()
c3.test3()