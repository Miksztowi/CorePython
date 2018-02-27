# -*- encoding:utf-8 -*-
# __author__=='Gan'
import asyncio


class GameContext:
    async def __aenter__(self):
        print('game loading...')
        await asyncio.sleep(1)

    async def __aexit__(self, exc_type, exc, tb):
        print('game exit...')
        await asyncio.sleep(1)


async def game():
    async with GameContext():
        print('game start...')
        await asyncio.sleep(2)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(game())
