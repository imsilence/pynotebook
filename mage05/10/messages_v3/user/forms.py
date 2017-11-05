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
    username = forms.CharField(label="用户名", error_messages={'required' : "用户名不能为空"})
    password = forms.CharField(widget=forms.PasswordInput, label="密码", error_messages={'required' : "密码不能为空"})
    age = forms.CharField(label="年龄", error_messages={'required' : "年龄不能为空"})
    tel = forms.CharField(label="电话号码", error_messages={'required' : "电话号码不能为空"})

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        try:
            models.User2.objects.get(username=username)
            raise forms.ValidationError("用户名已存在")
        except ObjectDoesNotExist as e:
            pass

        return username

    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        return crypt.CryptUtils.md5(password)

    def clean_age(self):
        age = self.cleaned_data.get('age', 0)
        if not str(age).isdigit():
            raise forms.ValidationError("年龄必须为0到80的整数")

        age = int(age)
        if age <= 0 or age >= 80:
            raise forms.ValidationError("年龄必须为0到80的整数")
        return age

    def clean_tel(self):
        tel = self.cleaned_data.get('tel', '')
        if len(tel) != 11:
            raise forms.ValidationError("手机号码不正确")

        return tel


class ModifyUserForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput, required=False)
    username = forms.CharField(label="用户名", error_messages={'required' : "用户名不能为空"})
    age = forms.CharField(label="年龄", error_messages={'required' : "年龄不能为空"})
    tel = forms.CharField(label="电话号码", error_messages={'required' : "电话号码不能为空"})

    def clean(self):
        cleaned_data = super(ModifyUserForm, self).clean()
        try:
            _id = cleaned_data.get('id', 0)
            if not str(_id).isdigit():
                raise forms.ValidationError("操作对象不存在")
            models.User2.objects.get(pk=_id)
        except ObjectDoesNotExist as e:
            raise forms.ValidationError("操作对象不存在")

        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        try:
            _id = self.cleaned_data.get('id', 0)
            if not str(_id).isdigit():
                raise forms.ValidationError("操作对象不存在")
            models.User2.objects.exclude(pk=_id).get(username=username)
            raise forms.ValidationError("用户名已存在")
        except ObjectDoesNotExist as e:
            pass

        return username

    def clean_age(self):
        age = self.cleaned_data.get('age', 0)
        if not str(age).isdigit():
            raise forms.ValidationError("年龄必须为0到80的整数")

        age = int(age)
        if age <= 0 or age >= 80:
            raise forms.ValidationError("年龄必须为0到80的整数")
        return age

    def clean_tel(self):
        tel = self.cleaned_data.get('tel', '')
        if len(tel) != 11:
            raise forms.ValidationError("手机号码不正确")

        return tel



class PasswordForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput, required=False)
    password = forms.CharField(widget=forms.PasswordInput, label="密码", error_messages={'required' : "密码不能为空"})

    def clean(self):
        cleaned_data = super(PasswordForm, self).clean()
        try:
            id = cleaned_data.get('id', 0)
            models.User2.objects.get(pk=id)
        except ObjectDoesNotExist as e:
            raise forms.ValidationError("操作对象不存在")

        return cleaned_data

    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        return crypt.CryptUtils.md5(password)

class PasswordForm2(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False)
    class Meta:
        model = models.User2
        fields = ['id', 'password']
        widgets = {
            'password' : forms.PasswordInput(),
        }
        labels = {
            'password' : "密码",
        }
        error_messages = {
            'password' : {
                'required' : "密码不能为空"
            }
        }

    def clean(self):
        cleaned_data = super(PasswordForm2, self).clean()
        try:
            _id = cleaned_data.get('id', 0)
            if not str(_id).isdigit():
                raise forms.ValidationError("操作对象不存在")
            models.User2.objects.get(pk=_id)
        except ObjectDoesNotExist as e:
            raise forms.ValidationError("操作对象不存在")

        return cleaned_data

    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        return crypt.CryptUtils.md5(password)
