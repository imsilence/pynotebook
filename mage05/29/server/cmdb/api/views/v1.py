#encoding: utf-8

import time

from .base import APIView
from agent.models import Client, Resource


class ClientView(APIView):

    def post(self, request, *args, **kwargs):
        _json = self.get_json(request)
        _client, _created = Client.register(kwargs.get('uuid'), **_json)
        return self.response({'created' : _created, 'client': _client.as_dict()})


class HeartbeatView(APIView):

    def post(self, request, *args, **kwargs):
        _json = self.get_json(request)
        Client.heartbeat(kwargs.get('uuid'))
        return self.response({'time' : time.time()})


class ResourceView(APIView):

    def post(self, request, *args, **kwargs):
        _json = self.get_json(request)
        _resource = Resource.create(kwargs.get('uuid'), **_json)
        return self.response(_resource.as_dict())