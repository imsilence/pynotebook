#encoding: utf-8

import json

from utils import dbutil

SQL_USER_LOGIN = 'select id, username, age, tel from user where username=%s and password=md5(%s)'
SQL_USER_LIST = 'select id, username, age, tel from user'
SQL_USER_DELETE = 'delete from user where id=%s'
SQL_USER_FIND_BY_NAME = 'select * from user where username=%s'
SQL_USER_CREATE = 'insert into user(username, age, tel, password) values (%s, %s, %s, md5(%s))'
SQL_USER_FIND_BY_ID = 'select * from user where id=%s'
SQL_USER_MODIFY = 'update user set username=%s, age=%s, tel=%s where id=%s'


def validate_login(name, password):
    return dbutil.execute_fetch(SQL_USER_LOGIN, (name, password), True)

def get_users():
    return dbutil.execute_fetch(SQL_USER_LIST)


def validate_add_user(name, age, tel, password):
    if len(name) < 0 or len(name) > 8:
        return False, '用户名必须在0到8个字符之间'

    if not(age.isdigit() and int(age) > 0 and int(age) < 100):
        return False, '年龄必须是1到100的整数'

    #从数据库中根据名称查询，如果查询到就名字重复

    user = get_user_by_username(name)
    if user:
        return False, '添加用户失败, 失败原因: 用户名已存在'

    return True, ''


def get_user_by_username(username):
    return dbutil.execute_fetch(SQL_USER_FIND_BY_NAME, (username, ), True)


def add_user(name, age, tel, password):
    dbutil.execute_commit(SQL_USER_CREATE, (name, age, tel, password))


def delete_user(uid):
    dbutil.execute_commit(SQL_USER_DELETE, (uid,))


def get_user_by_id(uid):
    return dbutil.execute_fetch(SQL_USER_FIND_BY_ID, (uid, ), True)


def validate_modify_user(uid, name, age, tel):
    user = get_user_by_id(uid)
    if user is None:
        return False, '用户不存在'

    user = get_user_by_username(name)
    if user and user['id'] != int(uid):
        return False, '用户名已存在'

    if not(age.isdigit() and int(age) > 0 and int(age) < 100):
        return False, '年龄必须是1到100的整数'

    return True, ''


def modify_user(uid, name, age, tel):
    dbutil.execute_commit(SQL_USER_MODIFY, (name, age, tel, uid))
