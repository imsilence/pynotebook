#encoding: utf-8

'''
插入排序
nums = [6, 4, 3, 5, 7, 2, 10, 9]
'''

'''
第一次
nums = [6, 4, 3, 5, 7, 2, 10, 9]
=> nums = [4, 6, 3, 5, 7, 2, 10, 9]
第二次(i)
=> nums = [4, 3, 6, 5, 7, 2, 10, 9] j =2
=> nums = [3, 4,  6, 5, 7, 2, 10, 9] j = 1
j = 0

结束条件，前面比后面小，或者索引为0(前面没有元素)
'''
nums = [6, 4, 3, 5, 7, 2, 10, 9]
for i in range(1, len(nums)):
    for j in range(i, 0, -1):
        if nums[j - 1] > nums[j]:
            temp = nums[j - 1]
            nums[j - 1] = nums[j]
            nums[j] = temp
        else:
            break

print(nums)
