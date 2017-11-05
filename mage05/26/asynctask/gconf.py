#encoding: utf-8

import os

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0

QUEUE_TASK_KEY = 'asynctask:watting:task'

COCURRENCE = 10