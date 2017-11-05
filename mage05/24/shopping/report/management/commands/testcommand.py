#encoding: utf-8
from django.core.management.base import BaseCommand

from django.db import connection
from django.utils import timezone
from datetime import timedelta
from report.models import DaySaleReport

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        now = timezone.now()
        start = (now - timedelta(days=1)).strftime('%Y-%m-%d')
        end = now.strftime('%Y-%m-%d')

        cursor = connection.cursor()
        
        sql = '''
            select sum(price) from goods_order
            where
            update_time between %s and %s 
            and status=%s
        '''
       
        cursor.execute(sql, (start, end, 2))
        line = cursor.fetchone()
        total_price = line[0] if line[0] else 0

        one = DaySaleReport(report_time=start, total_price=total_price)
        one.save()
        #one = DaySaleReport.objects.create(report_time=start, total_price=total_price)
        cursor.close()