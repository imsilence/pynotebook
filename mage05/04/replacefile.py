#encoding: utf-8

fhandler = open('src.txt', 'rt')
cxt = fhandler.read()
fhandler.close()

cxt = cxt.replace('kk', 'ada')

fhandler = open('src.txt', 'wt')
fhandler.write(cxt)
fhandler.close()
