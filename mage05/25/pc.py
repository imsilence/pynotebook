#encoding: utf-8

import threading
from queue import Queue
import logging
import time

logger = logging.getLogger(__name__)

def p(q, cnt):
    for i in range(cnt):
        logging.info('p:%s', i)
        q.put(i)
        time.sleep(0.1)


def c(ident, q):
    try:
        while True:
            cxt = q.get(timeout=3)
            logger.info("c:%s:%s", ident, cxt)
            time.sleep(0.3)
    except BaseException as e:
        pass

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    q = Queue()
    ths = []

    th = threading.Thread(target=p, args=(q, 100, ))
    th.start()
    ths.append(th)

    for i in range(3):
        th = threading.Thread(target=c, args=(i, q))
        th.start()
        ths.append(th)

    for th in ths:
        th.join()