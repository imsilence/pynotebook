from django.core.management.base import BaseCommand

from django.db import connection
from django.utils import timezone
from datetime import timedelta

from report.models import SaleReport

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        start = (timedelta(days=-1) + timezone.now()).strftime('%Y-%m-%d')
        end = timezone.now().strftime('%Y-%m-%d')
        cursor = connection.cursor()
        sql = '''
                SELECT sum(price) FROM goods_order
                WHERE status=%s and update_time >= %s and update_time < %s
        '''

        cursor.execute(sql, (4, start, end))
        line = cursor.fetchone()
        total_price = line[0] if line and line[0] else 0

        SaleReport.objects.create(total_price=total_price)
        cursor.close()