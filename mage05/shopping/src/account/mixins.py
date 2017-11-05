#encoding: utf-8

from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse

class LoginRequiredMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated() and not request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)

        if request.is_ajax():
            return JsonResponse({'status' : 401})

        return HttpResponseRedirect(reverse('index'))