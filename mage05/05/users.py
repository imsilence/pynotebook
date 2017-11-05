#encoding: utf-8

'''
1. 每一个用户存储信息修改为字典
{
    xx : {name : xxx, age : xxxx, tel: xxx, 'password' : 'xxx'},
    xxx: {}
}
2. 用户输入了三次，修改为一次，使用:分隔用户信息
3. 查找的时候使用包含关系，name包含查找的字符串
'''

path = 'users.txt'

users = {}
user_info_tpl = '|{0:>20}|{1:>5}|{2:>20}|{3:>20}|'
user_info_header = user_info_tpl.format('name', 'age', 'telephone', 'password')

fhandler = open(path, 'rt')
for line in fhandler:
    name, age, tel, password = line.strip().split(':')
    users[name] = {'name' : name, 'age' : age, 'tel' : tel, 'password' : password}
fhandler.close()

is_valid = False
#用户认证，最多3次，用户输入用户名和电话
for i in range(3):
    name = input('请输入用户名:')
    password = input('请输入密码:')
    #认证
    for user in users.values():
        if user['name'] == name and user['password'] == password:
            is_valid = True
            break

    if is_valid:
        break
    else:
        print('认证失败, 请重试')

if not is_valid:
    print('已超过最大认证次数，程序退出')
else:
    while True:
        action = input('please input(find/list/add/delete/update/exit):')
        if action == 'add':
            #增加用户
            user_txt = input('请输入用户信息(用户名:年龄:电话:密码):')
            name, age, tel, password = user_txt.split(':')
            if name in users:
                print('添加用户失败, 失败原因: 用户名已存在')
            else:
                users[name] = {'name' : name, 'age' : age, 'tel' : tel, 'password' : password}
        elif action == 'delete':
            #删除用户
            name = input('请输入你要删除的用户名:')
            if users.pop(name, None):
                print('删除用户成功')
            else:
                print('删除用户失败, 失败原因: 用户名不存在')
        elif action == 'update':
            # 更改用户
            user_txt = input('请输入用户信息(用户名:年龄:电话:密码):')
            name, age, tel, password = user_txt.split(':')
            if name in users:
                users[name] = {'name' : name, 'age' : age, 'tel' : tel, 'password' : password}
                print('更新用户成功')
            else:
                print('更新用户失败, 错误原因: 用户名不存在')

        elif action == 'find':
            # 查找用户
            name = input('请输入你要查询的用户名:')
            is_exists = False
            print(user_info_header)
            for user in users.values():
                if user['name'].find(name) != -1:
                    print(user_info_tpl.format(user['name'], user['age'], user['tel'], '*' * len(user['password'])))
                    is_exists = True

            if not is_exists:
                print('没有该用户信息')

        elif action == 'list':
            #罗列所有用户
            field = input('请输入排序的列(name, age, tel):')
            print(user_info_header)
            list_users = list(users.values())

            for j in range(len(list_users) - 1):
                for i in range(len(list_users) - 1):
                    if list_users[i][field] < list_users[i + 1][field]:
                        list_users[i], list_users[i + 1] = list_users[i + 1], list_users[i]

            for user in list_users:
                print(user_info_tpl.format(user['name'], user['age'], user['tel'], '*' * len(user['password'])))

        elif action == 'exit':
            #退出程序
            fhandler = open(path, 'wt')
            for user in users.values():
                fhandler.write('{0}:{1}:{2}:{3}\n'.format(user['name'], user['age'], user['tel'], user['password']))
            fhandler.close()
            break
        else:
            print('命令错误')
