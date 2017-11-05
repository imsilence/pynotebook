#encoding: utf-8

import logging
import time
from publisher import Publisher
logger = logging.getLogger(__name__)

def execute(*args, **kwargs):
    time.sleep(10)
    logger.debug('a execute:%s, %s', args, kwargs)
    publisher = Publisher()
    publisher.publish('B')

    return None