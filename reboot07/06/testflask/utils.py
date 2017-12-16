#encoding: utf-8

def load_static(filename, dirpath='static'):
    return load_file(filename, dirpath)

def load_template(filename, dirpath='templates'):
    return load_file(filename, dirpath)

def load_file(filename, dirpath):
    handle = open('%s/%s' % (dirpath, filename))
    cxt = handle.read()
    handle.close()
    return cxt