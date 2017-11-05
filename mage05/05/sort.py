#encoding: utf-8


def bubble_sort(l, key):
    for j in range(len(l) - 1):
        for i in range(len(l) - 1 - j):
            if key(l[i]) > key(l[i + 1]):
                l[i], l[i + 1] = l[i + 1], l[i]

def key(x):
    return x

nums = [6, 4, 5, 2, 3, 1]
#bubble_sort(nums, key)
nums.sort()
print(nums)


stat = {'a' : 6, 'b' : 10, 'c' : 2, 'e' : 1}
stat_list = list(stat.items())
#[('a', 6), ('b', 10), ('c', 2), ('e', 1))]

def key2(x):
    return x[1]

add = lambda *args: sum(args)

#bubble_sort(stat_list, key2)
stat_list.sort(key=lambda x: x[1])
print(stat_list)
