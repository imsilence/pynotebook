from django.db import models

# Create your models here.

class DaySaleReport(models.Model):
    report_time = models.DateField(unique=True)
    total_price = models.FloatField(default=0)

    class Meta:
        verbose_name = '每天营业额'
        verbose_name_plural = '每天营业额'