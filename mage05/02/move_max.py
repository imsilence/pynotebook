#encoding: utf-8
'''
nums=[6, 11, 7, 9, 4, 2, 1]
1. 比较多少次 n - 1
2. 依次两两比较
for i in range(n - 1):
    nums[i] , nums[i + 1] 前大后小， if
        交换
3. 如何交换
a , b
temp = a
a = b
b = temp
'''
nums=[6, 11, 7, 9, 4, 2, 1]
for j in range(len(nums) - 1):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            temp = nums[i]
            nums[i] = nums[i + 1]
            nums[i + 1] = temp
    print(nums)

print(nums)

# #nums = [6, 7, 9, 4, 2, 1, 11]
# for i in range(len(nums) - 1):
#     if nums[i] > nums[i + 1]:
#         temp = nums[i]
#         nums[i] = nums[i + 1]
#         nums[i + 1] = temp
# print(nums)
