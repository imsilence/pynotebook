#encoding: utf-8

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()

class LoginAuthBackend(object):

    def authenticate(self, username='', password=''):
        user = None
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist as e:
            try:
                user = User.objects.get(email=username)
            except ObjectDoesNotExist as e:
                pass

        if user and user.check_password(password) and user.userext.status == 1:
            return user

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except ObjectDoesNotExist as e:
            return None
