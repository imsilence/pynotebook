#encoding: utf-8

score = input('please input your score:')

if score.isdigit():
    score = int(score)

    if score >= 90:
        print('优秀')
    elif score >= 80:
        print('良好')
    elif score >= 60:
        print('及格')
    else:
        print('不及格')
else:
    print('你输入的数据有误!')
