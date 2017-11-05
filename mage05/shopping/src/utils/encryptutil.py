#encoding: utf-8

import os
import hashlib

def md5(txt):
    m = hashlib.md5()
    btxt = txt if isinstance(txt, bytes) else str(txt).encode()
    m.update(btxt)
    return m.hexdigest()



def random():
    return md5(os.urandom(32))
