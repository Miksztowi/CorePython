# -*- encoding:utf-8 -*-
# __author__=='Gan'

import asyncio


def run_sync(coro_or_future):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(coro_or_future)


@asyncio.coroutine
def coro():
    yield from asyncio.sleep(1)


if __name__ == '__main__':
    a = run_sync(coro())
