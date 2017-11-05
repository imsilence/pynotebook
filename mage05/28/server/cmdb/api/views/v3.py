#encoding: utf-8

import time
import json

from django_redis import get_redis_connection

from .base import AuthAPIView as APIView


class ClientView(APIView):

    def post(self, request, *args, **kwargs):
        _connect = get_redis_connection()
        _msg = {'uuid' : kwargs.get('uuid'), 'body' : self.get_json(request), 'time' : time.time()}
        _connect.lpush('cmdb:api:queue:client', json.dumps(_msg))
        return self.response(None)


class HeartbeatView(APIView):

    def post(self, request, *args, **kwargs):
        _connect = get_redis_connection()
        _msg = {'uuid' : kwargs.get('uuid'), 'body' : self.get_json(request), 'time' : time.time()}
        _connect.lpush('cmdb:api:queue:heartbeat', json.dumps(_msg))
        return self.response({'time' : time.time()})


class ResourceView(APIView):

    def post(self, request, *args, **kwargs):
        _connect = get_redis_connection()
        _msg = {'uuid' : kwargs.get('uuid'), 'body' : self.get_json(request), 'time' : time.time()}
        _connect.lpush('cmdb:api:queue:resource', json.dumps(_msg))
        return self.response(None)