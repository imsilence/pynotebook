#encoding: utf-8
import time
import random

from django.db import models
from django.contrib.auth import get_user_model

from .storage import FileStorage
from account.models import UserAddress


User = get_user_model()

class Category(models.Model):
    name = models.CharField("名称", max_length=64)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    status = models.IntegerField('状态', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类1'
        verbose_name_plural = '分类2'

def upload_to_goods_image(instance, filename):
    return 'goods/{prefix}_{suffix}_{random}.{fsuffix}'.format(prefix='goods', suffix=int(time.time() * 1000), random=random.randint(0, 1000), fsuffix=filename.split('.')[-1])

class Goods(models.Model):
    category = models.ForeignKey(Category)

    name = models.CharField(max_length=64)
    price = models.FloatField()
    #img = models.ImageField(upload_to=upload_to_goods_image)
    img = models.ImageField(upload_to='goods/', storage=FileStorage())
    create_time = models.DateTimeField(auto_now_add=True)
    store = models.IntegerField()
    desc = models.TextField()
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'

    def __str__(self):
        return self.name

class GoodsExt(models.Model):
    goods = models.ForeignKey(Goods)
    key = models.CharField(max_length=64)
    value = models.TextField()
    status = models.IntegerField(default=0)


    def __str__(self):
        return '{key}:{value}'.format(key=self.key, value=self.value)


class ShoppingCar(models.Model):
    user = models.ForeignKey(User)
    goods = models.ForeignKey(Goods)
    num = models.IntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(User)
    price = models.FloatField(default=0)
    user_address = models.ForeignKey(UserAddress)
    create_time = models.DateTimeField(auto_now_add=True)
    remark = models.TextField()
    pay_type = models.IntegerField(default=1)
    pay_status = models.IntegerField(default=1)
    status = models.IntegerField(default=1)
    update_time = models.DateTimeField(auto_now=True)
    invoice_type = models.IntegerField(default=1)
    invoice_title = models.CharField(max_length=256)

    STATUS_TEXT = {1:'正在发货', 2: '已发货', 3: '已收货', 4: '已取消'}

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = '订单'


    def status_text(self):
        return self.STATUS_TEXT.get(self.status, '')

class GoodsBuied(models.Model):
    order = models.ForeignKey(Order)
    goods = models.ForeignKey(Goods)
    num = models.IntegerField(default=1)
    price = models.FloatField(default=0)

    def total_price(self):
        return self.num  * self.price
        
    

class OrderLog(models.Model):
    order = models.ForeignKey(Order)
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField()
    remark = models.TextField()