#encoding: utf-8

input_sum = 0
input_count = 0

input_text = input('请输入数字或exit:')

while input_text != 'exit':
    input_sum += float(input_text)
    input_count += 1
    input_text = input('请输入数字或exit:')

print('总和:', input_sum)

if input_count != 0:
    print('平均数:', input_sum / input_count)
else:
    print('平均数:', 0)
