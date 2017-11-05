#encoding: utf-8
import json

from django.shortcuts import render

from django.views.generic import ListView, DetailView, View, TemplateView
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import transaction

from django.contrib import messages

from .models import Category, Goods, ShoppingCar, Order, GoodsBuied
from .forms import ShoppingCarForm
from account.mixins import LoginRequiredMixin
from account.models import UserAddress

class GoodsListView(ListView):
    model = Goods
    ordering = ['-create_time']

    def get_template_names(self):
        return ['index.html']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(status=0)

class GoodsDetailView(DetailView):
    model = Goods


class ShoppingCarCreateView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        form = ShoppingCarForm(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            try:
                car = ShoppingCar.objects.get(goods=model.goods, user=request.user)
                car.num += model.num
                car.save()
            except ObjectDoesNotExist as e:
                model.user = request.user
                model.save()
            return JsonResponse({'status' : 200})

        return JsonResponse({'status' : 400, 'errors' : json.loads(form.errors.as_json())})


class ShoppingCarNumView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        queryset = ShoppingCar.objects.filter(user=request.user)
        result = sum([car.num for car in queryset])
        return JsonResponse({'status' : 200, 'result' : result})


class ShoppingCarDeleteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pk = request.POST.get('car', 0)
        try:
            car = ShoppingCar.objects.get(pk=pk, user=request.user)
            car.delete()
        except ObjectDoesNotExist as e:
            pass

        return JsonResponse({'status' : 200})


class ShoppingCarUpdateView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        pk = request.POST.get('car', 0)
        num = request.POST.get('num', 0)
        try:
            car = ShoppingCar.objects.get(pk=pk, user=request.user)
            car.num = num
            car.save()
        except ObjectDoesNotExist as e:
            pass

        return JsonResponse({'status' : 200})


class ShoppingCarView(LoginRequiredMixin, TemplateView):

    template_name = 'goods/shopping_car.html'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['shopping_cars'] = ShoppingCar.objects.filter(user=self.request.user)
        kwargs['user_address'] = UserAddress.objects.filter(user=self.request.user, status=0)
        return kwargs
        

class OrderView(LoginRequiredMixin, ListView):
    template_name = 'goods/order.html'
    model = Order

    def post(self, request, *args, **kwargs):
        user_address_id = request.POST.get('user_address', 0)
        car_ids = request.POST.getlist('car')

        try:
            user_address = UserAddress.objects.get(pk=user_address_id, status=0)
            car_list = ShoppingCar.objects.filter(pk__in=car_ids)
            if len(car_list) == 0:
                raise BaseException('购买商品不能为空')
            with transaction.atomic():
                order = Order(user=request.user, user_address=user_address)
                order.save()
                total_price = 0
                for car in car_list:
                    total_price += car.num * car.goods.price
                    goods = GoodsBuied(order=order, goods=car.goods, num=car.num, price=car.goods.price)
                    goods.save()

                car_list.delete()
                order.price = total_price
                order.save()

                # self.object_list = self.get_queryset()

                # return self.render_to_response(self.get_context_data())
            return HttpResponseRedirect(reverse('goods:order_list'))
        except ObjectDoesNotExist as e:
            print(e)
            messages.add_message(request, messages.ERROR, '收件地址不能为空')
        except BaseException as e:
            messages.add_message(request, messages.ERROR, '购买商品不能为空')

        return HttpResponseRedirect(reverse('goods:shopping_car'))


class OrderListView(LoginRequiredMixin, ListView):
    template_name = 'goods/order.html'
    model = Order
    paginate_by = 5
    ordering = ['-create_time']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
        

class OrderOperateView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        op = request.POST.get('op', '')
        order_id = request.POST.get('order_id')
        try:
            order = Order.objects.get(user=self.request.user, pk=order_id)
            if op == 'makesure':
                order.status = 3
            elif op == 'cancel':
                order.status = 4
            order.save()
        except BaseException as e:
            print(e)

        return JsonResponse({'status' : 200})
