#encoding: utf-8

import logging
import time
import threading

logger = logging.getLogger(__name__)

g = []

lock = threading.Lock()

def print_n(ident, n):
    logger.info("%s ident start", ident)
    for i in range(n):
        lock.acquire()
        try:
            if i not in g:
                time.sleep(1)
                g.append(i)
        finally:
            lock.release()

        logger.info('ident[%s]:%s', ident, i)
       


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    th1 = threading.Thread(target=print_n, args=('a', 10))
    th2 = threading.Thread(target=print_n, args=('b', 10))
    th1.daemon = True
    th2.daemon = True
    th1.start()
    th2.start()

    th1.join(3)
    th2.join(3)
    print(g)
