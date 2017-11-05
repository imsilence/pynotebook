#encoding: utf-8

from threading import Thread
import time

from gconf import Event

class Heartbeat(Thread):
    def __init__(self, config, *args, **kwargs):
        super(Heartbeat, self).__init__(*args, **kwargs)
        self.name = 'heartbeat'
        self.daemon = True
        self.config = config

    def run(self):
        _config = self.config
        _mqueue = _config.QUEUE
        _interval = _config.INTERVAL_HEARTBEAT

        while _config.RUNNING:
            _evt = self._make_event()
            _mqueue.put(_evt.as_json())
            time.sleep(_interval)

    def _make_event(self):
        _evt = Event()
        _evt['type'] = self.name
        _evt['msg'] = {'time' : time.time()}
        return _evt