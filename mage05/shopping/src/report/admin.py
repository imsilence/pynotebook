from django.contrib import admin

# Register your models here.

from .models import SaleReport

class SaleReportAdmin(admin.ModelAdmin):
    list_display = ['report_time', 'total_price']

admin.site.register(SaleReport, SaleReportAdmin)