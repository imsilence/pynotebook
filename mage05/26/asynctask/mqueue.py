#encoding: utf-8

import redis

class RedisQueue(object):

    def __init__(self, name, host='127.0.0.1', port=6379, db=0):
        self._redis_cli = redis.StrictRedis(host=host, port=port, db=db)
        self._key = name


    def get(self, block=True, timeout=None):
        value = None
        if block:
            value = self._redis_cli.brpop(self._key, timeout)
            if value:
                value = value[1]
        else:
            value = self._redis_cli.rpop(self._key)

        return value

    def put(self, item, block=True, timeout=None):
        self._redis_cli.lpush(self._key, item)

    def size(self):
        return self._redis_cli.llen(self._key)


if __name__ == '__main__':
    q = RedisQueue('test')
    print(q.size())
    q.put(1)
    q.put(2)
    print(q.size())
    print(q.get())
    print(q.get(block=False))
    print(q.get(timeout=3))
    print(q.get(block=False))
    print(q.size())

