#encoding: utf-8

import json
from django.db import models

from django.contrib.auth.models import User



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
    sex = models.BooleanField(default=1)


class UserAddress(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=64)
    site = models.CharField(max_length=256)
    telephone = models.CharField(max_length=32)
    fixedphone = models.CharField(max_length=32)
    email = models.EmailField()
    status = models.IntegerField(default=0)


