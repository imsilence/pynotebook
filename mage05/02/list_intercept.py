
'''
1. 定义list存放结果
result = []
2. 遍历一个list，判断是否在另一个list中，如果在相同元素
3. 放入result之前判断是否在result中，如果不在就放入
'''

nums_1 = [1, 2, 3, 4, 5, 3, 10, 11]
nums_2 = [1, 2, 3, 1, 4, 5, 5, 3, 12, 34]

result = []
for num in nums_1:
    if num in nums_2 and num not in result:
        result.append(num)


print(result)
