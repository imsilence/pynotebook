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


class CreateUserForm(forms.Form):
    username = forms.CharField(label="用户名", error_messages={"required" : "用户名不能为空"})
    password = forms.CharField(label="密码", widget=forms.PasswordInput, error_messages={"required" : "密码不能为空"})
    other_password = forms.CharField(label="确认密码", required=False, widget=forms.PasswordInput)
    age = forms.CharField(label="年龄", error_messages={"required" : "年龄不能为空"})
    tel = forms.CharField(label="电话号码", error_messages={"required" : "手机号不能为空"})

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        #models.User2.filter(username=username).count()
        try:
            models.User2.objects.get(username=username)
            raise forms.ValidationError("名字已经存在")
        except ObjectDoesNotExist as e:
            pass

        return username

    def clean_password(self):
        return self.cleaned_data.get('password', '')

    def clean_other_password(self):
        password = self.cleaned_data.get('password', '')
        other_password = self.cleaned_data.get('other_password', '')

        if password != other_password:
            raise forms.ValidationError("两次密码不一致")

        return other_password

    def clean_age(self):
        age = self.cleaned_data.get('age', 0)
        if not str(age).isdigit():
            raise forms.ValidationError("年龄必须是10到80的数字")

        age = int(age)
        if age < 10 or age > 80:
            raise forms.ValidationError("年龄必须是10到80的数字")

        return age




class ModifyUserForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput)
    username = forms.CharField(label="用户名", error_messages={"required" : "用户名不能为空"})
    age = forms.CharField(label="年龄", error_messages={"required" : "年龄不能为空"})
    tel = forms.CharField(label="电话号码", error_messages={"required" : "手机号不能为空"})
