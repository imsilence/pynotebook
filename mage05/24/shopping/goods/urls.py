#encoding: utf-8


from django.conf.urls import url

from .views import GoodsListView, GoodsDetailView, \
                    ShoppingCarCreateView, ShoppingCarNumView, \
                    ShoppingCarView, ShoppingCarDeleteView, \
                    OrderCreateView, OrderListView, OrderOperateView

app_name = 'goods'

urlpatterns = [
    url(r'^$', GoodsListView.as_view(), name="goods"),
    url(r'^(?P<pk>\d+)/$', GoodsDetailView.as_view(), name="goods_detail"),
    url(r'^add_shopping_car/$', ShoppingCarCreateView.as_view(), name="add_shopping_car"),
    url(r'^get_shopping_car_num/$', ShoppingCarNumView.as_view(), name="get_shopping_car_num"),
    url(r'^shopping_car/$', ShoppingCarView.as_view(), name="shopping_car"),
    url(r'^remove_shopping_car/$', ShoppingCarDeleteView.as_view(), name='remove_shopping_car'),
    url(r'^create_order/$', OrderCreateView.as_view(), name="create_order"),
    url(r'^orders/$', OrderListView.as_view(), name="orders"),
    url(r'^order_operate/$', OrderOperateView.as_view(), name="order_operate"),
]