#encoding: utf-8

from  django.http import JsonResponse, HttpResponseRedirect, Http404
from django.conf import settings
from django.contrib.auth import logout

class LoginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated() or request.user.is_staff:
            if request.is_ajax():
                return JsonResponse({'status' : 401})
            else:
                return HttpResponseRedirect(settings.LOGIN_URL)

        return super().dispatch(request, *args, **kwargs)


class ObjectPermMixin(object):
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj:
            user = getattr(obj, 'user')
            if user and user != request.user:
                if request.is_ajax():
                    return JsonResponse({'status' : 404})
                else:
                    raise Http404('Object Perm')

        return super().dispatch(request, *args, **kwargs)