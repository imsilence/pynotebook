#encoding: utf-8

import logging

logger = logging.getLogger(__name__)

def execute(*args, **kwargs):
    logger.debug('tpl execute:%s, %s', args, kwargs)
    return None