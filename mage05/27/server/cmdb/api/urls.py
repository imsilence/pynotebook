#encoding: utf-8

from django.conf.urls import url


from api.views import v1

app_name = 'api'

urlpatterns = [
    url(r'^v1/client/(?P<uuid>\w{32,64})/$', v1.ClientView.as_view(), name='client'),
    url(r'^v1/heartbeat/(?P<uuid>\w{32,64})/$', v1.HeartbeatView.as_view(), name='heartbeat'),
    url(r'^v1/resource/(?P<uuid>\w{32,64})/$', v1.ResourceView.as_view(), name='resource'),
]