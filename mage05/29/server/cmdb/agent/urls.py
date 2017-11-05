#encoding: utf-8


from django.conf.urls import url

from .views import ClientListView, ResourceView

app_name = 'agent'

urlpatterns = [
    url('^client/$', ClientListView.as_view(), name='client'),
    url('^client/(?P<uuid>\w{32,64})/resource/$', ResourceView.as_view(), name='resource'),
]