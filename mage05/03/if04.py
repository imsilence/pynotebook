#encoding: utf-8

year = input('please input a year:')

if year.isdigit():
    year = int(year)

    if year % 4 == 0 and year % 100 != 0:
        print('闰年')
    elif year % 400 == 0:
        print('闰年')
    else:
        print('不是闰年')
else:
    print('你输入的数据有误!')
