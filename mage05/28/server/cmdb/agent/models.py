#encoding: utf-8

import logging
import traceback

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from datetime import timedelta, datetime

logger = logging.getLogger(__name__)

class BaseAttrDictMixin(object):

    def as_dict(self):
        _dict = {}
        for _key, _value in self.__dict__.items():
            if type(_value) in [int, float, str, bytes, bool, list, tuple, datetime]:
                _dict[_key] = _value
        return _dict


class Client(BaseAttrDictMixin, models.Model):
    STATUS_OK = 0
    STATUS_DELETE = 1

    uuid = models.CharField(max_length=64, unique=True, default='')
    hostname = models.CharField(max_length=128, default='')
    ip = models.GenericIPAddressField(default='0.0.0.0')
    mac = models.CharField(max_length=64, default='')
    platform = models.CharField(max_length=256, default='')
    arch = models.CharField(max_length=16, default='')
    cpu = models.IntegerField(default=0)
    mem = models.BigIntegerField(default=0)

    pid = models.IntegerField(default=0)
    time = models.FloatField(default=0)

    user = models.CharField(max_length=256, default='')
    application = models.CharField(max_length=256, default='')
    addr = models.CharField(max_length=256, default='')
    remark = models.CharField(max_length=512, default='')

    heartbeat_time = models.DateTimeField(auto_now_add=True)

    register_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0)

    @property
    def is_online(self):
        return timezone.now() - self.heartbeat_time < timedelta(minutes=5)

    @classmethod
    def register(cls, uuid, **kwargs):
        _instance = None
        _created = False
        try:
            _instance = cls.objects.get(uuid=uuid)
        except ObjectDoesNotExist as e:
            _instance = cls()
            setattr(_instance, 'uuid', uuid)
            _created = True

        for _key, _value in kwargs.items():
            if hasattr(_instance, _key):
                setattr(_instance, _key, _value)

        _instance.status = cls.STATUS_OK
        _instance.save()
        return _instance, _created

    @classmethod
    def heartbeat(cls, uuid):
        try:
            _instance = cls.objects.get(uuid=uuid)
            _instance.heartbeat_time = timezone.now()
            _instance.save()
        except ObjectDoesNotExist as e:
            logger.error(e)



class Resource(BaseAttrDictMixin, models.Model):
    uuid = models.CharField(max_length=64, default='')
    time = models.DateTimeField(auto_now_add=True)
    cpu = models.FloatField(default=0)
    mem = models.FloatField(default=0)

    @classmethod
    def create(cls, uuid, **kwargs):
        _instance = cls()
        setattr(_instance, 'uuid', uuid)
        for _key, _value in kwargs.items():
            if hasattr(_instance, _key):
                setattr(_instance, _key, _value)

        _instance.save()
        return _instance