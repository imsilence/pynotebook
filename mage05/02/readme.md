|A and B | A(True)  | A(False)|
|B(True) |  True    |  False  |      
|B(False)|  False   |  False  |


|A or B  | A(True)  | A(False)|
|B(True) |  True    |  True  |      
|B(False)|  True    |  False  |


| not A| A(True) | A(False) |
|      | False   | True     |

if condition_A:
    code_A

if condition_A:
    code_A
else:
    code_else

if condition_A:
    code_A
elif condition_B:
    code_B
elif condition_C:
    code_C
...
elif codition_N:
    code_N
else:
    code_else


while codition:
    code


while True:
    chars = input('please input chars:')
    if chars == 'exit':
        break

nums = [1, 2, 3, 5]
for ele in nums:
    print(ele)


作业
1. 文件名称使用python变量名命名规则
2. while, if, else, elif 后面的表达式可以不使用()包含
3. 变量名先定义再使用（在使用的同一级或者在前N级）
4. 缩进: tab和空格, 不要混用，copy到其他操作系统上会有兼容问题


nums=[6, 11, 7, 9, 4, 2, 1]

1.从nums中拿到第一个数放到变量hand中
2.从nums第二个元素开始比较，如果比hand中大，则重新赋值


nums[0] = 'kk'
nums[1:2] = ['a', 'b']
nums[1:2] = []
