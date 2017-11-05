#encoding: utf-8


from django.conf.urls import url

from .views import GoodsListView, GoodsDetailView, \
                    ShoppingCarNumView, ShoppingCarCreateView, ShoppingCarDeleteView, ShoppingCarUpdateView, ShoppingCarView, \
                    OrderView, OrderListView, OrderOperateView

app_name = 'goods'

urlpatterns = [
    url(r'^$', GoodsListView.as_view(), name='list'),
    url(r'^goods/(?P<pk>\d+)/$', GoodsDetailView.as_view(), name='detail'),
    url(r'^add_shopping_car/$', ShoppingCarCreateView.as_view(), name='add_shopping_car'),
    url(r'^shopping_car_num/$', ShoppingCarNumView.as_view(), name='shopping_car_num'),
    url(r'^remove_shopping_car/$', ShoppingCarDeleteView.as_view(), name='remove_shopping_car'),
    url(r'^update_shopping_car/$', ShoppingCarUpdateView.as_view(), name='update_shopping_car'),
    url(r'^shopping_car/$', ShoppingCarView.as_view(), name='shopping_car'),
    url(r'^order/$', OrderView.as_view(), name='order'),
    url(r'^order_list/$', OrderListView.as_view(), name='order_list'),
    url(r'^order_operate/$', OrderOperateView.as_view(), name='order_operate'),
]
