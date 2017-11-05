#encoding: utf-8

import json
import logging
import traceback

from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from django_redis import get_redis_connection

logger = logging.getLogger(__name__)

class APIView(View):

    def get_json(self, request):
        try:
            return json.loads(request.body.decode())
        except BaseException as e:
            logger.error(e)
            logger.error(traceback.format_exc())
            return {}

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(APIView, self).dispatch(request, *args, **kwargs)

    def response(self, result, code=200, text=''):
        return JsonResponse({'code' : code, 'text' : text, 'result' : result})



class AuthAPIView(View):

    def get_json(self, request):
        try:
            return json.loads(request.body.decode())
        except BaseException as e:
            logger.error(e)
            logger.error(traceback.format_exc())
            return {}

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        token_id = request.META.get('HTTP_CMDB_TOKEN_ID', '')
        token_secert = request.META.get('HTTP_CMDB_TOKEN_SECERT', '')

        conn = get_redis_connection()
        local_token_secert = conn.hget('cmdb:token', token_id)

        if local_token_secert == token_secert.encode():
            return super(AuthAPIView, self).dispatch(request, *args, **kwargs)
        else:
            return self.response(None, code=403, text='token不正确')

    def response(self, result, code=200, text=''):
        return JsonResponse({'code' : code, 'text' : text, 'result' : result})
