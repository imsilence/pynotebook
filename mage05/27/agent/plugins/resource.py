#encoding: utf-8

from threading import Thread
import time

import psutil

from gconf import Event

class Resource(Thread):
    def __init__(self, config, *args, **kwargs):
        super(Resource, self).__init__(*args, **kwargs)
        self.name = 'resource'
        self.daemon = True
        self.config = config

    def run(self):
        _config = self.config
        _mqueue = _config.QUEUE
        _interval = _config.INTERVAL_RESOURCE

        while _config.RUNNING:
            _evt = self._make_event()
            _mqueue.put(_evt.as_json())
            time.sleep(_interval)

    def _make_event(self):
        _evt = Event()
        _evt['type'] = self.name
        _evt['msg'] = {
            'time' : time.time(),
            'cpu' : psutil.cpu_percent(),
            'mem' : psutil.virtual_memory().percent,
        }
        return _evt