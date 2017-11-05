#encoding: utf-8


from django.conf.urls import url

from .views import GoodsListView

app_name = 'goods'

urlpatterns = [
    url(r'^$', GoodsListView.as_view(), name="goods"),
]
