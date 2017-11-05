from django.contrib import admin


from .models import User2
from utils.crypt import CryptUtils

class User2Admin(admin.ModelAdmin):
    list_display = ('username', 'age', 'tel')
    search_fields = ('username', 'tel')
    list_filter = ('age',)

    def save_model(self, request, obj, form, change):
        obj.password = CryptUtils.md5(obj.password)
        super(User2Admin, self).save_model(request, obj, form, change)

admin.site.register(User2, User2Admin)
