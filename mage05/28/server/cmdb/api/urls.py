#encoding: utf-8

from django.conf.urls import url


from api.views import v1, v2, v3

app_name = 'api'

urlpatterns = [
    url(r'^v1/client/(?P<uuid>\w{32,64})/$', v1.ClientView.as_view()),
    url(r'^v1/heartbeat/(?P<uuid>\w{32,64})/$', v1.HeartbeatView.as_view()),
    url(r'^v1/resource/(?P<uuid>\w{32,64})/$', v1.ResourceView.as_view()),

    url(r'^v2/client/(?P<uuid>\w{32,64})/$', v2.ClientView.as_view()),
    url(r'^v2/heartbeat/(?P<uuid>\w{32,64})/$', v2.HeartbeatView.as_view()),
    url(r'^v2/resource/(?P<uuid>\w{32,64})/$', v2.ResourceView.as_view()),

    url(r'^v3/client/(?P<uuid>\w{32,64})/$', v3.ClientView.as_view()),
    url(r'^v3/heartbeat/(?P<uuid>\w{32,64})/$', v3.HeartbeatView.as_view()),
    url(r'^v3/resource/(?P<uuid>\w{32,64})/$', v3.ResourceView.as_view()),

]