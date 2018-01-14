# -*- encoding:utf-8 -*-
# __author__=='Gan'

import signal
import sys
import asyncio
import aiohttp
import json

loop = asyncio.get_event_loop()
client = aiohttp.ClientSession(loop=loop)


async def get_json(client, url):
    async with client.get(url) as response:
        assert response.status == 200
        return await response.read()


async def get_reddit_top(subreddit, client):
    data1 = await get_json(client, 'https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5')

    j = json.loads(data1.decode('utf-8'))
    for i in j['data']['children']:
        score = i['data']['score']
        title = i['data']['title']
        link = i['data']['url']
        print(str(score) + ': ' + title + ' (' + link + ')')

    print('DONE:', subreddit + '\n')


def signal_handler(signal, frame):
    loop.stop()
    client.close()
    sys.exit(0)


def main():
    titles = ['python', 'programming', 'compsci']
    to_do = [get_reddit_top(title, client) for title in titles]
    wait = asyncio.wait(to_do)
    loop.run_until_complete(wait)
    loop.close()


if __name__ == '__main__':
    main()
    signal.signal(signal.SIGINT, signal_handler)
