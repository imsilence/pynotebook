#encoding: utf-8

path = 'kk.txt'
size = 2

# 打开文件
fhandler = open(path)

while True:
    cxt = fhandler.read(size)
    if cxt == '':
        break
    print(cxt)

#关闭文件
fhandler.close()
