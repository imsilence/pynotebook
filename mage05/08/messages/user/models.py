#encoding: utf-8

import json


import MySQLdb
from MySQLdb.cursors import DictCursor

HOST = '127.0.0.1'
PORT = 3306
DB = 'kk2'
USER = 'root'
PASSWD = '881019'
CHARSET = 'utf8'

SQL_USER_LOGIN = 'select id, username, age, tel from user where username=%s and password=%s'
SQL_USER_LIST = 'select id, username, age, tel from user'
SQL_USER_DELETE = 'delete from user where id=%s'

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

user_info_tpl = '|{0:>20}|{1:>5}|{2:>20}|{3:>20}|'
user_info_header = user_info_tpl.format('name', 'age', 'telephone', 'password')

def load_users(path):
    # users = {}
    fhandler = open(path, 'rt')
    # for line in fhandler:
    #     name, age, tel, password = line.strip().split(':')
    #     users[name] = {'name' : name, 'age' : age, 'tel' : tel, 'password' : password}
    users = json.loads(fhandler.read())
    fhandler.close()
    return users

def dump_users(path, users):
    fhandler = open(path, 'wt')
    # for user in users.values():
    #     fhandler.write('{0}:{1}:{2}:{3}\n'.format(user['name'], user['age'], user['tel'], user['password']))
    fhandler.write(json.dumps(users))
    fhandler.close()


def validate_login(name, password):
    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor(DictCursor)
    cur.execute(SQL_USER_LOGIN, (name, password))
    line = cur.fetchone()
    cur.close()
    conn.close()
    print(line)
    return line

def get_users():
    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor(DictCursor)
    cur.execute(SQL_USER_LIST)
    rt_list = cur.fetchall()
    cur.close()
    conn.close()
    print(rt_list)
    return rt_list


'''
return True/False, ''
'''
def validate_add_user(name, age, tel, password):
    if len(name) < 0 or len(name) > 8:
        return False, '用户名必须在0到8个字符之间'

    if not(age.isdigit() and int(age) > 0 and int(age) < 100):
        return False, '年龄必须是1到100的整数'

    users = load_users(path)
    if name in users:
        return False, '添加用户失败, 失败原因: 用户名已存在'

    return True, ''


def add_user(name, age, tel, password):
    users = load_users(path)
    users[name] = {'name' : name, 'age' : age, 'tel' : tel, 'password' : password}
    dump_users(path, users)


def input_add_user():
    user_txt = input('请输入用户信息(用户名:年龄:电话:密码):')
    name, age, tel, password = user_txt.split(':')
    return name, age, tel, password


def input_delete_user():
    return input('请输入你要删除的用户名:')


def validate_delete_user(name, users):
    user = users.get(name)
    if user:
        return True, ''
    else:
        return False, '删除用户失败, 失败原因: 用户名不存在'


def delete_user(uid):
    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_USER_DELETE, (uid,))
    conn.commit()
    cur.close()
    conn.close()

def get_user_by_name(name):
    users = load_users(path)
    return users.get(name, {})

def input_modify_user():
    user_txt = input('请输入用户信息(用户名:年龄:电话:密码):')
    name, age, tel, password = user_txt.split(':')
    return name, age, tel, password


def validate_modify_user(name, age, tel, password):
    users = load_users(path)
    if name not in users:
        return False, '更新用户失败, 错误原因: 用户名不存在'

    if len(password) < 8:
        return False, '密码长度必须大于等于8个字符'

    if not(age.isdigit() and int(age) > 0 and int(age) < 100):
        return False, '年龄必须是1到100的整数'

    return True, ''


def modify_user(name, age, tel, password):
    users = load_users(path)
    users[name] = {'name' : name, 'age' : age, 'tel' : tel, 'password' : password}
    dump_users(path, users)

def find_user(name, users):
    rt_list = []
    for user in users.values():
        if user['name'].find(name) != -1:
            rt_list.append(user)

    return rt_list

def list_user(field, users):
    user_list = list(users.values())
    return sorted(user_list, key=lambda x: x.get(field))


def main():
    users = load_users(path)

    is_valid = False
    #用户认证，最多3次，用户输入用户名和电话
    for i in range(3):
        name = input('请输入用户名:')
        password = input('请输入密码:')
        if validate_login(name, password, users):
            is_valid = True
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
                name, age, tel, password = input_add_user()
                rt_status, rt_reason = validate_add_user(name, age, tel, password, users)
                if rt_status:
                    add_user(name, age, tel, password, users)
                else:
                    print(rt_reason)
            elif action == 'delete':
                #删除用户
                name = input_delete_user()
                rt_status, rt_reason = validate_delete_user(name, users)
                if rt_status:
                    delete_user(name, users)
                    print('删除用户成功')
                else:
                    print(rt_reason)
            elif action == 'update':
                # 更改用户
                name, age, tel, password = input_modify_user()
                rt_status, rt_reason = validate_modify_user(name, age, tel, password, users)
                if rt_status:
                    modify_user(name, age, tel, password, users)
                    print('更新用户成功')
                else:
                    print(rt_reason)

            elif action == 'find':
                # 查找用户
                name = input('请输入你要查询的用户名:')
                rt_list = find_user(name, users)
                if rt_list:
                    print(user_info_header)
                    for user in rt_list:
                        print(user_info_tpl.format(user['name'], user['age'], user['tel'], '*' * len(user['password'])))
                else:
                    print('没有该用户信息')

            elif action == 'list':
                #罗列所有用户
                field = input('请输入排序的列(name, age, tel):')
                print(user_info_header)

                for user in list_user(field, users):
                    print(user_info_tpl.format(user['name'], user['age'], user['tel'], '*' * len(user['password'])))

            elif action == 'exit':
                #退出程序
                dump_users(path, users)
                break
            else:
                print('命令错误')



if __name__ == '__main__':
    main()
