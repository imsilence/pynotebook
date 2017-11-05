#encoding: utf-8
import time
from django.db import models

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

