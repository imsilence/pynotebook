#encoding: utf-8

import hashlib

SIZE = 1024 * 1024

def md5_str(string):
    if not isinstance(string, bytes):
        string = str(string).encode()

    md5 = hashlib.md5()
    md5.update(string)
    return md5.hexdigest()


def md5_file(path):
    md5 = hashlib.md5()

    fhandler = open(path, 'rb')
    while True:
        cxt = fhandler.read(SIZE)

        if not cxt:
            break

        md5.update(cxt)

    fhandler.close()
    return md5.hexdigest()



if __name__ == '__main__':
    print(md5_str(1))
    print(md5_str('kk'))
    print(md5_str(b'huangdou'))

    print(md5_file('./kk'))
    print(md5_file('./kk1'))



