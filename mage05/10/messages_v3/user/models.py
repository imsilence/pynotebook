#encoding: utf-8

import json

from django.db import models

class User2(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=512)
    age = models.IntegerField()
    tel = models.CharField(max_length=13)

    def as_dict(self):
        return {'id' : self.id, 'username' : self.username, 'age' : self.age, 'tel' : self.tel}

    def __str__(self):
        return json.dumps(self.as_dict())
