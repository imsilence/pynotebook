#encoding: utf-8

import json
import logging
import traceback

from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

logger = logging.getLogger(__name__)

class APIView(View):

    def get_json(self, request):
        try:
            return json.loads(request.body.decode())
        except BaseException as e:
            logger.error(e)
            logger.error(traceback.format_exc())
            return None

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(APIView, self).dispatch(request, *args, **kwargs)

    def response(self, result, code=200, text=''):
        return JsonResponse({'code' : code, 'text' : text, 'result' : result})

