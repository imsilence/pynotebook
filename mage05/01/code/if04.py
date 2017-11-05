#encoding: utf-8

year = input('please input a year:')

year = int(year)

if year % 4 == 0 and year % 100 != 0:
    print('闰年')
elif year % 400 == 0:
    print('闰年')
else:
    print('不是闰年')
