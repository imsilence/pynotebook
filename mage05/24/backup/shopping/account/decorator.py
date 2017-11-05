#encoding: utf-8

from functools import wraps
from django.http import HttpResponse

def login_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated():
            rt = func(request, *args, **kwargs)
            return rt
        else:
            return HttpResponse("未登陆")

    return wrapper