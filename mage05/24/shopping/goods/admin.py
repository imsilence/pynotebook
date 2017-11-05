#encoding: utf-8

from django.contrib import admin

from .models import Category, Goods, GoodsExt, Order, GoodsBuied
from .forms import GoodsAdminForm, OrderAdminForm

# Register your models here.
admin.site.site_header = 'KK的商城'
admin.site.site_title = 'KK的商城'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time']
    fields = ['name']
    search_fields = ['name']
    actions = None

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(status=0)

    def delete_model(self, request, obj):
        obj.status = 1
        obj.save()


class GoodsExtInline(admin.TabularInline):
    model = GoodsExt
    fields = ['key', 'value']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(status=0)


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'store']
    exclude = ['status']
    search_fields = ['name', 'desc', 'category__name']
    actions = None
    form = GoodsAdminForm
    inlines = [GoodsExtInline]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(status=0)

    def delete_model(self, request, obj):
        obj.status = 1
        obj.save()

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.status = 1
            obj.save()

        for obj in instances:
            obj.save()

        formset.save_m2m()

class GoodsBuiedInline(admin.TabularInline):
    model = GoodsBuied
    fields = ['goods', 'num', 'price']
    readonly_fields = ['price', 'goods', 'num']
    extra = 0
    can_delete = False

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'create_time', 'status_text', 'is_normal']
    actions = None
    readonly_fields = ['user', 'price', 'user_address', 'invoice_type', 'invoice_title', 'pay_type', 'create_time', 'status_text']
    form = OrderAdminForm
    inlines = [
        GoodsBuiedInline
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Order, OrderAdmin)
