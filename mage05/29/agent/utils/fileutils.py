#encoding: utf-8

import os

def read_file(path):
    _cxt = ''
    if os.path.isfile(path):
        with open(path, 'rb') as fhandler:
            _cxt = fhandler.read()
            _cxt = _cxt.decode()
    
    return _cxt


def write_file(path, cxt):
    if not isinstance(cxt, bytes):
        cxt = str(cxt).encode()

    with open(path, 'wb') as fhandler:
        fhandler.write(cxt)

    return True