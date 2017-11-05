#encoding: utf-8

import logging
import traceback

'''
日志(7)有不能严重级别
debug
info
error
'''

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)s %(lineno)d %(levelname)s: %(message)s',
                            filename='my.log',
                            filemode='w'
                        )

    logger.debug('debug msg')
    logger.info('info msg')
    logger.error('error msg')

    try:
        1/0
    except BaseException as e:
        logger.error(e)
        logger.error(traceback.format_exc())
