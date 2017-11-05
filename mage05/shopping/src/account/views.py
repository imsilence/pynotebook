#encoding: utf-8
import datetime
import time
import json

from django.conf import settings
from django.utils import timezone

from django.shortcuts import render
from django.views.generic import View, FormView, ListView, CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateResponseMixin
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth import get_user_model, login, logout
from django.contrib import messages
from django.urls import reverse, reverse_lazy

from django.db import transaction

from utils import emailutil, encryptutil

from .models import UserExt, UserAddress
from .forms import RegisterForm, LoginForm, \
                    PasswordResetForm, PasswordResetConfirmForm, PasswordModifyForm, \
                    UserExtForm, UserAvatarForm, \
                    UserAddressCreateForm

from .mixins import LoginRequiredMixin


User = get_user_model()


class RegisterView(View):

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        return self._register(form)


    def _register(self, form):
        if form.is_valid():
            try:
                with transaction.atomic():
                    username = form.cleaned_data.get('username', '')
                    password = form.cleaned_data.get('password', '')
                    email = form.cleaned_data.get('email', '')

                    user = User.objects.create_user(username=username, password=password, email=email)

                    validkey = encryptutil.random()
                    user_ext = UserExt.objects.create(user=user, realname='', birthday=datetime.date(1945, 1, 1), \
                                                        nickname=username, avatar='', telephone='', logintime=timezone.now(), validkey=validkey)

                    emailutil.register(self.request, username, validkey, email)
                return JsonResponse({'status': 200})
            except BaseException as e:
                return JsonResponse({'status': 500, 'errors' : ['注册失败请联系管理员']})
        else:
            return JsonResponse({'status': 400, 'errors': json.loads(form.errors.as_json()), 'result': ''})


    def get(self, request, *args, **kwargs):
        form = RegisterForm(request.GET)
        return self._register(form)


class  ActiveView(View):

    def get(self, request, *args, **kwargs):
        username = request.GET.get('username', '')
        validkey = request.GET.get('validkey', '')

        #objectdoesnotexist
        try:
            user = User.objects.get(username=username)
            if user.userext.status == 0 and user.userext.validkey != '' and user.userext.validkey == validkey:
                user.userext.status = 1
                user.userext.validkey = ''
                user.userext.save()
                messages.success(request, '用户已经激活')
            else:
                messages.error(request, '用户激活失败')
        except ObjectDoesNotExist as e:
            messages.error(request, '用户激活失败')
            #跳转到页面
        return HttpResponseRedirect(reverse('index'))

class LoginView(FormView):

    form_class = LoginForm

    def form_valid(self, form):
        login(self.request, form.user)
        return JsonResponse({'status' : 200})

    def form_invalid(self, form):
        return JsonResponse({'status' : 400, 'errors' : json.loads(form.errors.as_json())})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class PasswordResetView(FormView):
    template_name = 'account/password_reset.html'
    form_class = PasswordResetForm

    def form_valid(self, form):
        username = form.cleaned_data.get('username', '')
        email = form.cleaned_data.get('email', '')
        validkey = encryptutil.random()

        user = User.objects.get(username=username, email=email)
        user.userext.validkey = validkey
        user.userext.save()
        emailutil.password_reset(self.request, username, validkey, email)
        messages.success(self.request, '请查询邮件进行密码修改')
        return HttpResponseRedirect(reverse('index'))


class PasswordResetConfirmView(View):
    def get(self, request, *args, **kwargs):
        form = PasswordResetConfirmForm(initial=request.GET)
        return render(request, 'account/password_reset_confirm.html', {'form' : form})

    def post(self, request, *args, **kwargs):
        form = PasswordResetConfirmForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username', '')
            password = form.cleaned_data.get('password', '')
            user = User.objects.get(username=username)
            user.set_password(password)
            user.userext.validkey = ''
            user.save()
            user.userext.save()
            messages.success(request, '密码修改成功')
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'account/password_reset_confirm.html', {'form' : form})


class PasswordModifyView(LoginRequiredMixin, FormView):
    form_class = PasswordModifyForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        password = form.cleaned_data.get('password')
        user = self.request.user
        user.set_password(password)
        user.save()

        return JsonResponse({'status' : 200})

    def form_invalid(self, form):
        return JsonResponse({'status' : 400, 'errors' : json.loads(form.errors.as_json())})


class UserView(LoginRequiredMixin, TemplateResponseMixin, View):
    form_class = None
    template_name = 'account/user.html'
    nav_tab = None

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user.userext)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save(commit=True)
        return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        kwargs['nav_tab'] = self.nav_tab
        if kwargs.get('form') is not None:
            kwargs['{prefix}_form'.format(prefix=self.nav_tab)] = kwargs.get('form')

        if kwargs.get('user_ext_form') is None:
            kwargs['user_ext_form'] = UserExtForm(instance=self.request.user.userext)

        if kwargs.get('user_avatar_form') is None:
            kwargs['user_avatar_form'] = UserAvatarForm(instance=self.request.user.userext)
        return kwargs


class UserExtView(UserView):
    form_class = UserExtForm
    nav_tab = 'user_ext'


class UserAvatarView(UserView):
    form_class = UserAvatarForm
    nav_tab = 'user_avatar'

    def form_valid(self, form):
        avatar = self.request.FILES.get('avatar', None)
        fname = None
        if avatar:
            fname = 'avatar/{pk}_{time}.{fsuffix}'.format(pk=self.request.user.pk, time=int(time.time() * 1000), fsuffix=avatar.name.split('.')[-1])
            with open('{media}/{fname}'.format(media=settings.MEDIA_ROOT, fname=fname), 'wb+') as f:
                for chunk in avatar.chunks():
                    f.write(chunk)
        if fname:
            modal = form.save(commit=False)
            modal.avatar = fname
            modal.save()
        return self.render_to_response(self.get_context_data())


class UserAddressListView(LoginRequiredMixin, ListView):
    model = UserAddress
    template_name_suffix = ''

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user, status=0)


class UserAddressCreateView(LoginRequiredMixin, CreateView):
    model = UserAddress
    form_class = UserAddressCreateForm
    success_url = reverse_lazy('account:user_addresses')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class UserAddressDeleteView(LoginRequiredMixin, DeleteView):
    model = UserAddress
    success_url = reverse_lazy('account:user_addresses')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.status = 1
        self.object.save()
        return HttpResponseRedirect(success_url)


class UserAddressUpdateView(LoginRequiredMixin, UpdateView):
    model = UserAddress
    form_class = UserAddressCreateForm
    success_url = reverse_lazy('account:user_addresses')
