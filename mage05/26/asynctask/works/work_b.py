#encoding: utf-8
import time
import logging

from publisher import Publisher


logger = logging.getLogger(__name__)

def execute(*args, **kwargs):
    time.sleep(5)
    logger.debug('b execute:%s, %s', args, kwargs)
    publisher = Publisher()
    publisher.publish('C')
    return None