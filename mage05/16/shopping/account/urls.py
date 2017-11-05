#encoding: utf-8


from django.conf.urls import url

from .views import RegisterView, ActiveView

app_name = 'account'



urlpatterns = [
    url(r'^register/', RegisterView.as_view(), name="register"),
    url(r'^active/', ActiveView.as_view(), name="active"),
]
