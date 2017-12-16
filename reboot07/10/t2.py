class T(object):
    def __init__(self):
        print 'T'

    def test(self):
        print 'T test'

class T2(object):
    def __init__(self):
        print 'T2'

    def test(self):
        print 'T2 test'


class TS(T, T2):
    def __init__(self):
        super(TS, self).__init__()
        print 'TS'

    def test(self):
        super(TS, self).test()
        print 'TS test'

class TS2(T, T2):
    def __init__(self):
        T.__init__(self)
        T2.__init__(self)
        print 'TS2'

    def test(self):
        T.test(self)
        T2.test(self)
        print 'TS2 test'

if __name__ == '__main__':
    TS().test()
    TS2().test()