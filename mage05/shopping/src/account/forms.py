#encoding: utf-8
from django import forms

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate

from .models import UserExt, UserAddress


User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput, error_messages={'required' : '用户名不能为空'})
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required' : '密码不能为空'})
    password2 = forms.CharField(widget=forms.PasswordInput, required=False)
    email = forms.EmailField(error_messages={'required' : '邮箱不能为空', 'invalid' : '邮箱格式不正确'})

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        if len(username) < 6 or len(username) > 16:
            raise forms.ValidationError('用户名必须为6位到16位')
        try:
            User.objects.get(username=username)
            raise forms.ValidationError('用户名已经存在')
        except ObjectDoesNotExist as e:
            pass

        return username

    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        if len(password) < 6 or len(password) > 32:
            raise forms.ValidationError('密码必须为6位到32位')
        return password

    def clean_password2(self):
        password = self.cleaned_data.get('password', '')
        password2 = self.cleaned_data.get('password2', '')
        if password != password2:
            raise forms.ValidationError('两次密码不一致')

        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        try:
            User.objects.get(email=email)
            raise forms.ValidationError('邮件已注册')
        except ObjectDoesNotExist as e:
            pass

        return email


class LoginForm(forms.Form):
    username = forms.CharField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    user = None

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username', '')
        password = cleaned_data.get('password', '')
        if username == '' or password == '':
            raise forms.ValidationError('用户名或密码错误')

        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('用户名或密码错误')

        if user.is_staff:
            raise forms.ValidationError('员工账号不允许登录')

        if user.userext.status == 0:
            raise forms.ValidationError('用户未激活')

        self.user = user
        return cleaned_data


class PasswordResetForm(forms.Form):
    username = forms.CharField(required=False)
    email = forms.EmailField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username', '')
        email = cleaned_data.get('email', '')
        if username == '' or email == '':
            raise forms.ValidationError("用户名或邮箱错误")

        try:
            user = User.objects.get(username=username, email=email)
            if user.userext.status != 1:
                raise forms.ValidationError("用户名或邮箱错误")
        except ObjectDoesNotExist:
            raise forms.ValidationError("用户名或邮箱错误")

        return cleaned_data

class PasswordResetConfirmForm(forms.Form):
    username = forms.CharField(widget=forms.HiddenInput, required=False)
    validkey = forms.CharField(widget=forms.HiddenInput, required=False)
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required' : '密码不能为空'})
    password2 = forms.CharField(widget=forms.PasswordInput, required=False)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username', '')
        validkey = cleaned_data.get('validkey', '')
        try:
            user = User.objects.get(username=username)
            if user.userext.status != 1 or user.userext.validkey == '' or user.userext.validkey != validkey:
                raise forms.ValidationError('验证码不正确')
        except ObjectDoesNotExist as e:
            raise forms.ValidationError('验证码不正确')

        return cleaned_data

    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        if len(password) < 6 or len(password) > 32:
            raise forms.ValidationError('密码必须为6位到32位')
        return password

    def clean_password2(self):
        password = self.cleaned_data.get('password', '')
        password2 = self.cleaned_data.get('password2', '')
        if password != password2:
            raise forms.ValidationError('两次密码不一致')

        return password2


class PasswordModifyForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput, error_messages={'required' : '密码不能为空'})
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required' : '新密码不能为空'})
    password2 = forms.CharField(widget=forms.PasswordInput, required=False)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password', '')
        if not self.user.check_password(old_password):
            raise forms.ValidationError("密码错误")

        return old_password

    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        if len(password) < 6 or len(password) > 32:
            raise forms.ValidationError('新密码必须为6位到32位')
        return password

    def clean_password2(self):
        password = self.cleaned_data.get('password', '')
        password2 = self.cleaned_data.get('password2', '')
        if password != password2:
            raise forms.ValidationError('两次新密码不一致')

        return password2



class UserExtForm(forms.ModelForm):
    sex = forms.ChoiceField(widget=forms.RadioSelect, choices=[(1, '男'), (0, '女')])
    class Meta:
        model = UserExt
        fields = ['realname', 'sex', 'birthday', 'nickname', 'telephone']


class UserAvatarForm(forms.ModelForm):
    avatar = forms.FileField(required=True)

    class Meta:
        model = UserExt
        fields = ['avatar']

    def clean(self):
        cleaned_data = super().clean()
        avatar = cleaned_data.get('avatar')
        print(avatar)
        return cleaned_data


class UserAddressCreateForm(forms.ModelForm):

    class Meta:
        model = UserAddress
        fields = '__all__'
        exclude = ['user', 'status']

    def clean(self):
        pass
