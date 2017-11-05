#encoding: utf-8

from django.db import models

import json

from utils import dbutil

class User(object):
    SQL_USER_LOGIN = 'select * from user where username=%s and password=md5(%s)'
    SQL_USER_LIST = 'select id, username, age, tel from user'
    SQL_USER_CREATE = 'insert into user(username, age, tel, password) values (%s, %s, %s, md5(%s))'
    SQL_USER_FIND_BY_NAME = 'select * from user where username=%s'
    SQL_USER_DELETE = 'delete from user where id=%s'
    SQL_USER_FIND_BY_ID = 'select * from user where id=%s'
    SQL_USER_MODIFY = 'update user set username=%s, age=%s, tel=%s where id=%s'

    def __init__(self, id=None, username='', age=0, tel='', password=''):
        self.id = id
        self.username = username
        self.age = age
        self.tel = tel
        self.password = password

    @classmethod
    def get_by_username_password(cls, username, password):
        line = dbutil.execute_fetch(cls.SQL_USER_LOGIN, (username, password), True)
        return User(**line) if line else None

    @classmethod
    def all(cls):
        lines = dbutil.execute_fetch(cls.SQL_USER_LIST)
        return [User(**line) for line in lines]

    @classmethod
    def get_by_username(cls, username):
        line = dbutil.execute_fetch(cls.SQL_USER_FIND_BY_NAME, (username, ), True)
        return User(**line) if line else None


    def validate_add(self):
        if len(self.username) < 0 or len(self.username) > 8:
            return False, '用户名必须在0到8个字符之间'

        if not(self.age.isdigit() and int(self.age) > 0 and int(self.age) < 100):
            return False, '年龄必须是1到100的整数'

        user = self.get_by_username(self.username)
        if user:
            return False, '添加用户失败, 失败原因: 用户名已存在'
        return True, ''


    def validate_modify(self):
        user = self.get_by_username(self.username)
        if user and user.id != int(self.id):
            return False, '用户名已存在'

        if not(self.age.isdigit() and int(self.age) > 0 and int(self.age) < 100):
            return False, '年龄必须是1到100的整数'

        return True, ''


    def save(self):
        args = (self.username, self.age, self.tel, self.password)
        dbutil.execute_commit(self.SQL_USER_CREATE, args)


    def modify(self):
        args = (self.username, self.age, self.tel, self.id)
        dbutil.execute_commit(self.SQL_USER_MODIFY, args)

    @classmethod
    def delete_by_id(cls, id):
        dbutil.execute_commit(cls.SQL_USER_DELETE, (id,))

    @classmethod
    def get_by_id(cls, id):
        line = dbutil.execute_fetch(cls.SQL_USER_FIND_BY_ID, (id, ), True)
        return User(**line) if line else None

    def delete(self):
        dbutil.execute_commit(self.SQL_USER_DELETE, (self.id,))


    def as_dict(self):
        return {'id' : self.id, 'username' : self.username, 'age' : self.age, 'tel' : self.tel}

    def __str__(self):
        return json.dumps(self.as_dict())



class User2(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=512)
    age = models.IntegerField()
    tel = models.CharField(max_length=13)

    def __str__(self):
        return json.dumps(self.as_dict())

    def as_dict(self):
        return {"id" : self.id, "username" : self.username, "password" : self.password, "age" : self.age, "tel" : self.tel}
