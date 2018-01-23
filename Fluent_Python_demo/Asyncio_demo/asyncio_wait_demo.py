# -*- encoding:utf-8 -*-
# __author__=='Gan'

import asyncio
import random


async def coro(tag):
    print('>', tag)
    await asyncio.sleep(random.uniform(0.5, 5))
    print('<', tag)
    return tag


def first_result(loop, tasks):
    print('Get first result:')
    finished, unfinished = loop.run_until_complete(
        asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED))
    for task in finished:
        print(task)
    print('unfinished: {}\nlength: {}'.format(unfinished, len(unfinished)))


def timeout_2(loop, tasks):
    print('Get less than 2 seconds result:')
    finished, unfinished = loop.run_until_complete(asyncio.wait(tasks, timeout=2))
    for task in finished:
        print(task)
    print('unfinished: {}\nlength: {}'.format(unfinished, len(unfinished)))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [coro(i) for i in range(1, 11)]
    # first_result(loop, tasks)
    timeout_2(loop, tasks)
