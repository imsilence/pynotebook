#encoding: utf-8

import os
import logging
import traceback
import argparse
import time
import importlib

import gconf
from utils import fileutils
from utils import sysutils
from utils import mqueue


logger = logging.getLogger(__name__)


def load_plugins(config):
    _plugins = {}
    for _fname in os.listdir(os.path.join(config.PROJECT_PATH, 'plugins')):
        if _fname != '__init__.py' and _fname.endswith('.py'):
            _modname = _fname[:_fname.find('.')]
            try:
                _mod = importlib.import_module('plugins.%s' % _modname)
                _clazz = getattr(_mod, _modname.title(), getattr(_mod, _modname.upper(), None))

                if not _clazz:
                    logger.error('plugin[%s] class is not found', _modname)
                    continue

                logger.info('load plugin[%s] success', _modname)
                _plugins[_modname] = _clazz
            except BaseException as e:
                logger.error('error import plugin[%s]', _modname)
                logger.error(traceback.format_exc())

    return _plugins


def start_plugin(clazz, config):
    _th = clazz(config)
    _th.start()
    return _th


def main(config):
    _ths = {}

    for _plugin, _clazz in config.PLUGINS.items():
        _ths[_plugin] = start_plugin(_clazz, config)
        logger.info('plugin[%s] is running', _plugin)

    try:
        while config.RUNNING:
            for _plugin, _th in _ths.items():
                if not _th.is_alive():
                    logger.info('plugin[%s] is dead and restart', _plugin)
                    _clazz = config.PLUGINS.get(_plugin)
                    _ths[_plugin] = start_plugin(_clazz, config)

            time.sleep(config.INTERVAL)
    except KeyboardInterrupt as e:
        logger.info('agentd exit')
    except BaseException as e:
        logger.error(e)
        logger.error(traceback.format_exc())


if __name__ == '__main__':
    _parser = argparse.ArgumentParser()
    _parser.add_argument('-H', '--host', help='Server Address', type=str, default='127.0.0.1')
    _parser.add_argument('-P', '--port', help='Server Port', type=int, default=8090)
    _parser.add_argument('-V', '--verbose', help='Detailed Log', action='store_true')

    _args = _parser.parse_args()

    config = gconf.Config
    setattr(config, 'RUNNING', True)
    setattr(config, 'PROJECT_PATH', os.path.dirname(os.path.abspath(__file__)))
    setattr(config, 'UUID_FILE', os.path.join(config.PROJECT_PATH, 'UUID'))  
    setattr(config, 'PID', os.getpid())
    setattr(config, 'PID_FILE', os.path.join(config.PROJECT_PATH, 'agentd.pid'))
    setattr(config, 'SERVER_ADDR', _args.host)
    setattr(config, 'SERVER_PORT', _args.port)
    setattr(config, 'LOG_FILE', os.path.join(config.PROJECT_PATH, 'logs', 'agentd.log'))
    setattr(config, 'LOG_LEVEL', 'DEBUG' if _args.verbose else 'INFO')
    setattr(config, 'LOG_FORMAT', '%(asctime)s - %(name)s - %(levelname)s:%(message)s')
    setattr(config, 'LOG_MODE', 'w')
    setattr(config, 'QUEUE', mqueue.MQueue())

    setattr(config, 'INTERVAL', 3)
    setattr(config, 'INTERVAL_HEARTBEAT', 15)
    setattr(config, 'INTERVAL_CLIENT', 60)
    setattr(config, 'INTERVAL_RESOURCE', 60)

    setattr(config, 'TOKEN_ID', 'a')
    setattr(config, 'TOKEN_SECERT', 'b')

    setattr(config, 'PLUGINS', load_plugins(config))

    logging.basicConfig(
        level=config.LOG_LEVEL,
        format=config.LOG_FORMAT,
        filename=config.LOG_FILE,
        filemode=config.LOG_MODE
    )
    
    fileutils.write_file(config.PID_FILE, config.PID)
    _uuid = fileutils.read_file(config.UUID_FILE)
    if not _uuid:
        _uuid = sysutils.get_uuid()
        fileutils.write_file(config.UUID_FILE, _uuid)

    setattr(config, 'UUID', _uuid)

    logger.info('agent[%s][%s] is running...', config.UUID, config.PID)
    
    main(config)