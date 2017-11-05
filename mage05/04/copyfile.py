#encoding: utf-8


src = '/bin/ls'
dst = 'ls'

fhandler = open(src, 'rb')
cxt = fhandler.read()
fhandler.close()

fhandler = open(dst, 'wb')
fhandler.write(cxt)
fhandler.close()
