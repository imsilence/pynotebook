from django.db import models

from django.contrib.auth.models import User
import os
import hashlib


class UserExt(models.Model):
    user = models.OneToOneField(User)
    realname = models.CharField(max_length=64)
    birthday = models.DateField()
    nickname = models.CharField(max_length=64)
    avatar = models.CharField(max_length=256)
    telephone = models.CharField(max_length=32)
    score = models.IntegerField(default=0)
    logintime = models.DateTimeField()
    validkey = models.CharField(max_length=256)
    status = models.IntegerField(default=0)
    sex = models.IntegerField(default=1)


    @classmethod
    def gen_validkey(cls):
        m = hashlib.md5()
        m.update(os.urandom(32))
        return m.hexdigest()

    def nickname_text(self):
        return self.user.username if self.nickname == '' else self.nickname


class UserAddress(models.Model):
    STATUS_DELETE = 0
    STATUS_NORMAL = 1

    user = models.ForeignKey(User)
    name = models.CharField(max_length=64)
    addr = models.CharField(max_length=256)
    telephone = models.CharField(max_length=32)
    fixedphone = models.CharField(max_length=32)
    email = models.EmailField()
    status = models.IntegerField(default=1)