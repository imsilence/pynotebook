#encoding: utf-8

import logging
import json
import importlib
import traceback

import gconf
from mqueue import RedisQueue
from task import Task

logger = logging.getLogger(__name__)

class Executor(object):

    def __init__(self, work):
        self.queue = RedisQueue(gconf.QUEUE_TASK_KEY, \
                        gconf.REDIS_HOST, \
                        gconf.REDIS_PORT, \
                        gconf.REDIS_DB)

    def run(self):
        while True:
            _task = self.queue.get()
            _task = Task(**json.loads(_task.decode()))
            logger.info(_task)
            try:
                _module = importlib.import_module('works.work_{0}'.format(str(_task.script).lower()))
                _module.execute(**_task.script_kwargs)
            except ImportError as e:
                logger.error(e)
                logger.error(traceback.format_exc())