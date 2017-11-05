#encoding: utf-8

'''
1. 定义list用来存储数据
    users = []
    [(name, age, tel)]
2. while True:

3. 让用户输入: input find/list/add/delete/update/exit

4. if
    add
        input(name)
        input(age)
        input(tel)
        检查用户名是否存在 如果不存在则append users(name, age, tel)
                         提示用户已经存在
    delete
        input(name)
        检查用户名是否存在 如果不存在则提示用户不存在
                         删除 del, pop


    update
        input(name)
        input(age)
        input(tel)
        检查用户名是否存在 如果不存在提示用户不存在
                         提示用户已经存在update  [] = (name, age, tel)

    find
        input(name)
        遍历users, 比较名称是否相等
                         相等打印user信息
    list
        遍历users, 打印user信息
    exit
        break

'''

users = []
user_info_tpl = '|{0:>20}|{1:>5}|{2:>20}|'
user_info_header = user_info_tpl.format('name', 'age', 'telephone')
while True:
    action = input('please input(find/list/add/delete/update/exit):')
    if action == 'add':
        #增加用户
        name = input('请输入用户名:')
        age = input('请输入年龄:')
        tel = input('请输入电话号码:')
        is_exists = False
        for user in users:
            if name == user[0]:
                print('添加用户失败, 失败原因: 用户名已存在')
                is_exists = True
                break

        if not is_exists:
            users.append((name, age, tel))
            print('添加用户成功')
        #print(users)

    elif action == 'delete':
        #删除用户
        name = input('请输入你要删除的用户名:')
        is_exists = False
        for user in users:
        #for i in range(len(users))
            if name == user[0]:
            #if name == users[i][0]:
                is_exists = True
                users.remove(user)
                #del users[i]
                #users.pop(i)
                print('删除用户成功')
                break

        if not is_exists:
            print('删除用户失败, 失败原因: 用户名不存在')
        #print(users)
    elif action == 'update':
        # 更改用户
        name = input('请输入用户名:')
        age = input('请输入年龄:')
        tel = input('请输入电话号码:')
        is_exists = False
        for user in users:
            if name == user[0]:
                users.remove(user)
                is_exists = True
                break

        if is_exists:
            users.append((name, age, tel))
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
            if name == user[0]:
                print(user_info_tpl.format(user[0], user[1], user[2]))
                is_exists = True

        if not is_exists:
            print('没有该用户信息')

    elif action == 'list':
        #罗列所有用户
        print(user_info_header)
        for user in users:
            print(user_info_tpl.format(user[0], user[1], user[2]))

    elif action == 'exit':
        #退出程序
        break
    else:
        print('命令错误')
