#encoding: utf-8

from django.conf import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site

def register(request, username, validkey, to):
    site = get_current_site(request)
    content = '欢迎注册[KK的商城], 请点击此处进行激活用户: http://{site}/account/active/?username={username}&validkey={validkey}'.format(site=site, username=username, validkey=validkey)
    return send_mail('[KK的商城]用户注册', content, settings.EMAIL_HOST_USER, [to])

def password_reset(request, username, validkey, to):
    site = get_current_site(request)
    content = '请点击此处进行用户密码修改: http://{site}/account/password_reset_confirm/?username={username}&validkey={validkey}'.format(site=site, username=username, validkey=validkey)
    return send_mail('[KK的商城]密码重置', content, settings.EMAIL_HOST_USER, [to])
