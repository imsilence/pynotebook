#encoding: utf-8

from django.shortcuts import render
from django.views.generic import View, ListView

from django.http import JsonResponse

from .models import Client, Resource

class ClientListView(ListView):
    template_name = 'agent/client.html'
    model = Client


class ResourceView(View):
    SIZE = 180

    def get(self, request, *args, **kwargs):
        _uuid = kwargs.get('uuid')
        _resources = Resource.objects.filter(uuid=_uuid).order_by('-time')[:self.SIZE]
        _resources = [_resource.as_dict() for _resource in _resources]
        return JsonResponse({'code' : 200, 'text' : '', 'result' : _resources})
