from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from . import models
from .forms import LoginForm

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
    users = models.User.all()
    print(users)
    return render(request, 'user/list.html', {'users' : users})


def delete_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    _id = request.GET.get('id', '')

    # models.User.delte_by_id(_id)

    # user = models.User(id=_id)
    # user.delete()

    user = models.User.get_by_id(_id)
    print(user)
    if user:
        user.delete()

    return HttpResponseRedirect('/user/list_user/')


def create_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    return render(request, 'user/create.html')


def save_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    age = request.POST.get('age', '')
    tel = request.POST.get('tel', '')

    user = models.User(username=username, password=password, age=age, tel=tel)
    rt, error = user.validate_add()
    if rt:
        #验证成功
        user.save()
        return HttpResponseRedirect('/user/list_user/')
    else:
        context = {}
        context['error'] = error
        context['username'] = username
        context['password'] = password
        context['age'] = age
        context['tel'] = tel

        return render(request, 'user/create.html', context)


def view_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    uid = request.GET.get('id', '')
    user = models.User.get_by_id(uid)
    return render(request, 'user/view.html', {'user' : user})

def modify_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')

    uid = request.POST.get('id', '')
    username = request.POST.get('username', '')
    age = request.POST.get('age', '')
    tel = request.POST.get('tel', '')

    user = models.User.get_by_id(uid)
    error = '用户信息不存在'
    if user:
        user.username = username
        user.age = age
        user.tel = tel

        rt, error = user.validate_modify()
        if rt:
            #验证成功
            user.modify()
            return HttpResponseRedirect('/user/list_user/')

    context = {}
    context['error'] = error
    context['user'] = user
    return render(request, 'user/view.html', context)


def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/user/require_login/')
