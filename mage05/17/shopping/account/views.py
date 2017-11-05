#encoding: utf-8
import datetime
import json


from django.conf import settings
from django.utils import timezone

from django.shortcuts import render
from django.views.generic import View, FormView
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

from django.core.mail import send_mail
from django.db import transaction
from django.contrib import messages

from .models import UserExt
from .forms import RegisterForm, LoginForm, ResetPasswordForm, ResetPasswordConfirmForm

class RegisterView(View):

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        return self._register(form)


    def _register(self, form):
        if form.is_valid():
            username = form.cleaned_data.get('username', '')
            password = form.cleaned_data.get('password', '')
            email = form.cleaned_data.get('email', '')

            try:
                with transaction.atomic():
                    user = User.objects.create_user(username=username, password=password, email=email)
                    validkey = UserExt.gen_validkey()

                    user_ext = UserExt.objects.create(user=user, realname='', birthday=datetime.date(1945, 1, 1), \
                                                        nickname=username, avatar='default', telephone='', logintime=timezone.now(), validkey=validkey)

                    content = '欢迎注册[KK的商城], 请点击此处进行激活用户: http://192.168.1.116:8888/account/active/?username={username}&validkey={validkey}'.format(username=username, validkey=validkey)
                    send_mail('[KK的商城]用户注册', content, settings.EMAIL_HOST_USER, [email])
            except BaseException as e:
                return JsonResponse({'status': 500, 'errors' : ['服务器错误']})
            return JsonResponse({'status': 200})
        else:
            return JsonResponse({'status': 400, 'errors': json.loads(form.errors.as_json()), 'result': ''})


    def get(self, request, *args, **kwargs):
        form = RegisterForm(request.GET)
        return self._register(form)


class  ActiveView(View):

    def get(self, request, *args, **kwargs):
        username = request.GET.get('username', '')
        validkey = request.GET.get('validkey', '')

        #objectdoesnotexists
        try:
            user = User.objects.get(username=username)
            if user.userext.status == 0 and user.userext.validkey != '':
                if user.userext.validkey == validkey:
                    user.userext.status = 1
                    user.userext.validkey = ''
                    user.userext.save()
                    messages.add_message(request, messages.INFO, '激活成功, 请登录')
                else:
                    messages.add_message(request, messages.ERROR, '激活失败, 用户名或验证码不正确')
            else:
                messages.add_message(request, messages.ERROR, '激活失败, 用户名或验证码不正确')
        except ObjectDoesNotExist as e:
            messages.add_message(request, messages.ERROR, '激活失败, 用户名或验证码不正确')
            #跳转到页面\

        return HttpResponseRedirect(reverse('index'))
        # return HttpResponse("用户不存在")



class LoginView2(View):
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.cached_user)
            return JsonResponse({'status' : 200, 'errors' : {}, 'result' : {}})
        else:
            return JsonResponse({'status' : 400, 'errors' : json.loads(form.errors.as_json()), 'result' : {}})


class LoginView(FormView):
    form_class = LoginForm

    def form_valid(self, form):
        login(self.request, form.cached_user)
        return JsonResponse({'status' : 200, 'errors' : {}, 'result' : {}})

    def form_invalid(self, form):
        return JsonResponse({'status' : 400, 'errors' : json.loads(form.errors.as_json()), 'result' : {}})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class ModifyPasswordView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponse('success')
        else:
            return HttpResponse('fail')



class ResetPasswordView(FormView):
    template_name = 'account/reset_password.html'
    form_class = ResetPasswordForm

    def form_valid(self, form):
        try:
            with transaction.atomic():
                user = form.cached_user
                validkey = user.userext.gen_validkey()
                user.userext.validkey = validkey
                user.userext.save()
                content = '欢迎使用[KK的商城], 请点击此处进行重置用户: http://192.168.1.116:8888/account/reset_password_confirm/?username={username}&validkey={validkey}'.format(username=user.username, validkey=validkey)
                send_mail('[KK的商城]用户重置密码', content, settings.EMAIL_HOST_USER, [user.email])
                messages.add_message(self.request, messages.INFO, '重置密码邮件已发送, 请查收邮件进行密码重置')
        except BaseException as e:
            print(e)
            messages.add_message(self.request, messages.ERROR, '重置密码邮件发送失败，请重试')

        return HttpResponseRedirect(reverse('index'))

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form' : form})


class ResetPasswordConfirmView(FormView):
    template_name = 'account/reset_password_confirm.html'
    form_class = ResetPasswordConfirmForm

    def get_initial(self):
        return self.request.GET

    def form_valid(self, form):
        user = form.cached_user
        password = form.cleaned_data.get('password', '')
        user.set_password(password)
        user.save()
        user.userext.validkey = ''
        user.userext.save()
        messages.add_message(self.request, messages.INFO, '重置密码成功，请重新登陆')
        return HttpResponseRedirect(reverse('index'))

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form' : form})
