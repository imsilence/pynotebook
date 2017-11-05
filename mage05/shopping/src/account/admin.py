from django.contrib import admin

from .models import UserExt, UserAddress

admin.site.register(UserExt)
admin.site.register(UserAddress)
