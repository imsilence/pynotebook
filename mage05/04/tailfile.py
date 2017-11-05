#encoding: utf-8

'''
tail -n 0 -f path
1. 打开文件，将文件指针移动到文件末尾（相对位置0， 1， 2）
    二进制方式读取文件
2. readline获取文件内容，有内容，打印出来，如果没有内容让程序等一段时间(time.sleep)

'''

import time

src = '/tmp/log.txt'

fhandler = open(src, 'rb')
fhandler.seek(0, 2)
while True:
    line = fhandler.readline()
    if line != b'':
        print(line.decode(), end='')
    else:
        time.sleep(3)
