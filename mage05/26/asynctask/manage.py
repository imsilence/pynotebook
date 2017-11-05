#encoding: utf-8
import logging
import time
from multiprocessing import Process

import gconf
from executor import Executor

logger = logging.getLogger(__name__) 

class Manager(object):

    def create_process(self, target, args=()):
        _process = Process(target=target, args=args)
        _process.daemon = True
        _process.start()
        logger.info('process[%s] runing...', _process.pid)
        return _process

    def run_as_server(self):
        processes = {}
        for i in range(gconf.COCURRENCE):
            processes[i] = self.create_process(Executor().run)

        try:
            while True:
                for i, process in processes.items():
                    if not process.is_alive():
                        logger.info('process[%s] is dead, restart...', process.pid)
                        processes[i] = self.create_process(Executor().run)
                time.sleep(2)
        except KeyboardInterrupt as e:
            logger.info('manage exit')

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(lineno)d %(levelname)s: %(message)s')
    Manager().run_as_server()