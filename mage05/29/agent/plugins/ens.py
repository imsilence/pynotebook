#encoding: utf-8

import logging
import traceback
from threading import Thread
import time

import requests

from gconf import Event

logger = logging.getLogger(__name__)

class ENS(Thread):
    def __init__(self, config, *args, **kwargs):
        super(ENS, self).__init__(*args, **kwargs)
        self.name = 'ens'
        self.daemon = True
        self._config = config

    def run(self):
        _config = self._config
        _interval = _config.INTERVAL
        _mqueue = _config.QUEUE
        
        while _config.RUNNING:
            try:
                _msg = _mqueue.get(timeout=_interval)
                if _msg:
                    _evt = Event.loads(_msg)
                    self.dispatch(_evt)
            except BaseException as e:
                logger.error(e)
                logger.error(traceback.format_exc())
            
    def dispatch(self, evt):
        _config = self._config
        _url = 'http://{0}:{1}/api/v3/{2}/{3}/'.format(
            _config.SERVER_ADDR,
            _config.SERVER_PORT,
            evt['type'],
            _config.UUID
        )
        _headers = {
            'cmdb-token-id' : _config.TOKEN_ID,
            'cmdb-token-secert' : _config.TOKEN_SECERT
        }
        _response = requests.post(_url, json=evt['msg'], headers=_headers)
        if _response.ok:
            logger.debug('success send log[%s]:%s, result[%s]:%s', evt['type'], evt['msg'], _response.status_code, _response.text)
        else:
            logger.error('error send log[%s]: %s, result[%s]:%s', evt['type'], evt['msg'], _response.status_code, _response.text)