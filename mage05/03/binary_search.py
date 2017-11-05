#encoding: utf-8

'''
二分查找
'''
nums = [6, 11, 24, 32, 12, 16, 15, 13]
nums.sort()                             #保证list有序

print(nums)
find = input('please input find num:')
find = int(find)

start = 0
end = len(nums) - 1
while True:
    middle = (end + start) // 2   #middle = int((end + start) / 2)
    if find == nums[middle]:
        print('找到了, 索引位置:', middle)
        break
    elif find > nums[middle]:
        #从middle后面找
        start = middle + 1
    else:
        end = middle - 1

    if end < start:
        print('没找到')
        break
