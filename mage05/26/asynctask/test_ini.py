#encoding: utf-8

import os
from configparser import ConfigParser

import gconf


class Config(object):
    def __init__(self):
        self._attrs = {}

    def __getitem__(self, key):
        return self._attrs.get(key)

    def __setitem__(self, key, value):
        self._attrs[key] = value


path = os.path.join(gconf.PROJECT_PATH, 'etc', 'asynctask.ini')

parser = ConfigParser()

parser.read(path)

for _, section in parser.items():
    for key, value in section.items():
        setattr(Config, key.upper(), value)


print(getattr(Config, 'COCURRENCE'))
print(Config.QUEUE_TASK_KEY)
try:
    print(getattr(Config, 'COCURRENCE1'))
except BaseException as e:
    print(e)
print(getattr(Config, 'COCURRENCE1', 2))


config = Config()

config['test'] = 'a'

print(config['test'])