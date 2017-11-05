#encoding: utf-8

article = 'I was not delivered unto this world in defeat, nor does failure course in my veins. I am not a sheep waiting to be prodded by my shepherd. I am a lion and I refuse to talk, to walk, to sleep with the sheep. I will hear not those who weep and complain, for their disease is contagious. Let them join the sheep. The slaughterhouse of failure is not my destiny.'

stat_dict = {}

for ch in article:
    if not ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
        continue

    stat_dict[ch] = stat_dict.setdefault(ch, 0) + 1

print(stat_dict)

nums = list(stat_dict.items())
print(nums)

#冒泡排序
# nums = [6, 4, 5, 3, 2]
# nums = [('a', 6), ('b', 4), ('c', 5), ('d', 3), ('e', 2)]
for i in range(len(nums) - 1):
    for j in range(len(nums) - 1 - i):
        if nums[j][1] > nums[j + 1][1]:
            temp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = temp

print nums
print nums[-1:-11:-1]
