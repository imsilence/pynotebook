from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Create your views here.
from . import models


def index(request):
    if not request.session.get('user'):
        return redirect('/user/require_login/')

    messages = models.Message.all()
    for m in messages:
        print(m)
    context = {'messages' : messages}
    return render(request, 'online/index.html', context)


def create(request):
    if not request.session.get('user'):
        return redirect('/user/require_login/')

    return render(request, 'online/create.html')


def save(request):
    if not request.session.get('user'):
        return redirect('/user/require_login/')
    username = request.GET.get('username', '')
    title = request.GET.get('title', '')
    content = request.GET.get('content', '')
    message = models.Message(title=title, content=content, username=username)
    print(message)
    message.save()
    return HttpResponseRedirect('/online/')
