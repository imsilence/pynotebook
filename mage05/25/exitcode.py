#encoding: utf-8

import sys

if __name__ == '__main__':
    code = 0
    if len(sys.argv) > 1:
        code = int(sys.argv[1])

    print('exitcode')
    sys.exit(code)
    print('over')