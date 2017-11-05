#encoding: utf-8

import json

class Config(object):
    pass


class Event(object):
    
    def __init__(self, **kwargs):
        self._attrs = {}
        for key, value in kwargs.items():
            self._attrs[key] = value

    def __setitem__(self, key, value):
        self._attrs[key] = value

    def __getitem__(self, key):
        return self._attrs.get(key)

    def as_dict(self):
        return self._attrs

    def as_json(self):
        return json.dumps(self.as_dict())

    def __str__(self):
        return self.as_json()

    @classmethod
    def loads(cls, cxt):
        _json = json.loads(cxt)
        return cls(**_json)