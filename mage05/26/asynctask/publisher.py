#encoding: utf-8

import logging

import gconf
from task import Task

from mqueue import RedisQueue

logger = logging.getLogger(__name__)

class Publisher(object):
    def __init__(self):
        self.queue = RedisQueue(gconf.QUEUE_TASK_KEY, \
                                gconf.REDIS_HOST, \
                                gconf.REDIS_PORT, \
                                gconf.REDIS_DB)

    def publish(self, script, script_kwargs={}, ignore_result=True):
        task = Task(script=script,\
                    script_kwargs=script_kwargs, \
                    ignore_result=ignore_result)
        logger.info('publish task:%s', task)
        self.queue.put(task.as_json())


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    publisher = Publisher()
    publisher.publish('A')
    publisher.publish('B', {'b' : 1})
    publisher.publish('C', {'c' : 2}, False)