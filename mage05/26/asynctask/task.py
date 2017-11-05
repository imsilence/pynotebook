#encoding: utf-8

import uuid
import json

class Task(object):
    STATUS_WATING = 1
    STATUS_RUNNING = 2
    STATUS_SUCCESS = 3
    STATUS_FAILURE = 4

    def __init__(self, script, script_kwargs={}, ignore_result=True, tid=None, result=None, status=None):
        self.tid = str(uuid.uuid1()) if tid is None else tid 
        self.script = script
        self.script_kwargs = script_kwargs
        self.ignore_result = ignore_result
        self.result = result
        self.status = self.STATUS_WATING if status is None else status 


    def as_dict(self):
        return self.__dict__


    def as_json(self):
        return json.dumps(self.as_dict())


    def __str__(self):
        return '<Task>[tid:{tid}][script:{script}]'.format(tid=self.tid, script=self.script)


if __name__ == '__main__':
    t = Task('A', {'a':1})
    print(t)
    print(t.as_json())