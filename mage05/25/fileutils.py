#encoding: utf-8

import os

def list_dir(path, suffix=None):
    if not os.path.exists(path):
        return None
    elif os.path.isdir(path):
        names = os.listdir(path)
        for name in names:
            list_dir(os.path.join(path, name), suffix)
    elif suffix is None or path.endswith(suffix):
        print(os.path.abspath(path))


if __name__ == '__main__':
    list_dir('.')
    print('=' * 20)
    list_dir('.', '.txt')