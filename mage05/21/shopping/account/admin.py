from django.contrib import admin

# Register your models here.

from .models import UserExt, UserAddress

admin.site.register(UserExt)
admin.site.register(UserAddress)