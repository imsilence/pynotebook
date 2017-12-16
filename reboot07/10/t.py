class T(object):
    incr = 0
    __test = 0
    def __init__(self, name, pwd):
        T.incr += 1
        T.__test += 1
        self.__name = name
        self.__pwd = pwd
    
    def getName(self):
        return self.__name
    
    def __gpwd(self):
        return self.__pwd
    
    def getPwd(self):
        return self.__gpwd()
    
    @staticmethod
    def test():
        print 'test'
    
    @classmethod
    def testcls(cls):
        print cls.incr
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def pwd(self):
        return self.__pwd

    @pwd.setter
    def pwd(self, pwd):
        self.__pwd = pwd
        
if __name__ == '__main__':
    t = T('kk', '123')
    t2 = T('silence', 'test')
    print dir(t)
    print t.incr
    print t._T__test
    print t2.incr
    print t2._T__test
    print T.incr
    print T._T__test
    #print T.test()
    print t.test()
    print t2.test()
    
    print t.pwd
    print t.name
    
    t.name = 'silence'
    t.pwd = '123456'
    print t.name
    print t.pwd