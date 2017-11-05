#encoding: utf-8

import logging

logger = logging.getLogger(__name__)

def execute(*args, **kwargs):
    logger.debug('c execute:%s, %s', args, kwargs)
    return None