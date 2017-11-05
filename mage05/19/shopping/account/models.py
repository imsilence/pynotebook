from django.db import models

from django.contrib.auth.models import User
import os
import hashlib


class UserExt(models.Model):
    user = models.OneToOneField(User)
    realname = models.CharField("真实名称", max_length=64)
    birthday = models.DateField("生日")
    nickname = models.CharField("昵称", max_length=64)
    avatar = models.CharField("头像", max_length=256)
    telephone = models.CharField("电话号码", max_length=32)
    score = models.IntegerField("用户积分", default=0)
    logintime = models.DateTimeField("登陆时间")
    validkey = models.CharField("验证key", max_length=256)
    status = models.IntegerField("状态", default=0)
    sex = models.IntegerField("性别", default=1)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'


    @classmethod
    def gen_validkey(cls):
        m = hashlib.md5()
        m.update(os.urandom(32))
        return m.hexdigest()

    def nickname_text(self):
        return self.user.username if self.nickname == '' else self.nickname

    def __str__(self):
        return self.user.username


class UserAddress(models.Model):
    STATUS_DELETE = 0
    STATUS_NORMAL = 1

    user = models.ForeignKey(User)
    name = models.CharField("收货人姓名", max_length=64)
    addr = models.CharField("收获地址", max_length=256)
    telephone = models.CharField("联系方式", max_length=32)
    fixedphone = models.CharField("固定电话", max_length=32)
    email = models.EmailField("邮箱")
    status = models.IntegerField("状态", default=1)

    class Meta:
        verbose_name = '用户收获地址信息'
        verbose_name_plural = '用户收获地址信息'