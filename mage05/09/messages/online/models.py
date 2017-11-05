#encoding: utf-8
from datetime import datetime
import json

from utils import dbutil

class Message(object):

    SQL_MESSAGE_LIST = 'select id,username,title,content,publish_date from message3 order by publish_date desc;'
    SQL_MESSAGE_INSERT = 'insert into message3(username, title, content, publish_date) values(%s, %s, %s, %s)'

    def __init__(self, id=None, username=None, title=None, content=None, publish_date=None):
        self.id = id
        self.username = username
        self.title = title
        self.content = content
        self.publish_date = publish_date

    @classmethod
    def all(cls):
        rt_list = []
        lines = dbutil.execute_fetch(cls.SQL_MESSAGE_LIST)
        for message in lines:
            if message['publish_date']:
                message['publish_date'] = message['publish_date'].strftime('%Y-%m-%d %H:%M:%S')
            obj = Message(id=message['id'], username=message['username'],\
                            title=message['title'], content=message['content'], publish_date=message['publish_date'])
            rt_list.append(obj)
        return rt_list

    def __str__(self):
        return self.title

    def save(self):
        args = (self. username, self.title, self.content, datetime.now())
        dbutil.execute_commit(self.SQL_MESSAGE_INSERT, args)
