#encoding: utf-8

path = 'kk.txt'

# 打开文件
fhandler = open(path)

cxt = fhandler.read()
print(cxt)

#关闭文件
fhandler.close()
