#encoding: utf-8
import os

import redis

import gconf

class CacheBase(object):

    def get(self, key):
        raise BaseException('get method is not define')

    def set(self, key, value):
        raise BaseException('get method is not define')


class MemCache(CacheBase):
    _cached = {}

    def get(self, key):
        return self._cached.get(key, None)

    def set(self, key, value):
        self._cached[key] = value


class RedisCache(CacheBase):

    def __init__(self, host, port):
        self._redis_cli = redis.StrictRedis(host=host, port=port)
        self._key_tpl = 'cache:{0}'

    def get(self, key):
        return self._redis_cli.get(self._key_tpl.format(key))

    def set(self, key, value):
        self._redis_cli.set(self._key_tpl.format(key), value)


class DBCache(CacheBase):
    pass


class FileCache(CacheBase):

    def __init__(self):
        self._path_prefix = os.path.join(gconf.PROJECT_PATH, 'cache')

    def get(self, key):
        _path = '{0}/{1}'.format(self._path_prefix, key)
        if os.path.exists(_path):
            with open(_path, 'rb') as f:
                return f.read()

        return None

    def set(self, key, value):
        _path = '{0}/{1}'.format(self._path_prefix, key)
        with open(_path, 'wb') as f:
            f.write(str(value).encode())


#Cache =  RedisCache(gconf.REDIS_HOST, gconf.REDIS_PORT) if gconf.CACHE_TYPE == 'redis' else MemCache()

Cache = FileCache()

def get_cache(cache_type):
    return RedisCache(gconf.REDIS_HOST, gconf.REDIS_PORT) if \
                    cache_type == 'redis' else \
                    MemCache()