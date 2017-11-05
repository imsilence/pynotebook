from django.contrib import admin

# Register your models here.

from .models import DaySaleReport

class DaySaleReportAdmin(admin.ModelAdmin):
    list_display = ('report_time', 'total_price')


admin.site.register(DaySaleReport, DaySaleReportAdmin)