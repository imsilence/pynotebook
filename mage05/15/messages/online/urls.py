#encoding: utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^create/$', views.create, name='create'),
   url(r'^save/$', views.save, name='save'),
   url(r'^save_ajax/$', views.save_ajax, name='save_ajax'),
   url(r'^get_ajax/$', views.get_ajax, name='get_ajax'),
   url(r'^get_ajax2/$', views.get_ajax2, name='get_ajax2'),
]
