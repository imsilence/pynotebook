#encoding: utf-8

from threading import Thread
import time
import socket
import platform

import psutil

from gconf import Event
from utils import sysutils

class Client(Thread):
    def __init__(self, config, *args, **kwargs):
        super(Client, self).__init__(*args, **kwargs)
        self.name = 'client'
        self.daemon = True
        self.config = config

    def run(self):
        _config = self.config
        _mqueue = _config.QUEUE
        _interval = _config.INTERVAL_CLIENT

        while _config.RUNNING:
            _evt = self._make_event()
            _mqueue.put(_evt.as_json())
            time.sleep(_interval)

    def _make_event(self):
        _evt = Event()
        _evt['type'] = self.name
        _evt['msg'] = {
            'time' : time.time(),
            'ip' : sysutils.get_ip_address(),
            'mac' : sysutils.get_mac_address(),
            'hostname' : sysutils.get_hostname(),
            'pid' : self.config.PID,
            'platform' : platform.platform(),
            'arch' : platform.architecture()[0],
            'cpu' : psutil.cpu_count(),
            'mem' : psutil.virtual_memory().total,
        }
        return _evt