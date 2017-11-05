#encoding: utf-8
import json

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone

# Create your views here.
from . import models
from . import forms


def index(request):
    if not request.session.get('user'):
        return redirect('/user/require_login/')

    messages = models.Message2.objects.order_by('-publish_date')
    context = {'messages' : messages}
    return render(request, 'online/index.html', context)


def create(request):
    if not request.session.get('user'):
        return redirect('/user/require_login/')

    form = forms.MessageForm()
    return render(request, 'online/create.html', {'form' : form})


def save(request):
    if not request.session.get('user'):
        return redirect('/user/require_login/')

    form = forms.MessageForm(request.POST)
    if form.is_valid():
        message = models.Message2(title=form.cleaned_data['title'], \
                                    content=form.cleaned_data['content'], \
                                    username=form.cleaned_data['username'], \
                                    publish_date=timezone.now())
        message.save()
        return HttpResponseRedirect('/online/')
    else:
        return render(request, 'online/create.html', {'form' : form})



def save_ajax(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    username = request.session.get('user').get('username')

    message = models.Message2(title=title, \
                                content=content, \
                                username=username, \
                                publish_date=timezone.now())
    message.save()

    return HttpResponse(json.dumps({"status" : 200, "result" : ""}))

def get_ajax(request):
    messages = models.Message2.objects.order_by('-publish_date')[:10]
    messages = [message.as_dict() for message in messages]
    return HttpResponse(json.dumps({"messages" : messages, "status" : 200}))
