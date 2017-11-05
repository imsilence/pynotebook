
start = -1

pstr = 'abc' * 10
sstr = 'ab'

for i in range(8):
    start = pstr.find(sstr, start + 1)

print(start)



me = {'name' : 'kk', 'age' : 29}
me2 = me.copy()
me2['addr'] = 'beijing'
print(me)
print(me2)


me3 = me
me3['tel'] = 'xx'
print(me)
print(me3)


me_list = []
me_list.append(me)
me_list.append(me)
me_list.append(me)

me['addr'] = "xi'an"
