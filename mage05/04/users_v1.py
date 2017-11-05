#encoding: utf-8

'''
1. 每一个用户存储信息修改为字典
[{name : xxx, age : xxxx, tel: xxx}, {}]
2. 用户输入了三次，修改为一次，使用:分隔用户信息
3. 查找的时候使用包含关系，name包含查找的字符串
'''

users = []
user_info_tpl = '|{0:>20}|{1:>5}|{2:>20}|'
user_info_header = user_info_tpl.format('name', 'age', 'telephone')
while True:
    action = input('please input(find/list/add/delete/update/exit):')
    if action == 'add':
        #增加用户
        user_txt = input('请输入用户信息(用户名:年龄:电话):')
        name, age, tel = user_txt.split(':')
        is_exists = False
        for user in users:
            if name == user['name']:
                print('添加用户失败, 失败原因: 用户名已存在')
                is_exists = True
                break

        if not is_exists:
            users.append({'name' : name, 'age' : age, 'tel' : tel})
            print('添加用户成功')
        #print(users)

    elif action == 'delete':
        #删除用户
        name = input('请输入你要删除的用户名:')
        is_exists = False
        for user in users:
            if name == user['name']:
                is_exists = True
                users.remove(user)
                print('删除用户成功')
                break

        if not is_exists:
            print('删除用户失败, 失败原因: 用户名不存在')
        #print(users)
    elif action == 'update':
        # 更改用户
        user_txt = input('请输入用户信息(用户名:年龄:电话):')
        name, age, tel = user_txt.split(':')
        is_exists = False
        for user in users:
            if name == user['name']:
                users.remove(user)
                is_exists = True
                break

        if is_exists:
            users.append({'name' : name, 'age' : age, 'tel' : tel})
            print('更新用户成功')
            #print(users)
        else:
            print('更新用户失败, 错误原因: 用户名不存在')
    elif action == 'find':
        # 查找用户
        name = input('请输入你要查询的用户名:')
        is_exists = False
        print(user_info_header)
        for user in users:
            if user['name'].find(name) != -1:
                print(user_info_tpl.format(user['name'], user['age'], user['tel']))
                is_exists = True

        if not is_exists:
            print('没有该用户信息')

    elif action == 'list':
        #罗列所有用户
        print(user_info_header)
        for user in users:
            print(user_info_tpl.format(user['name'], user['age'], user['tel']))

    elif action == 'exit':
        #退出程序
        break
    else:
        print('命令错误')
