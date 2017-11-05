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


    @classmethod
    def gen_validkey(cls):
        m = hashlib.md5()
        m.update(os.urandom(32))
        return m.hexdigest()
