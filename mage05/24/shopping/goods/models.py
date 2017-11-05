#encoding: utf-8
import time
from django.db import models
from django.contrib.auth import get_user_model
from account.models import UserAddress

User = get_user_model()

class Category(models.Model):
    name = models.CharField("名称", max_length=64)
    create_time = models.DateTimeField("添加时间", auto_now_add=True)
    status = models.IntegerField("状态", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "商品分类"
        verbose_name_plural = "商品分类"


def upload_to_goods_img(instance, filename):
    return 'goods/{prefix}_{filename}.{suffix}'.format(prefix='goods', 
                filename=int(time.time() * 1000),
                suffix=filename.split('.')[-1])


class Goods(models.Model):
    category = models.ForeignKey(Category, verbose_name='分类')
    name = models.CharField("名称", max_length=64)
    price = models.FloatField("价格", default=0)
    img = models.ImageField("图片", upload_to=upload_to_goods_img)
    create_time = models.DateTimeField("添加时间")
    store = models.IntegerField("库存", default=0)
    desc = models.TextField("描述")
    status = models.IntegerField("状态", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "商品信息"
        verbose_name_plural = "商品信息"


class GoodsExt(models.Model):
    goods  = models.ForeignKey(Goods)
    key = models.CharField("属性名", max_length=128)
    value = models.TextField("属性值")
    status = models.IntegerField("状态", default=0)

    def __str__(self):
        return "{0}:{1}".format(self.goods.name, self.key)

    class Meta:
        verbose_name = "商品扩展信息"
        verbose_name_plural = "商品扩展信息"



class ShoppingCar(models.Model):
    user = models.ForeignKey(User, verbose_name="用户")
    goods = models.ForeignKey(Goods, verbose_name="商品")
    num = models.IntegerField("商品数量", default=1)

    def __str__(self):
        return "{0}:{1}:{2}".format(self.user.username, self.goods.name, self.num)

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = "购物车"

    def total_price(self):
        return self.goods.price * self.num


class Order(models.Model):
    STATUS_TEXTS = {0 : '正在发货', 1 : '已发货', 2 : '已收货', 3 : '取消'}

    user = models.ForeignKey(User, verbose_name="用户")
    price = models.FloatField("总价格", default=0)
    user_address = models.ForeignKey(UserAddress, verbose_name="收货人")
    create_time = models.DateTimeField("下单时间", auto_now_add=True)
    remark = models.TextField("备注")
    pay_type = models.IntegerField("付款方式", default=0)
    pay_status = models.IntegerField("付款状态", default=0)
    update_time = models.DateTimeField(auto_now=True)
    status = models.IntegerField("状态", default=0)
    invoice_type = models.IntegerField("发票类型", default=0)
    invoice_title = models.CharField("发票抬头", max_length=256)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = "订单"

    def status_text(self):
        return self.STATUS_TEXTS.get(self.status)

    status_text.short_description = '状态'

    def is_normal(self):
        return self.status != 3

    is_normal.short_description = '订单正常'
    is_normal.boolean = True



class GoodsBuied(models.Model):
    order = models.ForeignKey(Order, verbose_name="订单")
    price = models.FloatField("价格", default=0)
    num = models.IntegerField("数量", default=0)
    goods = models.ForeignKey(Goods, verbose_name="商品")


    def total_price(self):
        return self.num * self.price