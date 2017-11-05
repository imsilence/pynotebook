#encoding: utf-8

import hashlib

class CryptUtils(object):

    @staticmethod
    def md5(text):
        _md5 = hashlib.md5()
        _md5.update(text.encode())
        return _md5.hexdigest()



CryptUtils.md5('kkk')
CryptUtils.md5('123')
