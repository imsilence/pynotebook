#encoding: utf-8

from django.contrib import admin

from .models import Category, Goods, GoodsExt

# Register your models here.
admin.site.site_header = 'KK的商城'
admin.site.site_title = 'KK的商城'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time']
    fields = ['name']
    search_fields = ['name']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(status=0)

    def delete_model(self, request, obj):
        obj.status = 1
        obj.save()



admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods)
admin.site.register(GoodsExt)
