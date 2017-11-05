#encoding: utf-8

from queue import Queue, Empty, Full

class PyQueue(Queue):
    
    def get(self, block=True, timeout=None):
        try:
            return super(PyQueue, self).get(block, timeout)
        except Empty as e:
            return None

    def put(self, item, block=True, timeout=None):
        try:
            super(PyQueue, self).put(item, block, timeout)
        except Full as e:
            pass

    def qsize(self):
        super(PyQueue, self).qsize()


MQueue = PyQueue
