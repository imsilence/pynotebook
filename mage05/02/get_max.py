#encoding: utf-8

'''
nums=[6, 11, 7, 9, 4, 2, 1]
1.从nums中拿到第一个数放到变量hand中
2.从nums第二个元素开始比较，如果比hand中大，则重新赋值

nums=[6, 11, 7, 9, 4, 2, 1]
0.hand手里没有None
2.从nums第一个元素开始比较，如果比hand是None或者比hand中大，则重新赋值

None => 什么都没有
判断变量是否是None, hand is None
'''
nums=[6, 11, 7, 9, 4, 2, 1]

hand = None

for num in nums:
    if hand is None or num > hand:
        hand = num

print(hand)
