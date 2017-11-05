#encoding: utf-8

import time
import json

from django.core.management.base import BaseCommand

from django_redis import get_redis_connection


from agent.models import Client, Resource

class Command(BaseCommand):

    def handle(self, *args, **options):
        _connection = get_redis_connection()
        while True:
            _msg = _connection.rpop('cmdb:api:queue:client')
            if not _msg:
                time.sleep(3)
                continue

            _msg = json.loads(_msg.decode())
            Client.register(_msg.get('uuid'), **_msg.get('body'))
