#encoding: utf-8

from django import forms
from django.core.exceptions import ObjectDoesNotExist

from . import models
from utils import crypt

class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", required=False)
    password = forms.CharField(widget=forms.PasswordInput, label="密码", required=False)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        username = cleaned_data.get('username', '')
        password = cleaned_data.get('password', '')
        if username == '' or password == '':
            raise forms.ValidationError('用户名或密码为空')

        password = crypt.CryptUtils.md5(password)
        count = models.User2.objects.filter(username=username, password=password).count()
        if count == 0:
            raise forms.ValidationError("用户名或密码错误")
        # try:
        #     models.User2.objects.get(username=username, password=password)
        # except ObjectDoesNotExist as e:
        #     raise forms.ValidationError("用户名或密码错误")
        return cleaned_data

    def clean_username(self):
        self.cleaned_data.get()
