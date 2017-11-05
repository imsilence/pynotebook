#encoding: utf-8
import time
import random
import os
from django.core.files.storage import FileSystemStorage

class FileStorage(FileSystemStorage):
    def _save(self, name, content):
        dirname = os.path.dirname(name)
        name = '{dirname}/{prefix}_{suffix}_{random}.{fsuffix}'.format(dirname=dirname, prefix='goods', suffix=int(time.time() * 1000), random=random.randint(0, 1000), fsuffix=name.split('.')[-1])
        return super()._save(name, content)
