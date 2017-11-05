#encoding: utf-8

from django.db import models

class Message2(models.Model):
    username = models.CharField(max_length=256, null=True)
    title = models.CharField(max_length=512, null=True)
    content = models.TextField(null=True)
    publish_date = models.DateTimeField(null=True)


    def __str__(self):
        tpl = '<Message2:[username={username}, title={title}, content={content}, publish_date={publish_date}]>'
        return tpl.format(username=self.username, title=self.title, content=self.content, publish_date=self.publish_date)
