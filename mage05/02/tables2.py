#encoding: utf-8

'''
1 * 1 = 1  1 * 2 = 2                1 * 9 = 9   1 * (1 - 9)
2 * 1 = 2  2 * 2 = 4                2 * 9 = 18  2 * (1 - 9)
...
9 * 1 = 9                           9 * 9 = 81  9 * (1 - 9)
'''

for row in range(1, 10):
    for col in range(1, row + 1):
        print(row, '*', col, '=', row * col, end='\t')
    print()
