from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

from . import models
from .forms import LoginForm, CreateUserForm, ModifyUserForm, PasswordForm

# Create your views here.

def require_login(request):
    if request.session.get('user'):
        return HttpResponseRedirect('/user/list_user/')

    form = LoginForm()
    return render(request, 'user/login.html', {'form' : form})


def login(request):

    if request.session.get('user'):
        return HttpResponseRedirect('/user/list_user/')

    form = LoginForm(request.POST)
    if form.is_valid():
        request.session['user'] = {'username' : form.cleaned_data['username']}
        return HttpResponseRedirect('/user/list_user/')
    else:
        return render(request, 'user/login.html', {'form' : form})


def list_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    users = models.User2.objects.all()
    print(users)
    return render(request, 'user/list.html', {'users' : users})


def delete_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    _id = request.GET.get('id', '')
    user = None
    try:
        uid = request.GET.get('id', 0)
        user = models.User2.objects.get(pk=_id)
        user.delete()
    except ObjectDoesNotExist as e:
        pass
    return HttpResponseRedirect('/user/list_user/')


def create_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    form = CreateUserForm()
    return render(request, 'user/create.html', {'form' : form})


def save_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')

    form = CreateUserForm(request.POST)

    if form.is_valid():
        user = models.User2(username=form.cleaned_data['username'], password=form.cleaned_data['password'], age=form.cleaned_data['age'], tel=form.cleaned_data['tel'])
        user.save()
        return HttpResponseRedirect('/user/list_user/')
    else:
        return render(request, 'user/create.html', {'form' : form})


def view_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    form = None
    try:
        _id = request.GET.get('id', 0)
        user = models.User2.objects.get(pk=_id)
        form = ModifyUserForm(user.as_dict())
    except ObjectDoesNotExist as e:
        form = ModifyUserForm()

    return render(request, 'user/view.html', {'form' : form})

def modify_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')

    form = ModifyUserForm(request.POST)

    if form.is_valid():
        user = models.User2.objects.get(pk=form.cleaned_data['id'])
        user.username = form.cleaned_data['username']
        user.age = form.cleaned_data['age']
        user.tel = form.cleaned_data['tel']
        user.save()
        return HttpResponseRedirect('/user/list_user/')
    else:
        return render(request, 'user/view.html', {'form' : form})

def modify_password(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')

    form = None
    if request.method == 'GET':
        try:
            _id = request.GET.get('id', 0)
            user = models.User2.objects.get(pk=_id)
            form = PasswordForm(initial=user.as_dict())
        except ObjectDoesNotExist as e:
            form = PasswordForm()
    else:
        form = PasswordForm(request.POST)
        if form.is_valid():
            user = models.User2.objects.get(pk=form.cleaned_data['id'])
            user.password = form.cleaned_data['password']
            user.save()
            return HttpResponseRedirect('/user/list_user/')

    return render(request, 'user/password.html', {'form' : form})

def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/user/require_login/')
