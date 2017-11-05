#encoding: utf-8

BUFFERSIZE = 1024 #1kB
# BUFFERSIZE = 1024 * 1024 #1MB
# BUFFERSIZE = 10 * 1024 * 1024 #10MB


src = '/bin/ls'
dst = 'ls'


src_fhandler = open(src, 'rb')
dst_fhandler = open(dst, 'wb')

while True:
    cxt = src_fhandler.read(BUFFERSIZE)
    if b'' == cxt:
        break
    dst_fhandler.write(cxt)

src_fhandler.close()
dst_fhandler.close()
