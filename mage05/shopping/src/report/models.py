from django.db import models

# Create your models here.
class ActiveUserReport(models.Model):
    report_time = models.DateField(auto_now_add=True)
    num = models.IntegerField(default=0)


    class Meta:
        verbose_name = '活跃用户'
        verbose_name_plural = '活跃用户'

class SaleReport(models.Model):
    report_time = models.DateField(auto_now_add=True, unique=True)
    total_price = models.FloatField(default=0)

    class Meta:
        verbose_name = '每天销售额'
        verbose_name_plural = '每天销售额'