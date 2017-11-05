#encoding: utf-8
import asyncio
import logging
logger = logging.getLogger(__name__)

async def print_n(ident, n):
    logger.info('start %s', ident)
    for i in range(n):
        logger.info('print, %s, %s', ident, i)
        await asyncio.sleep(0.1)

    logger.info('over %s', ident)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    loop = asyncio.get_event_loop()

    tasks = []
    for i in range(2):
        tasks.append(print_n(i, 10))

    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()


