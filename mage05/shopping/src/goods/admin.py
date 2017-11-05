from django.contrib import admin

from .models import Category, Goods, GoodsExt, Order, GoodsBuied
from .forms import GoodsAdminForm, OrderAdminForm

admin.site.site_header = 'KK的商城'
admin.site.site_title = 'KK的商城'

class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'status']
    fields = ['name']
    search_fields = ['name']
    actions = None

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(status=0)

    def delete_model(self, request, obj):
        obj.status = 1
        obj.save()

    def save_model(self, request, obj, form, change):
        obj.save()

# class GoodsExtInline(admin.StackedInline):
#     model = GoodsExt

class GoodsExtInline(admin.TabularInline):
    model = GoodsExt
    fields = ['key', 'value']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(status=0)


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'price', 'store', 'desc']
    exclude = ['status']
    inlines = [
        GoodsExtInline
    ]
    form = GoodsAdminForm

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
        for instance in instances:
            instance.save()
        formset.save_m2m()

    def save_model(self, request, obj, form, change):
        obj.save()

class GoodsExtAdmin(admin.ModelAdmin):
    list_display = ['key', 'value']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(status=0)

class GoodsBuiedInline(admin.TabularInline):
    model = GoodsBuied
    fields = ['goods', 'num', 'price']
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'create_time', 'status_text']
    fields = ['status']
    form = OrderAdminForm
    actions = None
    inlines = [
        GoodsBuiedInline
    ]

admin.site.register(Order, OrderAdmin)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsExt, GoodsExtAdmin)
