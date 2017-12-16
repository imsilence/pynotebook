#encoding: utf-8

path = 'www_access_20140823.log'

stat_dict = {}


handle = open(path, 'r')

for _line in handle:
    _temp_list = _line.split(' ')
    _client_ip, _url, _status = _temp_list[0], _temp_list[6], _temp_list[8]
    stat_dict.setdefault((_client_ip, _url, _status,), 0)
    stat_dict[(_client_ip, _url, _status,)] += 1

handle.close()

count_stat_dict = {}
for _key, _value in stat_dict.items():
    count_stat_dict.setdefault(_value, [])
    count_stat_dict[_value].append([_key[2], _key[1], (_key[0], _value)])

count_list = count_stat_dict.keys()
for j in range(len(count_list) - 1):
    for i in range(len(count_list) - 1 - j):
        if count_list[i] < count_list[i + 1]:
            count_list[i], count_list[i + 1] = count_list[i + 1], count_list[i]

stat_list = []
for _count in count_list:
    for _item in count_stat_dict.get(_count):
        stat_list.append(str(_item)) 

handle = open('result.txt', 'w')
handle.write('\n'.join(stat_list))
handle.close()

'''
for j in range(len(stat_list) - 1):
    for i in range(len(stat_list) - 1 - j):
        if stat_list[i][2][1] < stat_list[i + 1][2][1]:
            stat_list[i], stat_list[i + 1] = stat_list[i + 1], stat_list[i]

'''